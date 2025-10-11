# SNMP MIB module (OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:24:41 2025
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

(DataPmEventType,
 MOD2Type,
 ObjType,
 PerformanceEventType,
 ValidflagType) = mibBuilder.importSymbols(
    "OPTIX-GLOBAL-TC-MIB",
    "DataPmEventType",
    "MOD2Type",
    "ObjType",
    "PerformanceEventType",
    "ValidflagType")

(optixGlobalTrap,
 rptAlmName,
 rptEvtEndTime,
 rptEvtNtfcnCde,
 rptEvtNumber,
 rptEvtObjType,
 rptEvtPara,
 rptEvtSrvEff,
 rptEvtStartTime,
 rptEvtState,
 rptEvtValue) = mibBuilder.importSymbols(
    "OPTIX-GLOBAL-TRAPS-MIB",
    "optixGlobalTrap",
    "rptAlmName",
    "rptEvtEndTime",
    "rptEvtNtfcnCde",
    "rptEvtNumber",
    "rptEvtObjType",
    "rptEvtPara",
    "rptEvtSrvEff",
    "rptEvtStartTime",
    "rptEvtState",
    "rptEvtValue")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixTrapsPER_ObjectIdentity = ObjectIdentity
optixTrapsPER = _OptixTrapsPER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30)
)

# Managed Objects groups


# Notification objects

perEvtRsbbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 1)
)
perEvtRsbbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRsbbe.setStatus(
        "current"
    )

perEvtRses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 2)
)
perEvtRses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRses.setStatus(
        "current"
    )

perEvtRsses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 3)
)
perEvtRsses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRsses.setStatus(
        "current"
    )

perEvtRsofs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 5)
)
perEvtRsofs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRsofs.setStatus(
        "current"
    )

perEvtRsuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 6)
)
perEvtRsuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRsuas.setStatus(
        "current"
    )

perEvtRscses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 7)
)
perEvtRscses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRscses.setStatus(
        "current"
    )

perEvtTlbmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 96)
)
perEvtTlbmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTlbmax.setStatus(
        "current"
    )

perEvtTlbmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 97)
)
perEvtTlbmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTlbmin.setStatus(
        "current"
    )

perEvtTlbcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 98)
)
perEvtTlbcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTlbcur.setStatus(
        "current"
    )

perEvtOspiccvmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 99)
)
perEvtOspiccvmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspiccvmax.setStatus(
        "current"
    )

perEvtOspiccvmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 100)
)
perEvtOspiccvmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspiccvmin.setStatus(
        "current"
    )

perEvtOspiccvcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 101)
)
perEvtOspiccvcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspiccvcur.setStatus(
        "current"
    )

perEvtTplmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 102)
)
perEvtTplmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTplmax.setStatus(
        "current"
    )

perEvtTplmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 103)
)
perEvtTplmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTplmin.setStatus(
        "current"
    )

perEvtTplcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 104)
)
perEvtTplcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTplcur.setStatus(
        "current"
    )

perEvtRplmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 105)
)
perEvtRplmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRplmax.setStatus(
        "current"
    )

perEvtRplmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 106)
)
perEvtRplmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRplmin.setStatus(
        "current"
    )

perEvtRplcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 107)
)
perEvtRplcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRplcur.setStatus(
        "current"
    )

perEvtOspitmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 108)
)
perEvtOspitmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspitmpmax.setStatus(
        "current"
    )

perEvtOspitmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 109)
)
perEvtOspitmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspitmpmin.setStatus(
        "current"
    )

perEvtOspitmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 110)
)
perEvtOspitmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOspitmpcur.setStatus(
        "current"
    )

perEvtWcvmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 112)
)
perEvtWcvmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtWcvmax.setStatus(
        "current"
    )

perEvtWcvmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 113)
)
perEvtWcvmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtWcvmin.setStatus(
        "current"
    )

perEvtWcvcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 114)
)
perEvtWcvcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtWcvcur.setStatus(
        "current"
    )

perEvtCcvmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 115)
)
perEvtCcvmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCcvmax.setStatus(
        "current"
    )

perEvtCcvmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 116)
)
perEvtCcvmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCcvmin.setStatus(
        "current"
    )

perEvtCcvcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 117)
)
perEvtCcvcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCcvcur.setStatus(
        "current"
    )

perEvtBcvmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 118)
)
perEvtBcvmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBcvmax.setStatus(
        "current"
    )

perEvtBcvmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 119)
)
perEvtBcvmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBcvmin.setStatus(
        "current"
    )

perEvtBcvcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 120)
)
perEvtBcvcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBcvcur.setStatus(
        "current"
    )

perEvtEdtplmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 121)
)
perEvtEdtplmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtplmax.setStatus(
        "current"
    )

perEvtEdtplmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 122)
)
perEvtEdtplmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtplmin.setStatus(
        "current"
    )

perEvtEdtplcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 123)
)
perEvtEdtplcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtplcur.setStatus(
        "current"
    )

perEvtEdtmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 130)
)
perEvtEdtmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtmpmax.setStatus(
        "current"
    )

perEvtEdtmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 131)
)
perEvtEdtmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtmpmin.setStatus(
        "current"
    )

perEvtEdtmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 132)
)
perEvtEdtmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEdtmpcur.setStatus(
        "current"
    )

perEvtfecCorrected0BitCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 133)
)
perEvtfecCorrected0BitCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecCorrected0BitCount.setStatus(
        "current"
    )

perEvtfecCorrected1BitCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 134)
)
perEvtfecCorrected1BitCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecCorrected1BitCount.setStatus(
        "current"
    )

perEvtfecCorrectedByteCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 135)
)
perEvtfecCorrectedByteCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecCorrectedByteCount.setStatus(
        "current"
    )

perEvtfecUnCorrectedBlockCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 136)
)
perEvtfecUnCorrectedBlockCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecUnCorrectedBlockCount.setStatus(
        "current"
    )

perEvtboardTemperatureMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 188)
)
perEvtboardTemperatureMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtboardTemperatureMaximum.setStatus(
        "current"
    )

perEvtboardTemperatureMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 189)
)
perEvtboardTemperatureMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtboardTemperatureMinimum.setStatus(
        "current"
    )

perEvtboardTemperatureCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 190)
)
perEvtboardTemperatureCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtboardTemperatureCurrent.setStatus(
        "current"
    )

perEvtw32LaserOutputOfPowerMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 198)
)
perEvtw32LaserOutputOfPowerMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserOutputOfPowerMaximum.setStatus(
        "current"
    )

perEvtw32LaserOutputOfPowerMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 199)
)
perEvtw32LaserOutputOfPowerMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserOutputOfPowerMinimum.setStatus(
        "current"
    )

perEvtw32LaserOutputOfPowerCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 200)
)
perEvtw32LaserOutputOfPowerCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserOutputOfPowerCurrent.setStatus(
        "current"
    )

perEvtw32LaserInputOfPowerMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 201)
)
perEvtw32LaserInputOfPowerMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserInputOfPowerMaximum.setStatus(
        "current"
    )

perEvtw32LaserInputOfPowerMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 202)
)
perEvtw32LaserInputOfPowerMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserInputOfPowerMinimum.setStatus(
        "current"
    )

perEvtw32LaserInputOfPowerCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 203)
)
perEvtw32LaserInputOfPowerCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserInputOfPowerCurrent.setStatus(
        "current"
    )

perEvtw32LaserWorkingTemperatureMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 204)
)
perEvtw32LaserWorkingTemperatureMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserWorkingTemperatureMaximum.setStatus(
        "current"
    )

perEvtw32LaserWorkingTemperatureMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 205)
)
perEvtw32LaserWorkingTemperatureMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserWorkingTemperatureMinimum.setStatus(
        "current"
    )

perEvtw32LaserWorkingTemperatureCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 206)
)
perEvtw32LaserWorkingTemperatureCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserWorkingTemperatureCurrent.setStatus(
        "current"
    )

perEvtw32LaserBiasMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 207)
)
perEvtw32LaserBiasMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserBiasMaximum.setStatus(
        "current"
    )

perEvtw32LaserBiasMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 208)
)
perEvtw32LaserBiasMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserBiasMinimum.setStatus(
        "current"
    )

perEvtw32LaserBiasCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 209)
)
perEvtw32LaserBiasCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserBiasCurrent.setStatus(
        "current"
    )

perEvtw32SumLaserInputOfPowerMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 210)
)
perEvtw32SumLaserInputOfPowerMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32SumLaserInputOfPowerMaximum.setStatus(
        "current"
    )

perEvtw32SumLaserInputOfPowerMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 211)
)
perEvtw32SumLaserInputOfPowerMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32SumLaserInputOfPowerMinimum.setStatus(
        "current"
    )

perEvtw32SumLaserInputOfPowerCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 212)
)
perEvtw32SumLaserInputOfPowerCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32SumLaserInputOfPowerCurrent.setStatus(
        "current"
    )

perEvtSumoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 213)
)
perEvtSumoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSumoopmax.setStatus(
        "current"
    )

perEvtSumoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 214)
)
perEvtSumoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSumoopmin.setStatus(
        "current"
    )

perEvtSumoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 215)
)
perEvtSumoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSumoopcur.setStatus(
        "current"
    )

perEvtEnvtmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 222)
)
perEvtEnvtmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEnvtmpmax.setStatus(
        "current"
    )

perEvtEnvtmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 223)
)
perEvtEnvtmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEnvtmpmin.setStatus(
        "current"
    )

perEvtEnvtmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 224)
)
perEvtEnvtmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEnvtmpcur.setStatus(
        "current"
    )

perEvtw32LaserCoolingMaximum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 225)
)
perEvtw32LaserCoolingMaximum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserCoolingMaximum.setStatus(
        "current"
    )

perEvtw32LaserCoolingMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 226)
)
perEvtw32LaserCoolingMinimum.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserCoolingMinimum.setStatus(
        "current"
    )

perEvtw32LaserCoolingCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 227)
)
perEvtw32LaserCoolingCurrent.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtw32LaserCoolingCurrent.setStatus(
        "current"
    )

perEvtPclswlmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 228)
)
perEvtPclswlmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlmax.setStatus(
        "current"
    )

perEvtPclswlmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 229)
)
perEvtPclswlmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlmin.setStatus(
        "current"
    )

perEvtPclswlcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 230)
)
perEvtPclswlcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlcur.setStatus(
        "current"
    )

perEvtPclswlomax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 231)
)
perEvtPclswlomax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlomax.setStatus(
        "current"
    )

perEvtPclswlomin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 232)
)
perEvtPclswlomin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlomin.setStatus(
        "current"
    )

perEvtPclswlocur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 233)
)
perEvtPclswlocur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclswlocur.setStatus(
        "current"
    )

perEvtPclsopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 234)
)
perEvtPclsopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclsopmax.setStatus(
        "current"
    )

perEvtPclsopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 235)
)
perEvtPclsopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclsopmin.setStatus(
        "current"
    )

perEvtPclsopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 236)
)
perEvtPclsopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclsopcur.setStatus(
        "current"
    )

perEvtPclssnmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 237)
)
perEvtPclssnmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclssnmax.setStatus(
        "current"
    )

perEvtPclssnmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 238)
)
perEvtPclssnmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclssnmin.setStatus(
        "current"
    )

perEvtPclssncur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 239)
)
perEvtPclssncur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPclssncur.setStatus(
        "current"
    )

perEvtIctmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 249)
)
perEvtIctmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIctmpmax.setStatus(
        "current"
    )

perEvtIctmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 250)
)
perEvtIctmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIctmpmin.setStatus(
        "current"
    )

perEvtIctmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 251)
)
perEvtIctmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIctmpcur.setStatus(
        "current"
    )

perEvtbeforeFECCorrectErrorRatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 252)
)
perEvtbeforeFECCorrectErrorRatio.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtbeforeFECCorrectErrorRatio.setStatus(
        "current"
    )

perEvtafterFECCorrectErrorRatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 253)
)
perEvtafterFECCorrectErrorRatio.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtafterFECCorrectErrorRatio.setStatus(
        "current"
    )

perEvtIcclcmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 4172)
)
perEvtIcclcmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIcclcmax.setStatus(
        "current"
    )

perEvtIcclcmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 4173)
)
perEvtIcclcmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIcclcmin.setStatus(
        "current"
    )

perEvtIcclccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 4174)
)
perEvtIcclccur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtIcclccur.setStatus(
        "current"
    )

perEvtOoprlmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 8612)
)
perEvtOoprlmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOoprlmax.setStatus(
        "current"
    )

perEvtOoprlmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 8613)
)
perEvtOoprlmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOoprlmin.setStatus(
        "current"
    )

perEvtOoprlcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 8614)
)
perEvtOoprlcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOoprlcur.setStatus(
        "current"
    )

perEvtOtu1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14336)
)
perEvtOtu1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Iaes.setStatus(
        "current"
    )

perEvtOtu1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14337)
)
perEvtOtu1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Biaes.setStatus(
        "current"
    )

perEvtOtu1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14338)
)
perEvtOtu1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Bbe.setStatus(
        "current"
    )

perEvtOtu1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14339)
)
perEvtOtu1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Es.setStatus(
        "current"
    )

perEvtOtu1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14340)
)
perEvtOtu1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Ses.setStatus(
        "current"
    )

perEvtOtu1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14341)
)
perEvtOtu1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Uas.setStatus(
        "current"
    )

perEvtOtu1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14342)
)
perEvtOtu1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Sesr.setStatus(
        "current"
    )

perEvtOtu1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14343)
)
perEvtOtu1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Bber.setStatus(
        "current"
    )

perEvtOtu1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14344)
)
perEvtOtu1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Febbe.setStatus(
        "current"
    )

perEvtOtu1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14345)
)
perEvtOtu1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Fees.setStatus(
        "current"
    )

perEvtOtu1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14346)
)
perEvtOtu1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Feses.setStatus(
        "current"
    )

perEvtOtu1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14347)
)
perEvtOtu1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Feuas.setStatus(
        "current"
    )

perEvtOtu1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14348)
)
perEvtOtu1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Fesesr.setStatus(
        "current"
    )

perEvtOtu1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14349)
)
perEvtOtu1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Febber.setStatus(
        "current"
    )

perEvtOtu2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14364)
)
perEvtOtu2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Iaes.setStatus(
        "current"
    )

perEvtOtu2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14365)
)
perEvtOtu2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Biaes.setStatus(
        "current"
    )

perEvtOtu2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14366)
)
perEvtOtu2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Bbe.setStatus(
        "current"
    )

perEvtOtu2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14367)
)
perEvtOtu2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Es.setStatus(
        "current"
    )

perEvtOtu2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14368)
)
perEvtOtu2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Ses.setStatus(
        "current"
    )

perEvtOtu2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14369)
)
perEvtOtu2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Uas.setStatus(
        "current"
    )

perEvtOtu2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14370)
)
perEvtOtu2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Sesr.setStatus(
        "current"
    )

perEvtOtu2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14371)
)
perEvtOtu2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Bber.setStatus(
        "current"
    )

perEvtOtu2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14372)
)
perEvtOtu2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Febbe.setStatus(
        "current"
    )

perEvtOtu2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14373)
)
perEvtOtu2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Fees.setStatus(
        "current"
    )

perEvtOtu2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14374)
)
perEvtOtu2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Feses.setStatus(
        "current"
    )

perEvtOtu2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14375)
)
perEvtOtu2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Feuas.setStatus(
        "current"
    )

perEvtOtu2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14376)
)
perEvtOtu2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Fesesr.setStatus(
        "current"
    )

perEvtOtu2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14377)
)
perEvtOtu2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Febber.setStatus(
        "current"
    )

perEvtOtu3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14378)
)
perEvtOtu3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Iaes.setStatus(
        "current"
    )

perEvtOtu3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14379)
)
perEvtOtu3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Biaes.setStatus(
        "current"
    )

perEvtOtu3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14380)
)
perEvtOtu3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Bbe.setStatus(
        "current"
    )

perEvtOtu3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14381)
)
perEvtOtu3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Es.setStatus(
        "current"
    )

perEvtOtu3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14382)
)
perEvtOtu3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Ses.setStatus(
        "current"
    )

perEvtOtu3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14383)
)
perEvtOtu3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Uas.setStatus(
        "current"
    )

perEvtOtu3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14384)
)
perEvtOtu3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Sesr.setStatus(
        "current"
    )

perEvtOtu3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14385)
)
perEvtOtu3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Bber.setStatus(
        "current"
    )

perEvtOtu3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14386)
)
perEvtOtu3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Febbe.setStatus(
        "current"
    )

perEvtOtu3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14387)
)
perEvtOtu3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Fees.setStatus(
        "current"
    )

perEvtOtu3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14388)
)
perEvtOtu3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Feses.setStatus(
        "current"
    )

perEvtOtu3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14389)
)
perEvtOtu3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Feuas.setStatus(
        "current"
    )

perEvtOtu3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14390)
)
perEvtOtu3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Fesesr.setStatus(
        "current"
    )

perEvtOtu3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14391)
)
perEvtOtu3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Febber.setStatus(
        "current"
    )

perEvtOdu1PmBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14392)
)
perEvtOdu1PmBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmBbe.setStatus(
        "current"
    )

perEvtOdu1PmEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14393)
)
perEvtOdu1PmEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmEs.setStatus(
        "current"
    )

perEvtOdu1PmSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14394)
)
perEvtOdu1PmSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmSes.setStatus(
        "current"
    )

perEvtOdu1PmUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14395)
)
perEvtOdu1PmUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmUas.setStatus(
        "current"
    )

perEvtOdu1PmSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14396)
)
perEvtOdu1PmSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmSesr.setStatus(
        "current"
    )

perEvtOdu1PmBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14397)
)
perEvtOdu1PmBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmBber.setStatus(
        "current"
    )

perEvtOdu1PmFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14398)
)
perEvtOdu1PmFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFebbe.setStatus(
        "current"
    )

perEvtOdu1PmFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14399)
)
perEvtOdu1PmFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFees.setStatus(
        "current"
    )

perEvtOdu1PmFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14400)
)
perEvtOdu1PmFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFeses.setStatus(
        "current"
    )

perEvtOdu1PmFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14401)
)
perEvtOdu1PmFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFeuas.setStatus(
        "current"
    )

perEvtOdu1PmFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14402)
)
perEvtOdu1PmFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFesesr.setStatus(
        "current"
    )

perEvtOdu1PmFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14403)
)
perEvtOdu1PmFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmFebber.setStatus(
        "current"
    )

perEvtodu2pmbbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14416)
)
perEvtodu2pmbbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmbbe.setStatus(
        "current"
    )

perEvtodu2pmes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14417)
)
perEvtodu2pmes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmes.setStatus(
        "current"
    )

perEvtodu2pmses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14418)
)
perEvtodu2pmses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmses.setStatus(
        "current"
    )

perEvtodu2pmuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14419)
)
perEvtodu2pmuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmuas.setStatus(
        "current"
    )

perEvtodu2pmsesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14420)
)
perEvtodu2pmsesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmsesr.setStatus(
        "current"
    )

perEvtodu2pmbber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14421)
)
perEvtodu2pmbber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmbber.setStatus(
        "current"
    )

perEvtodu2pmfebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14422)
)
perEvtodu2pmfebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfebbe.setStatus(
        "current"
    )

perEvtodu2pmfees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14423)
)
perEvtodu2pmfees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfees.setStatus(
        "current"
    )

perEvtodu2pmfeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14424)
)
perEvtodu2pmfeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfeses.setStatus(
        "current"
    )

perEvtodu2pmfeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14425)
)
perEvtodu2pmfeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfeuas.setStatus(
        "current"
    )

perEvtodu2pmfesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14426)
)
perEvtodu2pmfesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfesesr.setStatus(
        "current"
    )

perEvtodu2pmfebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14427)
)
perEvtodu2pmfebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2pmfebber.setStatus(
        "current"
    )

perEvtodu3pmbbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14428)
)
perEvtodu3pmbbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmbbe.setStatus(
        "current"
    )

perEvtodu3pmes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14429)
)
perEvtodu3pmes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmes.setStatus(
        "current"
    )

perEvtodu3pmses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14430)
)
perEvtodu3pmses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmses.setStatus(
        "current"
    )

perEvtodu3pmuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14431)
)
perEvtodu3pmuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmuas.setStatus(
        "current"
    )

perEvtodu3pmsesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14432)
)
perEvtodu3pmsesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmsesr.setStatus(
        "current"
    )

perEvtodu3pmbber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14433)
)
perEvtodu3pmbber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmbber.setStatus(
        "current"
    )

perEvtodu3pmfebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14434)
)
perEvtodu3pmfebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfebbe.setStatus(
        "current"
    )

perEvtodu3pmfees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14435)
)
perEvtodu3pmfees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfees.setStatus(
        "current"
    )

perEvtodu3pmfeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14436)
)
perEvtodu3pmfeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfeses.setStatus(
        "current"
    )

perEvtodu3pmfeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14437)
)
perEvtodu3pmfeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfeuas.setStatus(
        "current"
    )

perEvtodu3pmfesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14438)
)
perEvtodu3pmfesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfesesr.setStatus(
        "current"
    )

perEvtodu3pmfebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14439)
)
perEvtodu3pmfebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3pmfebber.setStatus(
        "current"
    )

perEvtOdu1Tcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14440)
)
perEvtOdu1Tcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14441)
)
perEvtOdu1Tcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14442)
)
perEvtOdu1Tcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14443)
)
perEvtOdu1Tcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14444)
)
perEvtOdu1Tcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14445)
)
perEvtOdu1Tcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Iaes.setStatus(
        "current"
    )

perEvtOdu1Tcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14446)
)
perEvtOdu1Tcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14447)
)
perEvtOdu1Tcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14448)
)
perEvtOdu1Tcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14449)
)
perEvtOdu1Tcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14450)
)
perEvtOdu1Tcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14451)
)
perEvtOdu1Tcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Biaes.setStatus(
        "current"
    )

perEvtOdu1Tcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14452)
)
perEvtOdu1Tcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14453)
)
perEvtOdu1Tcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Es.setStatus(
        "current"
    )

perEvtOdu1Tcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14454)
)
perEvtOdu1Tcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14455)
)
perEvtOdu1Tcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14456)
)
perEvtOdu1Tcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14457)
)
perEvtOdu1Tcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14458)
)
perEvtOdu1Tcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14459)
)
perEvtOdu1Tcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Es.setStatus(
        "current"
    )

perEvtOdu1Tcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14460)
)
perEvtOdu1Tcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14461)
)
perEvtOdu1Tcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14462)
)
perEvtOdu1Tcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14463)
)
perEvtOdu1Tcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14464)
)
perEvtOdu1Tcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14465)
)
perEvtOdu1Tcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Es.setStatus(
        "current"
    )

perEvtOdu1Tcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14466)
)
perEvtOdu1Tcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14467)
)
perEvtOdu1Tcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14468)
)
perEvtOdu1Tcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14469)
)
perEvtOdu1Tcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14470)
)
perEvtOdu1Tcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14471)
)
perEvtOdu1Tcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Es.setStatus(
        "current"
    )

perEvtOdu1Tcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14472)
)
perEvtOdu1Tcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14473)
)
perEvtOdu1Tcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14474)
)
perEvtOdu1Tcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14475)
)
perEvtOdu1Tcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14476)
)
perEvtOdu1Tcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14477)
)
perEvtOdu1Tcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Es.setStatus(
        "current"
    )

perEvtOdu1Tcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14478)
)
perEvtOdu1Tcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14479)
)
perEvtOdu1Tcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14480)
)
perEvtOdu1Tcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14481)
)
perEvtOdu1Tcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14482)
)
perEvtOdu1Tcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Bbe.setStatus(
        "current"
    )

perEvtOdu1Tcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14483)
)
perEvtOdu1Tcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Es.setStatus(
        "current"
    )

perEvtOdu1Tcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14484)
)
perEvtOdu1Tcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Ses.setStatus(
        "current"
    )

perEvtOdu1Tcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14485)
)
perEvtOdu1Tcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Uas.setStatus(
        "current"
    )

perEvtOdu1Tcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14486)
)
perEvtOdu1Tcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Sesr.setStatus(
        "current"
    )

perEvtOdu1Tcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14487)
)
perEvtOdu1Tcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Bber.setStatus(
        "current"
    )

perEvtOdu1Tcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14488)
)
perEvtOdu1Tcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14489)
)
perEvtOdu1Tcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14490)
)
perEvtOdu1Tcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14491)
)
perEvtOdu1Tcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14492)
)
perEvtOdu1Tcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14493)
)
perEvtOdu1Tcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Febber.setStatus(
        "current"
    )

perEvtOdu1Tcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14494)
)
perEvtOdu1Tcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14495)
)
perEvtOdu1Tcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14496)
)
perEvtOdu1Tcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14497)
)
perEvtOdu1Tcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14498)
)
perEvtOdu1Tcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14499)
)
perEvtOdu1Tcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Febber.setStatus(
        "current"
    )

perEvtOdu1Tcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14500)
)
perEvtOdu1Tcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14501)
)
perEvtOdu1Tcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14502)
)
perEvtOdu1Tcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14503)
)
perEvtOdu1Tcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14504)
)
perEvtOdu1Tcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14505)
)
perEvtOdu1Tcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Febber.setStatus(
        "current"
    )

perEvtOdu1Tcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14506)
)
perEvtOdu1Tcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14507)
)
perEvtOdu1Tcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14508)
)
perEvtOdu1Tcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14509)
)
perEvtOdu1Tcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14510)
)
perEvtOdu1Tcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14511)
)
perEvtOdu1Tcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Febber.setStatus(
        "current"
    )

perEvtOdu1Tcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14512)
)
perEvtOdu1Tcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14513)
)
perEvtOdu1Tcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14514)
)
perEvtOdu1Tcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14515)
)
perEvtOdu1Tcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14516)
)
perEvtOdu1Tcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14517)
)
perEvtOdu1Tcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Febber.setStatus(
        "current"
    )

perEvtOdu1Tcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14518)
)
perEvtOdu1Tcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Febbe.setStatus(
        "current"
    )

perEvtOdu1Tcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14519)
)
perEvtOdu1Tcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Fees.setStatus(
        "current"
    )

perEvtOdu1Tcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14520)
)
perEvtOdu1Tcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Feses.setStatus(
        "current"
    )

perEvtOdu1Tcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14521)
)
perEvtOdu1Tcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Feuas.setStatus(
        "current"
    )

perEvtOdu1Tcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14522)
)
perEvtOdu1Tcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Fesesr.setStatus(
        "current"
    )

perEvtOdu1Tcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14523)
)
perEvtOdu1Tcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14608)
)
perEvtOdu2Tcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14609)
)
perEvtOdu2Tcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14610)
)
perEvtOdu2Tcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14611)
)
perEvtOdu2Tcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14612)
)
perEvtOdu2Tcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14613)
)
perEvtOdu2Tcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Iaes.setStatus(
        "current"
    )

perEvtOdu2Tcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14614)
)
perEvtOdu2Tcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14615)
)
perEvtOdu2Tcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14616)
)
perEvtOdu2Tcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14617)
)
perEvtOdu2Tcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14618)
)
perEvtOdu2Tcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14619)
)
perEvtOdu2Tcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Biaes.setStatus(
        "current"
    )

perEvtOdu2Tcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14620)
)
perEvtOdu2Tcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14621)
)
perEvtOdu2Tcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Es.setStatus(
        "current"
    )

perEvtOdu2Tcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14622)
)
perEvtOdu2Tcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14623)
)
perEvtOdu2Tcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14624)
)
perEvtOdu2Tcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14625)
)
perEvtOdu2Tcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14626)
)
perEvtOdu2Tcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14627)
)
perEvtOdu2Tcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Es.setStatus(
        "current"
    )

perEvtOdu2Tcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14628)
)
perEvtOdu2Tcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14629)
)
perEvtOdu2Tcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14630)
)
perEvtOdu2Tcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14631)
)
perEvtOdu2Tcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14632)
)
perEvtOdu2Tcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14633)
)
perEvtOdu2Tcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Es.setStatus(
        "current"
    )

perEvtOdu2Tcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14634)
)
perEvtOdu2Tcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14635)
)
perEvtOdu2Tcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14636)
)
perEvtOdu2Tcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14637)
)
perEvtOdu2Tcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14638)
)
perEvtOdu2Tcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14639)
)
perEvtOdu2Tcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Es.setStatus(
        "current"
    )

perEvtOdu2Tcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14640)
)
perEvtOdu2Tcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14641)
)
perEvtOdu2Tcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14642)
)
perEvtOdu2Tcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14643)
)
perEvtOdu2Tcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14644)
)
perEvtOdu2Tcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14645)
)
perEvtOdu2Tcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Es.setStatus(
        "current"
    )

perEvtOdu2Tcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14646)
)
perEvtOdu2Tcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14647)
)
perEvtOdu2Tcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14648)
)
perEvtOdu2Tcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14649)
)
perEvtOdu2Tcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14650)
)
perEvtOdu2Tcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Bbe.setStatus(
        "current"
    )

perEvtOdu2Tcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14651)
)
perEvtOdu2Tcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Es.setStatus(
        "current"
    )

perEvtOdu2Tcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14652)
)
perEvtOdu2Tcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Ses.setStatus(
        "current"
    )

perEvtOdu2Tcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14653)
)
perEvtOdu2Tcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Uas.setStatus(
        "current"
    )

perEvtOdu2Tcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14654)
)
perEvtOdu2Tcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Sesr.setStatus(
        "current"
    )

perEvtOdu2Tcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14655)
)
perEvtOdu2Tcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Bber.setStatus(
        "current"
    )

perEvtOdu2Tcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14656)
)
perEvtOdu2Tcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14657)
)
perEvtOdu2Tcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14658)
)
perEvtOdu2Tcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14659)
)
perEvtOdu2Tcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14660)
)
perEvtOdu2Tcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14661)
)
perEvtOdu2Tcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14662)
)
perEvtOdu2Tcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14663)
)
perEvtOdu2Tcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14664)
)
perEvtOdu2Tcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14665)
)
perEvtOdu2Tcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14666)
)
perEvtOdu2Tcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14667)
)
perEvtOdu2Tcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14668)
)
perEvtOdu2Tcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14669)
)
perEvtOdu2Tcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14670)
)
perEvtOdu2Tcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14671)
)
perEvtOdu2Tcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14672)
)
perEvtOdu2Tcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14673)
)
perEvtOdu2Tcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14674)
)
perEvtOdu2Tcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14675)
)
perEvtOdu2Tcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14676)
)
perEvtOdu2Tcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14677)
)
perEvtOdu2Tcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14678)
)
perEvtOdu2Tcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14679)
)
perEvtOdu2Tcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14680)
)
perEvtOdu2Tcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14681)
)
perEvtOdu2Tcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14682)
)
perEvtOdu2Tcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14683)
)
perEvtOdu2Tcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14684)
)
perEvtOdu2Tcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14685)
)
perEvtOdu2Tcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Febber.setStatus(
        "current"
    )

perEvtOdu2Tcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14686)
)
perEvtOdu2Tcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Febbe.setStatus(
        "current"
    )

perEvtOdu2Tcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14687)
)
perEvtOdu2Tcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Fees.setStatus(
        "current"
    )

perEvtOdu2Tcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14688)
)
perEvtOdu2Tcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Feses.setStatus(
        "current"
    )

perEvtOdu2Tcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14689)
)
perEvtOdu2Tcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Feuas.setStatus(
        "current"
    )

perEvtOdu2Tcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14690)
)
perEvtOdu2Tcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Fesesr.setStatus(
        "current"
    )

perEvtOdu2Tcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14691)
)
perEvtOdu2Tcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14692)
)
perEvtOdu3Tcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14693)
)
perEvtOdu3Tcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14694)
)
perEvtOdu3Tcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14695)
)
perEvtOdu3Tcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14696)
)
perEvtOdu3Tcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14697)
)
perEvtOdu3Tcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Iaes.setStatus(
        "current"
    )

perEvtOdu3Tcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14698)
)
perEvtOdu3Tcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14699)
)
perEvtOdu3Tcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14700)
)
perEvtOdu3Tcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14701)
)
perEvtOdu3Tcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14702)
)
perEvtOdu3Tcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14703)
)
perEvtOdu3Tcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Biaes.setStatus(
        "current"
    )

perEvtOdu3Tcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14704)
)
perEvtOdu3Tcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14705)
)
perEvtOdu3Tcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Es.setStatus(
        "current"
    )

perEvtOdu3Tcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14706)
)
perEvtOdu3Tcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14707)
)
perEvtOdu3Tcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14708)
)
perEvtOdu3Tcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14709)
)
perEvtOdu3Tcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14710)
)
perEvtOdu3Tcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14711)
)
perEvtOdu3Tcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Es.setStatus(
        "current"
    )

perEvtOdu3Tcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14712)
)
perEvtOdu3Tcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14713)
)
perEvtOdu3Tcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14714)
)
perEvtOdu3Tcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14715)
)
perEvtOdu3Tcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14716)
)
perEvtOdu3Tcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14717)
)
perEvtOdu3Tcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Es.setStatus(
        "current"
    )

perEvtOdu3Tcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14718)
)
perEvtOdu3Tcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14719)
)
perEvtOdu3Tcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14720)
)
perEvtOdu3Tcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14721)
)
perEvtOdu3Tcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14722)
)
perEvtOdu3Tcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14723)
)
perEvtOdu3Tcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Es.setStatus(
        "current"
    )

perEvtOdu3Tcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14724)
)
perEvtOdu3Tcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14725)
)
perEvtOdu3Tcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14726)
)
perEvtOdu3Tcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14727)
)
perEvtOdu3Tcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14728)
)
perEvtOdu3Tcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14729)
)
perEvtOdu3Tcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Es.setStatus(
        "current"
    )

perEvtOdu3Tcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14730)
)
perEvtOdu3Tcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14731)
)
perEvtOdu3Tcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14732)
)
perEvtOdu3Tcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14733)
)
perEvtOdu3Tcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14734)
)
perEvtOdu3Tcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Bbe.setStatus(
        "current"
    )

perEvtOdu3Tcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14735)
)
perEvtOdu3Tcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Es.setStatus(
        "current"
    )

perEvtOdu3Tcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14736)
)
perEvtOdu3Tcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Ses.setStatus(
        "current"
    )

perEvtOdu3Tcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14737)
)
perEvtOdu3Tcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Uas.setStatus(
        "current"
    )

perEvtOdu3Tcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14738)
)
perEvtOdu3Tcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Sesr.setStatus(
        "current"
    )

perEvtOdu3Tcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14739)
)
perEvtOdu3Tcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Bber.setStatus(
        "current"
    )

perEvtOdu3Tcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14740)
)
perEvtOdu3Tcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14741)
)
perEvtOdu3Tcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14742)
)
perEvtOdu3Tcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14743)
)
perEvtOdu3Tcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14744)
)
perEvtOdu3Tcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14745)
)
perEvtOdu3Tcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14746)
)
perEvtOdu3Tcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14747)
)
perEvtOdu3Tcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14748)
)
perEvtOdu3Tcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14749)
)
perEvtOdu3Tcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14750)
)
perEvtOdu3Tcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14751)
)
perEvtOdu3Tcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14752)
)
perEvtOdu3Tcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14753)
)
perEvtOdu3Tcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14754)
)
perEvtOdu3Tcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14755)
)
perEvtOdu3Tcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14756)
)
perEvtOdu3Tcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14757)
)
perEvtOdu3Tcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14758)
)
perEvtOdu3Tcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14759)
)
perEvtOdu3Tcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14760)
)
perEvtOdu3Tcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14761)
)
perEvtOdu3Tcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14762)
)
perEvtOdu3Tcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14763)
)
perEvtOdu3Tcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14764)
)
perEvtOdu3Tcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14765)
)
perEvtOdu3Tcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14766)
)
perEvtOdu3Tcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14767)
)
perEvtOdu3Tcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14768)
)
perEvtOdu3Tcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14769)
)
perEvtOdu3Tcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Febber.setStatus(
        "current"
    )

perEvtOdu3Tcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14770)
)
perEvtOdu3Tcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Febbe.setStatus(
        "current"
    )

perEvtOdu3Tcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14771)
)
perEvtOdu3Tcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Fees.setStatus(
        "current"
    )

perEvtOdu3Tcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14772)
)
perEvtOdu3Tcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Feses.setStatus(
        "current"
    )

perEvtOdu3Tcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14773)
)
perEvtOdu3Tcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Feuas.setStatus(
        "current"
    )

perEvtOdu3Tcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14774)
)
perEvtOdu3Tcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Fesesr.setStatus(
        "current"
    )

perEvtOdu3Tcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14775)
)
perEvtOdu3Tcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Febber.setStatus(
        "current"
    )

perEvtTheDispersionCompensationMaximumValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14902)
)
perEvtTheDispersionCompensationMaximumValue.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTheDispersionCompensationMaximumValue.setStatus(
        "current"
    )

perEvtTheDispersionCompensationMinimumValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14903)
)
perEvtTheDispersionCompensationMinimumValue.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTheDispersionCompensationMinimumValue.setStatus(
        "current"
    )

perEvtTheDispersionCompensationCurrentValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14904)
)
perEvtTheDispersionCompensationCurrentValue.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtTheDispersionCompensationCurrentValue.setStatus(
        "current"
    )

perEvtCpTelDownCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14915)
)
perEvtCpTelDownCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpTelDownCount.setStatus(
        "current"
    )

perEvtCpTelDownTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14916)
)
perEvtCpTelDownTime.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpTelDownTime.setStatus(
        "current"
    )

perEvtCpCcDownCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14917)
)
perEvtCpCcDownCount.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpCcDownCount.setStatus(
        "current"
    )

perEvtCpCcDownTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14918)
)
perEvtCpCcDownTime.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpCcDownTime.setStatus(
        "current"
    )

perEvtCpuusagemax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14919)
)
perEvtCpuusagemax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpuusagemax.setStatus(
        "current"
    )

perEvtCpuusagemin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14920)
)
perEvtCpuusagemin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpuusagemin.setStatus(
        "current"
    )

perEvtCpuusagecur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14921)
)
perEvtCpuusagecur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCpuusagecur.setStatus(
        "current"
    )

perEvtMemusagemax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14922)
)
perEvtMemusagemax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMemusagemax.setStatus(
        "current"
    )

perEvtMemusagemin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14923)
)
perEvtMemusagemin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMemusagemin.setStatus(
        "current"
    )

perEvtMemusagecur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14924)
)
perEvtMemusagecur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMemusagecur.setStatus(
        "current"
    )

perEvtQValueEer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14925)
)
perEvtQValueEer.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtQValueEer.setStatus(
        "current"
    )

perEvtfecaftcoreravr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14926)
)
perEvtfecaftcoreravr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecaftcoreravr.setStatus(
        "current"
    )

perEvtfecbefcoreravr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14927)
)
perEvtfecbefcoreravr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecbefcoreravr.setStatus(
        "current"
    )

perEvtApdtemmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14976)
)
perEvtApdtemmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdtemmax.setStatus(
        "current"
    )

perEvtApdtemmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14977)
)
perEvtApdtemmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdtemmin.setStatus(
        "current"
    )

perEvtApdtemcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14978)
)
perEvtApdtemcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdtemcur.setStatus(
        "current"
    )

perEvtBdtempmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14991)
)
perEvtBdtempmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBdtempmax.setStatus(
        "current"
    )

perEvtBdtempmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14992)
)
perEvtBdtempmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBdtempmin.setStatus(
        "current"
    )

perEvtBdtempcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14993)
)
perEvtBdtempcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBdtempcur.setStatus(
        "current"
    )

perEvtApdcoolmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14994)
)
perEvtApdcoolmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdcoolmax.setStatus(
        "current"
    )

perEvtApdcoolmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14995)
)
perEvtApdcoolmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdcoolmin.setStatus(
        "current"
    )

perEvtApdcoolcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 14996)
)
perEvtApdcoolcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtApdcoolcur.setStatus(
        "current"
    )

perEvtfecbefcorerfloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15009)
)
perEvtfecbefcorerfloat.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecbefcorerfloat.setStatus(
        "current"
    )

perEvtfecaftcorerfloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15010)
)
perEvtfecaftcorerfloat.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtfecaftcorerfloat.setStatus(
        "current"
    )

perEvtOdu0PmBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15054)
)
perEvtOdu0PmBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmBbe.setStatus(
        "current"
    )

perEvtOdu0PmEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15055)
)
perEvtOdu0PmEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmEs.setStatus(
        "current"
    )

perEvtOdu0PmSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15056)
)
perEvtOdu0PmSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmSes.setStatus(
        "current"
    )

perEvtOdu0PmUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15057)
)
perEvtOdu0PmUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmUas.setStatus(
        "current"
    )

perEvtOdu0PmSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15058)
)
perEvtOdu0PmSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmSesr.setStatus(
        "current"
    )

perEvtOdu0PmBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15059)
)
perEvtOdu0PmBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmBber.setStatus(
        "current"
    )

perEvtOdu0PmFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15060)
)
perEvtOdu0PmFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFebbe.setStatus(
        "current"
    )

perEvtOdu0PmFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15061)
)
perEvtOdu0PmFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFees.setStatus(
        "current"
    )

perEvtOdu0PmFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15062)
)
perEvtOdu0PmFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFeses.setStatus(
        "current"
    )

perEvtOdu0PmFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15063)
)
perEvtOdu0PmFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFeuas.setStatus(
        "current"
    )

perEvtOdu0PmFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15064)
)
perEvtOdu0PmFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFesesr.setStatus(
        "current"
    )

perEvtOdu0PmFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15065)
)
perEvtOdu0PmFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmFebber.setStatus(
        "current"
    )

perEvtOscBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15074)
)
perEvtOscBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscBbe.setStatus(
        "current"
    )

perEvtOscEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15075)
)
perEvtOscEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscEs.setStatus(
        "current"
    )

perEvtOscSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15076)
)
perEvtOscSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscSes.setStatus(
        "current"
    )

perEvtOscUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15077)
)
perEvtOscUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscUas.setStatus(
        "current"
    )

perEvtOscSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15078)
)
perEvtOscSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscSesr.setStatus(
        "current"
    )

perEvtOscBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15079)
)
perEvtOscBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscBber.setStatus(
        "current"
    )

perEvtOscFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15080)
)
perEvtOscFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFebbe.setStatus(
        "current"
    )

perEvtOscFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15081)
)
perEvtOscFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFees.setStatus(
        "current"
    )

perEvtOscFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15082)
)
perEvtOscFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFeses.setStatus(
        "current"
    )

perEvtOscFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15083)
)
perEvtOscFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFeuas.setStatus(
        "current"
    )

perEvtOscFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15084)
)
perEvtOscFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFesesr.setStatus(
        "current"
    )

perEvtOscFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15085)
)
perEvtOscFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscFebber.setStatus(
        "current"
    )

perEvtOscIaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15086)
)
perEvtOscIaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscIaes.setStatus(
        "current"
    )

perEvtOscBiaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15087)
)
perEvtOscBiaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOscBiaes.setStatus(
        "current"
    )

perEvtMaxfreqdev = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15088)
)
perEvtMaxfreqdev.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxfreqdev.setStatus(
        "current"
    )

perEvtMinfreqdev = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15089)
)
perEvtMinfreqdev.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinfreqdev.setStatus(
        "current"
    )

perEvtAvgfreqdev = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15090)
)
perEvtAvgfreqdev.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgfreqdev.setStatus(
        "current"
    )

perEvtMaxphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15091)
)
perEvtMaxphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxphaseoffset.setStatus(
        "current"
    )

perEvtMinphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15092)
)
perEvtMinphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinphaseoffset.setStatus(
        "current"
    )

perEvtAvgphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15093)
)
perEvtAvgphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgphaseoffset.setStatus(
        "current"
    )

perEvtMaxmeanpathdelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15094)
)
perEvtMaxmeanpathdelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxmeanpathdelay.setStatus(
        "current"
    )

perEvtMinmeanpathdelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15095)
)
perEvtMinmeanpathdelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinmeanpathdelay.setStatus(
        "current"
    )

perEvtAvgmeanpathdelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15096)
)
perEvtAvgmeanpathdelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgmeanpathdelay.setStatus(
        "current"
    )

perEvtMaxpositivedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15103)
)
perEvtMaxpositivedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxpositivedelay.setStatus(
        "current"
    )

perEvtMinpositivedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15104)
)
perEvtMinpositivedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinpositivedelay.setStatus(
        "current"
    )

perEvtAvgpositivedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15105)
)
perEvtAvgpositivedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgpositivedelay.setStatus(
        "current"
    )

perEvtMaxnegativedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15106)
)
perEvtMaxnegativedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxnegativedelay.setStatus(
        "current"
    )

perEvtMinnegativedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15107)
)
perEvtMinnegativedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinnegativedelay.setStatus(
        "current"
    )

perEvtAvgnegativedelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15108)
)
perEvtAvgnegativedelay.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgnegativedelay.setStatus(
        "current"
    )

perEvtOtu4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15109)
)
perEvtOtu4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Iaes.setStatus(
        "current"
    )

perEvtOtu4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15110)
)
perEvtOtu4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Biaes.setStatus(
        "current"
    )

perEvtOtu4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15111)
)
perEvtOtu4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Bbe.setStatus(
        "current"
    )

perEvtOtu4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15112)
)
perEvtOtu4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Es.setStatus(
        "current"
    )

perEvtOtu4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15113)
)
perEvtOtu4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Ses.setStatus(
        "current"
    )

perEvtOtu4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15114)
)
perEvtOtu4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Uas.setStatus(
        "current"
    )

perEvtOtu4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15115)
)
perEvtOtu4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Sesr.setStatus(
        "current"
    )

perEvtOtu4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15116)
)
perEvtOtu4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Bber.setStatus(
        "current"
    )

perEvtOtu4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15117)
)
perEvtOtu4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Febbe.setStatus(
        "current"
    )

perEvtOtu4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15118)
)
perEvtOtu4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Fees.setStatus(
        "current"
    )

perEvtOtu4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15119)
)
perEvtOtu4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Feses.setStatus(
        "current"
    )

perEvtOtu4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15120)
)
perEvtOtu4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Feuas.setStatus(
        "current"
    )

perEvtOtu4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15121)
)
perEvtOtu4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Fesesr.setStatus(
        "current"
    )

perEvtOtu4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15122)
)
perEvtOtu4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Febber.setStatus(
        "current"
    )

perEvtOdu4Pmbbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15123)
)
perEvtOdu4Pmbbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmbbe.setStatus(
        "current"
    )

perEvtOdu4Pmes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15124)
)
perEvtOdu4Pmes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmes.setStatus(
        "current"
    )

perEvtOdu4Pmses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15125)
)
perEvtOdu4Pmses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmses.setStatus(
        "current"
    )

perEvtOtu4Pmuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15126)
)
perEvtOtu4Pmuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu4Pmuas.setStatus(
        "current"
    )

perEvtOdu4Pmsesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15127)
)
perEvtOdu4Pmsesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmsesr.setStatus(
        "current"
    )

perEvtOdu4Pmbber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15128)
)
perEvtOdu4Pmbber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmbber.setStatus(
        "current"
    )

perEvtOdu4Pmfebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15129)
)
perEvtOdu4Pmfebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfebbe.setStatus(
        "current"
    )

perEvtOdu4Pmfees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15130)
)
perEvtOdu4Pmfees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfees.setStatus(
        "current"
    )

perEvtOdu4Pmfeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15131)
)
perEvtOdu4Pmfeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfeses.setStatus(
        "current"
    )

perEvtOdu4Pmfeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15132)
)
perEvtOdu4Pmfeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfeuas.setStatus(
        "current"
    )

perEvtOdu4Pmfesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15133)
)
perEvtOdu4Pmfesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfesesr.setStatus(
        "current"
    )

perEvtOdu4Pmfebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15134)
)
perEvtOdu4Pmfebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Pmfebber.setStatus(
        "current"
    )

perEvtOdu4Tcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15135)
)
perEvtOdu4Tcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15136)
)
perEvtOdu4Tcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15137)
)
perEvtOdu4Tcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15138)
)
perEvtOdu4Tcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15139)
)
perEvtOdu4Tcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15140)
)
perEvtOdu4Tcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Iaes.setStatus(
        "current"
    )

perEvtOdu4Tcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15141)
)
perEvtOdu4Tcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15142)
)
perEvtOdu4Tcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15143)
)
perEvtOdu4Tcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15144)
)
perEvtOdu4Tcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15145)
)
perEvtOdu4Tcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15146)
)
perEvtOdu4Tcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Biaes.setStatus(
        "current"
    )

perEvtOdu4Tcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15147)
)
perEvtOdu4Tcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15148)
)
perEvtOdu4Tcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Es.setStatus(
        "current"
    )

perEvtOdu4Tcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15149)
)
perEvtOdu4Tcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15150)
)
perEvtOdu4Tcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15151)
)
perEvtOdu4Tcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15152)
)
perEvtOdu4Tcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15153)
)
perEvtOdu4Tcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15154)
)
perEvtOdu4Tcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Es.setStatus(
        "current"
    )

perEvtOdu4Tcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15155)
)
perEvtOdu4Tcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15156)
)
perEvtOdu4Tcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15157)
)
perEvtOdu4Tcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15158)
)
perEvtOdu4Tcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15159)
)
perEvtOdu4Tcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15160)
)
perEvtOdu4Tcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Es.setStatus(
        "current"
    )

perEvtOdu4Tcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15161)
)
perEvtOdu4Tcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15162)
)
perEvtOdu4Tcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15163)
)
perEvtOdu4Tcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15164)
)
perEvtOdu4Tcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15165)
)
perEvtOdu4Tcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15166)
)
perEvtOdu4Tcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Es.setStatus(
        "current"
    )

perEvtOdu4Tcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15167)
)
perEvtOdu4Tcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15168)
)
perEvtOdu4Tcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15169)
)
perEvtOdu4Tcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15170)
)
perEvtOdu4Tcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15171)
)
perEvtOdu4Tcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15172)
)
perEvtOdu4Tcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Es.setStatus(
        "current"
    )

perEvtOdu4Tcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15173)
)
perEvtOdu4Tcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15174)
)
perEvtOdu4Tcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15175)
)
perEvtOdu4Tcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15176)
)
perEvtOdu4Tcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15177)
)
perEvtOdu4Tcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Bbe.setStatus(
        "current"
    )

perEvtOdu4Tcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15178)
)
perEvtOdu4Tcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Es.setStatus(
        "current"
    )

perEvtOdu4Tcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15179)
)
perEvtOdu4Tcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Ses.setStatus(
        "current"
    )

perEvtOdu4Tcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15180)
)
perEvtOdu4Tcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Uas.setStatus(
        "current"
    )

perEvtOdu4Tcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15181)
)
perEvtOdu4Tcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Sesr.setStatus(
        "current"
    )

perEvtOdu4Tcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15182)
)
perEvtOdu4Tcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Bber.setStatus(
        "current"
    )

perEvtOdu4Tcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15183)
)
perEvtOdu4Tcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15184)
)
perEvtOdu4Tcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15185)
)
perEvtOdu4Tcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15186)
)
perEvtOdu4Tcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15187)
)
perEvtOdu4Tcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15188)
)
perEvtOdu4Tcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Febber.setStatus(
        "current"
    )

perEvtOdu4Tcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15189)
)
perEvtOdu4Tcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15190)
)
perEvtOdu4Tcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15191)
)
perEvtOdu4Tcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15192)
)
perEvtOdu4Tcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15193)
)
perEvtOdu4Tcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15194)
)
perEvtOdu4Tcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Febber.setStatus(
        "current"
    )

perEvtOdu4Tcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15195)
)
perEvtOdu4Tcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15196)
)
perEvtOdu4Tcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15197)
)
perEvtOdu4Tcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15198)
)
perEvtOdu4Tcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15199)
)
perEvtOdu4Tcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15200)
)
perEvtOdu4Tcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Febber.setStatus(
        "current"
    )

perEvtOdu4Tcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15201)
)
perEvtOdu4Tcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15202)
)
perEvtOdu4Tcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15203)
)
perEvtOdu4Tcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15204)
)
perEvtOdu4Tcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15205)
)
perEvtOdu4Tcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15206)
)
perEvtOdu4Tcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Febber.setStatus(
        "current"
    )

perEvtOdu4Tcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15207)
)
perEvtOdu4Tcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15208)
)
perEvtOdu4Tcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15209)
)
perEvtOdu4Tcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15210)
)
perEvtOdu4Tcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15211)
)
perEvtOdu4Tcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15212)
)
perEvtOdu4Tcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Febber.setStatus(
        "current"
    )

perEvtOdu4Tcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15213)
)
perEvtOdu4Tcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Febbe.setStatus(
        "current"
    )

perEvtOdu4Tcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15214)
)
perEvtOdu4Tcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Fees.setStatus(
        "current"
    )

perEvtOdu4Tcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15215)
)
perEvtOdu4Tcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Feses.setStatus(
        "current"
    )

perEvtOdu4Tcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15216)
)
perEvtOdu4Tcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Feuas.setStatus(
        "current"
    )

perEvtOdu4Tcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15217)
)
perEvtOdu4Tcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Fesesr.setStatus(
        "current"
    )

perEvtOdu4Tcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15218)
)
perEvtOdu4Tcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Febber.setStatus(
        "current"
    )

perEvtOduflexPmBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15267)
)
perEvtOduflexPmBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmBbe.setStatus(
        "current"
    )

perEvtOduflexPmEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15268)
)
perEvtOduflexPmEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmEs.setStatus(
        "current"
    )

perEvtOduflexPmSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15269)
)
perEvtOduflexPmSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmSes.setStatus(
        "current"
    )

perEvtOduflexPmUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15270)
)
perEvtOduflexPmUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmUas.setStatus(
        "current"
    )

perEvtOduflexPmSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15271)
)
perEvtOduflexPmSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmSesr.setStatus(
        "current"
    )

perEvtOduflexPmBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15272)
)
perEvtOduflexPmBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmBber.setStatus(
        "current"
    )

perEvtOduflexPmFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15273)
)
perEvtOduflexPmFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFebbe.setStatus(
        "current"
    )

perEvtOduflexPmFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15274)
)
perEvtOduflexPmFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFees.setStatus(
        "current"
    )

perEvtOduflexPmFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15275)
)
perEvtOduflexPmFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFeses.setStatus(
        "current"
    )

perEvtOduflexPmFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15276)
)
perEvtOduflexPmFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFeuas.setStatus(
        "current"
    )

perEvtOduflexPmFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15277)
)
perEvtOduflexPmFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFesesr.setStatus(
        "current"
    )

perEvtOduflexPmFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15278)
)
perEvtOduflexPmFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmFebber.setStatus(
        "current"
    )

perEvtOdu0Tcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15279)
)
perEvtOdu0Tcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15280)
)
perEvtOdu0Tcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Es.setStatus(
        "current"
    )

perEvtOdu0Tcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15281)
)
perEvtOdu0Tcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15282)
)
perEvtOdu0Tcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15283)
)
perEvtOdu0Tcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15284)
)
perEvtOdu0Tcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15285)
)
perEvtOdu0Tcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15286)
)
perEvtOdu0Tcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15287)
)
perEvtOdu0Tcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15288)
)
perEvtOdu0Tcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15289)
)
perEvtOdu0Tcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15290)
)
perEvtOdu0Tcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15291)
)
perEvtOdu0Tcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15292)
)
perEvtOdu0Tcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Biaes.setStatus(
        "current"
    )

perEvtOdu0Tcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15293)
)
perEvtOdu0Tcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15294)
)
perEvtOdu0Tcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Es.setStatus(
        "current"
    )

perEvtOdu0Tcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15295)
)
perEvtOdu0Tcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15296)
)
perEvtOdu0Tcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15297)
)
perEvtOdu0Tcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15298)
)
perEvtOdu0Tcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15299)
)
perEvtOdu0Tcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15300)
)
perEvtOdu0Tcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15301)
)
perEvtOdu0Tcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15302)
)
perEvtOdu0Tcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15303)
)
perEvtOdu0Tcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15304)
)
perEvtOdu0Tcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15305)
)
perEvtOdu0Tcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15306)
)
perEvtOdu0Tcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Biaes.setStatus(
        "current"
    )

perEvtOdu0Tcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15307)
)
perEvtOdu0Tcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15308)
)
perEvtOdu0Tcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Es.setStatus(
        "current"
    )

perEvtOdu0Tcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15309)
)
perEvtOdu0Tcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15310)
)
perEvtOdu0Tcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15311)
)
perEvtOdu0Tcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15312)
)
perEvtOdu0Tcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15313)
)
perEvtOdu0Tcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15314)
)
perEvtOdu0Tcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15315)
)
perEvtOdu0Tcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15316)
)
perEvtOdu0Tcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15317)
)
perEvtOdu0Tcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15318)
)
perEvtOdu0Tcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15319)
)
perEvtOdu0Tcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15320)
)
perEvtOdu0Tcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Biaes.setStatus(
        "current"
    )

perEvtOdu0Tcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15321)
)
perEvtOdu0Tcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15322)
)
perEvtOdu0Tcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Es.setStatus(
        "current"
    )

perEvtOdu0Tcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15323)
)
perEvtOdu0Tcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15324)
)
perEvtOdu0Tcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15325)
)
perEvtOdu0Tcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15326)
)
perEvtOdu0Tcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15327)
)
perEvtOdu0Tcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15328)
)
perEvtOdu0Tcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15329)
)
perEvtOdu0Tcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15330)
)
perEvtOdu0Tcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15331)
)
perEvtOdu0Tcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15332)
)
perEvtOdu0Tcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15333)
)
perEvtOdu0Tcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15334)
)
perEvtOdu0Tcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Biaes.setStatus(
        "current"
    )

perEvtOdu0Tcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15335)
)
perEvtOdu0Tcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15336)
)
perEvtOdu0Tcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Es.setStatus(
        "current"
    )

perEvtOdu0Tcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15337)
)
perEvtOdu0Tcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15338)
)
perEvtOdu0Tcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15339)
)
perEvtOdu0Tcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15340)
)
perEvtOdu0Tcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15341)
)
perEvtOdu0Tcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15342)
)
perEvtOdu0Tcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15343)
)
perEvtOdu0Tcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15344)
)
perEvtOdu0Tcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15345)
)
perEvtOdu0Tcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15346)
)
perEvtOdu0Tcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15347)
)
perEvtOdu0Tcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15348)
)
perEvtOdu0Tcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Biaes.setStatus(
        "current"
    )

perEvtOdu0Tcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15349)
)
perEvtOdu0Tcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Bbe.setStatus(
        "current"
    )

perEvtOdu0Tcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15350)
)
perEvtOdu0Tcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Es.setStatus(
        "current"
    )

perEvtOdu0Tcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15351)
)
perEvtOdu0Tcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Ses.setStatus(
        "current"
    )

perEvtOdu0Tcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15352)
)
perEvtOdu0Tcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Uas.setStatus(
        "current"
    )

perEvtOdu0Tcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15353)
)
perEvtOdu0Tcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Sesr.setStatus(
        "current"
    )

perEvtOdu0Tcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15354)
)
perEvtOdu0Tcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Bber.setStatus(
        "current"
    )

perEvtOdu0Tcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15355)
)
perEvtOdu0Tcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Febbe.setStatus(
        "current"
    )

perEvtOdu0Tcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15356)
)
perEvtOdu0Tcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Fees.setStatus(
        "current"
    )

perEvtOdu0Tcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15357)
)
perEvtOdu0Tcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Feses.setStatus(
        "current"
    )

perEvtOdu0Tcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15358)
)
perEvtOdu0Tcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Feuas.setStatus(
        "current"
    )

perEvtOdu0Tcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15359)
)
perEvtOdu0Tcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Fesesr.setStatus(
        "current"
    )

perEvtOdu0Tcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15360)
)
perEvtOdu0Tcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Febber.setStatus(
        "current"
    )

perEvtOdu0Tcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15361)
)
perEvtOdu0Tcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Iaes.setStatus(
        "current"
    )

perEvtOdu0Tcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15362)
)
perEvtOdu0Tcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Biaes.setStatus(
        "current"
    )

perEvtpmdmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15378)
)
perEvtpmdmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpmdmax.setStatus(
        "current"
    )

perEvtpmdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15379)
)
perEvtpmdmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpmdmin.setStatus(
        "current"
    )

perEvtpmdcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15380)
)
perEvtpmdcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpmdcur.setStatus(
        "current"
    )

perEvtpeakInpowerMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15381)
)
perEvtpeakInpowerMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakInpowerMax.setStatus(
        "current"
    )

perEvtpeakInpowerCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15382)
)
perEvtpeakInpowerCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakInpowerCur.setStatus(
        "current"
    )

perEvtpeakInpowerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15383)
)
perEvtpeakInpowerMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakInpowerMin.setStatus(
        "current"
    )

perEvtvalleyInpowerMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15384)
)
perEvtvalleyInpowerMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyInpowerMax.setStatus(
        "current"
    )

perEvtvalleyInpowerCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15385)
)
perEvtvalleyInpowerCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyInpowerCur.setStatus(
        "current"
    )

perEvtvalleyInpowerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15386)
)
perEvtvalleyInpowerMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyInpowerMin.setStatus(
        "current"
    )

perEvtpeakOutpowerMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15387)
)
perEvtpeakOutpowerMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakOutpowerMax.setStatus(
        "current"
    )

perEvtpeakOutpowerCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15388)
)
perEvtpeakOutpowerCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakOutpowerCur.setStatus(
        "current"
    )

perEvtpeakOutpowerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15389)
)
perEvtpeakOutpowerMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpeakOutpowerMin.setStatus(
        "current"
    )

perEvtvalleyOutpowerMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15390)
)
perEvtvalleyOutpowerMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyOutpowerMax.setStatus(
        "current"
    )

perEvtvalleyOutpowerCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15391)
)
perEvtvalleyOutpowerCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyOutpowerCur.setStatus(
        "current"
    )

perEvtvalleyOutpowerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15392)
)
perEvtvalleyOutpowerMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtvalleyOutpowerMin.setStatus(
        "current"
    )

perEvtPeakLstmpMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15393)
)
perEvtPeakLstmpMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLstmpMax.setStatus(
        "current"
    )

perEvtPeakLstmpCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15394)
)
perEvtPeakLstmpCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLstmpCur.setStatus(
        "current"
    )

perEvtPeakLstmpMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15395)
)
perEvtPeakLstmpMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLstmpMin.setStatus(
        "current"
    )

perEvtValleyLstmpMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15396)
)
perEvtValleyLstmpMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLstmpMax.setStatus(
        "current"
    )

perEvtValleyLstmpCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15397)
)
perEvtValleyLstmpCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLstmpCur.setStatus(
        "current"
    )

perEvtValleyLstmpMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15398)
)
perEvtValleyLstmpMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLstmpMin.setStatus(
        "current"
    )

perEvtPeakLsbiasMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15399)
)
perEvtPeakLsbiasMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLsbiasMax.setStatus(
        "current"
    )

perEvtPeakLsbiasCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15400)
)
perEvtPeakLsbiasCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLsbiasCur.setStatus(
        "current"
    )

perEvtPeakLsbiasMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15401)
)
perEvtPeakLsbiasMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPeakLsbiasMin.setStatus(
        "current"
    )

perEvtValleyLsbiasMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15402)
)
perEvtValleyLsbiasMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLsbiasMax.setStatus(
        "current"
    )

perEvtValleyLsbiasCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15403)
)
perEvtValleyLsbiasCur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLsbiasCur.setStatus(
        "current"
    )

perEvtValleyLsbiasMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15404)
)
perEvtValleyLsbiasMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtValleyLsbiasMin.setStatus(
        "current"
    )

perEvtpmdavg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15416)
)
perEvtpmdavg.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtpmdavg.setStatus(
        "current"
    )

perEvtOdu0PmTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15423)
)
perEvtOdu0PmTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0PmTmp.setStatus(
        "current"
    )

perEvtOdu0Tcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15424)
)
perEvtOdu0Tcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm1Tmp.setStatus(
        "current"
    )

perEvtOdu0Tcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15425)
)
perEvtOdu0Tcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm2Tmp.setStatus(
        "current"
    )

perEvtOdu0Tcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15426)
)
perEvtOdu0Tcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm3Tmp.setStatus(
        "current"
    )

perEvtOdu0Tcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15427)
)
perEvtOdu0Tcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm4Tmp.setStatus(
        "current"
    )

perEvtOdu0Tcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15428)
)
perEvtOdu0Tcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm5Tmp.setStatus(
        "current"
    )

perEvtOdu0Tcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15429)
)
perEvtOdu0Tcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu0Tcm6Tmp.setStatus(
        "current"
    )

perEvtOtu1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15430)
)
perEvtOtu1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu1Tmp.setStatus(
        "current"
    )

perEvtOdu1PmTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15431)
)
perEvtOdu1PmTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1PmTmp.setStatus(
        "current"
    )

perEvtOdu1Tcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15432)
)
perEvtOdu1Tcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm1Tmp.setStatus(
        "current"
    )

perEvtOdu1Tcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15433)
)
perEvtOdu1Tcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm2Tmp.setStatus(
        "current"
    )

perEvtOdu1Tcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15434)
)
perEvtOdu1Tcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm3Tmp.setStatus(
        "current"
    )

perEvtOdu1Tcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15435)
)
perEvtOdu1Tcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm4Tmp.setStatus(
        "current"
    )

perEvtOdu1Tcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15436)
)
perEvtOdu1Tcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm5Tmp.setStatus(
        "current"
    )

perEvtOdu1Tcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15437)
)
perEvtOdu1Tcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu1Tcm6Tmp.setStatus(
        "current"
    )

perEvtOtu2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15438)
)
perEvtOtu2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu2Tmp.setStatus(
        "current"
    )

perEvtodu2Pmtmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15439)
)
perEvtodu2Pmtmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu2Pmtmp.setStatus(
        "current"
    )

perEvtOdu2Tcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15440)
)
perEvtOdu2Tcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm1Tmp.setStatus(
        "current"
    )

perEvtOdu2Tcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15441)
)
perEvtOdu2Tcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm2Tmp.setStatus(
        "current"
    )

perEvtOdu2Tcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15442)
)
perEvtOdu2Tcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm3Tmp.setStatus(
        "current"
    )

perEvtOdu2Tcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15443)
)
perEvtOdu2Tcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm4Tmp.setStatus(
        "current"
    )

perEvtOdu2Tcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15444)
)
perEvtOdu2Tcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm5Tmp.setStatus(
        "current"
    )

perEvtOdu2Tcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15445)
)
perEvtOdu2Tcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu2Tcm6Tmp.setStatus(
        "current"
    )

perEvtOtu3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15446)
)
perEvtOtu3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtu3Tmp.setStatus(
        "current"
    )

perEvtodu3Pmtmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15447)
)
perEvtodu3Pmtmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu3Pmtmp.setStatus(
        "current"
    )

perEvtOdu3Tcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15448)
)
perEvtOdu3Tcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm1Tmp.setStatus(
        "current"
    )

perEvtOdu3Tcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15449)
)
perEvtOdu3Tcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm2Tmp.setStatus(
        "current"
    )

perEvtOdu3Tcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15450)
)
perEvtOdu3Tcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm3Tmp.setStatus(
        "current"
    )

perEvtOdu3Tcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15451)
)
perEvtOdu3Tcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm4Tmp.setStatus(
        "current"
    )

perEvtOdu3Tcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15452)
)
perEvtOdu3Tcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm5Tmp.setStatus(
        "current"
    )

perEvtOdu3Tcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15453)
)
perEvtOdu3Tcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu3Tcm6Tmp.setStatus(
        "current"
    )

perEvtotu4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15454)
)
perEvtotu4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtotu4Tmp.setStatus(
        "current"
    )

perEvtodu4Pmtmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15455)
)
perEvtodu4Pmtmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtodu4Pmtmp.setStatus(
        "current"
    )

perEvtOdu4Tcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15456)
)
perEvtOdu4Tcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm1Tmp.setStatus(
        "current"
    )

perEvtOdu4Tcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15457)
)
perEvtOdu4Tcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm2Tmp.setStatus(
        "current"
    )

perEvtOdu4Tcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15458)
)
perEvtOdu4Tcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm3Tmp.setStatus(
        "current"
    )

perEvtOdu4Tcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15459)
)
perEvtOdu4Tcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm4Tmp.setStatus(
        "current"
    )

perEvtOdu4Tcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15460)
)
perEvtOdu4Tcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm5Tmp.setStatus(
        "current"
    )

perEvtOdu4Tcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15461)
)
perEvtOdu4Tcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOdu4Tcm6Tmp.setStatus(
        "current"
    )

perEvtOduflexPmTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15470)
)
perEvtOduflexPmTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexPmTmp.setStatus(
        "current"
    )

perEvtFecTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15471)
)
perEvtFecTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFecTmp.setStatus(
        "current"
    )

perEvtRsTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15472)
)
perEvtRsTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRsTmp.setStatus(
        "current"
    )

perEvtRmiopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15476)
)
perEvtRmiopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRmiopmax.setStatus(
        "current"
    )

perEvtRmiopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15477)
)
perEvtRmiopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRmiopmin.setStatus(
        "current"
    )

perEvtRmiopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15478)
)
perEvtRmiopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtRmiopcur.setStatus(
        "current"
    )

perEvtAswiopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15483)
)
perEvtAswiopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswiopmax.setStatus(
        "current"
    )

perEvtAswiopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15484)
)
perEvtAswiopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswiopmin.setStatus(
        "current"
    )

perEvtAswiopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15485)
)
perEvtAswiopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswiopcur.setStatus(
        "current"
    )

perEvtAaospcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15486)
)
perEvtAaospcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaospcur.setStatus(
        "current"
    )

perEvtAswoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15487)
)
perEvtAswoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswoopmax.setStatus(
        "current"
    )

perEvtAswoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15488)
)
perEvtAswoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswoopmin.setStatus(
        "current"
    )

perEvtAswoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15489)
)
perEvtAswoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswoopcur.setStatus(
        "current"
    )

perEvtAswsnrmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15490)
)
perEvtAswsnrmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnrmax.setStatus(
        "current"
    )

perEvtAswsnrmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15491)
)
perEvtAswsnrmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnrmin.setStatus(
        "current"
    )

perEvtAswsnrcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15492)
)
perEvtAswsnrcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnrcur.setStatus(
        "current"
    )

perEvtAswsnlmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15493)
)
perEvtAswsnlmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnlmax.setStatus(
        "current"
    )

perEvtAswsnlmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15494)
)
perEvtAswsnlmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnlmin.setStatus(
        "current"
    )

perEvtAswsnlcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15495)
)
perEvtAswsnlcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAswsnlcur.setStatus(
        "current"
    )

perEvtAainpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15496)
)
perEvtAainpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAainpmax.setStatus(
        "current"
    )

perEvtAainpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15497)
)
perEvtAainpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAainpmin.setStatus(
        "current"
    )

perEvtAainpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15498)
)
perEvtAainpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAainpcur.setStatus(
        "current"
    )

perEvtAaispmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15499)
)
perEvtAaispmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaispmax.setStatus(
        "current"
    )

perEvtAaispmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15500)
)
perEvtAaispmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaispmin.setStatus(
        "current"
    )

perEvtAaispcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15501)
)
perEvtAaispcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaispcur.setStatus(
        "current"
    )

perEvtAaonpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15502)
)
perEvtAaonpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaonpmax.setStatus(
        "current"
    )

perEvtAaonpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15503)
)
perEvtAaonpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaonpmin.setStatus(
        "current"
    )

perEvtAaonpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15504)
)
perEvtAaonpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaonpcur.setStatus(
        "current"
    )

perEvtAaospmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15505)
)
perEvtAaospmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaospmax.setStatus(
        "current"
    )

perEvtAaospmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15506)
)
perEvtAaospmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAaospmin.setStatus(
        "current"
    )

perEvtOduflexTcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15511)
)
perEvtOduflexTcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15512)
)
perEvtOduflexTcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Tmp.setStatus(
        "current"
    )

perEvtOduflexTcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15513)
)
perEvtOduflexTcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15514)
)
perEvtOduflexTcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Feses.setStatus(
        "current"
    )

perEvtOduflexTcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15515)
)
perEvtOduflexTcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Ses.setStatus(
        "current"
    )

perEvtOduflexTcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15516)
)
perEvtOduflexTcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Fees.setStatus(
        "current"
    )

perEvtOduflexTcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15517)
)
perEvtOduflexTcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Es.setStatus(
        "current"
    )

perEvtOduflexTcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15518)
)
perEvtOduflexTcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15519)
)
perEvtOduflexTcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Bber.setStatus(
        "current"
    )

perEvtOduflexTcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15520)
)
perEvtOduflexTcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15521)
)
perEvtOduflexTcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15522)
)
perEvtOduflexTcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Uas.setStatus(
        "current"
    )

perEvtOduflexTcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15523)
)
perEvtOduflexTcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15524)
)
perEvtOduflexTcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15525)
)
perEvtOduflexTcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Febber.setStatus(
        "current"
    )

perEvtOduflexTcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15526)
)
perEvtOduflexTcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm6Tmp.setStatus(
        "current"
    )

perEvtOduflexTcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15527)
)
perEvtOduflexTcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Uas.setStatus(
        "current"
    )

perEvtOduflexTcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15528)
)
perEvtOduflexTcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15529)
)
perEvtOduflexTcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Febber.setStatus(
        "current"
    )

perEvtOduflexTcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15530)
)
perEvtOduflexTcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15531)
)
perEvtOduflexTcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Bber.setStatus(
        "current"
    )

perEvtOduflexTcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15532)
)
perEvtOduflexTcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15533)
)
perEvtOduflexTcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Fees.setStatus(
        "current"
    )

perEvtOduflexTcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15534)
)
perEvtOduflexTcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15535)
)
perEvtOduflexTcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15536)
)
perEvtOduflexTcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Feses.setStatus(
        "current"
    )

perEvtOduflexTcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15537)
)
perEvtOduflexTcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Uas.setStatus(
        "current"
    )

perEvtOduflexTcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15538)
)
perEvtOduflexTcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Ses.setStatus(
        "current"
    )

perEvtOduflexTcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15539)
)
perEvtOduflexTcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Es.setStatus(
        "current"
    )

perEvtOduflexTcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15540)
)
perEvtOduflexTcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15541)
)
perEvtOduflexTcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15542)
)
perEvtOduflexTcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm5Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15543)
)
perEvtOduflexTcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15544)
)
perEvtOduflexTcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15545)
)
perEvtOduflexTcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Febber.setStatus(
        "current"
    )

perEvtOduflexTcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15546)
)
perEvtOduflexTcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15547)
)
perEvtOduflexTcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15548)
)
perEvtOduflexTcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Feses.setStatus(
        "current"
    )

perEvtOduflexTcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15549)
)
perEvtOduflexTcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Fees.setStatus(
        "current"
    )

perEvtOduflexTcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15550)
)
perEvtOduflexTcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15551)
)
perEvtOduflexTcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Uas.setStatus(
        "current"
    )

perEvtOduflexTcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15552)
)
perEvtOduflexTcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Ses.setStatus(
        "current"
    )

perEvtOduflexTcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15553)
)
perEvtOduflexTcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Bber.setStatus(
        "current"
    )

perEvtOduflexTcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15554)
)
perEvtOduflexTcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15555)
)
perEvtOduflexTcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Es.setStatus(
        "current"
    )

perEvtOduflexTcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15556)
)
perEvtOduflexTcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15557)
)
perEvtOduflexTcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm4Tmp.setStatus(
        "current"
    )

perEvtOduflexTcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15558)
)
perEvtOduflexTcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15559)
)
perEvtOduflexTcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15560)
)
perEvtOduflexTcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Febber.setStatus(
        "current"
    )

perEvtOduflexTcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15561)
)
perEvtOduflexTcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15562)
)
perEvtOduflexTcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15563)
)
perEvtOduflexTcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Feses.setStatus(
        "current"
    )

perEvtOduflexTcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15564)
)
perEvtOduflexTcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15565)
)
perEvtOduflexTcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Bber.setStatus(
        "current"
    )

perEvtOduflexTcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15566)
)
perEvtOduflexTcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Fees.setStatus(
        "current"
    )

perEvtOduflexTcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15567)
)
perEvtOduflexTcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15568)
)
perEvtOduflexTcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Es.setStatus(
        "current"
    )

perEvtOduflexTcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15569)
)
perEvtOduflexTcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Ses.setStatus(
        "current"
    )

perEvtOduflexTcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15570)
)
perEvtOduflexTcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Uas.setStatus(
        "current"
    )

perEvtOduflexTcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15571)
)
perEvtOduflexTcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm1Tmp.setStatus(
        "current"
    )

perEvtOduflexTcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15572)
)
perEvtOduflexTcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15573)
)
perEvtOduflexTcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Fees.setStatus(
        "current"
    )

perEvtOduflexTcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15574)
)
perEvtOduflexTcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Feses.setStatus(
        "current"
    )

perEvtOduflexTcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15575)
)
perEvtOduflexTcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15576)
)
perEvtOduflexTcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15577)
)
perEvtOduflexTcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Febber.setStatus(
        "current"
    )

perEvtOduflexTcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15578)
)
perEvtOduflexTcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15579)
)
perEvtOduflexTcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15580)
)
perEvtOduflexTcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Bber.setStatus(
        "current"
    )

perEvtOduflexTcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15581)
)
perEvtOduflexTcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15582)
)
perEvtOduflexTcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Es.setStatus(
        "current"
    )

perEvtOduflexTcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15583)
)
perEvtOduflexTcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Ses.setStatus(
        "current"
    )

perEvtOduflexTcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15584)
)
perEvtOduflexTcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15585)
)
perEvtOduflexTcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm2Tmp.setStatus(
        "current"
    )

perEvtOduflexTcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15586)
)
perEvtOduflexTcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Uas.setStatus(
        "current"
    )

perEvtOduflexTcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15587)
)
perEvtOduflexTcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Sesr.setStatus(
        "current"
    )

perEvtOduflexTcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15588)
)
perEvtOduflexTcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Ses.setStatus(
        "current"
    )

perEvtOduflexTcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15589)
)
perEvtOduflexTcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Fees.setStatus(
        "current"
    )

perEvtOduflexTcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15590)
)
perEvtOduflexTcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Feses.setStatus(
        "current"
    )

perEvtOduflexTcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15591)
)
perEvtOduflexTcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Bber.setStatus(
        "current"
    )

perEvtOduflexTcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15592)
)
perEvtOduflexTcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Febbe.setStatus(
        "current"
    )

perEvtOduflexTcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15593)
)
perEvtOduflexTcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Febber.setStatus(
        "current"
    )

perEvtOduflexTcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15594)
)
perEvtOduflexTcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Feuas.setStatus(
        "current"
    )

perEvtOduflexTcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15595)
)
perEvtOduflexTcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Fesesr.setStatus(
        "current"
    )

perEvtOduflexTcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15596)
)
perEvtOduflexTcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Bbe.setStatus(
        "current"
    )

perEvtOduflexTcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15597)
)
perEvtOduflexTcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Es.setStatus(
        "current"
    )

perEvtOduflexTcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15598)
)
perEvtOduflexTcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Biaes.setStatus(
        "current"
    )

perEvtOduflexTcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15599)
)
perEvtOduflexTcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Iaes.setStatus(
        "current"
    )

perEvtOduflexTcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15600)
)
perEvtOduflexTcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOduflexTcm3Tmp.setStatus(
        "current"
    )

perEvtethBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15601)
)
perEvtethBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethBbe.setStatus(
        "current"
    )

perEvtethBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15602)
)
perEvtethBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethBber.setStatus(
        "current"
    )

perEvtethSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15603)
)
perEvtethSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethSesr.setStatus(
        "current"
    )

perEvtethUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15604)
)
perEvtethUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethUas.setStatus(
        "current"
    )

perEvtethEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15605)
)
perEvtethEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethEs.setStatus(
        "current"
    )

perEvtethSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15606)
)
perEvtethSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtethSes.setStatus(
        "current"
    )

perEvtAmbtempmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15623)
)
perEvtAmbtempmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAmbtempmax.setStatus(
        "current"
    )

perEvtAmbtempmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15624)
)
perEvtAmbtempmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAmbtempmin.setStatus(
        "current"
    )

perEvtAmbtempcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15625)
)
perEvtAmbtempcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAmbtempcur.setStatus(
        "current"
    )

perEvtEthEsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15626)
)
perEvtEthEsr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEthEsr.setStatus(
        "current"
    )

perEvtOtucnBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15627)
)
perEvtOtucnBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnBbe.setStatus(
        "current"
    )

perEvtOtucnFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15628)
)
perEvtOtucnFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFees.setStatus(
        "current"
    )

perEvtOtucnFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15629)
)
perEvtOtucnFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFebbe.setStatus(
        "current"
    )

perEvtOtucnBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15630)
)
perEvtOtucnBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnBber.setStatus(
        "current"
    )

perEvtOtucnSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15631)
)
perEvtOtucnSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnSesr.setStatus(
        "current"
    )

perEvtOtucnFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15632)
)
perEvtOtucnFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFeses.setStatus(
        "current"
    )

perEvtOtucnBiaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15633)
)
perEvtOtucnBiaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnBiaes.setStatus(
        "current"
    )

perEvtOtucnUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15634)
)
perEvtOtucnUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnUas.setStatus(
        "current"
    )

perEvtOtucnSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15635)
)
perEvtOtucnSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnSes.setStatus(
        "current"
    )

perEvtOtucnEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15636)
)
perEvtOtucnEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnEs.setStatus(
        "current"
    )

perEvtOtucnIaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15637)
)
perEvtOtucnIaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnIaes.setStatus(
        "current"
    )

perEvtOtucnFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15638)
)
perEvtOtucnFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFebber.setStatus(
        "current"
    )

perEvtOtucnFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15639)
)
perEvtOtucnFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFeuas.setStatus(
        "current"
    )

perEvtOtucnTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15640)
)
perEvtOtucnTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnTmp.setStatus(
        "current"
    )

perEvtOtucnFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15641)
)
perEvtOtucnFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOtucnFesesr.setStatus(
        "current"
    )

perEvtOducnPmFesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15642)
)
perEvtOducnPmFesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFesesr.setStatus(
        "current"
    )

perEvtOducnPmFebber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15643)
)
perEvtOducnPmFebber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFebber.setStatus(
        "current"
    )

perEvtOducnPmFees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15644)
)
perEvtOducnPmFees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFees.setStatus(
        "current"
    )

perEvtOducnPmFeses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15645)
)
perEvtOducnPmFeses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFeses.setStatus(
        "current"
    )

perEvtOducnPmFeuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15646)
)
perEvtOducnPmFeuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFeuas.setStatus(
        "current"
    )

perEvtOducnPmEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15647)
)
perEvtOducnPmEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmEs.setStatus(
        "current"
    )

perEvtOducnPmSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15648)
)
perEvtOducnPmSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmSes.setStatus(
        "current"
    )

perEvtOducnPmBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15649)
)
perEvtOducnPmBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmBbe.setStatus(
        "current"
    )

perEvtOducnPmBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15650)
)
perEvtOducnPmBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmBber.setStatus(
        "current"
    )

perEvtOducnPmFebbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15651)
)
perEvtOducnPmFebbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmFebbe.setStatus(
        "current"
    )

perEvtOducnPmUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15652)
)
perEvtOducnPmUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmUas.setStatus(
        "current"
    )

perEvtOducnPmSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15653)
)
perEvtOducnPmSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmSesr.setStatus(
        "current"
    )

perEvtOducnPmTmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15654)
)
perEvtOducnPmTmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnPmTmp.setStatus(
        "current"
    )

perEvtCfpLsiopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15656)
)
perEvtCfpLsiopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsiopmax.setStatus(
        "current"
    )

perEvtCfpLsiopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15657)
)
perEvtCfpLsiopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsiopmin.setStatus(
        "current"
    )

perEvtCfpLsiopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15658)
)
perEvtCfpLsiopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsiopcur.setStatus(
        "current"
    )

perEvtCfpLsoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15660)
)
perEvtCfpLsoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsoopmax.setStatus(
        "current"
    )

perEvtCfpLsoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15661)
)
perEvtCfpLsoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsoopmin.setStatus(
        "current"
    )

perEvtCfpLsoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15662)
)
perEvtCfpLsoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsoopcur.setStatus(
        "current"
    )

perEvtCfpLstmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15664)
)
perEvtCfpLstmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLstmpmax.setStatus(
        "current"
    )

perEvtCfpLstmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15665)
)
perEvtCfpLstmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLstmpmin.setStatus(
        "current"
    )

perEvtCfpLstmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15666)
)
perEvtCfpLstmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLstmpcur.setStatus(
        "current"
    )

perEvtCfpLsbiasmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15668)
)
perEvtCfpLsbiasmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsbiasmax.setStatus(
        "current"
    )

perEvtCfpLsbiasmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15669)
)
perEvtCfpLsbiasmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsbiasmin.setStatus(
        "current"
    )

perEvtCfpLsbiascur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15670)
)
perEvtCfpLsbiascur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtCfpLsbiascur.setStatus(
        "current"
    )

perEvtMaxsumphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15671)
)
perEvtMaxsumphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMaxsumphaseoffset.setStatus(
        "current"
    )

perEvtMinsumphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15672)
)
perEvtMinsumphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMinsumphaseoffset.setStatus(
        "current"
    )

perEvtAvgsumphaseoffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15673)
)
perEvtAvgsumphaseoffset.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAvgsumphaseoffset.setStatus(
        "current"
    )

perEvtQValueEerAver15m = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15674)
)
perEvtQValueEerAver15m.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtQValueEerAver15m.setStatus(
        "current"
    )

perEvtQValueEerAver24h = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15675)
)
perEvtQValueEerAver24h.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtQValueEerAver24h.setStatus(
        "current"
    )

perEvtPumporpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15862)
)
perEvtPumporpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPumporpcur.setStatus(
        "current"
    )

perEvtPumporpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15863)
)
perEvtPumporpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPumporpmax.setStatus(
        "current"
    )

perEvtPumporpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15864)
)
perEvtPumporpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPumporpmin.setStatus(
        "current"
    )

perEvtFswiopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15868)
)
perEvtFswiopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswiopmax.setStatus(
        "current"
    )

perEvtFswiopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15869)
)
perEvtFswiopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswiopmin.setStatus(
        "current"
    )

perEvtFswiopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15870)
)
perEvtFswiopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswiopcur.setStatus(
        "current"
    )

perEvtFswoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15871)
)
perEvtFswoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswoopmax.setStatus(
        "current"
    )

perEvtFswoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15872)
)
perEvtFswoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswoopmin.setStatus(
        "current"
    )

perEvtFswoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15873)
)
perEvtFswoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswoopcur.setStatus(
        "current"
    )

perEvtFswsnrmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15874)
)
perEvtFswsnrmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnrmax.setStatus(
        "current"
    )

perEvtFswsnrmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15875)
)
perEvtFswsnrmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnrmin.setStatus(
        "current"
    )

perEvtFswsnrcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15876)
)
perEvtFswsnrcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnrcur.setStatus(
        "current"
    )

perEvtFswsnlmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15877)
)
perEvtFswsnlmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnlmax.setStatus(
        "current"
    )

perEvtFswsnlmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15878)
)
perEvtFswsnlmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnlmin.setStatus(
        "current"
    )

perEvtFswsnlcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15879)
)
perEvtFswsnlcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFswsnlcur.setStatus(
        "current"
    )

perEvtFclsopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15880)
)
perEvtFclsopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFclsopmax.setStatus(
        "current"
    )

perEvtFclsopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15881)
)
perEvtFclsopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFclsopmin.setStatus(
        "current"
    )

perEvtFclsopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15882)
)
perEvtFclsopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFclsopcur.setStatus(
        "current"
    )

perEvtlanelsoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15883)
)
perEvtlanelsoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsoopmax.setStatus(
        "current"
    )

perEvtlanelsoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15884)
)
perEvtlanelsoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsoopmin.setStatus(
        "current"
    )

perEvtlanelsoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15885)
)
perEvtlanelsoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsoopcur.setStatus(
        "current"
    )

perEvtlanelsiopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15886)
)
perEvtlanelsiopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsiopmax.setStatus(
        "current"
    )

perEvtlanelsiopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15887)
)
perEvtlanelsiopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsiopmin.setStatus(
        "current"
    )

perEvtlanelsiopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15888)
)
perEvtlanelsiopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsiopcur.setStatus(
        "current"
    )

perEvtlanelsbiasmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15889)
)
perEvtlanelsbiasmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsbiasmax.setStatus(
        "current"
    )

perEvtlanelsbiasmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15890)
)
perEvtlanelsbiasmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsbiasmin.setStatus(
        "current"
    )

perEvtlanelsbiascur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15891)
)
perEvtlanelsbiascur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtlanelsbiascur.setStatus(
        "current"
    )

perEvtSubcardtmpmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15900)
)
perEvtSubcardtmpmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSubcardtmpmax.setStatus(
        "current"
    )

perEvtSubcardtmpmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15901)
)
perEvtSubcardtmpmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSubcardtmpmin.setStatus(
        "current"
    )

perEvtSubcardtmpcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15902)
)
perEvtSubcardtmpcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSubcardtmpcur.setStatus(
        "current"
    )

perEvtSdiBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15913)
)
perEvtSdiBbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiBbe.setStatus(
        "current"
    )

perEvtSdiBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15914)
)
perEvtSdiBber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiBber.setStatus(
        "current"
    )

perEvtSdiSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15915)
)
perEvtSdiSesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiSesr.setStatus(
        "current"
    )

perEvtSdiUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15916)
)
perEvtSdiUas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiUas.setStatus(
        "current"
    )

perEvtSdiEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15917)
)
perEvtSdiEs.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiEs.setStatus(
        "current"
    )

perEvtSdiSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15918)
)
perEvtSdiSes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSdiSes.setStatus(
        "current"
    )

perEvtFpclswlomax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15920)
)
perEvtFpclswlomax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFpclswlomax.setStatus(
        "current"
    )

perEvtFpclswlomin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15921)
)
perEvtFpclswlomin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFpclswlomin.setStatus(
        "current"
    )

perEvtFpclswlocur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15922)
)
perEvtFpclswlocur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFpclswlocur.setStatus(
        "current"
    )

perEvtGaincur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15980)
)
perEvtGaincur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtGaincur.setStatus(
        "current"
    )

perEvtGainmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15981)
)
perEvtGainmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtGainmax.setStatus(
        "current"
    )

perEvtGainmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15982)
)
perEvtGainmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtGainmin.setStatus(
        "current"
    )

perEvtLsvolmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15983)
)
perEvtLsvolmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtLsvolmax.setStatus(
        "current"
    )

perEvtLsvolmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15984)
)
perEvtLsvolmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtLsvolmin.setStatus(
        "current"
    )

perEvtLsvolcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15985)
)
perEvtLsvolcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtLsvolcur.setStatus(
        "current"
    )

perEvtOducnTcm1Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15989)
)
perEvtOducnTcm1Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Iaes.setStatus(
        "current"
    )

perEvtOducnTcm2Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15990)
)
perEvtOducnTcm2Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Iaes.setStatus(
        "current"
    )

perEvtOducnTcm3Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15991)
)
perEvtOducnTcm3Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Iaes.setStatus(
        "current"
    )

perEvtOducnTcm4Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15992)
)
perEvtOducnTcm4Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Iaes.setStatus(
        "current"
    )

perEvtOducnTcm5Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15993)
)
perEvtOducnTcm5Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Iaes.setStatus(
        "current"
    )

perEvtOducnTcm6Iaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15994)
)
perEvtOducnTcm6Iaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Iaes.setStatus(
        "current"
    )

perEvtOducnTcm1Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15995)
)
perEvtOducnTcm1Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Biaes.setStatus(
        "current"
    )

perEvtOducnTcm2Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15996)
)
perEvtOducnTcm2Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Biaes.setStatus(
        "current"
    )

perEvtOducnTcm3Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15997)
)
perEvtOducnTcm3Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Biaes.setStatus(
        "current"
    )

perEvtOducnTcm4Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15998)
)
perEvtOducnTcm4Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Biaes.setStatus(
        "current"
    )

perEvtOducnTcm5Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 15999)
)
perEvtOducnTcm5Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Biaes.setStatus(
        "current"
    )

perEvtOducnTcm6Biaes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16000)
)
perEvtOducnTcm6Biaes.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Biaes.setStatus(
        "current"
    )

perEvtOducnTcm1Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16001)
)
perEvtOducnTcm1Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Bbe.setStatus(
        "current"
    )

perEvtOducnTcm2Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16002)
)
perEvtOducnTcm2Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Bbe.setStatus(
        "current"
    )

perEvtOducnTcm3Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16003)
)
perEvtOducnTcm3Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Bbe.setStatus(
        "current"
    )

perEvtOducnTcm4Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16004)
)
perEvtOducnTcm4Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Bbe.setStatus(
        "current"
    )

perEvtOducnTcm5Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16005)
)
perEvtOducnTcm5Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Bbe.setStatus(
        "current"
    )

perEvtOducnTcm6Bbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16006)
)
perEvtOducnTcm6Bbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Bbe.setStatus(
        "current"
    )

perEvtOducnTcm1Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16007)
)
perEvtOducnTcm1Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Es.setStatus(
        "current"
    )

perEvtOducnTcm2Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16008)
)
perEvtOducnTcm2Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Es.setStatus(
        "current"
    )

perEvtOducnTcm3Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16009)
)
perEvtOducnTcm3Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Es.setStatus(
        "current"
    )

perEvtOducnTcm4Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16010)
)
perEvtOducnTcm4Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Es.setStatus(
        "current"
    )

perEvtOducnTcm5Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16011)
)
perEvtOducnTcm5Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Es.setStatus(
        "current"
    )

perEvtOducnTcm6Es = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16012)
)
perEvtOducnTcm6Es.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Es.setStatus(
        "current"
    )

perEvtOducnTcm1Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16013)
)
perEvtOducnTcm1Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Ses.setStatus(
        "current"
    )

perEvtOducnTcm2Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16014)
)
perEvtOducnTcm2Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Ses.setStatus(
        "current"
    )

perEvtOducnTcm3Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16015)
)
perEvtOducnTcm3Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Ses.setStatus(
        "current"
    )

perEvtOducnTcm4Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16016)
)
perEvtOducnTcm4Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Ses.setStatus(
        "current"
    )

perEvtOducnTcm5Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16017)
)
perEvtOducnTcm5Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Ses.setStatus(
        "current"
    )

perEvtOducnTcm6Ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16018)
)
perEvtOducnTcm6Ses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Ses.setStatus(
        "current"
    )

perEvtOducnTcm1Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16019)
)
perEvtOducnTcm1Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Uas.setStatus(
        "current"
    )

perEvtOducnTcm2Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16020)
)
perEvtOducnTcm2Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Uas.setStatus(
        "current"
    )

perEvtOducnTcm3Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16021)
)
perEvtOducnTcm3Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Uas.setStatus(
        "current"
    )

perEvtOducnTcm4Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16022)
)
perEvtOducnTcm4Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Uas.setStatus(
        "current"
    )

perEvtOducnTcm5Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16023)
)
perEvtOducnTcm5Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Uas.setStatus(
        "current"
    )

perEvtOducnTcm6Uas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16024)
)
perEvtOducnTcm6Uas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Uas.setStatus(
        "current"
    )

perEvtOducnTcm1Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16025)
)
perEvtOducnTcm1Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Sesr.setStatus(
        "current"
    )

perEvtOducnTcm2Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16026)
)
perEvtOducnTcm2Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Sesr.setStatus(
        "current"
    )

perEvtOducnTcm3Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16027)
)
perEvtOducnTcm3Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Sesr.setStatus(
        "current"
    )

perEvtOducnTcm4Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16028)
)
perEvtOducnTcm4Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Sesr.setStatus(
        "current"
    )

perEvtOducnTcm5Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16029)
)
perEvtOducnTcm5Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Sesr.setStatus(
        "current"
    )

perEvtOducnTcm6Sesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16030)
)
perEvtOducnTcm6Sesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Sesr.setStatus(
        "current"
    )

perEvtOducnTcm1Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16031)
)
perEvtOducnTcm1Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Bber.setStatus(
        "current"
    )

perEvtOducnTcm2Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16032)
)
perEvtOducnTcm2Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Bber.setStatus(
        "current"
    )

perEvtOducnTcm3Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16033)
)
perEvtOducnTcm3Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Bber.setStatus(
        "current"
    )

perEvtOducnTcm4Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16034)
)
perEvtOducnTcm4Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Bber.setStatus(
        "current"
    )

perEvtOducnTcm5Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16035)
)
perEvtOducnTcm5Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Bber.setStatus(
        "current"
    )

perEvtOducnTcm6Bber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16036)
)
perEvtOducnTcm6Bber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Bber.setStatus(
        "current"
    )

perEvtOducnTcm1Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16037)
)
perEvtOducnTcm1Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Febbe.setStatus(
        "current"
    )

perEvtOducnTcm2Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16038)
)
perEvtOducnTcm2Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Febbe.setStatus(
        "current"
    )

perEvtOducnTcm3Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16039)
)
perEvtOducnTcm3Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Febbe.setStatus(
        "current"
    )

perEvtOducnTcm4Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16040)
)
perEvtOducnTcm4Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Febbe.setStatus(
        "current"
    )

perEvtOducnTcm5Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16041)
)
perEvtOducnTcm5Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Febbe.setStatus(
        "current"
    )

perEvtOducnTcm6Febbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16042)
)
perEvtOducnTcm6Febbe.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Febbe.setStatus(
        "current"
    )

perEvtOducnTcm1Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16043)
)
perEvtOducnTcm1Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Fees.setStatus(
        "current"
    )

perEvtOducnTcm2Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16044)
)
perEvtOducnTcm2Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Fees.setStatus(
        "current"
    )

perEvtOducnTcm3Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16045)
)
perEvtOducnTcm3Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Fees.setStatus(
        "current"
    )

perEvtOducnTcm4Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16046)
)
perEvtOducnTcm4Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Fees.setStatus(
        "current"
    )

perEvtOducnTcm5Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16047)
)
perEvtOducnTcm5Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Fees.setStatus(
        "current"
    )

perEvtOducnTcm6Fees = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16048)
)
perEvtOducnTcm6Fees.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Fees.setStatus(
        "current"
    )

perEvtOducnTcm1Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16049)
)
perEvtOducnTcm1Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Feses.setStatus(
        "current"
    )

perEvtOducnTcm2Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16050)
)
perEvtOducnTcm2Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Feses.setStatus(
        "current"
    )

perEvtOducnTcm3Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16051)
)
perEvtOducnTcm3Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Feses.setStatus(
        "current"
    )

perEvtOducnTcm4Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16052)
)
perEvtOducnTcm4Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Feses.setStatus(
        "current"
    )

perEvtOducnTcm5Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16053)
)
perEvtOducnTcm5Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Feses.setStatus(
        "current"
    )

perEvtOducnTcm6Feses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16054)
)
perEvtOducnTcm6Feses.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Feses.setStatus(
        "current"
    )

perEvtOducnTcm1Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16055)
)
perEvtOducnTcm1Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Feuas.setStatus(
        "current"
    )

perEvtOducnTcm2Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16056)
)
perEvtOducnTcm2Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Feuas.setStatus(
        "current"
    )

perEvtOducnTcm3Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16057)
)
perEvtOducnTcm3Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Feuas.setStatus(
        "current"
    )

perEvtOducnTcm4Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16058)
)
perEvtOducnTcm4Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Feuas.setStatus(
        "current"
    )

perEvtOducnTcm5Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16059)
)
perEvtOducnTcm5Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Feuas.setStatus(
        "current"
    )

perEvtOducnTcm6Feuas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16060)
)
perEvtOducnTcm6Feuas.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Feuas.setStatus(
        "current"
    )

perEvtOducnTcm1Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16061)
)
perEvtOducnTcm1Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm2Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16062)
)
perEvtOducnTcm2Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm3Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16063)
)
perEvtOducnTcm3Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm4Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16064)
)
perEvtOducnTcm4Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm5Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16065)
)
perEvtOducnTcm5Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm6Fesesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16066)
)
perEvtOducnTcm6Fesesr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Fesesr.setStatus(
        "current"
    )

perEvtOducnTcm1Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16067)
)
perEvtOducnTcm1Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Febber.setStatus(
        "current"
    )

perEvtOducnTcm2Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16068)
)
perEvtOducnTcm2Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Febber.setStatus(
        "current"
    )

perEvtOducnTcm3Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16069)
)
perEvtOducnTcm3Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Febber.setStatus(
        "current"
    )

perEvtOducnTcm4Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16070)
)
perEvtOducnTcm4Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Febber.setStatus(
        "current"
    )

perEvtOducnTcm5Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16071)
)
perEvtOducnTcm5Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Febber.setStatus(
        "current"
    )

perEvtOducnTcm6Febber = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16072)
)
perEvtOducnTcm6Febber.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Febber.setStatus(
        "current"
    )

perEvtOducnTcm1Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16073)
)
perEvtOducnTcm1Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm1Tmp.setStatus(
        "current"
    )

perEvtOducnTcm2Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16074)
)
perEvtOducnTcm2Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm2Tmp.setStatus(
        "current"
    )

perEvtOducnTcm3Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16075)
)
perEvtOducnTcm3Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm3Tmp.setStatus(
        "current"
    )

perEvtOducnTcm4Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16076)
)
perEvtOducnTcm4Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm4Tmp.setStatus(
        "current"
    )

perEvtOducnTcm5Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16077)
)
perEvtOducnTcm5Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm5Tmp.setStatus(
        "current"
    )

perEvtOducnTcm6Tmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16078)
)
perEvtOducnTcm6Tmp.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOducnTcm6Tmp.setStatus(
        "current"
    )

perEvtSopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16097)
)
perEvtSopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSopcur.setStatus(
        "current"
    )

perEvtSopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16098)
)
perEvtSopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSopmin.setStatus(
        "current"
    )

perEvtSopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16099)
)
perEvtSopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtSopmax.setStatus(
        "current"
    )

perEvtXcstmpfluct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16110)
)
perEvtXcstmpfluct.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtXcstmpfluct.setStatus(
        "current"
    )

perEvtFanspeedmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16111)
)
perEvtFanspeedmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFanspeedmax.setStatus(
        "current"
    )

perEvtFanspeedmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16112)
)
perEvtFanspeedmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFanspeedmin.setStatus(
        "current"
    )

perEvtFanspeedcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16113)
)
perEvtFanspeedcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFanspeedcur.setStatus(
        "current"
    )

perEvtFanspeedfluct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16114)
)
perEvtFanspeedfluct.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFanspeedfluct.setStatus(
        "current"
    )

perEvtEsnrmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16115)
)
perEvtEsnrmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEsnrmin.setStatus(
        "current"
    )

perEvtEsnrmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16116)
)
perEvtEsnrmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEsnrmax.setStatus(
        "current"
    )

perEvtEsnrcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16117)
)
perEvtEsnrcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEsnrcur.setStatus(
        "current"
    )

perEvtEsnravg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16118)
)
perEvtEsnravg.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEsnravg.setStatus(
        "current"
    )

perEvtPdlmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16119)
)
perEvtPdlmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPdlmax.setStatus(
        "current"
    )

perEvtPdlmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16120)
)
perEvtPdlmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPdlmin.setStatus(
        "current"
    )

perEvtPdlcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16121)
)
perEvtPdlcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPdlcur.setStatus(
        "current"
    )

perEvtPdlavg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16122)
)
perEvtPdlavg.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPdlavg.setStatus(
        "current"
    )

perEvtPmdmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16123)
)
perEvtPmdmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPmdmax.setStatus(
        "current"
    )

perEvtPmdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16124)
)
perEvtPmdmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPmdmin.setStatus(
        "current"
    )

perEvtPmdcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16125)
)
perEvtPmdcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPmdcur.setStatus(
        "current"
    )

perEvtPmdavg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16126)
)
perEvtPmdavg.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtPmdavg.setStatus(
        "current"
    )

perEvtMcsoopmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16135)
)
perEvtMcsoopmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMcsoopmax.setStatus(
        "current"
    )

perEvtMcsoopmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16136)
)
perEvtMcsoopmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMcsoopmin.setStatus(
        "current"
    )

perEvtMcsoopcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16137)
)
perEvtMcsoopcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtMcsoopcur.setStatus(
        "current"
    )

perEvtQValueEerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16144)
)
perEvtQValueEerMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtQValueEerMin.setStatus(
        "current"
    )

perEvtQValueEerMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16145)
)
perEvtQValueEerMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtQValueEerMax.setStatus(
        "current"
    )

perEvtBefCorerFloatMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16146)
)
perEvtBefCorerFloatMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBefCorerFloatMin.setStatus(
        "current"
    )

perEvtBefCorerFloatMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16147)
)
perEvtBefCorerFloatMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBefCorerFloatMax.setStatus(
        "current"
    )

perEvtAftCorerFloatMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16148)
)
perEvtAftCorerFloatMax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAftCorerFloatMax.setStatus(
        "current"
    )

perEvtBefCorerFloatAvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16149)
)
perEvtBefCorerFloatAvr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBefCorerFloatAvr.setStatus(
        "current"
    )

perEvtAftCorerFloatAvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16150)
)
perEvtAftCorerFloatAvr.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAftCorerFloatAvr.setStatus(
        "current"
    )

perEvtAftCorerFloatMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16163)
)
perEvtAftCorerFloatMin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtAftCorerFloatMin.setStatus(
        "current"
    )

perEvtEvoaattncur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16164)
)
perEvtEvoaattncur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEvoaattncur.setStatus(
        "current"
    )

perEvtEvoaattnmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16165)
)
perEvtEvoaattnmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEvoaattnmax.setStatus(
        "current"
    )

perEvtEvoaattnmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16166)
)
perEvtEvoaattnmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtEvoaattnmin.setStatus(
        "current"
    )

perEvtFecCorBitsCnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16171)
)
perEvtFecCorBitsCnt.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtFecCorBitsCnt.setStatus(
        "current"
    )

perEvtBdCurPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16172)
)
perEvtBdCurPower.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtBdCurPower.setStatus(
        "current"
    )

perEvtInputvoltmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16174)
)
perEvtInputvoltmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputvoltmax.setStatus(
        "current"
    )

perEvtInputvoltcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16175)
)
perEvtInputvoltcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputvoltcur.setStatus(
        "current"
    )

perEvtInputvoltmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16176)
)
perEvtInputvoltmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputvoltmin.setStatus(
        "current"
    )

perEvtOutputvoltmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16177)
)
perEvtOutputvoltmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputvoltmax.setStatus(
        "current"
    )

perEvtOutputvoltcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16178)
)
perEvtOutputvoltcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputvoltcur.setStatus(
        "current"
    )

perEvtOutputvoltmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16179)
)
perEvtOutputvoltmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputvoltmin.setStatus(
        "current"
    )

perEvtOutputcurrentmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16180)
)
perEvtOutputcurrentmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputcurrentmax.setStatus(
        "current"
    )

perEvtOutputcurrentcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16181)
)
perEvtOutputcurrentcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputcurrentcur.setStatus(
        "current"
    )

perEvtOutputcurrentmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16182)
)
perEvtOutputcurrentmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtOutputcurrentmin.setStatus(
        "current"
    )

perEvtInputcurrentmax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16183)
)
perEvtInputcurrentmax.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputcurrentmax.setStatus(
        "current"
    )

perEvtInputcurrentcur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16184)
)
perEvtInputcurrentcur.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputcurrentcur.setStatus(
        "current"
    )

perEvtInputcurrentmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16185)
)
perEvtInputcurrentmin.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtInputcurrentmin.setStatus(
        "current"
    )

perEvtLswfrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 30, 16186)
)
perEvtLswfrequency.setObjects(
      *(("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtPeriod"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtValue"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtVldty"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtDateTime"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtObjType"),
        ("OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB", "rptEvtParaLen"),
        ("OPTIX-GLOBAL-TRAPS-MIB", "rptEvtPara"))
)
if mibBuilder.loadTexts:
    perEvtLswfrequency.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-GLOBAL-PER-TRAPS-NGWDM-MIB",
    **{"optixTrapsPER": optixTrapsPER,
       "perEvtRsbbe": perEvtRsbbe,
       "perEvtRses": perEvtRses,
       "perEvtRsses": perEvtRsses,
       "perEvtRsofs": perEvtRsofs,
       "perEvtRsuas": perEvtRsuas,
       "perEvtRscses": perEvtRscses,
       "perEvtTlbmax": perEvtTlbmax,
       "perEvtTlbmin": perEvtTlbmin,
       "perEvtTlbcur": perEvtTlbcur,
       "perEvtOspiccvmax": perEvtOspiccvmax,
       "perEvtOspiccvmin": perEvtOspiccvmin,
       "perEvtOspiccvcur": perEvtOspiccvcur,
       "perEvtTplmax": perEvtTplmax,
       "perEvtTplmin": perEvtTplmin,
       "perEvtTplcur": perEvtTplcur,
       "perEvtRplmax": perEvtRplmax,
       "perEvtRplmin": perEvtRplmin,
       "perEvtRplcur": perEvtRplcur,
       "perEvtOspitmpmax": perEvtOspitmpmax,
       "perEvtOspitmpmin": perEvtOspitmpmin,
       "perEvtOspitmpcur": perEvtOspitmpcur,
       "perEvtWcvmax": perEvtWcvmax,
       "perEvtWcvmin": perEvtWcvmin,
       "perEvtWcvcur": perEvtWcvcur,
       "perEvtCcvmax": perEvtCcvmax,
       "perEvtCcvmin": perEvtCcvmin,
       "perEvtCcvcur": perEvtCcvcur,
       "perEvtBcvmax": perEvtBcvmax,
       "perEvtBcvmin": perEvtBcvmin,
       "perEvtBcvcur": perEvtBcvcur,
       "perEvtEdtplmax": perEvtEdtplmax,
       "perEvtEdtplmin": perEvtEdtplmin,
       "perEvtEdtplcur": perEvtEdtplcur,
       "perEvtEdtmpmax": perEvtEdtmpmax,
       "perEvtEdtmpmin": perEvtEdtmpmin,
       "perEvtEdtmpcur": perEvtEdtmpcur,
       "perEvtfecCorrected0BitCount": perEvtfecCorrected0BitCount,
       "perEvtfecCorrected1BitCount": perEvtfecCorrected1BitCount,
       "perEvtfecCorrectedByteCount": perEvtfecCorrectedByteCount,
       "perEvtfecUnCorrectedBlockCount": perEvtfecUnCorrectedBlockCount,
       "perEvtboardTemperatureMaximum": perEvtboardTemperatureMaximum,
       "perEvtboardTemperatureMinimum": perEvtboardTemperatureMinimum,
       "perEvtboardTemperatureCurrent": perEvtboardTemperatureCurrent,
       "perEvtw32LaserOutputOfPowerMaximum": perEvtw32LaserOutputOfPowerMaximum,
       "perEvtw32LaserOutputOfPowerMinimum": perEvtw32LaserOutputOfPowerMinimum,
       "perEvtw32LaserOutputOfPowerCurrent": perEvtw32LaserOutputOfPowerCurrent,
       "perEvtw32LaserInputOfPowerMaximum": perEvtw32LaserInputOfPowerMaximum,
       "perEvtw32LaserInputOfPowerMinimum": perEvtw32LaserInputOfPowerMinimum,
       "perEvtw32LaserInputOfPowerCurrent": perEvtw32LaserInputOfPowerCurrent,
       "perEvtw32LaserWorkingTemperatureMaximum": perEvtw32LaserWorkingTemperatureMaximum,
       "perEvtw32LaserWorkingTemperatureMinimum": perEvtw32LaserWorkingTemperatureMinimum,
       "perEvtw32LaserWorkingTemperatureCurrent": perEvtw32LaserWorkingTemperatureCurrent,
       "perEvtw32LaserBiasMaximum": perEvtw32LaserBiasMaximum,
       "perEvtw32LaserBiasMinimum": perEvtw32LaserBiasMinimum,
       "perEvtw32LaserBiasCurrent": perEvtw32LaserBiasCurrent,
       "perEvtw32SumLaserInputOfPowerMaximum": perEvtw32SumLaserInputOfPowerMaximum,
       "perEvtw32SumLaserInputOfPowerMinimum": perEvtw32SumLaserInputOfPowerMinimum,
       "perEvtw32SumLaserInputOfPowerCurrent": perEvtw32SumLaserInputOfPowerCurrent,
       "perEvtSumoopmax": perEvtSumoopmax,
       "perEvtSumoopmin": perEvtSumoopmin,
       "perEvtSumoopcur": perEvtSumoopcur,
       "perEvtEnvtmpmax": perEvtEnvtmpmax,
       "perEvtEnvtmpmin": perEvtEnvtmpmin,
       "perEvtEnvtmpcur": perEvtEnvtmpcur,
       "perEvtw32LaserCoolingMaximum": perEvtw32LaserCoolingMaximum,
       "perEvtw32LaserCoolingMinimum": perEvtw32LaserCoolingMinimum,
       "perEvtw32LaserCoolingCurrent": perEvtw32LaserCoolingCurrent,
       "perEvtPclswlmax": perEvtPclswlmax,
       "perEvtPclswlmin": perEvtPclswlmin,
       "perEvtPclswlcur": perEvtPclswlcur,
       "perEvtPclswlomax": perEvtPclswlomax,
       "perEvtPclswlomin": perEvtPclswlomin,
       "perEvtPclswlocur": perEvtPclswlocur,
       "perEvtPclsopmax": perEvtPclsopmax,
       "perEvtPclsopmin": perEvtPclsopmin,
       "perEvtPclsopcur": perEvtPclsopcur,
       "perEvtPclssnmax": perEvtPclssnmax,
       "perEvtPclssnmin": perEvtPclssnmin,
       "perEvtPclssncur": perEvtPclssncur,
       "perEvtIctmpmax": perEvtIctmpmax,
       "perEvtIctmpmin": perEvtIctmpmin,
       "perEvtIctmpcur": perEvtIctmpcur,
       "perEvtbeforeFECCorrectErrorRatio": perEvtbeforeFECCorrectErrorRatio,
       "perEvtafterFECCorrectErrorRatio": perEvtafterFECCorrectErrorRatio,
       "perEvtIcclcmax": perEvtIcclcmax,
       "perEvtIcclcmin": perEvtIcclcmin,
       "perEvtIcclccur": perEvtIcclccur,
       "perEvtOoprlmax": perEvtOoprlmax,
       "perEvtOoprlmin": perEvtOoprlmin,
       "perEvtOoprlcur": perEvtOoprlcur,
       "perEvtOtu1Iaes": perEvtOtu1Iaes,
       "perEvtOtu1Biaes": perEvtOtu1Biaes,
       "perEvtOtu1Bbe": perEvtOtu1Bbe,
       "perEvtOtu1Es": perEvtOtu1Es,
       "perEvtOtu1Ses": perEvtOtu1Ses,
       "perEvtOtu1Uas": perEvtOtu1Uas,
       "perEvtOtu1Sesr": perEvtOtu1Sesr,
       "perEvtOtu1Bber": perEvtOtu1Bber,
       "perEvtOtu1Febbe": perEvtOtu1Febbe,
       "perEvtOtu1Fees": perEvtOtu1Fees,
       "perEvtOtu1Feses": perEvtOtu1Feses,
       "perEvtOtu1Feuas": perEvtOtu1Feuas,
       "perEvtOtu1Fesesr": perEvtOtu1Fesesr,
       "perEvtOtu1Febber": perEvtOtu1Febber,
       "perEvtOtu2Iaes": perEvtOtu2Iaes,
       "perEvtOtu2Biaes": perEvtOtu2Biaes,
       "perEvtOtu2Bbe": perEvtOtu2Bbe,
       "perEvtOtu2Es": perEvtOtu2Es,
       "perEvtOtu2Ses": perEvtOtu2Ses,
       "perEvtOtu2Uas": perEvtOtu2Uas,
       "perEvtOtu2Sesr": perEvtOtu2Sesr,
       "perEvtOtu2Bber": perEvtOtu2Bber,
       "perEvtOtu2Febbe": perEvtOtu2Febbe,
       "perEvtOtu2Fees": perEvtOtu2Fees,
       "perEvtOtu2Feses": perEvtOtu2Feses,
       "perEvtOtu2Feuas": perEvtOtu2Feuas,
       "perEvtOtu2Fesesr": perEvtOtu2Fesesr,
       "perEvtOtu2Febber": perEvtOtu2Febber,
       "perEvtOtu3Iaes": perEvtOtu3Iaes,
       "perEvtOtu3Biaes": perEvtOtu3Biaes,
       "perEvtOtu3Bbe": perEvtOtu3Bbe,
       "perEvtOtu3Es": perEvtOtu3Es,
       "perEvtOtu3Ses": perEvtOtu3Ses,
       "perEvtOtu3Uas": perEvtOtu3Uas,
       "perEvtOtu3Sesr": perEvtOtu3Sesr,
       "perEvtOtu3Bber": perEvtOtu3Bber,
       "perEvtOtu3Febbe": perEvtOtu3Febbe,
       "perEvtOtu3Fees": perEvtOtu3Fees,
       "perEvtOtu3Feses": perEvtOtu3Feses,
       "perEvtOtu3Feuas": perEvtOtu3Feuas,
       "perEvtOtu3Fesesr": perEvtOtu3Fesesr,
       "perEvtOtu3Febber": perEvtOtu3Febber,
       "perEvtOdu1PmBbe": perEvtOdu1PmBbe,
       "perEvtOdu1PmEs": perEvtOdu1PmEs,
       "perEvtOdu1PmSes": perEvtOdu1PmSes,
       "perEvtOdu1PmUas": perEvtOdu1PmUas,
       "perEvtOdu1PmSesr": perEvtOdu1PmSesr,
       "perEvtOdu1PmBber": perEvtOdu1PmBber,
       "perEvtOdu1PmFebbe": perEvtOdu1PmFebbe,
       "perEvtOdu1PmFees": perEvtOdu1PmFees,
       "perEvtOdu1PmFeses": perEvtOdu1PmFeses,
       "perEvtOdu1PmFeuas": perEvtOdu1PmFeuas,
       "perEvtOdu1PmFesesr": perEvtOdu1PmFesesr,
       "perEvtOdu1PmFebber": perEvtOdu1PmFebber,
       "perEvtodu2pmbbe": perEvtodu2pmbbe,
       "perEvtodu2pmes": perEvtodu2pmes,
       "perEvtodu2pmses": perEvtodu2pmses,
       "perEvtodu2pmuas": perEvtodu2pmuas,
       "perEvtodu2pmsesr": perEvtodu2pmsesr,
       "perEvtodu2pmbber": perEvtodu2pmbber,
       "perEvtodu2pmfebbe": perEvtodu2pmfebbe,
       "perEvtodu2pmfees": perEvtodu2pmfees,
       "perEvtodu2pmfeses": perEvtodu2pmfeses,
       "perEvtodu2pmfeuas": perEvtodu2pmfeuas,
       "perEvtodu2pmfesesr": perEvtodu2pmfesesr,
       "perEvtodu2pmfebber": perEvtodu2pmfebber,
       "perEvtodu3pmbbe": perEvtodu3pmbbe,
       "perEvtodu3pmes": perEvtodu3pmes,
       "perEvtodu3pmses": perEvtodu3pmses,
       "perEvtodu3pmuas": perEvtodu3pmuas,
       "perEvtodu3pmsesr": perEvtodu3pmsesr,
       "perEvtodu3pmbber": perEvtodu3pmbber,
       "perEvtodu3pmfebbe": perEvtodu3pmfebbe,
       "perEvtodu3pmfees": perEvtodu3pmfees,
       "perEvtodu3pmfeses": perEvtodu3pmfeses,
       "perEvtodu3pmfeuas": perEvtodu3pmfeuas,
       "perEvtodu3pmfesesr": perEvtodu3pmfesesr,
       "perEvtodu3pmfebber": perEvtodu3pmfebber,
       "perEvtOdu1Tcm1Iaes": perEvtOdu1Tcm1Iaes,
       "perEvtOdu1Tcm2Iaes": perEvtOdu1Tcm2Iaes,
       "perEvtOdu1Tcm3Iaes": perEvtOdu1Tcm3Iaes,
       "perEvtOdu1Tcm4Iaes": perEvtOdu1Tcm4Iaes,
       "perEvtOdu1Tcm5Iaes": perEvtOdu1Tcm5Iaes,
       "perEvtOdu1Tcm6Iaes": perEvtOdu1Tcm6Iaes,
       "perEvtOdu1Tcm1Biaes": perEvtOdu1Tcm1Biaes,
       "perEvtOdu1Tcm2Biaes": perEvtOdu1Tcm2Biaes,
       "perEvtOdu1Tcm3Biaes": perEvtOdu1Tcm3Biaes,
       "perEvtOdu1Tcm4Biaes": perEvtOdu1Tcm4Biaes,
       "perEvtOdu1Tcm5Biaes": perEvtOdu1Tcm5Biaes,
       "perEvtOdu1Tcm6Biaes": perEvtOdu1Tcm6Biaes,
       "perEvtOdu1Tcm1Bbe": perEvtOdu1Tcm1Bbe,
       "perEvtOdu1Tcm1Es": perEvtOdu1Tcm1Es,
       "perEvtOdu1Tcm1Ses": perEvtOdu1Tcm1Ses,
       "perEvtOdu1Tcm1Uas": perEvtOdu1Tcm1Uas,
       "perEvtOdu1Tcm1Sesr": perEvtOdu1Tcm1Sesr,
       "perEvtOdu1Tcm1Bber": perEvtOdu1Tcm1Bber,
       "perEvtOdu1Tcm2Bbe": perEvtOdu1Tcm2Bbe,
       "perEvtOdu1Tcm2Es": perEvtOdu1Tcm2Es,
       "perEvtOdu1Tcm2Ses": perEvtOdu1Tcm2Ses,
       "perEvtOdu1Tcm2Uas": perEvtOdu1Tcm2Uas,
       "perEvtOdu1Tcm2Sesr": perEvtOdu1Tcm2Sesr,
       "perEvtOdu1Tcm2Bber": perEvtOdu1Tcm2Bber,
       "perEvtOdu1Tcm3Bbe": perEvtOdu1Tcm3Bbe,
       "perEvtOdu1Tcm3Es": perEvtOdu1Tcm3Es,
       "perEvtOdu1Tcm3Ses": perEvtOdu1Tcm3Ses,
       "perEvtOdu1Tcm3Uas": perEvtOdu1Tcm3Uas,
       "perEvtOdu1Tcm3Sesr": perEvtOdu1Tcm3Sesr,
       "perEvtOdu1Tcm3Bber": perEvtOdu1Tcm3Bber,
       "perEvtOdu1Tcm4Bbe": perEvtOdu1Tcm4Bbe,
       "perEvtOdu1Tcm4Es": perEvtOdu1Tcm4Es,
       "perEvtOdu1Tcm4Ses": perEvtOdu1Tcm4Ses,
       "perEvtOdu1Tcm4Uas": perEvtOdu1Tcm4Uas,
       "perEvtOdu1Tcm4Sesr": perEvtOdu1Tcm4Sesr,
       "perEvtOdu1Tcm4Bber": perEvtOdu1Tcm4Bber,
       "perEvtOdu1Tcm5Bbe": perEvtOdu1Tcm5Bbe,
       "perEvtOdu1Tcm5Es": perEvtOdu1Tcm5Es,
       "perEvtOdu1Tcm5Ses": perEvtOdu1Tcm5Ses,
       "perEvtOdu1Tcm5Uas": perEvtOdu1Tcm5Uas,
       "perEvtOdu1Tcm5Sesr": perEvtOdu1Tcm5Sesr,
       "perEvtOdu1Tcm5Bber": perEvtOdu1Tcm5Bber,
       "perEvtOdu1Tcm6Bbe": perEvtOdu1Tcm6Bbe,
       "perEvtOdu1Tcm6Es": perEvtOdu1Tcm6Es,
       "perEvtOdu1Tcm6Ses": perEvtOdu1Tcm6Ses,
       "perEvtOdu1Tcm6Uas": perEvtOdu1Tcm6Uas,
       "perEvtOdu1Tcm6Sesr": perEvtOdu1Tcm6Sesr,
       "perEvtOdu1Tcm6Bber": perEvtOdu1Tcm6Bber,
       "perEvtOdu1Tcm1Febbe": perEvtOdu1Tcm1Febbe,
       "perEvtOdu1Tcm1Fees": perEvtOdu1Tcm1Fees,
       "perEvtOdu1Tcm1Feses": perEvtOdu1Tcm1Feses,
       "perEvtOdu1Tcm1Feuas": perEvtOdu1Tcm1Feuas,
       "perEvtOdu1Tcm1Fesesr": perEvtOdu1Tcm1Fesesr,
       "perEvtOdu1Tcm1Febber": perEvtOdu1Tcm1Febber,
       "perEvtOdu1Tcm2Febbe": perEvtOdu1Tcm2Febbe,
       "perEvtOdu1Tcm2Fees": perEvtOdu1Tcm2Fees,
       "perEvtOdu1Tcm2Feses": perEvtOdu1Tcm2Feses,
       "perEvtOdu1Tcm2Feuas": perEvtOdu1Tcm2Feuas,
       "perEvtOdu1Tcm2Fesesr": perEvtOdu1Tcm2Fesesr,
       "perEvtOdu1Tcm2Febber": perEvtOdu1Tcm2Febber,
       "perEvtOdu1Tcm3Febbe": perEvtOdu1Tcm3Febbe,
       "perEvtOdu1Tcm3Fees": perEvtOdu1Tcm3Fees,
       "perEvtOdu1Tcm3Feses": perEvtOdu1Tcm3Feses,
       "perEvtOdu1Tcm3Feuas": perEvtOdu1Tcm3Feuas,
       "perEvtOdu1Tcm3Fesesr": perEvtOdu1Tcm3Fesesr,
       "perEvtOdu1Tcm3Febber": perEvtOdu1Tcm3Febber,
       "perEvtOdu1Tcm4Febbe": perEvtOdu1Tcm4Febbe,
       "perEvtOdu1Tcm4Fees": perEvtOdu1Tcm4Fees,
       "perEvtOdu1Tcm4Feses": perEvtOdu1Tcm4Feses,
       "perEvtOdu1Tcm4Feuas": perEvtOdu1Tcm4Feuas,
       "perEvtOdu1Tcm4Fesesr": perEvtOdu1Tcm4Fesesr,
       "perEvtOdu1Tcm4Febber": perEvtOdu1Tcm4Febber,
       "perEvtOdu1Tcm5Febbe": perEvtOdu1Tcm5Febbe,
       "perEvtOdu1Tcm5Fees": perEvtOdu1Tcm5Fees,
       "perEvtOdu1Tcm5Feses": perEvtOdu1Tcm5Feses,
       "perEvtOdu1Tcm5Feuas": perEvtOdu1Tcm5Feuas,
       "perEvtOdu1Tcm5Fesesr": perEvtOdu1Tcm5Fesesr,
       "perEvtOdu1Tcm5Febber": perEvtOdu1Tcm5Febber,
       "perEvtOdu1Tcm6Febbe": perEvtOdu1Tcm6Febbe,
       "perEvtOdu1Tcm6Fees": perEvtOdu1Tcm6Fees,
       "perEvtOdu1Tcm6Feses": perEvtOdu1Tcm6Feses,
       "perEvtOdu1Tcm6Feuas": perEvtOdu1Tcm6Feuas,
       "perEvtOdu1Tcm6Fesesr": perEvtOdu1Tcm6Fesesr,
       "perEvtOdu1Tcm6Febber": perEvtOdu1Tcm6Febber,
       "perEvtOdu2Tcm1Iaes": perEvtOdu2Tcm1Iaes,
       "perEvtOdu2Tcm2Iaes": perEvtOdu2Tcm2Iaes,
       "perEvtOdu2Tcm3Iaes": perEvtOdu2Tcm3Iaes,
       "perEvtOdu2Tcm4Iaes": perEvtOdu2Tcm4Iaes,
       "perEvtOdu2Tcm5Iaes": perEvtOdu2Tcm5Iaes,
       "perEvtOdu2Tcm6Iaes": perEvtOdu2Tcm6Iaes,
       "perEvtOdu2Tcm1Biaes": perEvtOdu2Tcm1Biaes,
       "perEvtOdu2Tcm2Biaes": perEvtOdu2Tcm2Biaes,
       "perEvtOdu2Tcm3Biaes": perEvtOdu2Tcm3Biaes,
       "perEvtOdu2Tcm4Biaes": perEvtOdu2Tcm4Biaes,
       "perEvtOdu2Tcm5Biaes": perEvtOdu2Tcm5Biaes,
       "perEvtOdu2Tcm6Biaes": perEvtOdu2Tcm6Biaes,
       "perEvtOdu2Tcm1Bbe": perEvtOdu2Tcm1Bbe,
       "perEvtOdu2Tcm1Es": perEvtOdu2Tcm1Es,
       "perEvtOdu2Tcm1Ses": perEvtOdu2Tcm1Ses,
       "perEvtOdu2Tcm1Uas": perEvtOdu2Tcm1Uas,
       "perEvtOdu2Tcm1Sesr": perEvtOdu2Tcm1Sesr,
       "perEvtOdu2Tcm1Bber": perEvtOdu2Tcm1Bber,
       "perEvtOdu2Tcm2Bbe": perEvtOdu2Tcm2Bbe,
       "perEvtOdu2Tcm2Es": perEvtOdu2Tcm2Es,
       "perEvtOdu2Tcm2Ses": perEvtOdu2Tcm2Ses,
       "perEvtOdu2Tcm2Uas": perEvtOdu2Tcm2Uas,
       "perEvtOdu2Tcm2Sesr": perEvtOdu2Tcm2Sesr,
       "perEvtOdu2Tcm2Bber": perEvtOdu2Tcm2Bber,
       "perEvtOdu2Tcm3Bbe": perEvtOdu2Tcm3Bbe,
       "perEvtOdu2Tcm3Es": perEvtOdu2Tcm3Es,
       "perEvtOdu2Tcm3Ses": perEvtOdu2Tcm3Ses,
       "perEvtOdu2Tcm3Uas": perEvtOdu2Tcm3Uas,
       "perEvtOdu2Tcm3Sesr": perEvtOdu2Tcm3Sesr,
       "perEvtOdu2Tcm3Bber": perEvtOdu2Tcm3Bber,
       "perEvtOdu2Tcm4Bbe": perEvtOdu2Tcm4Bbe,
       "perEvtOdu2Tcm4Es": perEvtOdu2Tcm4Es,
       "perEvtOdu2Tcm4Ses": perEvtOdu2Tcm4Ses,
       "perEvtOdu2Tcm4Uas": perEvtOdu2Tcm4Uas,
       "perEvtOdu2Tcm4Sesr": perEvtOdu2Tcm4Sesr,
       "perEvtOdu2Tcm4Bber": perEvtOdu2Tcm4Bber,
       "perEvtOdu2Tcm5Bbe": perEvtOdu2Tcm5Bbe,
       "perEvtOdu2Tcm5Es": perEvtOdu2Tcm5Es,
       "perEvtOdu2Tcm5Ses": perEvtOdu2Tcm5Ses,
       "perEvtOdu2Tcm5Uas": perEvtOdu2Tcm5Uas,
       "perEvtOdu2Tcm5Sesr": perEvtOdu2Tcm5Sesr,
       "perEvtOdu2Tcm5Bber": perEvtOdu2Tcm5Bber,
       "perEvtOdu2Tcm6Bbe": perEvtOdu2Tcm6Bbe,
       "perEvtOdu2Tcm6Es": perEvtOdu2Tcm6Es,
       "perEvtOdu2Tcm6Ses": perEvtOdu2Tcm6Ses,
       "perEvtOdu2Tcm6Uas": perEvtOdu2Tcm6Uas,
       "perEvtOdu2Tcm6Sesr": perEvtOdu2Tcm6Sesr,
       "perEvtOdu2Tcm6Bber": perEvtOdu2Tcm6Bber,
       "perEvtOdu2Tcm1Febbe": perEvtOdu2Tcm1Febbe,
       "perEvtOdu2Tcm1Fees": perEvtOdu2Tcm1Fees,
       "perEvtOdu2Tcm1Feses": perEvtOdu2Tcm1Feses,
       "perEvtOdu2Tcm1Feuas": perEvtOdu2Tcm1Feuas,
       "perEvtOdu2Tcm1Fesesr": perEvtOdu2Tcm1Fesesr,
       "perEvtOdu2Tcm1Febber": perEvtOdu2Tcm1Febber,
       "perEvtOdu2Tcm2Febbe": perEvtOdu2Tcm2Febbe,
       "perEvtOdu2Tcm2Fees": perEvtOdu2Tcm2Fees,
       "perEvtOdu2Tcm2Feses": perEvtOdu2Tcm2Feses,
       "perEvtOdu2Tcm2Feuas": perEvtOdu2Tcm2Feuas,
       "perEvtOdu2Tcm2Fesesr": perEvtOdu2Tcm2Fesesr,
       "perEvtOdu2Tcm2Febber": perEvtOdu2Tcm2Febber,
       "perEvtOdu2Tcm3Febbe": perEvtOdu2Tcm3Febbe,
       "perEvtOdu2Tcm3Fees": perEvtOdu2Tcm3Fees,
       "perEvtOdu2Tcm3Feses": perEvtOdu2Tcm3Feses,
       "perEvtOdu2Tcm3Feuas": perEvtOdu2Tcm3Feuas,
       "perEvtOdu2Tcm3Fesesr": perEvtOdu2Tcm3Fesesr,
       "perEvtOdu2Tcm3Febber": perEvtOdu2Tcm3Febber,
       "perEvtOdu2Tcm4Febbe": perEvtOdu2Tcm4Febbe,
       "perEvtOdu2Tcm4Fees": perEvtOdu2Tcm4Fees,
       "perEvtOdu2Tcm4Feses": perEvtOdu2Tcm4Feses,
       "perEvtOdu2Tcm4Feuas": perEvtOdu2Tcm4Feuas,
       "perEvtOdu2Tcm4Fesesr": perEvtOdu2Tcm4Fesesr,
       "perEvtOdu2Tcm4Febber": perEvtOdu2Tcm4Febber,
       "perEvtOdu2Tcm5Febbe": perEvtOdu2Tcm5Febbe,
       "perEvtOdu2Tcm5Fees": perEvtOdu2Tcm5Fees,
       "perEvtOdu2Tcm5Feses": perEvtOdu2Tcm5Feses,
       "perEvtOdu2Tcm5Feuas": perEvtOdu2Tcm5Feuas,
       "perEvtOdu2Tcm5Fesesr": perEvtOdu2Tcm5Fesesr,
       "perEvtOdu2Tcm5Febber": perEvtOdu2Tcm5Febber,
       "perEvtOdu2Tcm6Febbe": perEvtOdu2Tcm6Febbe,
       "perEvtOdu2Tcm6Fees": perEvtOdu2Tcm6Fees,
       "perEvtOdu2Tcm6Feses": perEvtOdu2Tcm6Feses,
       "perEvtOdu2Tcm6Feuas": perEvtOdu2Tcm6Feuas,
       "perEvtOdu2Tcm6Fesesr": perEvtOdu2Tcm6Fesesr,
       "perEvtOdu2Tcm6Febber": perEvtOdu2Tcm6Febber,
       "perEvtOdu3Tcm1Iaes": perEvtOdu3Tcm1Iaes,
       "perEvtOdu3Tcm2Iaes": perEvtOdu3Tcm2Iaes,
       "perEvtOdu3Tcm3Iaes": perEvtOdu3Tcm3Iaes,
       "perEvtOdu3Tcm4Iaes": perEvtOdu3Tcm4Iaes,
       "perEvtOdu3Tcm5Iaes": perEvtOdu3Tcm5Iaes,
       "perEvtOdu3Tcm6Iaes": perEvtOdu3Tcm6Iaes,
       "perEvtOdu3Tcm1Biaes": perEvtOdu3Tcm1Biaes,
       "perEvtOdu3Tcm2Biaes": perEvtOdu3Tcm2Biaes,
       "perEvtOdu3Tcm3Biaes": perEvtOdu3Tcm3Biaes,
       "perEvtOdu3Tcm4Biaes": perEvtOdu3Tcm4Biaes,
       "perEvtOdu3Tcm5Biaes": perEvtOdu3Tcm5Biaes,
       "perEvtOdu3Tcm6Biaes": perEvtOdu3Tcm6Biaes,
       "perEvtOdu3Tcm1Bbe": perEvtOdu3Tcm1Bbe,
       "perEvtOdu3Tcm1Es": perEvtOdu3Tcm1Es,
       "perEvtOdu3Tcm1Ses": perEvtOdu3Tcm1Ses,
       "perEvtOdu3Tcm1Uas": perEvtOdu3Tcm1Uas,
       "perEvtOdu3Tcm1Sesr": perEvtOdu3Tcm1Sesr,
       "perEvtOdu3Tcm1Bber": perEvtOdu3Tcm1Bber,
       "perEvtOdu3Tcm2Bbe": perEvtOdu3Tcm2Bbe,
       "perEvtOdu3Tcm2Es": perEvtOdu3Tcm2Es,
       "perEvtOdu3Tcm2Ses": perEvtOdu3Tcm2Ses,
       "perEvtOdu3Tcm2Uas": perEvtOdu3Tcm2Uas,
       "perEvtOdu3Tcm2Sesr": perEvtOdu3Tcm2Sesr,
       "perEvtOdu3Tcm2Bber": perEvtOdu3Tcm2Bber,
       "perEvtOdu3Tcm3Bbe": perEvtOdu3Tcm3Bbe,
       "perEvtOdu3Tcm3Es": perEvtOdu3Tcm3Es,
       "perEvtOdu3Tcm3Ses": perEvtOdu3Tcm3Ses,
       "perEvtOdu3Tcm3Uas": perEvtOdu3Tcm3Uas,
       "perEvtOdu3Tcm3Sesr": perEvtOdu3Tcm3Sesr,
       "perEvtOdu3Tcm3Bber": perEvtOdu3Tcm3Bber,
       "perEvtOdu3Tcm4Bbe": perEvtOdu3Tcm4Bbe,
       "perEvtOdu3Tcm4Es": perEvtOdu3Tcm4Es,
       "perEvtOdu3Tcm4Ses": perEvtOdu3Tcm4Ses,
       "perEvtOdu3Tcm4Uas": perEvtOdu3Tcm4Uas,
       "perEvtOdu3Tcm4Sesr": perEvtOdu3Tcm4Sesr,
       "perEvtOdu3Tcm4Bber": perEvtOdu3Tcm4Bber,
       "perEvtOdu3Tcm5Bbe": perEvtOdu3Tcm5Bbe,
       "perEvtOdu3Tcm5Es": perEvtOdu3Tcm5Es,
       "perEvtOdu3Tcm5Ses": perEvtOdu3Tcm5Ses,
       "perEvtOdu3Tcm5Uas": perEvtOdu3Tcm5Uas,
       "perEvtOdu3Tcm5Sesr": perEvtOdu3Tcm5Sesr,
       "perEvtOdu3Tcm5Bber": perEvtOdu3Tcm5Bber,
       "perEvtOdu3Tcm6Bbe": perEvtOdu3Tcm6Bbe,
       "perEvtOdu3Tcm6Es": perEvtOdu3Tcm6Es,
       "perEvtOdu3Tcm6Ses": perEvtOdu3Tcm6Ses,
       "perEvtOdu3Tcm6Uas": perEvtOdu3Tcm6Uas,
       "perEvtOdu3Tcm6Sesr": perEvtOdu3Tcm6Sesr,
       "perEvtOdu3Tcm6Bber": perEvtOdu3Tcm6Bber,
       "perEvtOdu3Tcm1Febbe": perEvtOdu3Tcm1Febbe,
       "perEvtOdu3Tcm1Fees": perEvtOdu3Tcm1Fees,
       "perEvtOdu3Tcm1Feses": perEvtOdu3Tcm1Feses,
       "perEvtOdu3Tcm1Feuas": perEvtOdu3Tcm1Feuas,
       "perEvtOdu3Tcm1Fesesr": perEvtOdu3Tcm1Fesesr,
       "perEvtOdu3Tcm1Febber": perEvtOdu3Tcm1Febber,
       "perEvtOdu3Tcm2Febbe": perEvtOdu3Tcm2Febbe,
       "perEvtOdu3Tcm2Fees": perEvtOdu3Tcm2Fees,
       "perEvtOdu3Tcm2Feses": perEvtOdu3Tcm2Feses,
       "perEvtOdu3Tcm2Feuas": perEvtOdu3Tcm2Feuas,
       "perEvtOdu3Tcm2Fesesr": perEvtOdu3Tcm2Fesesr,
       "perEvtOdu3Tcm2Febber": perEvtOdu3Tcm2Febber,
       "perEvtOdu3Tcm3Febbe": perEvtOdu3Tcm3Febbe,
       "perEvtOdu3Tcm3Fees": perEvtOdu3Tcm3Fees,
       "perEvtOdu3Tcm3Feses": perEvtOdu3Tcm3Feses,
       "perEvtOdu3Tcm3Feuas": perEvtOdu3Tcm3Feuas,
       "perEvtOdu3Tcm3Fesesr": perEvtOdu3Tcm3Fesesr,
       "perEvtOdu3Tcm3Febber": perEvtOdu3Tcm3Febber,
       "perEvtOdu3Tcm4Febbe": perEvtOdu3Tcm4Febbe,
       "perEvtOdu3Tcm4Fees": perEvtOdu3Tcm4Fees,
       "perEvtOdu3Tcm4Feses": perEvtOdu3Tcm4Feses,
       "perEvtOdu3Tcm4Feuas": perEvtOdu3Tcm4Feuas,
       "perEvtOdu3Tcm4Fesesr": perEvtOdu3Tcm4Fesesr,
       "perEvtOdu3Tcm4Febber": perEvtOdu3Tcm4Febber,
       "perEvtOdu3Tcm5Febbe": perEvtOdu3Tcm5Febbe,
       "perEvtOdu3Tcm5Fees": perEvtOdu3Tcm5Fees,
       "perEvtOdu3Tcm5Feses": perEvtOdu3Tcm5Feses,
       "perEvtOdu3Tcm5Feuas": perEvtOdu3Tcm5Feuas,
       "perEvtOdu3Tcm5Fesesr": perEvtOdu3Tcm5Fesesr,
       "perEvtOdu3Tcm5Febber": perEvtOdu3Tcm5Febber,
       "perEvtOdu3Tcm6Febbe": perEvtOdu3Tcm6Febbe,
       "perEvtOdu3Tcm6Fees": perEvtOdu3Tcm6Fees,
       "perEvtOdu3Tcm6Feses": perEvtOdu3Tcm6Feses,
       "perEvtOdu3Tcm6Feuas": perEvtOdu3Tcm6Feuas,
       "perEvtOdu3Tcm6Fesesr": perEvtOdu3Tcm6Fesesr,
       "perEvtOdu3Tcm6Febber": perEvtOdu3Tcm6Febber,
       "perEvtTheDispersionCompensationMaximumValue": perEvtTheDispersionCompensationMaximumValue,
       "perEvtTheDispersionCompensationMinimumValue": perEvtTheDispersionCompensationMinimumValue,
       "perEvtTheDispersionCompensationCurrentValue": perEvtTheDispersionCompensationCurrentValue,
       "perEvtCpTelDownCount": perEvtCpTelDownCount,
       "perEvtCpTelDownTime": perEvtCpTelDownTime,
       "perEvtCpCcDownCount": perEvtCpCcDownCount,
       "perEvtCpCcDownTime": perEvtCpCcDownTime,
       "perEvtCpuusagemax": perEvtCpuusagemax,
       "perEvtCpuusagemin": perEvtCpuusagemin,
       "perEvtCpuusagecur": perEvtCpuusagecur,
       "perEvtMemusagemax": perEvtMemusagemax,
       "perEvtMemusagemin": perEvtMemusagemin,
       "perEvtMemusagecur": perEvtMemusagecur,
       "perEvtQValueEer": perEvtQValueEer,
       "perEvtfecaftcoreravr": perEvtfecaftcoreravr,
       "perEvtfecbefcoreravr": perEvtfecbefcoreravr,
       "perEvtApdtemmax": perEvtApdtemmax,
       "perEvtApdtemmin": perEvtApdtemmin,
       "perEvtApdtemcur": perEvtApdtemcur,
       "perEvtBdtempmax": perEvtBdtempmax,
       "perEvtBdtempmin": perEvtBdtempmin,
       "perEvtBdtempcur": perEvtBdtempcur,
       "perEvtApdcoolmax": perEvtApdcoolmax,
       "perEvtApdcoolmin": perEvtApdcoolmin,
       "perEvtApdcoolcur": perEvtApdcoolcur,
       "perEvtfecbefcorerfloat": perEvtfecbefcorerfloat,
       "perEvtfecaftcorerfloat": perEvtfecaftcorerfloat,
       "perEvtOdu0PmBbe": perEvtOdu0PmBbe,
       "perEvtOdu0PmEs": perEvtOdu0PmEs,
       "perEvtOdu0PmSes": perEvtOdu0PmSes,
       "perEvtOdu0PmUas": perEvtOdu0PmUas,
       "perEvtOdu0PmSesr": perEvtOdu0PmSesr,
       "perEvtOdu0PmBber": perEvtOdu0PmBber,
       "perEvtOdu0PmFebbe": perEvtOdu0PmFebbe,
       "perEvtOdu0PmFees": perEvtOdu0PmFees,
       "perEvtOdu0PmFeses": perEvtOdu0PmFeses,
       "perEvtOdu0PmFeuas": perEvtOdu0PmFeuas,
       "perEvtOdu0PmFesesr": perEvtOdu0PmFesesr,
       "perEvtOdu0PmFebber": perEvtOdu0PmFebber,
       "perEvtOscBbe": perEvtOscBbe,
       "perEvtOscEs": perEvtOscEs,
       "perEvtOscSes": perEvtOscSes,
       "perEvtOscUas": perEvtOscUas,
       "perEvtOscSesr": perEvtOscSesr,
       "perEvtOscBber": perEvtOscBber,
       "perEvtOscFebbe": perEvtOscFebbe,
       "perEvtOscFees": perEvtOscFees,
       "perEvtOscFeses": perEvtOscFeses,
       "perEvtOscFeuas": perEvtOscFeuas,
       "perEvtOscFesesr": perEvtOscFesesr,
       "perEvtOscFebber": perEvtOscFebber,
       "perEvtOscIaes": perEvtOscIaes,
       "perEvtOscBiaes": perEvtOscBiaes,
       "perEvtMaxfreqdev": perEvtMaxfreqdev,
       "perEvtMinfreqdev": perEvtMinfreqdev,
       "perEvtAvgfreqdev": perEvtAvgfreqdev,
       "perEvtMaxphaseoffset": perEvtMaxphaseoffset,
       "perEvtMinphaseoffset": perEvtMinphaseoffset,
       "perEvtAvgphaseoffset": perEvtAvgphaseoffset,
       "perEvtMaxmeanpathdelay": perEvtMaxmeanpathdelay,
       "perEvtMinmeanpathdelay": perEvtMinmeanpathdelay,
       "perEvtAvgmeanpathdelay": perEvtAvgmeanpathdelay,
       "perEvtMaxpositivedelay": perEvtMaxpositivedelay,
       "perEvtMinpositivedelay": perEvtMinpositivedelay,
       "perEvtAvgpositivedelay": perEvtAvgpositivedelay,
       "perEvtMaxnegativedelay": perEvtMaxnegativedelay,
       "perEvtMinnegativedelay": perEvtMinnegativedelay,
       "perEvtAvgnegativedelay": perEvtAvgnegativedelay,
       "perEvtOtu4Iaes": perEvtOtu4Iaes,
       "perEvtOtu4Biaes": perEvtOtu4Biaes,
       "perEvtOtu4Bbe": perEvtOtu4Bbe,
       "perEvtOtu4Es": perEvtOtu4Es,
       "perEvtOtu4Ses": perEvtOtu4Ses,
       "perEvtOtu4Uas": perEvtOtu4Uas,
       "perEvtOtu4Sesr": perEvtOtu4Sesr,
       "perEvtOtu4Bber": perEvtOtu4Bber,
       "perEvtOtu4Febbe": perEvtOtu4Febbe,
       "perEvtOtu4Fees": perEvtOtu4Fees,
       "perEvtOtu4Feses": perEvtOtu4Feses,
       "perEvtOtu4Feuas": perEvtOtu4Feuas,
       "perEvtOtu4Fesesr": perEvtOtu4Fesesr,
       "perEvtOtu4Febber": perEvtOtu4Febber,
       "perEvtOdu4Pmbbe": perEvtOdu4Pmbbe,
       "perEvtOdu4Pmes": perEvtOdu4Pmes,
       "perEvtOdu4Pmses": perEvtOdu4Pmses,
       "perEvtOtu4Pmuas": perEvtOtu4Pmuas,
       "perEvtOdu4Pmsesr": perEvtOdu4Pmsesr,
       "perEvtOdu4Pmbber": perEvtOdu4Pmbber,
       "perEvtOdu4Pmfebbe": perEvtOdu4Pmfebbe,
       "perEvtOdu4Pmfees": perEvtOdu4Pmfees,
       "perEvtOdu4Pmfeses": perEvtOdu4Pmfeses,
       "perEvtOdu4Pmfeuas": perEvtOdu4Pmfeuas,
       "perEvtOdu4Pmfesesr": perEvtOdu4Pmfesesr,
       "perEvtOdu4Pmfebber": perEvtOdu4Pmfebber,
       "perEvtOdu4Tcm1Iaes": perEvtOdu4Tcm1Iaes,
       "perEvtOdu4Tcm2Iaes": perEvtOdu4Tcm2Iaes,
       "perEvtOdu4Tcm3Iaes": perEvtOdu4Tcm3Iaes,
       "perEvtOdu4Tcm4Iaes": perEvtOdu4Tcm4Iaes,
       "perEvtOdu4Tcm5Iaes": perEvtOdu4Tcm5Iaes,
       "perEvtOdu4Tcm6Iaes": perEvtOdu4Tcm6Iaes,
       "perEvtOdu4Tcm1Biaes": perEvtOdu4Tcm1Biaes,
       "perEvtOdu4Tcm2Biaes": perEvtOdu4Tcm2Biaes,
       "perEvtOdu4Tcm3Biaes": perEvtOdu4Tcm3Biaes,
       "perEvtOdu4Tcm4Biaes": perEvtOdu4Tcm4Biaes,
       "perEvtOdu4Tcm5Biaes": perEvtOdu4Tcm5Biaes,
       "perEvtOdu4Tcm6Biaes": perEvtOdu4Tcm6Biaes,
       "perEvtOdu4Tcm1Bbe": perEvtOdu4Tcm1Bbe,
       "perEvtOdu4Tcm1Es": perEvtOdu4Tcm1Es,
       "perEvtOdu4Tcm1Ses": perEvtOdu4Tcm1Ses,
       "perEvtOdu4Tcm1Uas": perEvtOdu4Tcm1Uas,
       "perEvtOdu4Tcm1Sesr": perEvtOdu4Tcm1Sesr,
       "perEvtOdu4Tcm1Bber": perEvtOdu4Tcm1Bber,
       "perEvtOdu4Tcm2Bbe": perEvtOdu4Tcm2Bbe,
       "perEvtOdu4Tcm2Es": perEvtOdu4Tcm2Es,
       "perEvtOdu4Tcm2Ses": perEvtOdu4Tcm2Ses,
       "perEvtOdu4Tcm2Uas": perEvtOdu4Tcm2Uas,
       "perEvtOdu4Tcm2Sesr": perEvtOdu4Tcm2Sesr,
       "perEvtOdu4Tcm2Bber": perEvtOdu4Tcm2Bber,
       "perEvtOdu4Tcm3Bbe": perEvtOdu4Tcm3Bbe,
       "perEvtOdu4Tcm3Es": perEvtOdu4Tcm3Es,
       "perEvtOdu4Tcm3Ses": perEvtOdu4Tcm3Ses,
       "perEvtOdu4Tcm3Uas": perEvtOdu4Tcm3Uas,
       "perEvtOdu4Tcm3Sesr": perEvtOdu4Tcm3Sesr,
       "perEvtOdu4Tcm3Bber": perEvtOdu4Tcm3Bber,
       "perEvtOdu4Tcm4Bbe": perEvtOdu4Tcm4Bbe,
       "perEvtOdu4Tcm4Es": perEvtOdu4Tcm4Es,
       "perEvtOdu4Tcm4Ses": perEvtOdu4Tcm4Ses,
       "perEvtOdu4Tcm4Uas": perEvtOdu4Tcm4Uas,
       "perEvtOdu4Tcm4Sesr": perEvtOdu4Tcm4Sesr,
       "perEvtOdu4Tcm4Bber": perEvtOdu4Tcm4Bber,
       "perEvtOdu4Tcm5Bbe": perEvtOdu4Tcm5Bbe,
       "perEvtOdu4Tcm5Es": perEvtOdu4Tcm5Es,
       "perEvtOdu4Tcm5Ses": perEvtOdu4Tcm5Ses,
       "perEvtOdu4Tcm5Uas": perEvtOdu4Tcm5Uas,
       "perEvtOdu4Tcm5Sesr": perEvtOdu4Tcm5Sesr,
       "perEvtOdu4Tcm5Bber": perEvtOdu4Tcm5Bber,
       "perEvtOdu4Tcm6Bbe": perEvtOdu4Tcm6Bbe,
       "perEvtOdu4Tcm6Es": perEvtOdu4Tcm6Es,
       "perEvtOdu4Tcm6Ses": perEvtOdu4Tcm6Ses,
       "perEvtOdu4Tcm6Uas": perEvtOdu4Tcm6Uas,
       "perEvtOdu4Tcm6Sesr": perEvtOdu4Tcm6Sesr,
       "perEvtOdu4Tcm6Bber": perEvtOdu4Tcm6Bber,
       "perEvtOdu4Tcm1Febbe": perEvtOdu4Tcm1Febbe,
       "perEvtOdu4Tcm1Fees": perEvtOdu4Tcm1Fees,
       "perEvtOdu4Tcm1Feses": perEvtOdu4Tcm1Feses,
       "perEvtOdu4Tcm1Feuas": perEvtOdu4Tcm1Feuas,
       "perEvtOdu4Tcm1Fesesr": perEvtOdu4Tcm1Fesesr,
       "perEvtOdu4Tcm1Febber": perEvtOdu4Tcm1Febber,
       "perEvtOdu4Tcm2Febbe": perEvtOdu4Tcm2Febbe,
       "perEvtOdu4Tcm2Fees": perEvtOdu4Tcm2Fees,
       "perEvtOdu4Tcm2Feses": perEvtOdu4Tcm2Feses,
       "perEvtOdu4Tcm2Feuas": perEvtOdu4Tcm2Feuas,
       "perEvtOdu4Tcm2Fesesr": perEvtOdu4Tcm2Fesesr,
       "perEvtOdu4Tcm2Febber": perEvtOdu4Tcm2Febber,
       "perEvtOdu4Tcm3Febbe": perEvtOdu4Tcm3Febbe,
       "perEvtOdu4Tcm3Fees": perEvtOdu4Tcm3Fees,
       "perEvtOdu4Tcm3Feses": perEvtOdu4Tcm3Feses,
       "perEvtOdu4Tcm3Feuas": perEvtOdu4Tcm3Feuas,
       "perEvtOdu4Tcm3Fesesr": perEvtOdu4Tcm3Fesesr,
       "perEvtOdu4Tcm3Febber": perEvtOdu4Tcm3Febber,
       "perEvtOdu4Tcm4Febbe": perEvtOdu4Tcm4Febbe,
       "perEvtOdu4Tcm4Fees": perEvtOdu4Tcm4Fees,
       "perEvtOdu4Tcm4Feses": perEvtOdu4Tcm4Feses,
       "perEvtOdu4Tcm4Feuas": perEvtOdu4Tcm4Feuas,
       "perEvtOdu4Tcm4Fesesr": perEvtOdu4Tcm4Fesesr,
       "perEvtOdu4Tcm4Febber": perEvtOdu4Tcm4Febber,
       "perEvtOdu4Tcm5Febbe": perEvtOdu4Tcm5Febbe,
       "perEvtOdu4Tcm5Fees": perEvtOdu4Tcm5Fees,
       "perEvtOdu4Tcm5Feses": perEvtOdu4Tcm5Feses,
       "perEvtOdu4Tcm5Feuas": perEvtOdu4Tcm5Feuas,
       "perEvtOdu4Tcm5Fesesr": perEvtOdu4Tcm5Fesesr,
       "perEvtOdu4Tcm5Febber": perEvtOdu4Tcm5Febber,
       "perEvtOdu4Tcm6Febbe": perEvtOdu4Tcm6Febbe,
       "perEvtOdu4Tcm6Fees": perEvtOdu4Tcm6Fees,
       "perEvtOdu4Tcm6Feses": perEvtOdu4Tcm6Feses,
       "perEvtOdu4Tcm6Feuas": perEvtOdu4Tcm6Feuas,
       "perEvtOdu4Tcm6Fesesr": perEvtOdu4Tcm6Fesesr,
       "perEvtOdu4Tcm6Febber": perEvtOdu4Tcm6Febber,
       "perEvtOduflexPmBbe": perEvtOduflexPmBbe,
       "perEvtOduflexPmEs": perEvtOduflexPmEs,
       "perEvtOduflexPmSes": perEvtOduflexPmSes,
       "perEvtOduflexPmUas": perEvtOduflexPmUas,
       "perEvtOduflexPmSesr": perEvtOduflexPmSesr,
       "perEvtOduflexPmBber": perEvtOduflexPmBber,
       "perEvtOduflexPmFebbe": perEvtOduflexPmFebbe,
       "perEvtOduflexPmFees": perEvtOduflexPmFees,
       "perEvtOduflexPmFeses": perEvtOduflexPmFeses,
       "perEvtOduflexPmFeuas": perEvtOduflexPmFeuas,
       "perEvtOduflexPmFesesr": perEvtOduflexPmFesesr,
       "perEvtOduflexPmFebber": perEvtOduflexPmFebber,
       "perEvtOdu0Tcm1Bbe": perEvtOdu0Tcm1Bbe,
       "perEvtOdu0Tcm1Es": perEvtOdu0Tcm1Es,
       "perEvtOdu0Tcm1Ses": perEvtOdu0Tcm1Ses,
       "perEvtOdu0Tcm1Uas": perEvtOdu0Tcm1Uas,
       "perEvtOdu0Tcm1Sesr": perEvtOdu0Tcm1Sesr,
       "perEvtOdu0Tcm1Bber": perEvtOdu0Tcm1Bber,
       "perEvtOdu0Tcm1Febbe": perEvtOdu0Tcm1Febbe,
       "perEvtOdu0Tcm1Fees": perEvtOdu0Tcm1Fees,
       "perEvtOdu0Tcm1Feses": perEvtOdu0Tcm1Feses,
       "perEvtOdu0Tcm1Feuas": perEvtOdu0Tcm1Feuas,
       "perEvtOdu0Tcm1Fesesr": perEvtOdu0Tcm1Fesesr,
       "perEvtOdu0Tcm1Febber": perEvtOdu0Tcm1Febber,
       "perEvtOdu0Tcm1Iaes": perEvtOdu0Tcm1Iaes,
       "perEvtOdu0Tcm1Biaes": perEvtOdu0Tcm1Biaes,
       "perEvtOdu0Tcm2Bbe": perEvtOdu0Tcm2Bbe,
       "perEvtOdu0Tcm2Es": perEvtOdu0Tcm2Es,
       "perEvtOdu0Tcm2Ses": perEvtOdu0Tcm2Ses,
       "perEvtOdu0Tcm2Uas": perEvtOdu0Tcm2Uas,
       "perEvtOdu0Tcm2Sesr": perEvtOdu0Tcm2Sesr,
       "perEvtOdu0Tcm2Bber": perEvtOdu0Tcm2Bber,
       "perEvtOdu0Tcm2Febbe": perEvtOdu0Tcm2Febbe,
       "perEvtOdu0Tcm2Fees": perEvtOdu0Tcm2Fees,
       "perEvtOdu0Tcm2Feses": perEvtOdu0Tcm2Feses,
       "perEvtOdu0Tcm2Feuas": perEvtOdu0Tcm2Feuas,
       "perEvtOdu0Tcm2Fesesr": perEvtOdu0Tcm2Fesesr,
       "perEvtOdu0Tcm2Febber": perEvtOdu0Tcm2Febber,
       "perEvtOdu0Tcm2Iaes": perEvtOdu0Tcm2Iaes,
       "perEvtOdu0Tcm2Biaes": perEvtOdu0Tcm2Biaes,
       "perEvtOdu0Tcm3Bbe": perEvtOdu0Tcm3Bbe,
       "perEvtOdu0Tcm3Es": perEvtOdu0Tcm3Es,
       "perEvtOdu0Tcm3Ses": perEvtOdu0Tcm3Ses,
       "perEvtOdu0Tcm3Uas": perEvtOdu0Tcm3Uas,
       "perEvtOdu0Tcm3Sesr": perEvtOdu0Tcm3Sesr,
       "perEvtOdu0Tcm3Bber": perEvtOdu0Tcm3Bber,
       "perEvtOdu0Tcm3Febbe": perEvtOdu0Tcm3Febbe,
       "perEvtOdu0Tcm3Fees": perEvtOdu0Tcm3Fees,
       "perEvtOdu0Tcm3Feses": perEvtOdu0Tcm3Feses,
       "perEvtOdu0Tcm3Feuas": perEvtOdu0Tcm3Feuas,
       "perEvtOdu0Tcm3Fesesr": perEvtOdu0Tcm3Fesesr,
       "perEvtOdu0Tcm3Febber": perEvtOdu0Tcm3Febber,
       "perEvtOdu0Tcm3Iaes": perEvtOdu0Tcm3Iaes,
       "perEvtOdu0Tcm3Biaes": perEvtOdu0Tcm3Biaes,
       "perEvtOdu0Tcm4Bbe": perEvtOdu0Tcm4Bbe,
       "perEvtOdu0Tcm4Es": perEvtOdu0Tcm4Es,
       "perEvtOdu0Tcm4Ses": perEvtOdu0Tcm4Ses,
       "perEvtOdu0Tcm4Uas": perEvtOdu0Tcm4Uas,
       "perEvtOdu0Tcm4Sesr": perEvtOdu0Tcm4Sesr,
       "perEvtOdu0Tcm4Bber": perEvtOdu0Tcm4Bber,
       "perEvtOdu0Tcm4Febbe": perEvtOdu0Tcm4Febbe,
       "perEvtOdu0Tcm4Fees": perEvtOdu0Tcm4Fees,
       "perEvtOdu0Tcm4Feses": perEvtOdu0Tcm4Feses,
       "perEvtOdu0Tcm4Feuas": perEvtOdu0Tcm4Feuas,
       "perEvtOdu0Tcm4Fesesr": perEvtOdu0Tcm4Fesesr,
       "perEvtOdu0Tcm4Febber": perEvtOdu0Tcm4Febber,
       "perEvtOdu0Tcm4Iaes": perEvtOdu0Tcm4Iaes,
       "perEvtOdu0Tcm4Biaes": perEvtOdu0Tcm4Biaes,
       "perEvtOdu0Tcm5Bbe": perEvtOdu0Tcm5Bbe,
       "perEvtOdu0Tcm5Es": perEvtOdu0Tcm5Es,
       "perEvtOdu0Tcm5Ses": perEvtOdu0Tcm5Ses,
       "perEvtOdu0Tcm5Uas": perEvtOdu0Tcm5Uas,
       "perEvtOdu0Tcm5Sesr": perEvtOdu0Tcm5Sesr,
       "perEvtOdu0Tcm5Bber": perEvtOdu0Tcm5Bber,
       "perEvtOdu0Tcm5Febbe": perEvtOdu0Tcm5Febbe,
       "perEvtOdu0Tcm5Fees": perEvtOdu0Tcm5Fees,
       "perEvtOdu0Tcm5Feses": perEvtOdu0Tcm5Feses,
       "perEvtOdu0Tcm5Feuas": perEvtOdu0Tcm5Feuas,
       "perEvtOdu0Tcm5Fesesr": perEvtOdu0Tcm5Fesesr,
       "perEvtOdu0Tcm5Febber": perEvtOdu0Tcm5Febber,
       "perEvtOdu0Tcm5Iaes": perEvtOdu0Tcm5Iaes,
       "perEvtOdu0Tcm5Biaes": perEvtOdu0Tcm5Biaes,
       "perEvtOdu0Tcm6Bbe": perEvtOdu0Tcm6Bbe,
       "perEvtOdu0Tcm6Es": perEvtOdu0Tcm6Es,
       "perEvtOdu0Tcm6Ses": perEvtOdu0Tcm6Ses,
       "perEvtOdu0Tcm6Uas": perEvtOdu0Tcm6Uas,
       "perEvtOdu0Tcm6Sesr": perEvtOdu0Tcm6Sesr,
       "perEvtOdu0Tcm6Bber": perEvtOdu0Tcm6Bber,
       "perEvtOdu0Tcm6Febbe": perEvtOdu0Tcm6Febbe,
       "perEvtOdu0Tcm6Fees": perEvtOdu0Tcm6Fees,
       "perEvtOdu0Tcm6Feses": perEvtOdu0Tcm6Feses,
       "perEvtOdu0Tcm6Feuas": perEvtOdu0Tcm6Feuas,
       "perEvtOdu0Tcm6Fesesr": perEvtOdu0Tcm6Fesesr,
       "perEvtOdu0Tcm6Febber": perEvtOdu0Tcm6Febber,
       "perEvtOdu0Tcm6Iaes": perEvtOdu0Tcm6Iaes,
       "perEvtOdu0Tcm6Biaes": perEvtOdu0Tcm6Biaes,
       "perEvtpmdmax": perEvtpmdmax,
       "perEvtpmdmin": perEvtpmdmin,
       "perEvtpmdcur": perEvtpmdcur,
       "perEvtpeakInpowerMax": perEvtpeakInpowerMax,
       "perEvtpeakInpowerCur": perEvtpeakInpowerCur,
       "perEvtpeakInpowerMin": perEvtpeakInpowerMin,
       "perEvtvalleyInpowerMax": perEvtvalleyInpowerMax,
       "perEvtvalleyInpowerCur": perEvtvalleyInpowerCur,
       "perEvtvalleyInpowerMin": perEvtvalleyInpowerMin,
       "perEvtpeakOutpowerMax": perEvtpeakOutpowerMax,
       "perEvtpeakOutpowerCur": perEvtpeakOutpowerCur,
       "perEvtpeakOutpowerMin": perEvtpeakOutpowerMin,
       "perEvtvalleyOutpowerMax": perEvtvalleyOutpowerMax,
       "perEvtvalleyOutpowerCur": perEvtvalleyOutpowerCur,
       "perEvtvalleyOutpowerMin": perEvtvalleyOutpowerMin,
       "perEvtPeakLstmpMax": perEvtPeakLstmpMax,
       "perEvtPeakLstmpCur": perEvtPeakLstmpCur,
       "perEvtPeakLstmpMin": perEvtPeakLstmpMin,
       "perEvtValleyLstmpMax": perEvtValleyLstmpMax,
       "perEvtValleyLstmpCur": perEvtValleyLstmpCur,
       "perEvtValleyLstmpMin": perEvtValleyLstmpMin,
       "perEvtPeakLsbiasMax": perEvtPeakLsbiasMax,
       "perEvtPeakLsbiasCur": perEvtPeakLsbiasCur,
       "perEvtPeakLsbiasMin": perEvtPeakLsbiasMin,
       "perEvtValleyLsbiasMax": perEvtValleyLsbiasMax,
       "perEvtValleyLsbiasCur": perEvtValleyLsbiasCur,
       "perEvtValleyLsbiasMin": perEvtValleyLsbiasMin,
       "perEvtpmdavg": perEvtpmdavg,
       "perEvtOdu0PmTmp": perEvtOdu0PmTmp,
       "perEvtOdu0Tcm1Tmp": perEvtOdu0Tcm1Tmp,
       "perEvtOdu0Tcm2Tmp": perEvtOdu0Tcm2Tmp,
       "perEvtOdu0Tcm3Tmp": perEvtOdu0Tcm3Tmp,
       "perEvtOdu0Tcm4Tmp": perEvtOdu0Tcm4Tmp,
       "perEvtOdu0Tcm5Tmp": perEvtOdu0Tcm5Tmp,
       "perEvtOdu0Tcm6Tmp": perEvtOdu0Tcm6Tmp,
       "perEvtOtu1Tmp": perEvtOtu1Tmp,
       "perEvtOdu1PmTmp": perEvtOdu1PmTmp,
       "perEvtOdu1Tcm1Tmp": perEvtOdu1Tcm1Tmp,
       "perEvtOdu1Tcm2Tmp": perEvtOdu1Tcm2Tmp,
       "perEvtOdu1Tcm3Tmp": perEvtOdu1Tcm3Tmp,
       "perEvtOdu1Tcm4Tmp": perEvtOdu1Tcm4Tmp,
       "perEvtOdu1Tcm5Tmp": perEvtOdu1Tcm5Tmp,
       "perEvtOdu1Tcm6Tmp": perEvtOdu1Tcm6Tmp,
       "perEvtOtu2Tmp": perEvtOtu2Tmp,
       "perEvtodu2Pmtmp": perEvtodu2Pmtmp,
       "perEvtOdu2Tcm1Tmp": perEvtOdu2Tcm1Tmp,
       "perEvtOdu2Tcm2Tmp": perEvtOdu2Tcm2Tmp,
       "perEvtOdu2Tcm3Tmp": perEvtOdu2Tcm3Tmp,
       "perEvtOdu2Tcm4Tmp": perEvtOdu2Tcm4Tmp,
       "perEvtOdu2Tcm5Tmp": perEvtOdu2Tcm5Tmp,
       "perEvtOdu2Tcm6Tmp": perEvtOdu2Tcm6Tmp,
       "perEvtOtu3Tmp": perEvtOtu3Tmp,
       "perEvtodu3Pmtmp": perEvtodu3Pmtmp,
       "perEvtOdu3Tcm1Tmp": perEvtOdu3Tcm1Tmp,
       "perEvtOdu3Tcm2Tmp": perEvtOdu3Tcm2Tmp,
       "perEvtOdu3Tcm3Tmp": perEvtOdu3Tcm3Tmp,
       "perEvtOdu3Tcm4Tmp": perEvtOdu3Tcm4Tmp,
       "perEvtOdu3Tcm5Tmp": perEvtOdu3Tcm5Tmp,
       "perEvtOdu3Tcm6Tmp": perEvtOdu3Tcm6Tmp,
       "perEvtotu4Tmp": perEvtotu4Tmp,
       "perEvtodu4Pmtmp": perEvtodu4Pmtmp,
       "perEvtOdu4Tcm1Tmp": perEvtOdu4Tcm1Tmp,
       "perEvtOdu4Tcm2Tmp": perEvtOdu4Tcm2Tmp,
       "perEvtOdu4Tcm3Tmp": perEvtOdu4Tcm3Tmp,
       "perEvtOdu4Tcm4Tmp": perEvtOdu4Tcm4Tmp,
       "perEvtOdu4Tcm5Tmp": perEvtOdu4Tcm5Tmp,
       "perEvtOdu4Tcm6Tmp": perEvtOdu4Tcm6Tmp,
       "perEvtOduflexPmTmp": perEvtOduflexPmTmp,
       "perEvtFecTmp": perEvtFecTmp,
       "perEvtRsTmp": perEvtRsTmp,
       "perEvtRmiopmax": perEvtRmiopmax,
       "perEvtRmiopmin": perEvtRmiopmin,
       "perEvtRmiopcur": perEvtRmiopcur,
       "perEvtAswiopmax": perEvtAswiopmax,
       "perEvtAswiopmin": perEvtAswiopmin,
       "perEvtAswiopcur": perEvtAswiopcur,
       "perEvtAaospcur": perEvtAaospcur,
       "perEvtAswoopmax": perEvtAswoopmax,
       "perEvtAswoopmin": perEvtAswoopmin,
       "perEvtAswoopcur": perEvtAswoopcur,
       "perEvtAswsnrmax": perEvtAswsnrmax,
       "perEvtAswsnrmin": perEvtAswsnrmin,
       "perEvtAswsnrcur": perEvtAswsnrcur,
       "perEvtAswsnlmax": perEvtAswsnlmax,
       "perEvtAswsnlmin": perEvtAswsnlmin,
       "perEvtAswsnlcur": perEvtAswsnlcur,
       "perEvtAainpmax": perEvtAainpmax,
       "perEvtAainpmin": perEvtAainpmin,
       "perEvtAainpcur": perEvtAainpcur,
       "perEvtAaispmax": perEvtAaispmax,
       "perEvtAaispmin": perEvtAaispmin,
       "perEvtAaispcur": perEvtAaispcur,
       "perEvtAaonpmax": perEvtAaonpmax,
       "perEvtAaonpmin": perEvtAaonpmin,
       "perEvtAaonpcur": perEvtAaonpcur,
       "perEvtAaospmax": perEvtAaospmax,
       "perEvtAaospmin": perEvtAaospmin,
       "perEvtOduflexTcm6Fesesr": perEvtOduflexTcm6Fesesr,
       "perEvtOduflexTcm5Tmp": perEvtOduflexTcm5Tmp,
       "perEvtOduflexTcm6Feuas": perEvtOduflexTcm6Feuas,
       "perEvtOduflexTcm6Feses": perEvtOduflexTcm6Feses,
       "perEvtOduflexTcm6Ses": perEvtOduflexTcm6Ses,
       "perEvtOduflexTcm6Fees": perEvtOduflexTcm6Fees,
       "perEvtOduflexTcm6Es": perEvtOduflexTcm6Es,
       "perEvtOduflexTcm6Bbe": perEvtOduflexTcm6Bbe,
       "perEvtOduflexTcm6Bber": perEvtOduflexTcm6Bber,
       "perEvtOduflexTcm6Febbe": perEvtOduflexTcm6Febbe,
       "perEvtOduflexTcm6Sesr": perEvtOduflexTcm6Sesr,
       "perEvtOduflexTcm6Uas": perEvtOduflexTcm6Uas,
       "perEvtOduflexTcm6Iaes": perEvtOduflexTcm6Iaes,
       "perEvtOduflexTcm6Biaes": perEvtOduflexTcm6Biaes,
       "perEvtOduflexTcm6Febber": perEvtOduflexTcm6Febber,
       "perEvtOduflexTcm6Tmp": perEvtOduflexTcm6Tmp,
       "perEvtOduflexTcm2Uas": perEvtOduflexTcm2Uas,
       "perEvtOduflexTcm1Febbe": perEvtOduflexTcm1Febbe,
       "perEvtOduflexTcm5Febber": perEvtOduflexTcm5Febber,
       "perEvtOduflexTcm5Fesesr": perEvtOduflexTcm5Fesesr,
       "perEvtOduflexTcm5Bber": perEvtOduflexTcm5Bber,
       "perEvtOduflexTcm5Sesr": perEvtOduflexTcm5Sesr,
       "perEvtOduflexTcm5Fees": perEvtOduflexTcm5Fees,
       "perEvtOduflexTcm5Febbe": perEvtOduflexTcm5Febbe,
       "perEvtOduflexTcm5Feuas": perEvtOduflexTcm5Feuas,
       "perEvtOduflexTcm5Feses": perEvtOduflexTcm5Feses,
       "perEvtOduflexTcm5Uas": perEvtOduflexTcm5Uas,
       "perEvtOduflexTcm5Ses": perEvtOduflexTcm5Ses,
       "perEvtOduflexTcm5Es": perEvtOduflexTcm5Es,
       "perEvtOduflexTcm5Bbe": perEvtOduflexTcm5Bbe,
       "perEvtOduflexTcm5Biaes": perEvtOduflexTcm5Biaes,
       "perEvtOduflexTcm5Iaes": perEvtOduflexTcm5Iaes,
       "perEvtOduflexTcm4Biaes": perEvtOduflexTcm4Biaes,
       "perEvtOduflexTcm4Iaes": perEvtOduflexTcm4Iaes,
       "perEvtOduflexTcm4Febber": perEvtOduflexTcm4Febber,
       "perEvtOduflexTcm4Fesesr": perEvtOduflexTcm4Fesesr,
       "perEvtOduflexTcm4Feuas": perEvtOduflexTcm4Feuas,
       "perEvtOduflexTcm4Feses": perEvtOduflexTcm4Feses,
       "perEvtOduflexTcm4Fees": perEvtOduflexTcm4Fees,
       "perEvtOduflexTcm4Febbe": perEvtOduflexTcm4Febbe,
       "perEvtOduflexTcm4Uas": perEvtOduflexTcm4Uas,
       "perEvtOduflexTcm4Ses": perEvtOduflexTcm4Ses,
       "perEvtOduflexTcm4Bber": perEvtOduflexTcm4Bber,
       "perEvtOduflexTcm4Sesr": perEvtOduflexTcm4Sesr,
       "perEvtOduflexTcm4Es": perEvtOduflexTcm4Es,
       "perEvtOduflexTcm4Bbe": perEvtOduflexTcm4Bbe,
       "perEvtOduflexTcm4Tmp": perEvtOduflexTcm4Tmp,
       "perEvtOduflexTcm1Fesesr": perEvtOduflexTcm1Fesesr,
       "perEvtOduflexTcm1Biaes": perEvtOduflexTcm1Biaes,
       "perEvtOduflexTcm1Febber": perEvtOduflexTcm1Febber,
       "perEvtOduflexTcm1Iaes": perEvtOduflexTcm1Iaes,
       "perEvtOduflexTcm1Feuas": perEvtOduflexTcm1Feuas,
       "perEvtOduflexTcm1Feses": perEvtOduflexTcm1Feses,
       "perEvtOduflexTcm1Sesr": perEvtOduflexTcm1Sesr,
       "perEvtOduflexTcm1Bber": perEvtOduflexTcm1Bber,
       "perEvtOduflexTcm1Fees": perEvtOduflexTcm1Fees,
       "perEvtOduflexTcm1Bbe": perEvtOduflexTcm1Bbe,
       "perEvtOduflexTcm1Es": perEvtOduflexTcm1Es,
       "perEvtOduflexTcm1Ses": perEvtOduflexTcm1Ses,
       "perEvtOduflexTcm1Uas": perEvtOduflexTcm1Uas,
       "perEvtOduflexTcm1Tmp": perEvtOduflexTcm1Tmp,
       "perEvtOduflexTcm2Febbe": perEvtOduflexTcm2Febbe,
       "perEvtOduflexTcm2Fees": perEvtOduflexTcm2Fees,
       "perEvtOduflexTcm2Feses": perEvtOduflexTcm2Feses,
       "perEvtOduflexTcm2Feuas": perEvtOduflexTcm2Feuas,
       "perEvtOduflexTcm2Fesesr": perEvtOduflexTcm2Fesesr,
       "perEvtOduflexTcm2Febber": perEvtOduflexTcm2Febber,
       "perEvtOduflexTcm2Iaes": perEvtOduflexTcm2Iaes,
       "perEvtOduflexTcm2Biaes": perEvtOduflexTcm2Biaes,
       "perEvtOduflexTcm2Bber": perEvtOduflexTcm2Bber,
       "perEvtOduflexTcm2Sesr": perEvtOduflexTcm2Sesr,
       "perEvtOduflexTcm2Es": perEvtOduflexTcm2Es,
       "perEvtOduflexTcm2Ses": perEvtOduflexTcm2Ses,
       "perEvtOduflexTcm2Bbe": perEvtOduflexTcm2Bbe,
       "perEvtOduflexTcm2Tmp": perEvtOduflexTcm2Tmp,
       "perEvtOduflexTcm3Uas": perEvtOduflexTcm3Uas,
       "perEvtOduflexTcm3Sesr": perEvtOduflexTcm3Sesr,
       "perEvtOduflexTcm3Ses": perEvtOduflexTcm3Ses,
       "perEvtOduflexTcm3Fees": perEvtOduflexTcm3Fees,
       "perEvtOduflexTcm3Feses": perEvtOduflexTcm3Feses,
       "perEvtOduflexTcm3Bber": perEvtOduflexTcm3Bber,
       "perEvtOduflexTcm3Febbe": perEvtOduflexTcm3Febbe,
       "perEvtOduflexTcm3Febber": perEvtOduflexTcm3Febber,
       "perEvtOduflexTcm3Feuas": perEvtOduflexTcm3Feuas,
       "perEvtOduflexTcm3Fesesr": perEvtOduflexTcm3Fesesr,
       "perEvtOduflexTcm3Bbe": perEvtOduflexTcm3Bbe,
       "perEvtOduflexTcm3Es": perEvtOduflexTcm3Es,
       "perEvtOduflexTcm3Biaes": perEvtOduflexTcm3Biaes,
       "perEvtOduflexTcm3Iaes": perEvtOduflexTcm3Iaes,
       "perEvtOduflexTcm3Tmp": perEvtOduflexTcm3Tmp,
       "perEvtethBbe": perEvtethBbe,
       "perEvtethBber": perEvtethBber,
       "perEvtethSesr": perEvtethSesr,
       "perEvtethUas": perEvtethUas,
       "perEvtethEs": perEvtethEs,
       "perEvtethSes": perEvtethSes,
       "perEvtAmbtempmax": perEvtAmbtempmax,
       "perEvtAmbtempmin": perEvtAmbtempmin,
       "perEvtAmbtempcur": perEvtAmbtempcur,
       "perEvtEthEsr": perEvtEthEsr,
       "perEvtOtucnBbe": perEvtOtucnBbe,
       "perEvtOtucnFees": perEvtOtucnFees,
       "perEvtOtucnFebbe": perEvtOtucnFebbe,
       "perEvtOtucnBber": perEvtOtucnBber,
       "perEvtOtucnSesr": perEvtOtucnSesr,
       "perEvtOtucnFeses": perEvtOtucnFeses,
       "perEvtOtucnBiaes": perEvtOtucnBiaes,
       "perEvtOtucnUas": perEvtOtucnUas,
       "perEvtOtucnSes": perEvtOtucnSes,
       "perEvtOtucnEs": perEvtOtucnEs,
       "perEvtOtucnIaes": perEvtOtucnIaes,
       "perEvtOtucnFebber": perEvtOtucnFebber,
       "perEvtOtucnFeuas": perEvtOtucnFeuas,
       "perEvtOtucnTmp": perEvtOtucnTmp,
       "perEvtOtucnFesesr": perEvtOtucnFesesr,
       "perEvtOducnPmFesesr": perEvtOducnPmFesesr,
       "perEvtOducnPmFebber": perEvtOducnPmFebber,
       "perEvtOducnPmFees": perEvtOducnPmFees,
       "perEvtOducnPmFeses": perEvtOducnPmFeses,
       "perEvtOducnPmFeuas": perEvtOducnPmFeuas,
       "perEvtOducnPmEs": perEvtOducnPmEs,
       "perEvtOducnPmSes": perEvtOducnPmSes,
       "perEvtOducnPmBbe": perEvtOducnPmBbe,
       "perEvtOducnPmBber": perEvtOducnPmBber,
       "perEvtOducnPmFebbe": perEvtOducnPmFebbe,
       "perEvtOducnPmUas": perEvtOducnPmUas,
       "perEvtOducnPmSesr": perEvtOducnPmSesr,
       "perEvtOducnPmTmp": perEvtOducnPmTmp,
       "perEvtCfpLsiopmax": perEvtCfpLsiopmax,
       "perEvtCfpLsiopmin": perEvtCfpLsiopmin,
       "perEvtCfpLsiopcur": perEvtCfpLsiopcur,
       "perEvtCfpLsoopmax": perEvtCfpLsoopmax,
       "perEvtCfpLsoopmin": perEvtCfpLsoopmin,
       "perEvtCfpLsoopcur": perEvtCfpLsoopcur,
       "perEvtCfpLstmpmax": perEvtCfpLstmpmax,
       "perEvtCfpLstmpmin": perEvtCfpLstmpmin,
       "perEvtCfpLstmpcur": perEvtCfpLstmpcur,
       "perEvtCfpLsbiasmax": perEvtCfpLsbiasmax,
       "perEvtCfpLsbiasmin": perEvtCfpLsbiasmin,
       "perEvtCfpLsbiascur": perEvtCfpLsbiascur,
       "perEvtMaxsumphaseoffset": perEvtMaxsumphaseoffset,
       "perEvtMinsumphaseoffset": perEvtMinsumphaseoffset,
       "perEvtAvgsumphaseoffset": perEvtAvgsumphaseoffset,
       "perEvtQValueEerAver15m": perEvtQValueEerAver15m,
       "perEvtQValueEerAver24h": perEvtQValueEerAver24h,
       "perEvtPumporpcur": perEvtPumporpcur,
       "perEvtPumporpmax": perEvtPumporpmax,
       "perEvtPumporpmin": perEvtPumporpmin,
       "perEvtFswiopmax": perEvtFswiopmax,
       "perEvtFswiopmin": perEvtFswiopmin,
       "perEvtFswiopcur": perEvtFswiopcur,
       "perEvtFswoopmax": perEvtFswoopmax,
       "perEvtFswoopmin": perEvtFswoopmin,
       "perEvtFswoopcur": perEvtFswoopcur,
       "perEvtFswsnrmax": perEvtFswsnrmax,
       "perEvtFswsnrmin": perEvtFswsnrmin,
       "perEvtFswsnrcur": perEvtFswsnrcur,
       "perEvtFswsnlmax": perEvtFswsnlmax,
       "perEvtFswsnlmin": perEvtFswsnlmin,
       "perEvtFswsnlcur": perEvtFswsnlcur,
       "perEvtFclsopmax": perEvtFclsopmax,
       "perEvtFclsopmin": perEvtFclsopmin,
       "perEvtFclsopcur": perEvtFclsopcur,
       "perEvtlanelsoopmax": perEvtlanelsoopmax,
       "perEvtlanelsoopmin": perEvtlanelsoopmin,
       "perEvtlanelsoopcur": perEvtlanelsoopcur,
       "perEvtlanelsiopmax": perEvtlanelsiopmax,
       "perEvtlanelsiopmin": perEvtlanelsiopmin,
       "perEvtlanelsiopcur": perEvtlanelsiopcur,
       "perEvtlanelsbiasmax": perEvtlanelsbiasmax,
       "perEvtlanelsbiasmin": perEvtlanelsbiasmin,
       "perEvtlanelsbiascur": perEvtlanelsbiascur,
       "perEvtSubcardtmpmax": perEvtSubcardtmpmax,
       "perEvtSubcardtmpmin": perEvtSubcardtmpmin,
       "perEvtSubcardtmpcur": perEvtSubcardtmpcur,
       "perEvtSdiBbe": perEvtSdiBbe,
       "perEvtSdiBber": perEvtSdiBber,
       "perEvtSdiSesr": perEvtSdiSesr,
       "perEvtSdiUas": perEvtSdiUas,
       "perEvtSdiEs": perEvtSdiEs,
       "perEvtSdiSes": perEvtSdiSes,
       "perEvtFpclswlomax": perEvtFpclswlomax,
       "perEvtFpclswlomin": perEvtFpclswlomin,
       "perEvtFpclswlocur": perEvtFpclswlocur,
       "perEvtGaincur": perEvtGaincur,
       "perEvtGainmax": perEvtGainmax,
       "perEvtGainmin": perEvtGainmin,
       "perEvtLsvolmax": perEvtLsvolmax,
       "perEvtLsvolmin": perEvtLsvolmin,
       "perEvtLsvolcur": perEvtLsvolcur,
       "perEvtOducnTcm1Iaes": perEvtOducnTcm1Iaes,
       "perEvtOducnTcm2Iaes": perEvtOducnTcm2Iaes,
       "perEvtOducnTcm3Iaes": perEvtOducnTcm3Iaes,
       "perEvtOducnTcm4Iaes": perEvtOducnTcm4Iaes,
       "perEvtOducnTcm5Iaes": perEvtOducnTcm5Iaes,
       "perEvtOducnTcm6Iaes": perEvtOducnTcm6Iaes,
       "perEvtOducnTcm1Biaes": perEvtOducnTcm1Biaes,
       "perEvtOducnTcm2Biaes": perEvtOducnTcm2Biaes,
       "perEvtOducnTcm3Biaes": perEvtOducnTcm3Biaes,
       "perEvtOducnTcm4Biaes": perEvtOducnTcm4Biaes,
       "perEvtOducnTcm5Biaes": perEvtOducnTcm5Biaes,
       "perEvtOducnTcm6Biaes": perEvtOducnTcm6Biaes,
       "perEvtOducnTcm1Bbe": perEvtOducnTcm1Bbe,
       "perEvtOducnTcm2Bbe": perEvtOducnTcm2Bbe,
       "perEvtOducnTcm3Bbe": perEvtOducnTcm3Bbe,
       "perEvtOducnTcm4Bbe": perEvtOducnTcm4Bbe,
       "perEvtOducnTcm5Bbe": perEvtOducnTcm5Bbe,
       "perEvtOducnTcm6Bbe": perEvtOducnTcm6Bbe,
       "perEvtOducnTcm1Es": perEvtOducnTcm1Es,
       "perEvtOducnTcm2Es": perEvtOducnTcm2Es,
       "perEvtOducnTcm3Es": perEvtOducnTcm3Es,
       "perEvtOducnTcm4Es": perEvtOducnTcm4Es,
       "perEvtOducnTcm5Es": perEvtOducnTcm5Es,
       "perEvtOducnTcm6Es": perEvtOducnTcm6Es,
       "perEvtOducnTcm1Ses": perEvtOducnTcm1Ses,
       "perEvtOducnTcm2Ses": perEvtOducnTcm2Ses,
       "perEvtOducnTcm3Ses": perEvtOducnTcm3Ses,
       "perEvtOducnTcm4Ses": perEvtOducnTcm4Ses,
       "perEvtOducnTcm5Ses": perEvtOducnTcm5Ses,
       "perEvtOducnTcm6Ses": perEvtOducnTcm6Ses,
       "perEvtOducnTcm1Uas": perEvtOducnTcm1Uas,
       "perEvtOducnTcm2Uas": perEvtOducnTcm2Uas,
       "perEvtOducnTcm3Uas": perEvtOducnTcm3Uas,
       "perEvtOducnTcm4Uas": perEvtOducnTcm4Uas,
       "perEvtOducnTcm5Uas": perEvtOducnTcm5Uas,
       "perEvtOducnTcm6Uas": perEvtOducnTcm6Uas,
       "perEvtOducnTcm1Sesr": perEvtOducnTcm1Sesr,
       "perEvtOducnTcm2Sesr": perEvtOducnTcm2Sesr,
       "perEvtOducnTcm3Sesr": perEvtOducnTcm3Sesr,
       "perEvtOducnTcm4Sesr": perEvtOducnTcm4Sesr,
       "perEvtOducnTcm5Sesr": perEvtOducnTcm5Sesr,
       "perEvtOducnTcm6Sesr": perEvtOducnTcm6Sesr,
       "perEvtOducnTcm1Bber": perEvtOducnTcm1Bber,
       "perEvtOducnTcm2Bber": perEvtOducnTcm2Bber,
       "perEvtOducnTcm3Bber": perEvtOducnTcm3Bber,
       "perEvtOducnTcm4Bber": perEvtOducnTcm4Bber,
       "perEvtOducnTcm5Bber": perEvtOducnTcm5Bber,
       "perEvtOducnTcm6Bber": perEvtOducnTcm6Bber,
       "perEvtOducnTcm1Febbe": perEvtOducnTcm1Febbe,
       "perEvtOducnTcm2Febbe": perEvtOducnTcm2Febbe,
       "perEvtOducnTcm3Febbe": perEvtOducnTcm3Febbe,
       "perEvtOducnTcm4Febbe": perEvtOducnTcm4Febbe,
       "perEvtOducnTcm5Febbe": perEvtOducnTcm5Febbe,
       "perEvtOducnTcm6Febbe": perEvtOducnTcm6Febbe,
       "perEvtOducnTcm1Fees": perEvtOducnTcm1Fees,
       "perEvtOducnTcm2Fees": perEvtOducnTcm2Fees,
       "perEvtOducnTcm3Fees": perEvtOducnTcm3Fees,
       "perEvtOducnTcm4Fees": perEvtOducnTcm4Fees,
       "perEvtOducnTcm5Fees": perEvtOducnTcm5Fees,
       "perEvtOducnTcm6Fees": perEvtOducnTcm6Fees,
       "perEvtOducnTcm1Feses": perEvtOducnTcm1Feses,
       "perEvtOducnTcm2Feses": perEvtOducnTcm2Feses,
       "perEvtOducnTcm3Feses": perEvtOducnTcm3Feses,
       "perEvtOducnTcm4Feses": perEvtOducnTcm4Feses,
       "perEvtOducnTcm5Feses": perEvtOducnTcm5Feses,
       "perEvtOducnTcm6Feses": perEvtOducnTcm6Feses,
       "perEvtOducnTcm1Feuas": perEvtOducnTcm1Feuas,
       "perEvtOducnTcm2Feuas": perEvtOducnTcm2Feuas,
       "perEvtOducnTcm3Feuas": perEvtOducnTcm3Feuas,
       "perEvtOducnTcm4Feuas": perEvtOducnTcm4Feuas,
       "perEvtOducnTcm5Feuas": perEvtOducnTcm5Feuas,
       "perEvtOducnTcm6Feuas": perEvtOducnTcm6Feuas,
       "perEvtOducnTcm1Fesesr": perEvtOducnTcm1Fesesr,
       "perEvtOducnTcm2Fesesr": perEvtOducnTcm2Fesesr,
       "perEvtOducnTcm3Fesesr": perEvtOducnTcm3Fesesr,
       "perEvtOducnTcm4Fesesr": perEvtOducnTcm4Fesesr,
       "perEvtOducnTcm5Fesesr": perEvtOducnTcm5Fesesr,
       "perEvtOducnTcm6Fesesr": perEvtOducnTcm6Fesesr,
       "perEvtOducnTcm1Febber": perEvtOducnTcm1Febber,
       "perEvtOducnTcm2Febber": perEvtOducnTcm2Febber,
       "perEvtOducnTcm3Febber": perEvtOducnTcm3Febber,
       "perEvtOducnTcm4Febber": perEvtOducnTcm4Febber,
       "perEvtOducnTcm5Febber": perEvtOducnTcm5Febber,
       "perEvtOducnTcm6Febber": perEvtOducnTcm6Febber,
       "perEvtOducnTcm1Tmp": perEvtOducnTcm1Tmp,
       "perEvtOducnTcm2Tmp": perEvtOducnTcm2Tmp,
       "perEvtOducnTcm3Tmp": perEvtOducnTcm3Tmp,
       "perEvtOducnTcm4Tmp": perEvtOducnTcm4Tmp,
       "perEvtOducnTcm5Tmp": perEvtOducnTcm5Tmp,
       "perEvtOducnTcm6Tmp": perEvtOducnTcm6Tmp,
       "perEvtSopcur": perEvtSopcur,
       "perEvtSopmin": perEvtSopmin,
       "perEvtSopmax": perEvtSopmax,
       "perEvtXcstmpfluct": perEvtXcstmpfluct,
       "perEvtFanspeedmax": perEvtFanspeedmax,
       "perEvtFanspeedmin": perEvtFanspeedmin,
       "perEvtFanspeedcur": perEvtFanspeedcur,
       "perEvtFanspeedfluct": perEvtFanspeedfluct,
       "perEvtEsnrmin": perEvtEsnrmin,
       "perEvtEsnrmax": perEvtEsnrmax,
       "perEvtEsnrcur": perEvtEsnrcur,
       "perEvtEsnravg": perEvtEsnravg,
       "perEvtPdlmax": perEvtPdlmax,
       "perEvtPdlmin": perEvtPdlmin,
       "perEvtPdlcur": perEvtPdlcur,
       "perEvtPdlavg": perEvtPdlavg,
       "perEvtPmdmax": perEvtPmdmax,
       "perEvtPmdmin": perEvtPmdmin,
       "perEvtPmdcur": perEvtPmdcur,
       "perEvtPmdavg": perEvtPmdavg,
       "perEvtMcsoopmax": perEvtMcsoopmax,
       "perEvtMcsoopmin": perEvtMcsoopmin,
       "perEvtMcsoopcur": perEvtMcsoopcur,
       "perEvtQValueEerMin": perEvtQValueEerMin,
       "perEvtQValueEerMax": perEvtQValueEerMax,
       "perEvtBefCorerFloatMin": perEvtBefCorerFloatMin,
       "perEvtBefCorerFloatMax": perEvtBefCorerFloatMax,
       "perEvtAftCorerFloatMax": perEvtAftCorerFloatMax,
       "perEvtBefCorerFloatAvr": perEvtBefCorerFloatAvr,
       "perEvtAftCorerFloatAvr": perEvtAftCorerFloatAvr,
       "perEvtAftCorerFloatMin": perEvtAftCorerFloatMin,
       "perEvtEvoaattncur": perEvtEvoaattncur,
       "perEvtEvoaattnmax": perEvtEvoaattnmax,
       "perEvtEvoaattnmin": perEvtEvoaattnmin,
       "perEvtFecCorBitsCnt": perEvtFecCorBitsCnt,
       "perEvtBdCurPower": perEvtBdCurPower,
       "perEvtInputvoltmax": perEvtInputvoltmax,
       "perEvtInputvoltcur": perEvtInputvoltcur,
       "perEvtInputvoltmin": perEvtInputvoltmin,
       "perEvtOutputvoltmax": perEvtOutputvoltmax,
       "perEvtOutputvoltcur": perEvtOutputvoltcur,
       "perEvtOutputvoltmin": perEvtOutputvoltmin,
       "perEvtOutputcurrentmax": perEvtOutputcurrentmax,
       "perEvtOutputcurrentcur": perEvtOutputcurrentcur,
       "perEvtOutputcurrentmin": perEvtOutputcurrentmin,
       "perEvtInputcurrentmax": perEvtInputcurrentmax,
       "perEvtInputcurrentcur": perEvtInputcurrentcur,
       "perEvtInputcurrentmin": perEvtInputcurrentmin,
       "perEvtLswfrequency": perEvtLswfrequency}
)
