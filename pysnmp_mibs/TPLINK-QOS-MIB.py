# SNMP MIB module (TPLINK-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:19 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22)
)
if mibBuilder.loadTexts:
    tplinkQosMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkQosMIBObjects_ObjectIdentity = ObjectIdentity
tplinkQosMIBObjects = _TplinkQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1)
)
_TplinkQosBasicConfig_ObjectIdentity = ObjectIdentity
tplinkQosBasicConfig = _TplinkQosBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1)
)
_TpQosBasicConfigTable_Object = MibTable
tpQosBasicConfigTable = _TpQosBasicConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpQosBasicConfigTable.setStatus("current")
_TpQosBasicConfigEntry_Object = MibTableRow
tpQosBasicConfigEntry = _TpQosBasicConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1)
)
tpQosBasicConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpQosBasicConfigEntry.setStatus("current")
_TpQosBasicConfigPort_Type = DisplayString
_TpQosBasicConfigPort_Object = MibTableColumn
tpQosBasicConfigPort = _TpQosBasicConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 1),
    _TpQosBasicConfigPort_Type()
)
tpQosBasicConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosBasicConfigPort.setStatus("current")


class _TpQosBasicConfigPri_Type(Integer32):
    """Custom type tpQosBasicConfigPri based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )


_TpQosBasicConfigPri_Type.__name__ = "Integer32"
_TpQosBasicConfigPri_Object = MibTableColumn
tpQosBasicConfigPri = _TpQosBasicConfigPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 2),
    _TpQosBasicConfigPri_Type()
)
tpQosBasicConfigPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosBasicConfigPri.setStatus("current")


class _TpQosBasicConfigTrust_Type(Integer32):
    """Custom type tpQosBasicConfigTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 0),
          ("trust-8021p", 1),
          ("trust-DSCP", 2))
    )


_TpQosBasicConfigTrust_Type.__name__ = "Integer32"
_TpQosBasicConfigTrust_Object = MibTableColumn
tpQosBasicConfigTrust = _TpQosBasicConfigTrust_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 3),
    _TpQosBasicConfigTrust_Type()
)
tpQosBasicConfigTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosBasicConfigTrust.setStatus("current")


class _TpQosBasicConfigLag_Type(OctetString):
    """Custom type tpQosBasicConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpQosBasicConfigLag_Type.__name__ = "OctetString"
_TpQosBasicConfigLag_Object = MibTableColumn
tpQosBasicConfigLag = _TpQosBasicConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 4),
    _TpQosBasicConfigLag_Type()
)
tpQosBasicConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosBasicConfigLag.setStatus("current")
_TplinkQosScheduler_ObjectIdentity = ObjectIdentity
tplinkQosScheduler = _TplinkQosScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2)
)
_TpQosSchedulerPort_Type = OctetString
_TpQosSchedulerPort_Object = MibScalar
tpQosSchedulerPort = _TpQosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 1),
    _TpQosSchedulerPort_Type()
)
tpQosSchedulerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerPort.setStatus("current")
_TpQosSchedulerTable_Object = MibTable
tpQosSchedulerTable = _TpQosSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpQosSchedulerTable.setStatus("current")
_TpQosSchedulerEntry_Object = MibTableRow
tpQosSchedulerEntry = _TpQosSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1)
)
tpQosSchedulerEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQosSchedulerConfigTc"),
)
if mibBuilder.loadTexts:
    tpQosSchedulerEntry.setStatus("current")


class _TpQosSchedulerConfigTc_Type(Integer32):
    """Custom type tpQosSchedulerConfigTc based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7))
    )


_TpQosSchedulerConfigTc_Type.__name__ = "Integer32"
_TpQosSchedulerConfigTc_Object = MibTableColumn
tpQosSchedulerConfigTc = _TpQosSchedulerConfigTc_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 1),
    _TpQosSchedulerConfigTc_Type()
)
tpQosSchedulerConfigTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosSchedulerConfigTc.setStatus("current")


class _TpQosSchedulerConfigMode_Type(Integer32):
    """Custom type tpQosSchedulerConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("weighted", 1))
    )


_TpQosSchedulerConfigMode_Type.__name__ = "Integer32"
_TpQosSchedulerConfigMode_Object = MibTableColumn
tpQosSchedulerConfigMode = _TpQosSchedulerConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 2),
    _TpQosSchedulerConfigMode_Type()
)
tpQosSchedulerConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerConfigMode.setStatus("current")
_TpQosSchedulerConfigWeight_Type = Integer32
_TpQosSchedulerConfigWeight_Object = MibTableColumn
tpQosSchedulerConfigWeight = _TpQosSchedulerConfigWeight_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 3),
    _TpQosSchedulerConfigWeight_Type()
)
tpQosSchedulerConfigWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerConfigWeight.setStatus("current")
_TpQosSchedulerConfigMinBandwidth_Type = Integer32
_TpQosSchedulerConfigMinBandwidth_Object = MibTableColumn
tpQosSchedulerConfigMinBandwidth = _TpQosSchedulerConfigMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 4),
    _TpQosSchedulerConfigMinBandwidth_Type()
)
tpQosSchedulerConfigMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerConfigMinBandwidth.setStatus("current")


class _TpQosSchedulerConfigManagementType_Type(Integer32):
    """Custom type tpQosSchedulerConfigManagementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("taildrop", 0)
    )


_TpQosSchedulerConfigManagementType_Type.__name__ = "Integer32"
_TpQosSchedulerConfigManagementType_Object = MibTableColumn
tpQosSchedulerConfigManagementType = _TpQosSchedulerConfigManagementType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 5),
    _TpQosSchedulerConfigManagementType_Type()
)
tpQosSchedulerConfigManagementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerConfigManagementType.setStatus("current")
_TplinkQos8021p_ObjectIdentity = ObjectIdentity
tplinkQos8021p = _TplinkQos8021p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3)
)
_TpQos8021pTable_Object = MibTable
tpQos8021pTable = _TpQos8021pTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpQos8021pTable.setStatus("current")
_TpQos8021pEntry_Object = MibTableRow
tpQos8021pEntry = _TpQos8021pEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 1, 1)
)
tpQos8021pEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQos8021pPriTag"),
)
if mibBuilder.loadTexts:
    tpQos8021pEntry.setStatus("current")
_TpQos8021pPriTag_Type = Integer32
_TpQos8021pPriTag_Object = MibTableColumn
tpQos8021pPriTag = _TpQos8021pPriTag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 1, 1, 1),
    _TpQos8021pPriTag_Type()
)
tpQos8021pPriTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQos8021pPriTag.setStatus("current")


class _TpQos8021pPriLevel_Type(Integer32):
    """Custom type tpQos8021pPriLevel based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7))
    )


_TpQos8021pPriLevel_Type.__name__ = "Integer32"
_TpQos8021pPriLevel_Object = MibTableColumn
tpQos8021pPriLevel = _TpQos8021pPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 1, 1, 2),
    _TpQos8021pPriLevel_Type()
)
tpQos8021pPriLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriLevel.setStatus("current")
_TplinkQos8021pRemap_ObjectIdentity = ObjectIdentity
tplinkQos8021pRemap = _TplinkQos8021pRemap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4)
)
_TpQos8021pRemapTable_Object = MibTable
tpQos8021pRemapTable = _TpQos8021pRemapTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpQos8021pRemapTable.setStatus("current")
_TpQos8021pRemapEntry_Object = MibTableRow
tpQos8021pRemapEntry = _TpQos8021pRemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1)
)
tpQos8021pRemapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpQos8021pRemapEntry.setStatus("current")
_TpQos8021pPort_Type = DisplayString
_TpQos8021pPort_Object = MibTableColumn
tpQos8021pPort = _TpQos8021pPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 1),
    _TpQos8021pPort_Type()
)
tpQos8021pPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQos8021pPort.setStatus("current")
_TpQos8021pPriTag0_Type = Integer32
_TpQos8021pPriTag0_Object = MibTableColumn
tpQos8021pPriTag0 = _TpQos8021pPriTag0_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 2),
    _TpQos8021pPriTag0_Type()
)
tpQos8021pPriTag0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag0.setStatus("current")
_TpQos8021pPriTag1_Type = Integer32
_TpQos8021pPriTag1_Object = MibTableColumn
tpQos8021pPriTag1 = _TpQos8021pPriTag1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 3),
    _TpQos8021pPriTag1_Type()
)
tpQos8021pPriTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag1.setStatus("current")
_TpQos8021pPriTag2_Type = Integer32
_TpQos8021pPriTag2_Object = MibTableColumn
tpQos8021pPriTag2 = _TpQos8021pPriTag2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 4),
    _TpQos8021pPriTag2_Type()
)
tpQos8021pPriTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag2.setStatus("current")
_TpQos8021pPriTag3_Type = Integer32
_TpQos8021pPriTag3_Object = MibTableColumn
tpQos8021pPriTag3 = _TpQos8021pPriTag3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 5),
    _TpQos8021pPriTag3_Type()
)
tpQos8021pPriTag3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag3.setStatus("current")
_TpQos8021pPriTag4_Type = Integer32
_TpQos8021pPriTag4_Object = MibTableColumn
tpQos8021pPriTag4 = _TpQos8021pPriTag4_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 6),
    _TpQos8021pPriTag4_Type()
)
tpQos8021pPriTag4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag4.setStatus("current")
_TpQos8021pPriTag5_Type = Integer32
_TpQos8021pPriTag5_Object = MibTableColumn
tpQos8021pPriTag5 = _TpQos8021pPriTag5_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 7),
    _TpQos8021pPriTag5_Type()
)
tpQos8021pPriTag5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag5.setStatus("current")
_TpQos8021pPriTag6_Type = Integer32
_TpQos8021pPriTag6_Object = MibTableColumn
tpQos8021pPriTag6 = _TpQos8021pPriTag6_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 8),
    _TpQos8021pPriTag6_Type()
)
tpQos8021pPriTag6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag6.setStatus("current")
_TpQos8021pPriTag7_Type = Integer32
_TpQos8021pPriTag7_Object = MibTableColumn
tpQos8021pPriTag7 = _TpQos8021pPriTag7_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 9),
    _TpQos8021pPriTag7_Type()
)
tpQos8021pPriTag7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriTag7.setStatus("current")


class _TpQos8021pPriLag_Type(OctetString):
    """Custom type tpQos8021pPriLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpQos8021pPriLag_Type.__name__ = "OctetString"
_TpQos8021pPriLag_Object = MibTableColumn
tpQos8021pPriLag = _TpQos8021pPriLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1, 1, 10),
    _TpQos8021pPriLag_Type()
)
tpQos8021pPriLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQos8021pPriLag.setStatus("current")
_TplinkQosDSCP_ObjectIdentity = ObjectIdentity
tplinkQosDSCP = _TplinkQosDSCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5)
)
_TpQosDSCPPort_Type = OctetString
_TpQosDSCPPort_Object = MibScalar
tpQosDSCPPort = _TpQosDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 1),
    _TpQosDSCPPort_Type()
)
tpQosDSCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosDSCPPort.setStatus("current")
_TpQosDSCPTable_Object = MibTable
tpQosDSCPTable = _TpQosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tpQosDSCPTable.setStatus("current")
_TpQosDSCPEntry_Object = MibTableRow
tpQosDSCPEntry = _TpQosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 2, 1)
)
tpQosDSCPEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQosDSCPPriTag"),
)
if mibBuilder.loadTexts:
    tpQosDSCPEntry.setStatus("current")
_TpQosDSCPPriTag_Type = Integer32
_TpQosDSCPPriTag_Object = MibTableColumn
tpQosDSCPPriTag = _TpQosDSCPPriTag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 2, 1, 1),
    _TpQosDSCPPriTag_Type()
)
tpQosDSCPPriTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosDSCPPriTag.setStatus("current")


class _TpQosDSCPPriLevel_Type(Integer32):
    """Custom type tpQosDSCPPriLevel based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )


_TpQosDSCPPriLevel_Type.__name__ = "Integer32"
_TpQosDSCPPriLevel_Object = MibTableColumn
tpQosDSCPPriLevel = _TpQosDSCPPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 2, 1, 2),
    _TpQosDSCPPriLevel_Type()
)
tpQosDSCPPriLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosDSCPPriLevel.setStatus("current")
_TpQosDSCPPriRemap_Type = Integer32
_TpQosDSCPPriRemap_Object = MibTableColumn
tpQosDSCPPriRemap = _TpQosDSCPPriRemap_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 5, 2, 1, 3),
    _TpQosDSCPPriRemap_Type()
)
tpQosDSCPPriRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosDSCPPriRemap.setStatus("current")
_TplinkQosNotifications_ObjectIdentity = ObjectIdentity
tplinkQosNotifications = _TplinkQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-QOS-MIB",
    **{"tplinkQosMIB": tplinkQosMIB,
       "tplinkQosMIBObjects": tplinkQosMIBObjects,
       "tplinkQosBasicConfig": tplinkQosBasicConfig,
       "tpQosBasicConfigTable": tpQosBasicConfigTable,
       "tpQosBasicConfigEntry": tpQosBasicConfigEntry,
       "tpQosBasicConfigPort": tpQosBasicConfigPort,
       "tpQosBasicConfigPri": tpQosBasicConfigPri,
       "tpQosBasicConfigTrust": tpQosBasicConfigTrust,
       "tpQosBasicConfigLag": tpQosBasicConfigLag,
       "tplinkQosScheduler": tplinkQosScheduler,
       "tpQosSchedulerPort": tpQosSchedulerPort,
       "tpQosSchedulerTable": tpQosSchedulerTable,
       "tpQosSchedulerEntry": tpQosSchedulerEntry,
       "tpQosSchedulerConfigTc": tpQosSchedulerConfigTc,
       "tpQosSchedulerConfigMode": tpQosSchedulerConfigMode,
       "tpQosSchedulerConfigWeight": tpQosSchedulerConfigWeight,
       "tpQosSchedulerConfigMinBandwidth": tpQosSchedulerConfigMinBandwidth,
       "tpQosSchedulerConfigManagementType": tpQosSchedulerConfigManagementType,
       "tplinkQos8021p": tplinkQos8021p,
       "tpQos8021pTable": tpQos8021pTable,
       "tpQos8021pEntry": tpQos8021pEntry,
       "tpQos8021pPriTag": tpQos8021pPriTag,
       "tpQos8021pPriLevel": tpQos8021pPriLevel,
       "tplinkQos8021pRemap": tplinkQos8021pRemap,
       "tpQos8021pRemapTable": tpQos8021pRemapTable,
       "tpQos8021pRemapEntry": tpQos8021pRemapEntry,
       "tpQos8021pPort": tpQos8021pPort,
       "tpQos8021pPriTag0": tpQos8021pPriTag0,
       "tpQos8021pPriTag1": tpQos8021pPriTag1,
       "tpQos8021pPriTag2": tpQos8021pPriTag2,
       "tpQos8021pPriTag3": tpQos8021pPriTag3,
       "tpQos8021pPriTag4": tpQos8021pPriTag4,
       "tpQos8021pPriTag5": tpQos8021pPriTag5,
       "tpQos8021pPriTag6": tpQos8021pPriTag6,
       "tpQos8021pPriTag7": tpQos8021pPriTag7,
       "tpQos8021pPriLag": tpQos8021pPriLag,
       "tplinkQosDSCP": tplinkQosDSCP,
       "tpQosDSCPPort": tpQosDSCPPort,
       "tpQosDSCPTable": tpQosDSCPTable,
       "tpQosDSCPEntry": tpQosDSCPEntry,
       "tpQosDSCPPriTag": tpQosDSCPPriTag,
       "tpQosDSCPPriLevel": tpQosDSCPPriLevel,
       "tpQosDSCPPriRemap": tpQosDSCPPriRemap,
       "tplinkQosNotifications": tplinkQosNotifications}
)
