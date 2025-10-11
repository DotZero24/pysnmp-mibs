# SNMP MIB module (LUM-IFPERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFPERF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:19 2025
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

(lumIfPerfMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfPerfMIB",
    "lumModules")

(AdminStatusWithNA,
 CommandString,
 FaultStatusWithNA,
 MgmtNameString,
 OnOff,
 OperStatusWithNA,
 ResetWithNA,
 Signed32WithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "CommandString",
    "FaultStatusWithNA",
    "MgmtNameString",
    "OnOff",
    "OperStatusWithNA",
    "ResetWithNA",
    "Signed32WithNA",
    "Unsigned32WithNA")

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

lumIfPerfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 56)
)
if mibBuilder.loadTexts:
    lumIfPerfMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-09-30 00:00",
         "2016-01-11 00:00",
         "2015-12-22 00:00",
         "2015-11-30 00:00",
         "2015-05-29 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PerfPeriodWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("period15minutes", 1),
          ("period24hours", 2),
          ("notApplicable", 2147483647))
    )



class G826MonitorLevelWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("opu0", 1),
          ("odu0", 2),
          ("otu0", 3),
          ("opu1", 4),
          ("odu1", 5),
          ("otu1", 6),
          ("opu2", 7),
          ("odu2", 8),
          ("otu2", 9),
          ("opu3", 10),
          ("odu3", 11),
          ("otu3", 12),
          ("opu4", 13),
          ("odu4", 14),
          ("otu4", 15),
          ("oduFlex", 16),
          ("rs", 17),
          ("ms", 18),
          ("mac", 19),
          ("pcs", 20),
          ("cpriL1", 21),
          ("obsaiL1", 22),
          ("irsoh", 23),
          ("imsoh", 24),
          ("otuj2", 25),
          ("opuFlex", 26),
          ("notApplicable", 2147483647))
    )



class G826MonitorChannelWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("sm", 1),
          ("pm", 2),
          ("tcm1", 3),
          ("tcm2", 4),
          ("tcm3", 5),
          ("tcm4", 6),
          ("tcm5", 7),
          ("tcm6", 8),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )



class L1MeasurementTypeWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("notApplicable", 2147483647))
    )



class L2MeasurementTypeWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("notApplicable", 2147483647))
    )



class G826MeasurementTypeWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("uniDi", 3),
          ("biDi", 4),
          ("notApplicable", 2147483647))
    )



class BooleanValueWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )



# MIB Managed Objects in the order of their OIDs

_LumIfPerfConfs_ObjectIdentity = ObjectIdentity
lumIfPerfConfs = _LumIfPerfConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1)
)
_LumIfPerfGroups_ObjectIdentity = ObjectIdentity
lumIfPerfGroups = _LumIfPerfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1)
)
_LumIfPerfCompl_ObjectIdentity = ObjectIdentity
lumIfPerfCompl = _LumIfPerfCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2)
)
_LumIfPerfMIBObjects_ObjectIdentity = ObjectIdentity
lumIfPerfMIBObjects = _LumIfPerfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2)
)
_IfPerfGeneral_ObjectIdentity = ObjectIdentity
ifPerfGeneral = _IfPerfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1)
)
_IfPerfGeneralConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralConfigLastChangeTime_Object = MibScalar
ifPerfGeneralConfigLastChangeTime = _IfPerfGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 1),
    _IfPerfGeneralConfigLastChangeTime_Type()
)
ifPerfGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralConfigLastChangeTime.setStatus("current")
_IfPerfGeneralStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralStateLastChangeTime_Object = MibScalar
ifPerfGeneralStateLastChangeTime = _IfPerfGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 2),
    _IfPerfGeneralStateLastChangeTime_Type()
)
ifPerfGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralStateLastChangeTime.setStatus("current")
_IfPerfGeneralAdminTableSize_Type = Unsigned32
_IfPerfGeneralAdminTableSize_Object = MibScalar
ifPerfGeneralAdminTableSize = _IfPerfGeneralAdminTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 3),
    _IfPerfGeneralAdminTableSize_Type()
)
ifPerfGeneralAdminTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralAdminTableSize.setStatus("current")
_IfPerfGeneralAdminConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralAdminConfigLastChangeTime_Object = MibScalar
ifPerfGeneralAdminConfigLastChangeTime = _IfPerfGeneralAdminConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 4),
    _IfPerfGeneralAdminConfigLastChangeTime_Type()
)
ifPerfGeneralAdminConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralAdminConfigLastChangeTime.setStatus("current")
_IfPerfGeneralAdminStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralAdminStateLastChangeTime_Object = MibScalar
ifPerfGeneralAdminStateLastChangeTime = _IfPerfGeneralAdminStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 5),
    _IfPerfGeneralAdminStateLastChangeTime_Type()
)
ifPerfGeneralAdminStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralAdminStateLastChangeTime.setStatus("current")
_IfPerfGeneralFecTableSize_Type = Unsigned32
_IfPerfGeneralFecTableSize_Object = MibScalar
ifPerfGeneralFecTableSize = _IfPerfGeneralFecTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 6),
    _IfPerfGeneralFecTableSize_Type()
)
ifPerfGeneralFecTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralFecTableSize.setStatus("current")
_IfPerfGeneralFecConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralFecConfigLastChangeTime_Object = MibScalar
ifPerfGeneralFecConfigLastChangeTime = _IfPerfGeneralFecConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 7),
    _IfPerfGeneralFecConfigLastChangeTime_Type()
)
ifPerfGeneralFecConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralFecConfigLastChangeTime.setStatus("current")
_IfPerfGeneralFecStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralFecStateLastChangeTime_Object = MibScalar
ifPerfGeneralFecStateLastChangeTime = _IfPerfGeneralFecStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 8),
    _IfPerfGeneralFecStateLastChangeTime_Type()
)
ifPerfGeneralFecStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralFecStateLastChangeTime.setStatus("current")
_IfPerfGeneralG826TableSize_Type = Unsigned32
_IfPerfGeneralG826TableSize_Object = MibScalar
ifPerfGeneralG826TableSize = _IfPerfGeneralG826TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 9),
    _IfPerfGeneralG826TableSize_Type()
)
ifPerfGeneralG826TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralG826TableSize.setStatus("current")
_IfPerfGeneralG826ConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralG826ConfigLastChangeTime_Object = MibScalar
ifPerfGeneralG826ConfigLastChangeTime = _IfPerfGeneralG826ConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 10),
    _IfPerfGeneralG826ConfigLastChangeTime_Type()
)
ifPerfGeneralG826ConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralG826ConfigLastChangeTime.setStatus("current")
_IfPerfGeneralG826StateLastChangeTime_Type = DateAndTime
_IfPerfGeneralG826StateLastChangeTime_Object = MibScalar
ifPerfGeneralG826StateLastChangeTime = _IfPerfGeneralG826StateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 11),
    _IfPerfGeneralG826StateLastChangeTime_Type()
)
ifPerfGeneralG826StateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralG826StateLastChangeTime.setStatus("current")
_IfPerfGeneralL1TableSize_Type = Unsigned32
_IfPerfGeneralL1TableSize_Object = MibScalar
ifPerfGeneralL1TableSize = _IfPerfGeneralL1TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 12),
    _IfPerfGeneralL1TableSize_Type()
)
ifPerfGeneralL1TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL1TableSize.setStatus("current")
_IfPerfGeneralL1ConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralL1ConfigLastChangeTime_Object = MibScalar
ifPerfGeneralL1ConfigLastChangeTime = _IfPerfGeneralL1ConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 13),
    _IfPerfGeneralL1ConfigLastChangeTime_Type()
)
ifPerfGeneralL1ConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL1ConfigLastChangeTime.setStatus("current")
_IfPerfGeneralL1StateLastChangeTime_Type = DateAndTime
_IfPerfGeneralL1StateLastChangeTime_Object = MibScalar
ifPerfGeneralL1StateLastChangeTime = _IfPerfGeneralL1StateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 14),
    _IfPerfGeneralL1StateLastChangeTime_Type()
)
ifPerfGeneralL1StateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL1StateLastChangeTime.setStatus("current")
_IfPerfGeneralL0TableSize_Type = Unsigned32
_IfPerfGeneralL0TableSize_Object = MibScalar
ifPerfGeneralL0TableSize = _IfPerfGeneralL0TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 15),
    _IfPerfGeneralL0TableSize_Type()
)
ifPerfGeneralL0TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL0TableSize.setStatus("current")
_IfPerfGeneralL0ConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralL0ConfigLastChangeTime_Object = MibScalar
ifPerfGeneralL0ConfigLastChangeTime = _IfPerfGeneralL0ConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 16),
    _IfPerfGeneralL0ConfigLastChangeTime_Type()
)
ifPerfGeneralL0ConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL0ConfigLastChangeTime.setStatus("current")
_IfPerfGeneralL0StateLastChangeTime_Type = DateAndTime
_IfPerfGeneralL0StateLastChangeTime_Object = MibScalar
ifPerfGeneralL0StateLastChangeTime = _IfPerfGeneralL0StateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 17),
    _IfPerfGeneralL0StateLastChangeTime_Type()
)
ifPerfGeneralL0StateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL0StateLastChangeTime.setStatus("current")
_IfPerfGeneralL2StatTableSize_Type = Unsigned32
_IfPerfGeneralL2StatTableSize_Object = MibScalar
ifPerfGeneralL2StatTableSize = _IfPerfGeneralL2StatTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 18),
    _IfPerfGeneralL2StatTableSize_Type()
)
ifPerfGeneralL2StatTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2StatTableSize.setStatus("current")
_IfPerfGeneralL2StatConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralL2StatConfigLastChangeTime_Object = MibScalar
ifPerfGeneralL2StatConfigLastChangeTime = _IfPerfGeneralL2StatConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 19),
    _IfPerfGeneralL2StatConfigLastChangeTime_Type()
)
ifPerfGeneralL2StatConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2StatConfigLastChangeTime.setStatus("current")
_IfPerfGeneralL2StatStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralL2StatStateLastChangeTime_Object = MibScalar
ifPerfGeneralL2StatStateLastChangeTime = _IfPerfGeneralL2StatStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 20),
    _IfPerfGeneralL2StatStateLastChangeTime_Type()
)
ifPerfGeneralL2StatStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2StatStateLastChangeTime.setStatus("current")
_IfPerfGeneralL2ErrorTableSize_Type = Unsigned32
_IfPerfGeneralL2ErrorTableSize_Object = MibScalar
ifPerfGeneralL2ErrorTableSize = _IfPerfGeneralL2ErrorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 21),
    _IfPerfGeneralL2ErrorTableSize_Type()
)
ifPerfGeneralL2ErrorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2ErrorTableSize.setStatus("current")
_IfPerfGeneralL2ErrorConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralL2ErrorConfigLastChangeTime_Object = MibScalar
ifPerfGeneralL2ErrorConfigLastChangeTime = _IfPerfGeneralL2ErrorConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 22),
    _IfPerfGeneralL2ErrorConfigLastChangeTime_Type()
)
ifPerfGeneralL2ErrorConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2ErrorConfigLastChangeTime.setStatus("current")
_IfPerfGeneralL2ErrorStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralL2ErrorStateLastChangeTime_Object = MibScalar
ifPerfGeneralL2ErrorStateLastChangeTime = _IfPerfGeneralL2ErrorStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 23),
    _IfPerfGeneralL2ErrorStateLastChangeTime_Type()
)
ifPerfGeneralL2ErrorStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralL2ErrorStateLastChangeTime.setStatus("current")
_IfPerfGeneralDelayTableSize_Type = Unsigned32
_IfPerfGeneralDelayTableSize_Object = MibScalar
ifPerfGeneralDelayTableSize = _IfPerfGeneralDelayTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 24),
    _IfPerfGeneralDelayTableSize_Type()
)
ifPerfGeneralDelayTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralDelayTableSize.setStatus("current")
_IfPerfGeneralDelayConfigLastChangeTime_Type = DateAndTime
_IfPerfGeneralDelayConfigLastChangeTime_Object = MibScalar
ifPerfGeneralDelayConfigLastChangeTime = _IfPerfGeneralDelayConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 25),
    _IfPerfGeneralDelayConfigLastChangeTime_Type()
)
ifPerfGeneralDelayConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralDelayConfigLastChangeTime.setStatus("current")
_IfPerfGeneralDelayStateLastChangeTime_Type = DateAndTime
_IfPerfGeneralDelayStateLastChangeTime_Object = MibScalar
ifPerfGeneralDelayStateLastChangeTime = _IfPerfGeneralDelayStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 1, 26),
    _IfPerfGeneralDelayStateLastChangeTime_Type()
)
ifPerfGeneralDelayStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfGeneralDelayStateLastChangeTime.setStatus("current")
_IfPerfAdminList_ObjectIdentity = ObjectIdentity
ifPerfAdminList = _IfPerfAdminList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2)
)
_IfPerfAdminTable_Object = MibTable
ifPerfAdminTable = _IfPerfAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifPerfAdminTable.setStatus("current")
_IfPerfAdminEntry_Object = MibTableRow
ifPerfAdminEntry = _IfPerfAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1)
)
ifPerfAdminEntry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfAdminIndex"),
)
if mibBuilder.loadTexts:
    ifPerfAdminEntry.setStatus("current")
_IfPerfAdminIndex_Type = Unsigned32
_IfPerfAdminIndex_Object = MibTableColumn
ifPerfAdminIndex = _IfPerfAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 1),
    _IfPerfAdminIndex_Type()
)
ifPerfAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminIndex.setStatus("current")
_IfPerfAdminName_Type = MgmtNameString
_IfPerfAdminName_Object = MibTableColumn
ifPerfAdminName = _IfPerfAdminName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 2),
    _IfPerfAdminName_Type()
)
ifPerfAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfAdminName.setStatus("current")
_IfPerfAdminConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfPerfAdminConnIfBasicIfIndex_Object = MibTableColumn
ifPerfAdminConnIfBasicIfIndex = _IfPerfAdminConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 3),
    _IfPerfAdminConnIfBasicIfIndex_Type()
)
ifPerfAdminConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfAdminConnIfBasicIfIndex.setStatus("current")


class _IfPerfAdminAdminStatus_Type(AdminStatusWithNA):
    """Custom type ifPerfAdminAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_IfPerfAdminAdminStatus_Type.__name__ = "AdminStatusWithNA"
_IfPerfAdminAdminStatus_Object = MibTableColumn
ifPerfAdminAdminStatus = _IfPerfAdminAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 4),
    _IfPerfAdminAdminStatus_Type()
)
ifPerfAdminAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfAdminAdminStatus.setStatus("current")


class _IfPerfAdminReportMode_Type(OnOff):
    """Custom type ifPerfAdminReportMode based on OnOff"""
    defaultValue = 2


_IfPerfAdminReportMode_Type.__name__ = "OnOff"
_IfPerfAdminReportMode_Object = MibTableColumn
ifPerfAdminReportMode = _IfPerfAdminReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 5),
    _IfPerfAdminReportMode_Type()
)
ifPerfAdminReportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminReportMode.setStatus("current")


class _IfPerfAdminOperStatus_Type(OperStatusWithNA):
    """Custom type ifPerfAdminOperStatus based on OperStatusWithNA"""
    defaultValue = 1


_IfPerfAdminOperStatus_Type.__name__ = "OperStatusWithNA"
_IfPerfAdminOperStatus_Object = MibTableColumn
ifPerfAdminOperStatus = _IfPerfAdminOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 6),
    _IfPerfAdminOperStatus_Type()
)
ifPerfAdminOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminOperStatus.setStatus("current")
_IfPerfAdminIsSuspect15m_Type = BooleanValueWithNA
_IfPerfAdminIsSuspect15m_Object = MibTableColumn
ifPerfAdminIsSuspect15m = _IfPerfAdminIsSuspect15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 7),
    _IfPerfAdminIsSuspect15m_Type()
)
ifPerfAdminIsSuspect15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminIsSuspect15m.setStatus("current")
_IfPerfAdminIsSuspect24h_Type = BooleanValueWithNA
_IfPerfAdminIsSuspect24h_Object = MibTableColumn
ifPerfAdminIsSuspect24h = _IfPerfAdminIsSuspect24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 8),
    _IfPerfAdminIsSuspect24h_Type()
)
ifPerfAdminIsSuspect24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminIsSuspect24h.setStatus("current")


class _IfPerfAdminReset15m_Type(ResetWithNA):
    """Custom type ifPerfAdminReset15m based on ResetWithNA"""
    defaultValue = 2


_IfPerfAdminReset15m_Type.__name__ = "ResetWithNA"
_IfPerfAdminReset15m_Object = MibTableColumn
ifPerfAdminReset15m = _IfPerfAdminReset15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 9),
    _IfPerfAdminReset15m_Type()
)
ifPerfAdminReset15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminReset15m.setStatus("current")


class _IfPerfAdminReset24h_Type(ResetWithNA):
    """Custom type ifPerfAdminReset24h based on ResetWithNA"""
    defaultValue = 2


_IfPerfAdminReset24h_Type.__name__ = "ResetWithNA"
_IfPerfAdminReset24h_Object = MibTableColumn
ifPerfAdminReset24h = _IfPerfAdminReset24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 10),
    _IfPerfAdminReset24h_Type()
)
ifPerfAdminReset24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminReset24h.setStatus("current")


class _IfPerfAdminUpId_Type(Unsigned32):
    """Custom type ifPerfAdminUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfPerfAdminUpId_Type.__name__ = "Unsigned32"
_IfPerfAdminUpId_Object = MibTableColumn
ifPerfAdminUpId = _IfPerfAdminUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 2, 1, 1, 11),
    _IfPerfAdminUpId_Type()
)
ifPerfAdminUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfAdminUpId.setStatus("current")
_IfPerfFecList_ObjectIdentity = ObjectIdentity
ifPerfFecList = _IfPerfFecList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3)
)
_IfPerfFecTable_Object = MibTable
ifPerfFecTable = _IfPerfFecTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifPerfFecTable.setStatus("current")
_IfPerfFecEntry_Object = MibTableRow
ifPerfFecEntry = _IfPerfFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1)
)
ifPerfFecEntry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfFecIndex"),
)
if mibBuilder.loadTexts:
    ifPerfFecEntry.setStatus("current")
_IfPerfFecIndex_Type = Unsigned32
_IfPerfFecIndex_Object = MibTableColumn
ifPerfFecIndex = _IfPerfFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 1),
    _IfPerfFecIndex_Type()
)
ifPerfFecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecIndex.setStatus("current")
_IfPerfFecName_Type = MgmtNameString
_IfPerfFecName_Object = MibTableColumn
ifPerfFecName = _IfPerfFecName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 2),
    _IfPerfFecName_Type()
)
ifPerfFecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfFecName.setStatus("current")
_IfPerfFecConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfFecConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfFecConnIfPerfAdminIfIndex = _IfPerfFecConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 3),
    _IfPerfFecConnIfPerfAdminIfIndex_Type()
)
ifPerfFecConnIfPerfAdminIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfFecConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfFecCorrectedZeros_Type = Unsigned32WithNA
_IfPerfFecCorrectedZeros_Object = MibTableColumn
ifPerfFecCorrectedZeros = _IfPerfFecCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 4),
    _IfPerfFecCorrectedZeros_Type()
)
ifPerfFecCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecCorrectedZeros.setStatus("current")
_IfPerfFecCorrectedOnes_Type = Unsigned32WithNA
_IfPerfFecCorrectedOnes_Object = MibTableColumn
ifPerfFecCorrectedOnes = _IfPerfFecCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 5),
    _IfPerfFecCorrectedOnes_Type()
)
ifPerfFecCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecCorrectedOnes.setStatus("current")
_IfPerfFecRxBerEstimation_Type = Unsigned32WithNA
_IfPerfFecRxBerEstimation_Object = MibTableColumn
ifPerfFecRxBerEstimation = _IfPerfFecRxBerEstimation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 6),
    _IfPerfFecRxBerEstimation_Type()
)
ifPerfFecRxBerEstimation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecRxBerEstimation.setStatus("current")
_IfPerfFecRxAvgPreFecBer_Type = Unsigned32WithNA
_IfPerfFecRxAvgPreFecBer_Object = MibTableColumn
ifPerfFecRxAvgPreFecBer = _IfPerfFecRxAvgPreFecBer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 7),
    _IfPerfFecRxAvgPreFecBer_Type()
)
ifPerfFecRxAvgPreFecBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecRxAvgPreFecBer.setStatus("current")
_IfPerfFecCorrectedBits_Type = Unsigned32WithNA
_IfPerfFecCorrectedBits_Object = MibTableColumn
ifPerfFecCorrectedBits = _IfPerfFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 8),
    _IfPerfFecCorrectedBits_Type()
)
ifPerfFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecCorrectedBits.setStatus("current")


class _IfPerfFecRxBitErrorEstimation_Type(DisplayString):
    """Custom type ifPerfFecRxBitErrorEstimation based on DisplayString"""
    defaultValue = OctetString(" ")


_IfPerfFecRxBitErrorEstimation_Type.__name__ = "DisplayString"
_IfPerfFecRxBitErrorEstimation_Object = MibTableColumn
ifPerfFecRxBitErrorEstimation = _IfPerfFecRxBitErrorEstimation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 9),
    _IfPerfFecRxBitErrorEstimation_Type()
)
ifPerfFecRxBitErrorEstimation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecRxBitErrorEstimation.setStatus("current")
_IfPerfFecOpticalSNR_Type = Unsigned32WithNA
_IfPerfFecOpticalSNR_Object = MibTableColumn
ifPerfFecOpticalSNR = _IfPerfFecOpticalSNR_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 10),
    _IfPerfFecOpticalSNR_Type()
)
ifPerfFecOpticalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecOpticalSNR.setStatus("current")


class _IfPerfFecUpId_Type(Unsigned32):
    """Custom type ifPerfFecUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfPerfFecUpId_Type.__name__ = "Unsigned32"
_IfPerfFecUpId_Object = MibTableColumn
ifPerfFecUpId = _IfPerfFecUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 3, 1, 1, 11),
    _IfPerfFecUpId_Type()
)
ifPerfFecUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfFecUpId.setStatus("current")
_IfPerfG826List_ObjectIdentity = ObjectIdentity
ifPerfG826List = _IfPerfG826List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4)
)
_IfPerfG826Table_Object = MibTable
ifPerfG826Table = _IfPerfG826Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifPerfG826Table.setStatus("current")
_IfPerfG826Entry_Object = MibTableRow
ifPerfG826Entry = _IfPerfG826Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1)
)
ifPerfG826Entry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfG826Index"),
)
if mibBuilder.loadTexts:
    ifPerfG826Entry.setStatus("current")
_IfPerfG826Index_Type = Unsigned32
_IfPerfG826Index_Object = MibTableColumn
ifPerfG826Index = _IfPerfG826Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 1),
    _IfPerfG826Index_Type()
)
ifPerfG826Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826Index.setStatus("current")
_IfPerfG826Name_Type = MgmtNameString
_IfPerfG826Name_Object = MibTableColumn
ifPerfG826Name = _IfPerfG826Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 2),
    _IfPerfG826Name_Type()
)
ifPerfG826Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826Name.setStatus("current")
_IfPerfG826ConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfG826ConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfG826ConnIfPerfAdminIfIndex = _IfPerfG826ConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 3),
    _IfPerfG826ConnIfPerfAdminIfIndex_Type()
)
ifPerfG826ConnIfPerfAdminIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826ConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfG826Period_Type = PerfPeriodWithNA
_IfPerfG826Period_Object = MibTableColumn
ifPerfG826Period = _IfPerfG826Period_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 4),
    _IfPerfG826Period_Type()
)
ifPerfG826Period.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826Period.setStatus("current")
_IfPerfG826Type_Type = G826MeasurementTypeWithNA
_IfPerfG826Type_Object = MibTableColumn
ifPerfG826Type = _IfPerfG826Type_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 5),
    _IfPerfG826Type_Type()
)
ifPerfG826Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826Type.setStatus("current")
_IfPerfG826MonitorLevel_Type = G826MonitorLevelWithNA
_IfPerfG826MonitorLevel_Object = MibTableColumn
ifPerfG826MonitorLevel = _IfPerfG826MonitorLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 6),
    _IfPerfG826MonitorLevel_Type()
)
ifPerfG826MonitorLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826MonitorLevel.setStatus("current")
_IfPerfG826MonitorChannel_Type = G826MonitorChannelWithNA
_IfPerfG826MonitorChannel_Object = MibTableColumn
ifPerfG826MonitorChannel = _IfPerfG826MonitorChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 7),
    _IfPerfG826MonitorChannel_Type()
)
ifPerfG826MonitorChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfG826MonitorChannel.setStatus("current")
_IfPerfG826CounterEs_Type = Unsigned32WithNA
_IfPerfG826CounterEs_Object = MibTableColumn
ifPerfG826CounterEs = _IfPerfG826CounterEs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 8),
    _IfPerfG826CounterEs_Type()
)
ifPerfG826CounterEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826CounterEs.setStatus("current")
_IfPerfG826CounterSes_Type = Unsigned32WithNA
_IfPerfG826CounterSes_Object = MibTableColumn
ifPerfG826CounterSes = _IfPerfG826CounterSes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 9),
    _IfPerfG826CounterSes_Type()
)
ifPerfG826CounterSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826CounterSes.setStatus("current")
_IfPerfG826CounterUas_Type = Unsigned32WithNA
_IfPerfG826CounterUas_Object = MibTableColumn
ifPerfG826CounterUas = _IfPerfG826CounterUas_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 10),
    _IfPerfG826CounterUas_Type()
)
ifPerfG826CounterUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826CounterUas.setStatus("current")
_IfPerfG826CounterBbe_Type = Counter64
_IfPerfG826CounterBbe_Object = MibTableColumn
ifPerfG826CounterBbe = _IfPerfG826CounterBbe_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 11),
    _IfPerfG826CounterBbe_Type()
)
ifPerfG826CounterBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826CounterBbe.setStatus("current")


class _IfPerfG826ThresholdEs_Type(Unsigned32WithNA):
    """Custom type ifPerfG826ThresholdEs based on Unsigned32WithNA"""
    defaultValue = 20


_IfPerfG826ThresholdEs_Type.__name__ = "Unsigned32WithNA"
_IfPerfG826ThresholdEs_Object = MibTableColumn
ifPerfG826ThresholdEs = _IfPerfG826ThresholdEs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 12),
    _IfPerfG826ThresholdEs_Type()
)
ifPerfG826ThresholdEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfG826ThresholdEs.setStatus("current")


class _IfPerfG826ThresholdSes_Type(Unsigned32WithNA):
    """Custom type ifPerfG826ThresholdSes based on Unsigned32WithNA"""
    defaultValue = 10


_IfPerfG826ThresholdSes_Type.__name__ = "Unsigned32WithNA"
_IfPerfG826ThresholdSes_Object = MibTableColumn
ifPerfG826ThresholdSes = _IfPerfG826ThresholdSes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 13),
    _IfPerfG826ThresholdSes_Type()
)
ifPerfG826ThresholdSes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfG826ThresholdSes.setStatus("current")


class _IfPerfG826ThresholdUas_Type(Unsigned32WithNA):
    """Custom type ifPerfG826ThresholdUas based on Unsigned32WithNA"""
    defaultValue = 30


_IfPerfG826ThresholdUas_Type.__name__ = "Unsigned32WithNA"
_IfPerfG826ThresholdUas_Object = MibTableColumn
ifPerfG826ThresholdUas = _IfPerfG826ThresholdUas_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 14),
    _IfPerfG826ThresholdUas_Type()
)
ifPerfG826ThresholdUas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfG826ThresholdUas.setStatus("current")


class _IfPerfG826ThresholdBbe_Type(Counter64):
    """Custom type ifPerfG826ThresholdBbe based on Counter64"""
    defaultValue = 100000


_IfPerfG826ThresholdBbe_Type.__name__ = "Counter64"
_IfPerfG826ThresholdBbe_Object = MibTableColumn
ifPerfG826ThresholdBbe = _IfPerfG826ThresholdBbe_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 15),
    _IfPerfG826ThresholdBbe_Type()
)
ifPerfG826ThresholdBbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfG826ThresholdBbe.setStatus("current")
_IfPerfG826FaultStatusEs_Type = FaultStatusWithNA
_IfPerfG826FaultStatusEs_Object = MibTableColumn
ifPerfG826FaultStatusEs = _IfPerfG826FaultStatusEs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 16),
    _IfPerfG826FaultStatusEs_Type()
)
ifPerfG826FaultStatusEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826FaultStatusEs.setStatus("current")
_IfPerfG826FaultStatusSes_Type = FaultStatusWithNA
_IfPerfG826FaultStatusSes_Object = MibTableColumn
ifPerfG826FaultStatusSes = _IfPerfG826FaultStatusSes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 17),
    _IfPerfG826FaultStatusSes_Type()
)
ifPerfG826FaultStatusSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826FaultStatusSes.setStatus("current")
_IfPerfG826FaultStatusUas_Type = FaultStatusWithNA
_IfPerfG826FaultStatusUas_Object = MibTableColumn
ifPerfG826FaultStatusUas = _IfPerfG826FaultStatusUas_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 18),
    _IfPerfG826FaultStatusUas_Type()
)
ifPerfG826FaultStatusUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826FaultStatusUas.setStatus("current")
_IfPerfG826FaultStatusBbe_Type = FaultStatusWithNA
_IfPerfG826FaultStatusBbe_Object = MibTableColumn
ifPerfG826FaultStatusBbe = _IfPerfG826FaultStatusBbe_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 19),
    _IfPerfG826FaultStatusBbe_Type()
)
ifPerfG826FaultStatusBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826FaultStatusBbe.setStatus("current")


class _IfPerfG826UpId_Type(Unsigned32):
    """Custom type ifPerfG826UpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfPerfG826UpId_Type.__name__ = "Unsigned32"
_IfPerfG826UpId_Object = MibTableColumn
ifPerfG826UpId = _IfPerfG826UpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 4, 1, 1, 20),
    _IfPerfG826UpId_Type()
)
ifPerfG826UpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfG826UpId.setStatus("current")
_IfPerfL1List_ObjectIdentity = ObjectIdentity
ifPerfL1List = _IfPerfL1List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5)
)
_IfPerfL1Table_Object = MibTable
ifPerfL1Table = _IfPerfL1Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ifPerfL1Table.setStatus("current")
_IfPerfL1Entry_Object = MibTableRow
ifPerfL1Entry = _IfPerfL1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1)
)
ifPerfL1Entry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfL1Index"),
)
if mibBuilder.loadTexts:
    ifPerfL1Entry.setStatus("current")
_IfPerfL1Index_Type = Unsigned32
_IfPerfL1Index_Object = MibTableColumn
ifPerfL1Index = _IfPerfL1Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 1),
    _IfPerfL1Index_Type()
)
ifPerfL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1Index.setStatus("current")
_IfPerfL1Name_Type = MgmtNameString
_IfPerfL1Name_Object = MibTableColumn
ifPerfL1Name = _IfPerfL1Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 2),
    _IfPerfL1Name_Type()
)
ifPerfL1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1Name.setStatus("current")
_IfPerfL1ConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfL1ConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfL1ConnIfPerfAdminIfIndex = _IfPerfL1ConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 3),
    _IfPerfL1ConnIfPerfAdminIfIndex_Type()
)
ifPerfL1ConnIfPerfAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1ConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfL1Period_Type = PerfPeriodWithNA
_IfPerfL1Period_Object = MibTableColumn
ifPerfL1Period = _IfPerfL1Period_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 4),
    _IfPerfL1Period_Type()
)
ifPerfL1Period.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1Period.setStatus("current")
_IfPerfL1Type_Type = L1MeasurementTypeWithNA
_IfPerfL1Type_Object = MibTableColumn
ifPerfL1Type = _IfPerfL1Type_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 5),
    _IfPerfL1Type_Type()
)
ifPerfL1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1Type.setStatus("current")
_IfPerfL1MaxUtilization_Type = Unsigned32WithNA
_IfPerfL1MaxUtilization_Object = MibTableColumn
ifPerfL1MaxUtilization = _IfPerfL1MaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 6),
    _IfPerfL1MaxUtilization_Type()
)
ifPerfL1MaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1MaxUtilization.setStatus("current")
_IfPerfL1AverageUtilization_Type = Unsigned32WithNA
_IfPerfL1AverageUtilization_Object = MibTableColumn
ifPerfL1AverageUtilization = _IfPerfL1AverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 7),
    _IfPerfL1AverageUtilization_Type()
)
ifPerfL1AverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1AverageUtilization.setStatus("current")
_IfPerfL1CurrentUtilization_Type = Unsigned32WithNA
_IfPerfL1CurrentUtilization_Object = MibTableColumn
ifPerfL1CurrentUtilization = _IfPerfL1CurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 5, 1, 1, 8),
    _IfPerfL1CurrentUtilization_Type()
)
ifPerfL1CurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL1CurrentUtilization.setStatus("current")
_IfPerfL0List_ObjectIdentity = ObjectIdentity
ifPerfL0List = _IfPerfL0List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6)
)
_IfPerfL0Table_Object = MibTable
ifPerfL0Table = _IfPerfL0Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ifPerfL0Table.setStatus("current")
_IfPerfL0Entry_Object = MibTableRow
ifPerfL0Entry = _IfPerfL0Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1)
)
ifPerfL0Entry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfL0Index"),
)
if mibBuilder.loadTexts:
    ifPerfL0Entry.setStatus("current")
_IfPerfL0Index_Type = Unsigned32
_IfPerfL0Index_Object = MibTableColumn
ifPerfL0Index = _IfPerfL0Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 1),
    _IfPerfL0Index_Type()
)
ifPerfL0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0Index.setStatus("current")
_IfPerfL0Name_Type = MgmtNameString
_IfPerfL0Name_Object = MibTableColumn
ifPerfL0Name = _IfPerfL0Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 2),
    _IfPerfL0Name_Type()
)
ifPerfL0Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifPerfL0Name.setStatus("current")
_IfPerfL0ConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfL0ConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfL0ConnIfPerfAdminIfIndex = _IfPerfL0ConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 3),
    _IfPerfL0ConnIfPerfAdminIfIndex_Type()
)
ifPerfL0ConnIfPerfAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0ConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfL0RxPower_Type = Signed32WithNA
_IfPerfL0RxPower_Object = MibTableColumn
ifPerfL0RxPower = _IfPerfL0RxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 4),
    _IfPerfL0RxPower_Type()
)
ifPerfL0RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0RxPower.setStatus("current")
_IfPerfL0TxPower_Type = Signed32WithNA
_IfPerfL0TxPower_Object = MibTableColumn
ifPerfL0TxPower = _IfPerfL0TxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 5),
    _IfPerfL0TxPower_Type()
)
ifPerfL0TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0TxPower.setStatus("current")
_IfPerfL0InitialRxPower_Type = Signed32WithNA
_IfPerfL0InitialRxPower_Object = MibTableColumn
ifPerfL0InitialRxPower = _IfPerfL0InitialRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 6),
    _IfPerfL0InitialRxPower_Type()
)
ifPerfL0InitialRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0InitialRxPower.setStatus("current")
_IfPerfL0ChromaticDispersion_Type = Signed32WithNA
_IfPerfL0ChromaticDispersion_Object = MibTableColumn
ifPerfL0ChromaticDispersion = _IfPerfL0ChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 7),
    _IfPerfL0ChromaticDispersion_Type()
)
ifPerfL0ChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0ChromaticDispersion.setStatus("current")
_IfPerfL0DifferentialGroupDelay_Type = Unsigned32WithNA
_IfPerfL0DifferentialGroupDelay_Object = MibTableColumn
ifPerfL0DifferentialGroupDelay = _IfPerfL0DifferentialGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 8),
    _IfPerfL0DifferentialGroupDelay_Type()
)
ifPerfL0DifferentialGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0DifferentialGroupDelay.setStatus("current")
_IfPerfL0InitialDifferentialGroupDelay_Type = Unsigned32WithNA
_IfPerfL0InitialDifferentialGroupDelay_Object = MibTableColumn
ifPerfL0InitialDifferentialGroupDelay = _IfPerfL0InitialDifferentialGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 9),
    _IfPerfL0InitialDifferentialGroupDelay_Type()
)
ifPerfL0InitialDifferentialGroupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfL0InitialDifferentialGroupDelay.setStatus("current")


class _IfPerfL0UpId_Type(Unsigned32):
    """Custom type ifPerfL0UpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfPerfL0UpId_Type.__name__ = "Unsigned32"
_IfPerfL0UpId_Object = MibTableColumn
ifPerfL0UpId = _IfPerfL0UpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 6, 1, 1, 10),
    _IfPerfL0UpId_Type()
)
ifPerfL0UpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL0UpId.setStatus("current")
_IfPerfL2StatList_ObjectIdentity = ObjectIdentity
ifPerfL2StatList = _IfPerfL2StatList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7)
)
_IfPerfL2StatTable_Object = MibTable
ifPerfL2StatTable = _IfPerfL2StatTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ifPerfL2StatTable.setStatus("current")
_IfPerfL2StatEntry_Object = MibTableRow
ifPerfL2StatEntry = _IfPerfL2StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1)
)
ifPerfL2StatEntry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfL2StatIndex"),
)
if mibBuilder.loadTexts:
    ifPerfL2StatEntry.setStatus("current")
_IfPerfL2StatIndex_Type = Unsigned32
_IfPerfL2StatIndex_Object = MibTableColumn
ifPerfL2StatIndex = _IfPerfL2StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 1),
    _IfPerfL2StatIndex_Type()
)
ifPerfL2StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatIndex.setStatus("current")
_IfPerfL2StatName_Type = MgmtNameString
_IfPerfL2StatName_Object = MibTableColumn
ifPerfL2StatName = _IfPerfL2StatName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 2),
    _IfPerfL2StatName_Type()
)
ifPerfL2StatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatName.setStatus("current")
_IfPerfL2StatConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfL2StatConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfL2StatConnIfPerfAdminIfIndex = _IfPerfL2StatConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 3),
    _IfPerfL2StatConnIfPerfAdminIfIndex_Type()
)
ifPerfL2StatConnIfPerfAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfL2StatPeriod_Type = PerfPeriodWithNA
_IfPerfL2StatPeriod_Object = MibTableColumn
ifPerfL2StatPeriod = _IfPerfL2StatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 4),
    _IfPerfL2StatPeriod_Type()
)
ifPerfL2StatPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatPeriod.setStatus("current")
_IfPerfL2StatType_Type = L2MeasurementTypeWithNA
_IfPerfL2StatType_Object = MibTableColumn
ifPerfL2StatType = _IfPerfL2StatType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 5),
    _IfPerfL2StatType_Type()
)
ifPerfL2StatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatType.setStatus("current")
_IfPerfL2StatCurrentFrames_Type = Counter64
_IfPerfL2StatCurrentFrames_Object = MibTableColumn
ifPerfL2StatCurrentFrames = _IfPerfL2StatCurrentFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 6),
    _IfPerfL2StatCurrentFrames_Type()
)
ifPerfL2StatCurrentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentFrames.setStatus("current")
_IfPerfL2StatCurrentBytes_Type = Counter64
_IfPerfL2StatCurrentBytes_Object = MibTableColumn
ifPerfL2StatCurrentBytes = _IfPerfL2StatCurrentBytes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 7),
    _IfPerfL2StatCurrentBytes_Type()
)
ifPerfL2StatCurrentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentBytes.setStatus("current")
_IfPerfL2StatCurrentUnicastFrames_Type = Counter64
_IfPerfL2StatCurrentUnicastFrames_Object = MibTableColumn
ifPerfL2StatCurrentUnicastFrames = _IfPerfL2StatCurrentUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 8),
    _IfPerfL2StatCurrentUnicastFrames_Type()
)
ifPerfL2StatCurrentUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentUnicastFrames.setStatus("current")
_IfPerfL2StatCurrentMulticastFrames_Type = Counter64
_IfPerfL2StatCurrentMulticastFrames_Object = MibTableColumn
ifPerfL2StatCurrentMulticastFrames = _IfPerfL2StatCurrentMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 9),
    _IfPerfL2StatCurrentMulticastFrames_Type()
)
ifPerfL2StatCurrentMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentMulticastFrames.setStatus("current")
_IfPerfL2StatCurrentBroadcastFrames_Type = Counter64
_IfPerfL2StatCurrentBroadcastFrames_Object = MibTableColumn
ifPerfL2StatCurrentBroadcastFrames = _IfPerfL2StatCurrentBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 10),
    _IfPerfL2StatCurrentBroadcastFrames_Type()
)
ifPerfL2StatCurrentBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentBroadcastFrames.setStatus("current")
_IfPerfL2StatMaxUtilization_Type = Unsigned32WithNA
_IfPerfL2StatMaxUtilization_Object = MibTableColumn
ifPerfL2StatMaxUtilization = _IfPerfL2StatMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 11),
    _IfPerfL2StatMaxUtilization_Type()
)
ifPerfL2StatMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatMaxUtilization.setStatus("current")
_IfPerfL2StatAverageUtilization_Type = Unsigned32WithNA
_IfPerfL2StatAverageUtilization_Object = MibTableColumn
ifPerfL2StatAverageUtilization = _IfPerfL2StatAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 12),
    _IfPerfL2StatAverageUtilization_Type()
)
ifPerfL2StatAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatAverageUtilization.setStatus("current")
_IfPerfL2StatCurrentUtilization_Type = Unsigned32WithNA
_IfPerfL2StatCurrentUtilization_Object = MibTableColumn
ifPerfL2StatCurrentUtilization = _IfPerfL2StatCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 7, 1, 1, 13),
    _IfPerfL2StatCurrentUtilization_Type()
)
ifPerfL2StatCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2StatCurrentUtilization.setStatus("current")
_IfPerfL2ErrorList_ObjectIdentity = ObjectIdentity
ifPerfL2ErrorList = _IfPerfL2ErrorList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8)
)
_IfPerfL2ErrorTable_Object = MibTable
ifPerfL2ErrorTable = _IfPerfL2ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ifPerfL2ErrorTable.setStatus("current")
_IfPerfL2ErrorEntry_Object = MibTableRow
ifPerfL2ErrorEntry = _IfPerfL2ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1)
)
ifPerfL2ErrorEntry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfL2ErrorIndex"),
)
if mibBuilder.loadTexts:
    ifPerfL2ErrorEntry.setStatus("current")
_IfPerfL2ErrorIndex_Type = Unsigned32
_IfPerfL2ErrorIndex_Object = MibTableColumn
ifPerfL2ErrorIndex = _IfPerfL2ErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 1),
    _IfPerfL2ErrorIndex_Type()
)
ifPerfL2ErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorIndex.setStatus("current")
_IfPerfL2ErrorName_Type = MgmtNameString
_IfPerfL2ErrorName_Object = MibTableColumn
ifPerfL2ErrorName = _IfPerfL2ErrorName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 2),
    _IfPerfL2ErrorName_Type()
)
ifPerfL2ErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorName.setStatus("current")
_IfPerfL2ErrorConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfL2ErrorConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfL2ErrorConnIfPerfAdminIfIndex = _IfPerfL2ErrorConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 3),
    _IfPerfL2ErrorConnIfPerfAdminIfIndex_Type()
)
ifPerfL2ErrorConnIfPerfAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorConnIfPerfAdminIfIndex.setStatus("current")
_IfPerfL2ErrorPeriod_Type = PerfPeriodWithNA
_IfPerfL2ErrorPeriod_Object = MibTableColumn
ifPerfL2ErrorPeriod = _IfPerfL2ErrorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 4),
    _IfPerfL2ErrorPeriod_Type()
)
ifPerfL2ErrorPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorPeriod.setStatus("current")
_IfPerfL2ErrorType_Type = L2MeasurementTypeWithNA
_IfPerfL2ErrorType_Object = MibTableColumn
ifPerfL2ErrorType = _IfPerfL2ErrorType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 5),
    _IfPerfL2ErrorType_Type()
)
ifPerfL2ErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorType.setStatus("current")
_IfPerfL2ErrorCurrentUndersizedFrames_Type = Counter64
_IfPerfL2ErrorCurrentUndersizedFrames_Object = MibTableColumn
ifPerfL2ErrorCurrentUndersizedFrames = _IfPerfL2ErrorCurrentUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 6),
    _IfPerfL2ErrorCurrentUndersizedFrames_Type()
)
ifPerfL2ErrorCurrentUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorCurrentUndersizedFrames.setStatus("current")
_IfPerfL2ErrorCurrentOversizedFrames_Type = Counter64
_IfPerfL2ErrorCurrentOversizedFrames_Object = MibTableColumn
ifPerfL2ErrorCurrentOversizedFrames = _IfPerfL2ErrorCurrentOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 7),
    _IfPerfL2ErrorCurrentOversizedFrames_Type()
)
ifPerfL2ErrorCurrentOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorCurrentOversizedFrames.setStatus("current")
_IfPerfL2ErrorCurrentFragments_Type = Counter64
_IfPerfL2ErrorCurrentFragments_Object = MibTableColumn
ifPerfL2ErrorCurrentFragments = _IfPerfL2ErrorCurrentFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 8),
    _IfPerfL2ErrorCurrentFragments_Type()
)
ifPerfL2ErrorCurrentFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorCurrentFragments.setStatus("current")
_IfPerfL2ErrorCurrentFcsErrors_Type = Counter64
_IfPerfL2ErrorCurrentFcsErrors_Object = MibTableColumn
ifPerfL2ErrorCurrentFcsErrors = _IfPerfL2ErrorCurrentFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 9),
    _IfPerfL2ErrorCurrentFcsErrors_Type()
)
ifPerfL2ErrorCurrentFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorCurrentFcsErrors.setStatus("current")


class _IfPerfL2ErrorUndersizedFramesThreshold_Type(Counter64):
    """Custom type ifPerfL2ErrorUndersizedFramesThreshold based on Counter64"""
    defaultValue = 10


_IfPerfL2ErrorUndersizedFramesThreshold_Type.__name__ = "Counter64"
_IfPerfL2ErrorUndersizedFramesThreshold_Object = MibTableColumn
ifPerfL2ErrorUndersizedFramesThreshold = _IfPerfL2ErrorUndersizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 10),
    _IfPerfL2ErrorUndersizedFramesThreshold_Type()
)
ifPerfL2ErrorUndersizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfL2ErrorUndersizedFramesThreshold.setStatus("current")


class _IfPerfL2ErrorOversizedFramesThreshold_Type(Counter64):
    """Custom type ifPerfL2ErrorOversizedFramesThreshold based on Counter64"""
    defaultValue = 10


_IfPerfL2ErrorOversizedFramesThreshold_Type.__name__ = "Counter64"
_IfPerfL2ErrorOversizedFramesThreshold_Object = MibTableColumn
ifPerfL2ErrorOversizedFramesThreshold = _IfPerfL2ErrorOversizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 11),
    _IfPerfL2ErrorOversizedFramesThreshold_Type()
)
ifPerfL2ErrorOversizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfL2ErrorOversizedFramesThreshold.setStatus("current")


class _IfPerfL2ErrorFragmentsThreshold_Type(Counter64):
    """Custom type ifPerfL2ErrorFragmentsThreshold based on Counter64"""
    defaultValue = 10


_IfPerfL2ErrorFragmentsThreshold_Type.__name__ = "Counter64"
_IfPerfL2ErrorFragmentsThreshold_Object = MibTableColumn
ifPerfL2ErrorFragmentsThreshold = _IfPerfL2ErrorFragmentsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 12),
    _IfPerfL2ErrorFragmentsThreshold_Type()
)
ifPerfL2ErrorFragmentsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfL2ErrorFragmentsThreshold.setStatus("current")


class _IfPerfL2ErrorFcsErrorsThreshold_Type(Counter64):
    """Custom type ifPerfL2ErrorFcsErrorsThreshold based on Counter64"""
    defaultValue = 10


_IfPerfL2ErrorFcsErrorsThreshold_Type.__name__ = "Counter64"
_IfPerfL2ErrorFcsErrorsThreshold_Object = MibTableColumn
ifPerfL2ErrorFcsErrorsThreshold = _IfPerfL2ErrorFcsErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 13),
    _IfPerfL2ErrorFcsErrorsThreshold_Type()
)
ifPerfL2ErrorFcsErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPerfL2ErrorFcsErrorsThreshold.setStatus("current")
_IfPerfL2ErrorUndersizedFramesFault_Type = FaultStatusWithNA
_IfPerfL2ErrorUndersizedFramesFault_Object = MibTableColumn
ifPerfL2ErrorUndersizedFramesFault = _IfPerfL2ErrorUndersizedFramesFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 14),
    _IfPerfL2ErrorUndersizedFramesFault_Type()
)
ifPerfL2ErrorUndersizedFramesFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorUndersizedFramesFault.setStatus("current")
_IfPerfL2ErrorOversizedFramesFault_Type = FaultStatusWithNA
_IfPerfL2ErrorOversizedFramesFault_Object = MibTableColumn
ifPerfL2ErrorOversizedFramesFault = _IfPerfL2ErrorOversizedFramesFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 15),
    _IfPerfL2ErrorOversizedFramesFault_Type()
)
ifPerfL2ErrorOversizedFramesFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorOversizedFramesFault.setStatus("current")
_IfPerfL2ErrorFragmentsFault_Type = FaultStatusWithNA
_IfPerfL2ErrorFragmentsFault_Object = MibTableColumn
ifPerfL2ErrorFragmentsFault = _IfPerfL2ErrorFragmentsFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 16),
    _IfPerfL2ErrorFragmentsFault_Type()
)
ifPerfL2ErrorFragmentsFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorFragmentsFault.setStatus("current")
_IfPerfL2ErrorFcsErrorsFault_Type = FaultStatusWithNA
_IfPerfL2ErrorFcsErrorsFault_Object = MibTableColumn
ifPerfL2ErrorFcsErrorsFault = _IfPerfL2ErrorFcsErrorsFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 8, 1, 1, 17),
    _IfPerfL2ErrorFcsErrorsFault_Type()
)
ifPerfL2ErrorFcsErrorsFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfL2ErrorFcsErrorsFault.setStatus("current")
_IfPerfDelayList_ObjectIdentity = ObjectIdentity
ifPerfDelayList = _IfPerfDelayList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9)
)
_IfPerfDelayTable_Object = MibTable
ifPerfDelayTable = _IfPerfDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1)
)
if mibBuilder.loadTexts:
    ifPerfDelayTable.setStatus("current")
_IfPerfDelayEntry_Object = MibTableRow
ifPerfDelayEntry = _IfPerfDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1)
)
ifPerfDelayEntry.setIndexNames(
    (0, "LUM-IFPERF-MIB", "ifPerfDelayIndex"),
)
if mibBuilder.loadTexts:
    ifPerfDelayEntry.setStatus("current")
_IfPerfDelayIndex_Type = Unsigned32
_IfPerfDelayIndex_Object = MibTableColumn
ifPerfDelayIndex = _IfPerfDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1, 1),
    _IfPerfDelayIndex_Type()
)
ifPerfDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfDelayIndex.setStatus("current")
_IfPerfDelayUId_Type = Unsigned32
_IfPerfDelayUId_Object = MibTableColumn
ifPerfDelayUId = _IfPerfDelayUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1, 2),
    _IfPerfDelayUId_Type()
)
ifPerfDelayUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfDelayUId.setStatus("current")
_IfPerfDelayName_Type = MgmtNameString
_IfPerfDelayName_Object = MibTableColumn
ifPerfDelayName = _IfPerfDelayName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1, 3),
    _IfPerfDelayName_Type()
)
ifPerfDelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfDelayName.setStatus("current")
_IfPerfDelayTwoWayFiberDelay_Type = Unsigned32WithNA
_IfPerfDelayTwoWayFiberDelay_Object = MibTableColumn
ifPerfDelayTwoWayFiberDelay = _IfPerfDelayTwoWayFiberDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1, 4),
    _IfPerfDelayTwoWayFiberDelay_Type()
)
ifPerfDelayTwoWayFiberDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfDelayTwoWayFiberDelay.setStatus("current")
_IfPerfDelayConnIfPerfAdminIfIndex_Type = Unsigned32WithNA
_IfPerfDelayConnIfPerfAdminIfIndex_Object = MibTableColumn
ifPerfDelayConnIfPerfAdminIfIndex = _IfPerfDelayConnIfPerfAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 2, 9, 1, 1, 5),
    _IfPerfDelayConnIfPerfAdminIfIndex_Type()
)
ifPerfDelayConnIfPerfAdminIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPerfDelayConnIfPerfAdminIfIndex.setStatus("current")

# Managed Objects groups

ifPerfGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 1)
)
ifPerfGeneralGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0StateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifPerfGeneralGroupV1.setStatus("deprecated")

ifPerfAdminGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 2)
)
ifPerfAdminGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfAdminIndex"),
        ("LUM-IFPERF-MIB", "ifPerfAdminName"),
        ("LUM-IFPERF-MIB", "ifPerfAdminConnIfBasicIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfAdminAdminStatus"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReportMode"),
        ("LUM-IFPERF-MIB", "ifPerfAdminOperStatus"),
        ("LUM-IFPERF-MIB", "ifPerfAdminIsSuspect15m"),
        ("LUM-IFPERF-MIB", "ifPerfAdminIsSuspect24h"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReset15m"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReset24h"))
)
if mibBuilder.loadTexts:
    ifPerfAdminGroupV1.setStatus("deprecated")

ifPerfFecGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 3)
)
ifPerfFecGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfFecIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecName"),
        ("LUM-IFPERF-MIB", "ifPerfFecConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedZeros"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedOnes"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBerEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxAvgPreFecBer"))
)
if mibBuilder.loadTexts:
    ifPerfFecGroupV1.setStatus("deprecated")

ifPerfG826GroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 4)
)
ifPerfG826GroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfG826Index"),
        ("LUM-IFPERF-MIB", "ifPerfG826Name"),
        ("LUM-IFPERF-MIB", "ifPerfG826ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfG826Period"),
        ("LUM-IFPERF-MIB", "ifPerfG826Type"),
        ("LUM-IFPERF-MIB", "ifPerfG826MonitorLevel"),
        ("LUM-IFPERF-MIB", "ifPerfG826MonitorChannel"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterBbe"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdBbe"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusBbe"))
)
if mibBuilder.loadTexts:
    ifPerfG826GroupV1.setStatus("deprecated")

ifPerfL1GroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 5)
)
ifPerfL1GroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL1Index"),
        ("LUM-IFPERF-MIB", "ifPerfL1Name"),
        ("LUM-IFPERF-MIB", "ifPerfL1ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL1Period"),
        ("LUM-IFPERF-MIB", "ifPerfL1Type"),
        ("LUM-IFPERF-MIB", "ifPerfL1MaxUtilization"),
        ("LUM-IFPERF-MIB", "ifPerfL1AverageUtilization"))
)
if mibBuilder.loadTexts:
    ifPerfL1GroupV1.setStatus("deprecated")

ifPerfL0GroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 6)
)
ifPerfL0GroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL0Index"),
        ("LUM-IFPERF-MIB", "ifPerfL0Name"),
        ("LUM-IFPERF-MIB", "ifPerfL0ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL0RxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0TxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0InitialRxPower"))
)
if mibBuilder.loadTexts:
    ifPerfL0GroupV1.setStatus("deprecated")

ifPerfGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 7)
)
ifPerfGeneralGroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifPerfGeneralGroupV2.setStatus("deprecated")

ifPerfL2StatGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 8)
)
ifPerfL2StatGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL2StatIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatName"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatPeriod"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatType"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentBytes"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentUnicastFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentMulticastFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentBroadcastFrames"))
)
if mibBuilder.loadTexts:
    ifPerfL2StatGroupV1.setStatus("deprecated")

ifPerfL1GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 9)
)
ifPerfL1GroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL1Index"),
        ("LUM-IFPERF-MIB", "ifPerfL1Name"),
        ("LUM-IFPERF-MIB", "ifPerfL1ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL1Period"),
        ("LUM-IFPERF-MIB", "ifPerfL1Type"),
        ("LUM-IFPERF-MIB", "ifPerfL1MaxUtilization"),
        ("LUM-IFPERF-MIB", "ifPerfL1AverageUtilization"),
        ("LUM-IFPERF-MIB", "ifPerfL1CurrentUtilization"))
)
if mibBuilder.loadTexts:
    ifPerfL1GroupV2.setStatus("current")

ifPerfL0GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 10)
)
ifPerfL0GroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL0Index"),
        ("LUM-IFPERF-MIB", "ifPerfL0Name"),
        ("LUM-IFPERF-MIB", "ifPerfL0ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL0RxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0TxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0InitialRxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0ChromaticDispersion"),
        ("LUM-IFPERF-MIB", "ifPerfL0DifferentialGroupDelay"),
        ("LUM-IFPERF-MIB", "ifPerfL0InitialDifferentialGroupDelay"))
)
if mibBuilder.loadTexts:
    ifPerfL0GroupV2.setStatus("deprecated")

ifPerfL2ErrorGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 11)
)
ifPerfL2ErrorGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL2ErrorIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorName"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorPeriod"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorType"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorCurrentUndersizedFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorCurrentOversizedFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorCurrentFragments"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorCurrentFcsErrors"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorUndersizedFramesThreshold"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorOversizedFramesThreshold"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorFragmentsThreshold"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorFcsErrorsThreshold"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorUndersizedFramesFault"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorOversizedFramesFault"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorFragmentsFault"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorFcsErrorsFault"))
)
if mibBuilder.loadTexts:
    ifPerfL2ErrorGroupV1.setStatus("current")

ifPerfFecGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 12)
)
ifPerfFecGroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfFecIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecName"),
        ("LUM-IFPERF-MIB", "ifPerfFecConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedZeros"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedOnes"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBerEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxAvgPreFecBer"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedBits"))
)
if mibBuilder.loadTexts:
    ifPerfFecGroupV2.setStatus("deprecated")

ifPerfFecGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 13)
)
ifPerfFecGroupV3.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfFecIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecName"),
        ("LUM-IFPERF-MIB", "ifPerfFecConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedZeros"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedOnes"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBerEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxAvgPreFecBer"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedBits"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBitErrorEstimation"))
)
if mibBuilder.loadTexts:
    ifPerfFecGroupV3.setStatus("deprecated")

ifPerfAdminGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 14)
)
ifPerfAdminGroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfAdminIndex"),
        ("LUM-IFPERF-MIB", "ifPerfAdminName"),
        ("LUM-IFPERF-MIB", "ifPerfAdminConnIfBasicIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfAdminAdminStatus"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReportMode"),
        ("LUM-IFPERF-MIB", "ifPerfAdminOperStatus"),
        ("LUM-IFPERF-MIB", "ifPerfAdminIsSuspect15m"),
        ("LUM-IFPERF-MIB", "ifPerfAdminIsSuspect24h"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReset15m"),
        ("LUM-IFPERF-MIB", "ifPerfAdminReset24h"),
        ("LUM-IFPERF-MIB", "ifPerfAdminUpId"))
)
if mibBuilder.loadTexts:
    ifPerfAdminGroupV2.setStatus("current")

ifPerfG826GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 15)
)
ifPerfG826GroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfG826Index"),
        ("LUM-IFPERF-MIB", "ifPerfG826Name"),
        ("LUM-IFPERF-MIB", "ifPerfG826ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfG826Period"),
        ("LUM-IFPERF-MIB", "ifPerfG826Type"),
        ("LUM-IFPERF-MIB", "ifPerfG826MonitorLevel"),
        ("LUM-IFPERF-MIB", "ifPerfG826MonitorChannel"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826CounterBbe"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826ThresholdBbe"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusEs"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusSes"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusUas"),
        ("LUM-IFPERF-MIB", "ifPerfG826FaultStatusBbe"),
        ("LUM-IFPERF-MIB", "ifPerfG826UpId"))
)
if mibBuilder.loadTexts:
    ifPerfG826GroupV2.setStatus("current")

ifPerfL2StatGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 16)
)
ifPerfL2StatGroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL2StatIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatName"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatPeriod"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatType"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentBytes"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentUnicastFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentMulticastFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentBroadcastFrames"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatMaxUtilization"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatAverageUtilization"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatCurrentUtilization"))
)
if mibBuilder.loadTexts:
    ifPerfL2StatGroupV2.setStatus("current")

ifPerfFecGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 17)
)
ifPerfFecGroupV4.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfFecIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecName"),
        ("LUM-IFPERF-MIB", "ifPerfFecConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedZeros"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedOnes"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBerEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxAvgPreFecBer"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedBits"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBitErrorEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecOpticalSNR"))
)
if mibBuilder.loadTexts:
    ifPerfFecGroupV4.setStatus("deprecated")

ifPerfL0GroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 18)
)
ifPerfL0GroupV3.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfL0Index"),
        ("LUM-IFPERF-MIB", "ifPerfL0Name"),
        ("LUM-IFPERF-MIB", "ifPerfL0ConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfL0RxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0TxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0InitialRxPower"),
        ("LUM-IFPERF-MIB", "ifPerfL0ChromaticDispersion"),
        ("LUM-IFPERF-MIB", "ifPerfL0DifferentialGroupDelay"),
        ("LUM-IFPERF-MIB", "ifPerfL0InitialDifferentialGroupDelay"),
        ("LUM-IFPERF-MIB", "ifPerfL0UpId"))
)
if mibBuilder.loadTexts:
    ifPerfL0GroupV3.setStatus("current")

ifPerfFecGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 19)
)
ifPerfFecGroupV5.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfFecIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecName"),
        ("LUM-IFPERF-MIB", "ifPerfFecConnIfPerfAdminIfIndex"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedZeros"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedOnes"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBerEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxAvgPreFecBer"),
        ("LUM-IFPERF-MIB", "ifPerfFecCorrectedBits"),
        ("LUM-IFPERF-MIB", "ifPerfFecRxBitErrorEstimation"),
        ("LUM-IFPERF-MIB", "ifPerfFecOpticalSNR"),
        ("LUM-IFPERF-MIB", "ifPerfFecUpId"))
)
if mibBuilder.loadTexts:
    ifPerfFecGroupV5.setStatus("current")

ifPerfGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 20)
)
ifPerfGeneralGroupV3.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralAdminStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralFecStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralG826StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL1StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0TableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0ConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL0StateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2StatStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralL2ErrorStateLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralDelayTableSize"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralDelayConfigLastChangeTime"),
        ("LUM-IFPERF-MIB", "ifPerfGeneralDelayStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifPerfGeneralGroupV3.setStatus("current")

ifPerfDelayGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 21)
)
ifPerfDelayGroupV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfDelayIndex"),
        ("LUM-IFPERF-MIB", "ifPerfDelayUId"),
        ("LUM-IFPERF-MIB", "ifPerfDelayName"),
        ("LUM-IFPERF-MIB", "ifPerfDelayTwoWayFiberDelay"))
)
if mibBuilder.loadTexts:
    ifPerfDelayGroupV1.setStatus("deprecated")

ifPerfDelayGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 1, 22)
)
ifPerfDelayGroupV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfDelayIndex"),
        ("LUM-IFPERF-MIB", "ifPerfDelayUId"),
        ("LUM-IFPERF-MIB", "ifPerfDelayName"),
        ("LUM-IFPERF-MIB", "ifPerfDelayTwoWayFiberDelay"),
        ("LUM-IFPERF-MIB", "ifPerfDelayConnIfPerfAdminIfIndex"))
)
if mibBuilder.loadTexts:
    ifPerfDelayGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfPerfComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 1)
)
lumIfPerfComplV1.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV1.setStatus(
        "deprecated"
    )

lumIfPerfComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 2)
)
lumIfPerfComplV2.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV2.setStatus(
        "deprecated"
    )

lumIfPerfComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 3)
)
lumIfPerfComplV3.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV3.setStatus(
        "deprecated"
    )

lumIfPerfComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 4)
)
lumIfPerfComplV4.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV4.setStatus(
        "deprecated"
    )

lumIfPerfComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 5)
)
lumIfPerfComplV5.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV5.setStatus(
        "deprecated"
    )

lumIfPerfComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 6)
)
lumIfPerfComplV6.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV6.setStatus(
        "deprecated"
    )

lumIfPerfComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 7)
)
lumIfPerfComplV7.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV7.setStatus(
        "deprecated"
    )

lumIfPerfComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 8)
)
lumIfPerfComplV8.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV4"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV8.setStatus(
        "deprecated"
    )

lumIfPerfComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 9)
)
lumIfPerfComplV9.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV4"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV9.setStatus(
        "deprecated"
    )

lumIfPerfComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 10)
)
lumIfPerfComplV10.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV5"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV10.setStatus(
        "deprecated"
    )

lumIfPerfComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 11)
)
lumIfPerfComplV11.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV5"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfDelayGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV11.setStatus(
        "deprecated"
    )

lumIfPerfComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56, 1, 2, 12)
)
lumIfPerfComplV12.setObjects(
      *(("LUM-IFPERF-MIB", "ifPerfGeneralGroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfAdminGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfFecGroupV5"),
        ("LUM-IFPERF-MIB", "ifPerfG826GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL1GroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL0GroupV3"),
        ("LUM-IFPERF-MIB", "ifPerfL2StatGroupV2"),
        ("LUM-IFPERF-MIB", "ifPerfL2ErrorGroupV1"),
        ("LUM-IFPERF-MIB", "ifPerfDelayGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfPerfComplV12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFPERF-MIB",
    **{"PerfPeriodWithNA": PerfPeriodWithNA,
       "G826MonitorLevelWithNA": G826MonitorLevelWithNA,
       "G826MonitorChannelWithNA": G826MonitorChannelWithNA,
       "L1MeasurementTypeWithNA": L1MeasurementTypeWithNA,
       "L2MeasurementTypeWithNA": L2MeasurementTypeWithNA,
       "G826MeasurementTypeWithNA": G826MeasurementTypeWithNA,
       "BooleanValueWithNA": BooleanValueWithNA,
       "lumIfPerfMIBModule": lumIfPerfMIBModule,
       "lumIfPerfConfs": lumIfPerfConfs,
       "lumIfPerfGroups": lumIfPerfGroups,
       "ifPerfGeneralGroupV1": ifPerfGeneralGroupV1,
       "ifPerfAdminGroupV1": ifPerfAdminGroupV1,
       "ifPerfFecGroupV1": ifPerfFecGroupV1,
       "ifPerfG826GroupV1": ifPerfG826GroupV1,
       "ifPerfL1GroupV1": ifPerfL1GroupV1,
       "ifPerfL0GroupV1": ifPerfL0GroupV1,
       "ifPerfGeneralGroupV2": ifPerfGeneralGroupV2,
       "ifPerfL2StatGroupV1": ifPerfL2StatGroupV1,
       "ifPerfL1GroupV2": ifPerfL1GroupV2,
       "ifPerfL0GroupV2": ifPerfL0GroupV2,
       "ifPerfL2ErrorGroupV1": ifPerfL2ErrorGroupV1,
       "ifPerfFecGroupV2": ifPerfFecGroupV2,
       "ifPerfFecGroupV3": ifPerfFecGroupV3,
       "ifPerfAdminGroupV2": ifPerfAdminGroupV2,
       "ifPerfG826GroupV2": ifPerfG826GroupV2,
       "ifPerfL2StatGroupV2": ifPerfL2StatGroupV2,
       "ifPerfFecGroupV4": ifPerfFecGroupV4,
       "ifPerfL0GroupV3": ifPerfL0GroupV3,
       "ifPerfFecGroupV5": ifPerfFecGroupV5,
       "ifPerfGeneralGroupV3": ifPerfGeneralGroupV3,
       "ifPerfDelayGroupV1": ifPerfDelayGroupV1,
       "ifPerfDelayGroupV2": ifPerfDelayGroupV2,
       "lumIfPerfCompl": lumIfPerfCompl,
       "lumIfPerfComplV1": lumIfPerfComplV1,
       "lumIfPerfComplV2": lumIfPerfComplV2,
       "lumIfPerfComplV3": lumIfPerfComplV3,
       "lumIfPerfComplV4": lumIfPerfComplV4,
       "lumIfPerfComplV5": lumIfPerfComplV5,
       "lumIfPerfComplV6": lumIfPerfComplV6,
       "lumIfPerfComplV7": lumIfPerfComplV7,
       "lumIfPerfComplV8": lumIfPerfComplV8,
       "lumIfPerfComplV9": lumIfPerfComplV9,
       "lumIfPerfComplV10": lumIfPerfComplV10,
       "lumIfPerfComplV11": lumIfPerfComplV11,
       "lumIfPerfComplV12": lumIfPerfComplV12,
       "lumIfPerfMIBObjects": lumIfPerfMIBObjects,
       "ifPerfGeneral": ifPerfGeneral,
       "ifPerfGeneralConfigLastChangeTime": ifPerfGeneralConfigLastChangeTime,
       "ifPerfGeneralStateLastChangeTime": ifPerfGeneralStateLastChangeTime,
       "ifPerfGeneralAdminTableSize": ifPerfGeneralAdminTableSize,
       "ifPerfGeneralAdminConfigLastChangeTime": ifPerfGeneralAdminConfigLastChangeTime,
       "ifPerfGeneralAdminStateLastChangeTime": ifPerfGeneralAdminStateLastChangeTime,
       "ifPerfGeneralFecTableSize": ifPerfGeneralFecTableSize,
       "ifPerfGeneralFecConfigLastChangeTime": ifPerfGeneralFecConfigLastChangeTime,
       "ifPerfGeneralFecStateLastChangeTime": ifPerfGeneralFecStateLastChangeTime,
       "ifPerfGeneralG826TableSize": ifPerfGeneralG826TableSize,
       "ifPerfGeneralG826ConfigLastChangeTime": ifPerfGeneralG826ConfigLastChangeTime,
       "ifPerfGeneralG826StateLastChangeTime": ifPerfGeneralG826StateLastChangeTime,
       "ifPerfGeneralL1TableSize": ifPerfGeneralL1TableSize,
       "ifPerfGeneralL1ConfigLastChangeTime": ifPerfGeneralL1ConfigLastChangeTime,
       "ifPerfGeneralL1StateLastChangeTime": ifPerfGeneralL1StateLastChangeTime,
       "ifPerfGeneralL0TableSize": ifPerfGeneralL0TableSize,
       "ifPerfGeneralL0ConfigLastChangeTime": ifPerfGeneralL0ConfigLastChangeTime,
       "ifPerfGeneralL0StateLastChangeTime": ifPerfGeneralL0StateLastChangeTime,
       "ifPerfGeneralL2StatTableSize": ifPerfGeneralL2StatTableSize,
       "ifPerfGeneralL2StatConfigLastChangeTime": ifPerfGeneralL2StatConfigLastChangeTime,
       "ifPerfGeneralL2StatStateLastChangeTime": ifPerfGeneralL2StatStateLastChangeTime,
       "ifPerfGeneralL2ErrorTableSize": ifPerfGeneralL2ErrorTableSize,
       "ifPerfGeneralL2ErrorConfigLastChangeTime": ifPerfGeneralL2ErrorConfigLastChangeTime,
       "ifPerfGeneralL2ErrorStateLastChangeTime": ifPerfGeneralL2ErrorStateLastChangeTime,
       "ifPerfGeneralDelayTableSize": ifPerfGeneralDelayTableSize,
       "ifPerfGeneralDelayConfigLastChangeTime": ifPerfGeneralDelayConfigLastChangeTime,
       "ifPerfGeneralDelayStateLastChangeTime": ifPerfGeneralDelayStateLastChangeTime,
       "ifPerfAdminList": ifPerfAdminList,
       "ifPerfAdminTable": ifPerfAdminTable,
       "ifPerfAdminEntry": ifPerfAdminEntry,
       "ifPerfAdminIndex": ifPerfAdminIndex,
       "ifPerfAdminName": ifPerfAdminName,
       "ifPerfAdminConnIfBasicIfIndex": ifPerfAdminConnIfBasicIfIndex,
       "ifPerfAdminAdminStatus": ifPerfAdminAdminStatus,
       "ifPerfAdminReportMode": ifPerfAdminReportMode,
       "ifPerfAdminOperStatus": ifPerfAdminOperStatus,
       "ifPerfAdminIsSuspect15m": ifPerfAdminIsSuspect15m,
       "ifPerfAdminIsSuspect24h": ifPerfAdminIsSuspect24h,
       "ifPerfAdminReset15m": ifPerfAdminReset15m,
       "ifPerfAdminReset24h": ifPerfAdminReset24h,
       "ifPerfAdminUpId": ifPerfAdminUpId,
       "ifPerfFecList": ifPerfFecList,
       "ifPerfFecTable": ifPerfFecTable,
       "ifPerfFecEntry": ifPerfFecEntry,
       "ifPerfFecIndex": ifPerfFecIndex,
       "ifPerfFecName": ifPerfFecName,
       "ifPerfFecConnIfPerfAdminIfIndex": ifPerfFecConnIfPerfAdminIfIndex,
       "ifPerfFecCorrectedZeros": ifPerfFecCorrectedZeros,
       "ifPerfFecCorrectedOnes": ifPerfFecCorrectedOnes,
       "ifPerfFecRxBerEstimation": ifPerfFecRxBerEstimation,
       "ifPerfFecRxAvgPreFecBer": ifPerfFecRxAvgPreFecBer,
       "ifPerfFecCorrectedBits": ifPerfFecCorrectedBits,
       "ifPerfFecRxBitErrorEstimation": ifPerfFecRxBitErrorEstimation,
       "ifPerfFecOpticalSNR": ifPerfFecOpticalSNR,
       "ifPerfFecUpId": ifPerfFecUpId,
       "ifPerfG826List": ifPerfG826List,
       "ifPerfG826Table": ifPerfG826Table,
       "ifPerfG826Entry": ifPerfG826Entry,
       "ifPerfG826Index": ifPerfG826Index,
       "ifPerfG826Name": ifPerfG826Name,
       "ifPerfG826ConnIfPerfAdminIfIndex": ifPerfG826ConnIfPerfAdminIfIndex,
       "ifPerfG826Period": ifPerfG826Period,
       "ifPerfG826Type": ifPerfG826Type,
       "ifPerfG826MonitorLevel": ifPerfG826MonitorLevel,
       "ifPerfG826MonitorChannel": ifPerfG826MonitorChannel,
       "ifPerfG826CounterEs": ifPerfG826CounterEs,
       "ifPerfG826CounterSes": ifPerfG826CounterSes,
       "ifPerfG826CounterUas": ifPerfG826CounterUas,
       "ifPerfG826CounterBbe": ifPerfG826CounterBbe,
       "ifPerfG826ThresholdEs": ifPerfG826ThresholdEs,
       "ifPerfG826ThresholdSes": ifPerfG826ThresholdSes,
       "ifPerfG826ThresholdUas": ifPerfG826ThresholdUas,
       "ifPerfG826ThresholdBbe": ifPerfG826ThresholdBbe,
       "ifPerfG826FaultStatusEs": ifPerfG826FaultStatusEs,
       "ifPerfG826FaultStatusSes": ifPerfG826FaultStatusSes,
       "ifPerfG826FaultStatusUas": ifPerfG826FaultStatusUas,
       "ifPerfG826FaultStatusBbe": ifPerfG826FaultStatusBbe,
       "ifPerfG826UpId": ifPerfG826UpId,
       "ifPerfL1List": ifPerfL1List,
       "ifPerfL1Table": ifPerfL1Table,
       "ifPerfL1Entry": ifPerfL1Entry,
       "ifPerfL1Index": ifPerfL1Index,
       "ifPerfL1Name": ifPerfL1Name,
       "ifPerfL1ConnIfPerfAdminIfIndex": ifPerfL1ConnIfPerfAdminIfIndex,
       "ifPerfL1Period": ifPerfL1Period,
       "ifPerfL1Type": ifPerfL1Type,
       "ifPerfL1MaxUtilization": ifPerfL1MaxUtilization,
       "ifPerfL1AverageUtilization": ifPerfL1AverageUtilization,
       "ifPerfL1CurrentUtilization": ifPerfL1CurrentUtilization,
       "ifPerfL0List": ifPerfL0List,
       "ifPerfL0Table": ifPerfL0Table,
       "ifPerfL0Entry": ifPerfL0Entry,
       "ifPerfL0Index": ifPerfL0Index,
       "ifPerfL0Name": ifPerfL0Name,
       "ifPerfL0ConnIfPerfAdminIfIndex": ifPerfL0ConnIfPerfAdminIfIndex,
       "ifPerfL0RxPower": ifPerfL0RxPower,
       "ifPerfL0TxPower": ifPerfL0TxPower,
       "ifPerfL0InitialRxPower": ifPerfL0InitialRxPower,
       "ifPerfL0ChromaticDispersion": ifPerfL0ChromaticDispersion,
       "ifPerfL0DifferentialGroupDelay": ifPerfL0DifferentialGroupDelay,
       "ifPerfL0InitialDifferentialGroupDelay": ifPerfL0InitialDifferentialGroupDelay,
       "ifPerfL0UpId": ifPerfL0UpId,
       "ifPerfL2StatList": ifPerfL2StatList,
       "ifPerfL2StatTable": ifPerfL2StatTable,
       "ifPerfL2StatEntry": ifPerfL2StatEntry,
       "ifPerfL2StatIndex": ifPerfL2StatIndex,
       "ifPerfL2StatName": ifPerfL2StatName,
       "ifPerfL2StatConnIfPerfAdminIfIndex": ifPerfL2StatConnIfPerfAdminIfIndex,
       "ifPerfL2StatPeriod": ifPerfL2StatPeriod,
       "ifPerfL2StatType": ifPerfL2StatType,
       "ifPerfL2StatCurrentFrames": ifPerfL2StatCurrentFrames,
       "ifPerfL2StatCurrentBytes": ifPerfL2StatCurrentBytes,
       "ifPerfL2StatCurrentUnicastFrames": ifPerfL2StatCurrentUnicastFrames,
       "ifPerfL2StatCurrentMulticastFrames": ifPerfL2StatCurrentMulticastFrames,
       "ifPerfL2StatCurrentBroadcastFrames": ifPerfL2StatCurrentBroadcastFrames,
       "ifPerfL2StatMaxUtilization": ifPerfL2StatMaxUtilization,
       "ifPerfL2StatAverageUtilization": ifPerfL2StatAverageUtilization,
       "ifPerfL2StatCurrentUtilization": ifPerfL2StatCurrentUtilization,
       "ifPerfL2ErrorList": ifPerfL2ErrorList,
       "ifPerfL2ErrorTable": ifPerfL2ErrorTable,
       "ifPerfL2ErrorEntry": ifPerfL2ErrorEntry,
       "ifPerfL2ErrorIndex": ifPerfL2ErrorIndex,
       "ifPerfL2ErrorName": ifPerfL2ErrorName,
       "ifPerfL2ErrorConnIfPerfAdminIfIndex": ifPerfL2ErrorConnIfPerfAdminIfIndex,
       "ifPerfL2ErrorPeriod": ifPerfL2ErrorPeriod,
       "ifPerfL2ErrorType": ifPerfL2ErrorType,
       "ifPerfL2ErrorCurrentUndersizedFrames": ifPerfL2ErrorCurrentUndersizedFrames,
       "ifPerfL2ErrorCurrentOversizedFrames": ifPerfL2ErrorCurrentOversizedFrames,
       "ifPerfL2ErrorCurrentFragments": ifPerfL2ErrorCurrentFragments,
       "ifPerfL2ErrorCurrentFcsErrors": ifPerfL2ErrorCurrentFcsErrors,
       "ifPerfL2ErrorUndersizedFramesThreshold": ifPerfL2ErrorUndersizedFramesThreshold,
       "ifPerfL2ErrorOversizedFramesThreshold": ifPerfL2ErrorOversizedFramesThreshold,
       "ifPerfL2ErrorFragmentsThreshold": ifPerfL2ErrorFragmentsThreshold,
       "ifPerfL2ErrorFcsErrorsThreshold": ifPerfL2ErrorFcsErrorsThreshold,
       "ifPerfL2ErrorUndersizedFramesFault": ifPerfL2ErrorUndersizedFramesFault,
       "ifPerfL2ErrorOversizedFramesFault": ifPerfL2ErrorOversizedFramesFault,
       "ifPerfL2ErrorFragmentsFault": ifPerfL2ErrorFragmentsFault,
       "ifPerfL2ErrorFcsErrorsFault": ifPerfL2ErrorFcsErrorsFault,
       "ifPerfDelayList": ifPerfDelayList,
       "ifPerfDelayTable": ifPerfDelayTable,
       "ifPerfDelayEntry": ifPerfDelayEntry,
       "ifPerfDelayIndex": ifPerfDelayIndex,
       "ifPerfDelayUId": ifPerfDelayUId,
       "ifPerfDelayName": ifPerfDelayName,
       "ifPerfDelayTwoWayFiberDelay": ifPerfDelayTwoWayFiberDelay,
       "ifPerfDelayConnIfPerfAdminIfIndex": ifPerfDelayConnIfPerfAdminIfIndex}
)
