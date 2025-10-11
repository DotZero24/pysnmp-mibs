# SNMP MIB module (LUM-IFAMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFAMPLIFIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:40 2025
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

(lumIfAmplifierMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfAmplifierMIB",
    "lumModules")

(AdminStatusWithNA,
 FaultStatusWithNA,
 Integer32WithNA,
 MgmtNameString,
 OperStatusWithNA,
 Signed32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "FaultStatusWithNA",
    "Integer32WithNA",
    "MgmtNameString",
    "OperStatusWithNA",
    "Signed32WithNA")

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

lumIfAmplifierMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 65)
)
if mibBuilder.loadTexts:
    lumIfAmplifierMIBModule.setRevisions(
        ("2018-09-28 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-05-30 00:00",
         "2015-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfAmplifierConfs_ObjectIdentity = ObjectIdentity
lumIfAmplifierConfs = _LumIfAmplifierConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1)
)
_LumIfAmplifierGroups_ObjectIdentity = ObjectIdentity
lumIfAmplifierGroups = _LumIfAmplifierGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1)
)
_LumIfAmplifierCompl_ObjectIdentity = ObjectIdentity
lumIfAmplifierCompl = _LumIfAmplifierCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 2)
)
_LumIfAmplifierMIBObjects_ObjectIdentity = ObjectIdentity
lumIfAmplifierMIBObjects = _LumIfAmplifierMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2)
)
_IfAmplifierGeneral_ObjectIdentity = ObjectIdentity
ifAmplifierGeneral = _IfAmplifierGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1)
)
_IfAmplifierGeneralConfigLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralConfigLastChangeTime_Object = MibScalar
ifAmplifierGeneralConfigLastChangeTime = _IfAmplifierGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 1),
    _IfAmplifierGeneralConfigLastChangeTime_Type()
)
ifAmplifierGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralConfigLastChangeTime.setStatus("current")
_IfAmplifierGeneralStateLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralStateLastChangeTime_Object = MibScalar
ifAmplifierGeneralStateLastChangeTime = _IfAmplifierGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 2),
    _IfAmplifierGeneralStateLastChangeTime_Type()
)
ifAmplifierGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralStateLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Type = Unsigned32
_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Object = MibScalar
ifAmplifierGeneralIfAmplifierAmplifierTableSize = _IfAmplifierGeneralIfAmplifierAmplifierTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 3),
    _IfAmplifierGeneralIfAmplifierAmplifierTableSize_Type()
)
ifAmplifierGeneralIfAmplifierAmplifierTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierAmplifierTableSize.setStatus("current")
_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime = _IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 4),
    _IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime = _IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 5),
    _IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierModuleTableSize_Type = Unsigned32
_IfAmplifierGeneralIfAmplifierModuleTableSize_Object = MibScalar
ifAmplifierGeneralIfAmplifierModuleTableSize = _IfAmplifierGeneralIfAmplifierModuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 6),
    _IfAmplifierGeneralIfAmplifierModuleTableSize_Type()
)
ifAmplifierGeneralIfAmplifierModuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierModuleTableSize.setStatus("current")
_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime = _IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 7),
    _IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime = _IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 8),
    _IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierRamanTableSize_Type = Unsigned32
_IfAmplifierGeneralIfAmplifierRamanTableSize_Object = MibScalar
ifAmplifierGeneralIfAmplifierRamanTableSize = _IfAmplifierGeneralIfAmplifierRamanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 9),
    _IfAmplifierGeneralIfAmplifierRamanTableSize_Type()
)
ifAmplifierGeneralIfAmplifierRamanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierRamanTableSize.setStatus("current")
_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime = _IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 10),
    _IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime = _IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 11),
    _IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierEdfaTableSize_Type = Unsigned32
_IfAmplifierGeneralIfAmplifierEdfaTableSize_Object = MibScalar
ifAmplifierGeneralIfAmplifierEdfaTableSize = _IfAmplifierGeneralIfAmplifierEdfaTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 12),
    _IfAmplifierGeneralIfAmplifierEdfaTableSize_Type()
)
ifAmplifierGeneralIfAmplifierEdfaTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierEdfaTableSize.setStatus("current")
_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime = _IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 13),
    _IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime.setStatus("current")
_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Type = DateAndTime
_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Object = MibScalar
ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime = _IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 1, 14),
    _IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Type()
)
ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime.setStatus("current")
_IfAmplifierAmplifierList_ObjectIdentity = ObjectIdentity
ifAmplifierAmplifierList = _IfAmplifierAmplifierList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2)
)
_IfAmplifierAmplifierTable_Object = MibTable
ifAmplifierAmplifierTable = _IfAmplifierAmplifierTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierTable.setStatus("current")
_IfAmplifierAmplifierEntry_Object = MibTableRow
ifAmplifierAmplifierEntry = _IfAmplifierAmplifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1)
)
ifAmplifierAmplifierEntry.setIndexNames(
    (0, "LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierIndex"),
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierEntry.setStatus("current")
_IfAmplifierAmplifierIndex_Type = Unsigned32
_IfAmplifierAmplifierIndex_Object = MibTableColumn
ifAmplifierAmplifierIndex = _IfAmplifierAmplifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 1),
    _IfAmplifierAmplifierIndex_Type()
)
ifAmplifierAmplifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierIndex.setStatus("current")
_IfAmplifierAmplifierName_Type = MgmtNameString
_IfAmplifierAmplifierName_Object = MibTableColumn
ifAmplifierAmplifierName = _IfAmplifierAmplifierName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 2),
    _IfAmplifierAmplifierName_Type()
)
ifAmplifierAmplifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierName.setStatus("current")
_IfAmplifierAmplifierUId_Type = Unsigned32
_IfAmplifierAmplifierUId_Object = MibTableColumn
ifAmplifierAmplifierUId = _IfAmplifierAmplifierUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 3),
    _IfAmplifierAmplifierUId_Type()
)
ifAmplifierAmplifierUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierUId.setStatus("current")
_IfAmplifierAmplifierRxPower_Type = Signed32WithNA
_IfAmplifierAmplifierRxPower_Object = MibTableColumn
ifAmplifierAmplifierRxPower = _IfAmplifierAmplifierRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 4),
    _IfAmplifierAmplifierRxPower_Type()
)
ifAmplifierAmplifierRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierRxPower.setStatus("current")
_IfAmplifierAmplifierTxPower_Type = Signed32WithNA
_IfAmplifierAmplifierTxPower_Object = MibTableColumn
ifAmplifierAmplifierTxPower = _IfAmplifierAmplifierTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 5),
    _IfAmplifierAmplifierTxPower_Type()
)
ifAmplifierAmplifierTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierTxPower.setStatus("current")
_IfAmplifierAmplifierWantedGain_Type = Signed32WithNA
_IfAmplifierAmplifierWantedGain_Object = MibTableColumn
ifAmplifierAmplifierWantedGain = _IfAmplifierAmplifierWantedGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 6),
    _IfAmplifierAmplifierWantedGain_Type()
)
ifAmplifierAmplifierWantedGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierWantedGain.setStatus("current")
_IfAmplifierAmplifierActualGain_Type = Signed32WithNA
_IfAmplifierAmplifierActualGain_Object = MibTableColumn
ifAmplifierAmplifierActualGain = _IfAmplifierAmplifierActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 7),
    _IfAmplifierAmplifierActualGain_Type()
)
ifAmplifierAmplifierActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierActualGain.setStatus("current")


class _IfAmplifierAmplifierAdminStatus_Type(AdminStatusWithNA):
    """Custom type ifAmplifierAmplifierAdminStatus based on AdminStatusWithNA"""
    defaultValue = 1


_IfAmplifierAmplifierAdminStatus_Type.__name__ = "AdminStatusWithNA"
_IfAmplifierAmplifierAdminStatus_Object = MibTableColumn
ifAmplifierAmplifierAdminStatus = _IfAmplifierAmplifierAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 8),
    _IfAmplifierAmplifierAdminStatus_Type()
)
ifAmplifierAmplifierAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierAdminStatus.setStatus("current")


class _IfAmplifierAmplifierOperStatus_Type(OperStatusWithNA):
    """Custom type ifAmplifierAmplifierOperStatus based on OperStatusWithNA"""
    defaultValue = 1


_IfAmplifierAmplifierOperStatus_Type.__name__ = "OperStatusWithNA"
_IfAmplifierAmplifierOperStatus_Object = MibTableColumn
ifAmplifierAmplifierOperStatus = _IfAmplifierAmplifierOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 9),
    _IfAmplifierAmplifierOperStatus_Type()
)
ifAmplifierAmplifierOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierOperStatus.setStatus("current")
_IfAmplifierAmplifierMidStageLoss_Type = Signed32WithNA
_IfAmplifierAmplifierMidStageLoss_Object = MibTableColumn
ifAmplifierAmplifierMidStageLoss = _IfAmplifierAmplifierMidStageLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 10),
    _IfAmplifierAmplifierMidStageLoss_Type()
)
ifAmplifierAmplifierMidStageLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierMidStageLoss.setStatus("current")
_IfAmplifierAmplifierTxIfIndex_Type = Unsigned32
_IfAmplifierAmplifierTxIfIndex_Object = MibTableColumn
ifAmplifierAmplifierTxIfIndex = _IfAmplifierAmplifierTxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 11),
    _IfAmplifierAmplifierTxIfIndex_Type()
)
ifAmplifierAmplifierTxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierTxIfIndex.setStatus("current")
_IfAmplifierAmplifierRxIfIndex_Type = Unsigned32
_IfAmplifierAmplifierRxIfIndex_Object = MibTableColumn
ifAmplifierAmplifierRxIfIndex = _IfAmplifierAmplifierRxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 12),
    _IfAmplifierAmplifierRxIfIndex_Type()
)
ifAmplifierAmplifierRxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierRxIfIndex.setStatus("current")
_IfAmplifierAmplifierSubrack_Type = Unsigned32
_IfAmplifierAmplifierSubrack_Object = MibTableColumn
ifAmplifierAmplifierSubrack = _IfAmplifierAmplifierSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 13),
    _IfAmplifierAmplifierSubrack_Type()
)
ifAmplifierAmplifierSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierSubrack.setStatus("current")
_IfAmplifierAmplifierSlot_Type = Unsigned32
_IfAmplifierAmplifierSlot_Object = MibTableColumn
ifAmplifierAmplifierSlot = _IfAmplifierAmplifierSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 14),
    _IfAmplifierAmplifierSlot_Type()
)
ifAmplifierAmplifierSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierSlot.setStatus("current")
_IfAmplifierAmplifierOutputPowerFail_Type = FaultStatusWithNA
_IfAmplifierAmplifierOutputPowerFail_Object = MibTableColumn
ifAmplifierAmplifierOutputPowerFail = _IfAmplifierAmplifierOutputPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 15),
    _IfAmplifierAmplifierOutputPowerFail_Type()
)
ifAmplifierAmplifierOutputPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierOutputPowerFail.setStatus("current")
_IfAmplifierAmplifierSaturation_Type = FaultStatusWithNA
_IfAmplifierAmplifierSaturation_Object = MibTableColumn
ifAmplifierAmplifierSaturation = _IfAmplifierAmplifierSaturation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 16),
    _IfAmplifierAmplifierSaturation_Type()
)
ifAmplifierAmplifierSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierSaturation.setStatus("current")


class _IfAmplifierAmplifierFunctionalType_Type(Integer32):
    """Custom type ifAmplifierAmplifierFunctionalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("preAmp", 2),
          ("offLinePreAmp", 3),
          ("lineAmp", 4),
          ("booster", 5))
    )


_IfAmplifierAmplifierFunctionalType_Type.__name__ = "Integer32"
_IfAmplifierAmplifierFunctionalType_Object = MibTableColumn
ifAmplifierAmplifierFunctionalType = _IfAmplifierAmplifierFunctionalType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 17),
    _IfAmplifierAmplifierFunctionalType_Type()
)
ifAmplifierAmplifierFunctionalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierFunctionalType.setStatus("current")


class _IfAmplifierAmplifierDescr_Type(DisplayString):
    """Custom type ifAmplifierAmplifierDescr based on DisplayString"""
    defaultValue = OctetString("")


_IfAmplifierAmplifierDescr_Type.__name__ = "DisplayString"
_IfAmplifierAmplifierDescr_Object = MibTableColumn
ifAmplifierAmplifierDescr = _IfAmplifierAmplifierDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 2, 1, 1, 18),
    _IfAmplifierAmplifierDescr_Type()
)
ifAmplifierAmplifierDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierAmplifierDescr.setStatus("current")
_IfAmplifierModuleList_ObjectIdentity = ObjectIdentity
ifAmplifierModuleList = _IfAmplifierModuleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3)
)
_IfAmplifierModuleTable_Object = MibTable
ifAmplifierModuleTable = _IfAmplifierModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifAmplifierModuleTable.setStatus("current")
_IfAmplifierModuleEntry_Object = MibTableRow
ifAmplifierModuleEntry = _IfAmplifierModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1)
)
ifAmplifierModuleEntry.setIndexNames(
    (0, "LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleIndex"),
)
if mibBuilder.loadTexts:
    ifAmplifierModuleEntry.setStatus("current")
_IfAmplifierModuleIndex_Type = Unsigned32
_IfAmplifierModuleIndex_Object = MibTableColumn
ifAmplifierModuleIndex = _IfAmplifierModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 1),
    _IfAmplifierModuleIndex_Type()
)
ifAmplifierModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleIndex.setStatus("current")
_IfAmplifierModuleName_Type = MgmtNameString
_IfAmplifierModuleName_Object = MibTableColumn
ifAmplifierModuleName = _IfAmplifierModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 2),
    _IfAmplifierModuleName_Type()
)
ifAmplifierModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleName.setStatus("current")
_IfAmplifierModuleUId_Type = Unsigned32
_IfAmplifierModuleUId_Object = MibTableColumn
ifAmplifierModuleUId = _IfAmplifierModuleUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 3),
    _IfAmplifierModuleUId_Type()
)
ifAmplifierModuleUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleUId.setStatus("current")
_IfAmplifierModuleTemperature_Type = Integer32WithNA
_IfAmplifierModuleTemperature_Object = MibTableColumn
ifAmplifierModuleTemperature = _IfAmplifierModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 4),
    _IfAmplifierModuleTemperature_Type()
)
ifAmplifierModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleTemperature.setStatus("current")
_IfAmplifierModuleInfo_Type = DisplayString
_IfAmplifierModuleInfo_Object = MibTableColumn
ifAmplifierModuleInfo = _IfAmplifierModuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 5),
    _IfAmplifierModuleInfo_Type()
)
ifAmplifierModuleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleInfo.setStatus("current")
_IfAmplifierModuleHighModuleTemperature_Type = FaultStatusWithNA
_IfAmplifierModuleHighModuleTemperature_Object = MibTableColumn
ifAmplifierModuleHighModuleTemperature = _IfAmplifierModuleHighModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 6),
    _IfAmplifierModuleHighModuleTemperature_Type()
)
ifAmplifierModuleHighModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleHighModuleTemperature.setStatus("current")
_IfAmplifierModuleHighPumpCurrent_Type = FaultStatusWithNA
_IfAmplifierModuleHighPumpCurrent_Object = MibTableColumn
ifAmplifierModuleHighPumpCurrent = _IfAmplifierModuleHighPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 7),
    _IfAmplifierModuleHighPumpCurrent_Type()
)
ifAmplifierModuleHighPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleHighPumpCurrent.setStatus("current")
_IfAmplifierModuleHighPumpTemperature_Type = FaultStatusWithNA
_IfAmplifierModuleHighPumpTemperature_Object = MibTableColumn
ifAmplifierModuleHighPumpTemperature = _IfAmplifierModuleHighPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 8),
    _IfAmplifierModuleHighPumpTemperature_Type()
)
ifAmplifierModuleHighPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleHighPumpTemperature.setStatus("current")
_IfAmplifierModuleCommunicationFailure_Type = FaultStatusWithNA
_IfAmplifierModuleCommunicationFailure_Object = MibTableColumn
ifAmplifierModuleCommunicationFailure = _IfAmplifierModuleCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 9),
    _IfAmplifierModuleCommunicationFailure_Type()
)
ifAmplifierModuleCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleCommunicationFailure.setStatus("current")


class _IfAmplifierModuleColdRestart_Type(Integer32):
    """Custom type ifAmplifierModuleColdRestart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doSoftwareColdRestart", 1),
          ("doNotSoftwareColdRestart", 2))
    )


_IfAmplifierModuleColdRestart_Type.__name__ = "Integer32"
_IfAmplifierModuleColdRestart_Object = MibTableColumn
ifAmplifierModuleColdRestart = _IfAmplifierModuleColdRestart_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 10),
    _IfAmplifierModuleColdRestart_Type()
)
ifAmplifierModuleColdRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierModuleColdRestart.setStatus("current")
_IfAmplifierModuleSubrack_Type = Unsigned32
_IfAmplifierModuleSubrack_Object = MibTableColumn
ifAmplifierModuleSubrack = _IfAmplifierModuleSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 11),
    _IfAmplifierModuleSubrack_Type()
)
ifAmplifierModuleSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleSubrack.setStatus("current")
_IfAmplifierModuleSlot_Type = Unsigned32
_IfAmplifierModuleSlot_Object = MibTableColumn
ifAmplifierModuleSlot = _IfAmplifierModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 3, 1, 1, 12),
    _IfAmplifierModuleSlot_Type()
)
ifAmplifierModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierModuleSlot.setStatus("current")
_IfAmplifierRamanList_ObjectIdentity = ObjectIdentity
ifAmplifierRamanList = _IfAmplifierRamanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4)
)
_IfAmplifierRamanTable_Object = MibTable
ifAmplifierRamanTable = _IfAmplifierRamanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifAmplifierRamanTable.setStatus("current")
_IfAmplifierRamanEntry_Object = MibTableRow
ifAmplifierRamanEntry = _IfAmplifierRamanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1)
)
ifAmplifierRamanEntry.setIndexNames(
    (0, "LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanIndex"),
)
if mibBuilder.loadTexts:
    ifAmplifierRamanEntry.setStatus("current")
_IfAmplifierRamanIndex_Type = Unsigned32
_IfAmplifierRamanIndex_Object = MibTableColumn
ifAmplifierRamanIndex = _IfAmplifierRamanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 1),
    _IfAmplifierRamanIndex_Type()
)
ifAmplifierRamanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanIndex.setStatus("current")
_IfAmplifierRamanName_Type = MgmtNameString
_IfAmplifierRamanName_Object = MibTableColumn
ifAmplifierRamanName = _IfAmplifierRamanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 2),
    _IfAmplifierRamanName_Type()
)
ifAmplifierRamanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanName.setStatus("current")
_IfAmplifierRamanUId_Type = Unsigned32
_IfAmplifierRamanUId_Object = MibTableColumn
ifAmplifierRamanUId = _IfAmplifierRamanUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 3),
    _IfAmplifierRamanUId_Type()
)
ifAmplifierRamanUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanUId.setStatus("current")


class _IfAmplifierRamanLineFiberType_Type(Integer32):
    """Custom type ifAmplifierRamanLineFiberType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ftG652", 1),
          ("ftG655", 2),
          ("notApplicable", 2147483647))
    )


_IfAmplifierRamanLineFiberType_Type.__name__ = "Integer32"
_IfAmplifierRamanLineFiberType_Object = MibTableColumn
ifAmplifierRamanLineFiberType = _IfAmplifierRamanLineFiberType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 4),
    _IfAmplifierRamanLineFiberType_Type()
)
ifAmplifierRamanLineFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAmplifierRamanLineFiberType.setStatus("current")


class _IfAmplifierRamanWantedGainTilt_Type(Signed32WithNA):
    """Custom type ifAmplifierRamanWantedGainTilt based on Signed32WithNA"""
    defaultValue = 0

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 5),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfAmplifierRamanWantedGainTilt_Type.__name__ = "Signed32WithNA"
_IfAmplifierRamanWantedGainTilt_Object = MibTableColumn
ifAmplifierRamanWantedGainTilt = _IfAmplifierRamanWantedGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 5),
    _IfAmplifierRamanWantedGainTilt_Type()
)
ifAmplifierRamanWantedGainTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierRamanWantedGainTilt.setStatus("current")
_IfAmplifierRamanReceivedPowerLevel_Type = Signed32WithNA
_IfAmplifierRamanReceivedPowerLevel_Object = MibTableColumn
ifAmplifierRamanReceivedPowerLevel = _IfAmplifierRamanReceivedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 6),
    _IfAmplifierRamanReceivedPowerLevel_Type()
)
ifAmplifierRamanReceivedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanReceivedPowerLevel.setStatus("current")
_IfAmplifierRamanPump1Power_Type = Signed32WithNA
_IfAmplifierRamanPump1Power_Object = MibTableColumn
ifAmplifierRamanPump1Power = _IfAmplifierRamanPump1Power_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 7),
    _IfAmplifierRamanPump1Power_Type()
)
ifAmplifierRamanPump1Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanPump1Power.setStatus("current")


class _IfAmplifierRamanPump1Status_Type(Integer32):
    """Custom type ifAmplifierRamanPump1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )


_IfAmplifierRamanPump1Status_Type.__name__ = "Integer32"
_IfAmplifierRamanPump1Status_Object = MibTableColumn
ifAmplifierRamanPump1Status = _IfAmplifierRamanPump1Status_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 8),
    _IfAmplifierRamanPump1Status_Type()
)
ifAmplifierRamanPump1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanPump1Status.setStatus("current")
_IfAmplifierRamanPump2Power_Type = Signed32WithNA
_IfAmplifierRamanPump2Power_Object = MibTableColumn
ifAmplifierRamanPump2Power = _IfAmplifierRamanPump2Power_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 9),
    _IfAmplifierRamanPump2Power_Type()
)
ifAmplifierRamanPump2Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanPump2Power.setStatus("current")


class _IfAmplifierRamanPump2Status_Type(Integer32):
    """Custom type ifAmplifierRamanPump2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )


_IfAmplifierRamanPump2Status_Type.__name__ = "Integer32"
_IfAmplifierRamanPump2Status_Object = MibTableColumn
ifAmplifierRamanPump2Status = _IfAmplifierRamanPump2Status_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 10),
    _IfAmplifierRamanPump2Status_Type()
)
ifAmplifierRamanPump2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanPump2Status.setStatus("current")
_IfAmplifierRamanTotalPumpPower_Type = Signed32WithNA
_IfAmplifierRamanTotalPumpPower_Object = MibTableColumn
ifAmplifierRamanTotalPumpPower = _IfAmplifierRamanTotalPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 11),
    _IfAmplifierRamanTotalPumpPower_Type()
)
ifAmplifierRamanTotalPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanTotalPumpPower.setStatus("current")
_IfAmplifierRamanBackReflectionPower_Type = Signed32WithNA
_IfAmplifierRamanBackReflectionPower_Object = MibTableColumn
ifAmplifierRamanBackReflectionPower = _IfAmplifierRamanBackReflectionPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 12),
    _IfAmplifierRamanBackReflectionPower_Type()
)
ifAmplifierRamanBackReflectionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanBackReflectionPower.setStatus("current")
_IfAmplifierRamanBackReflectionPowerRatio_Type = Signed32WithNA
_IfAmplifierRamanBackReflectionPowerRatio_Object = MibTableColumn
ifAmplifierRamanBackReflectionPowerRatio = _IfAmplifierRamanBackReflectionPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 13),
    _IfAmplifierRamanBackReflectionPowerRatio_Type()
)
ifAmplifierRamanBackReflectionPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanBackReflectionPowerRatio.setStatus("current")
_IfAmplifierRamanHighBackReflection_Type = FaultStatusWithNA
_IfAmplifierRamanHighBackReflection_Object = MibTableColumn
ifAmplifierRamanHighBackReflection = _IfAmplifierRamanHighBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 14),
    _IfAmplifierRamanHighBackReflection_Type()
)
ifAmplifierRamanHighBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanHighBackReflection.setStatus("current")


class _IfAmplifierRamanHighBackReflectionThld_Type(Signed32WithNA):
    """Custom type ifAmplifierRamanHighBackReflectionThld based on Signed32WithNA"""
    defaultValue = 260

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 280),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfAmplifierRamanHighBackReflectionThld_Type.__name__ = "Signed32WithNA"
_IfAmplifierRamanHighBackReflectionThld_Object = MibTableColumn
ifAmplifierRamanHighBackReflectionThld = _IfAmplifierRamanHighBackReflectionThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 15),
    _IfAmplifierRamanHighBackReflectionThld_Type()
)
ifAmplifierRamanHighBackReflectionThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierRamanHighBackReflectionThld.setStatus("current")
_IfAmplifierRamanPointInsertionLoss_Type = Signed32WithNA
_IfAmplifierRamanPointInsertionLoss_Object = MibTableColumn
ifAmplifierRamanPointInsertionLoss = _IfAmplifierRamanPointInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 16),
    _IfAmplifierRamanPointInsertionLoss_Type()
)
ifAmplifierRamanPointInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanPointInsertionLoss.setStatus("current")


class _IfAmplifierRamanPointInsertionLossThld_Type(Signed32WithNA):
    """Custom type ifAmplifierRamanPointInsertionLossThld based on Signed32WithNA"""
    defaultValue = -10


_IfAmplifierRamanPointInsertionLossThld_Type.__name__ = "Signed32WithNA"
_IfAmplifierRamanPointInsertionLossThld_Object = MibTableColumn
ifAmplifierRamanPointInsertionLossThld = _IfAmplifierRamanPointInsertionLossThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 17),
    _IfAmplifierRamanPointInsertionLossThld_Type()
)
ifAmplifierRamanPointInsertionLossThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierRamanPointInsertionLossThld.setStatus("current")
_IfAmplifierRamanHighPointInsertionLoss_Type = FaultStatusWithNA
_IfAmplifierRamanHighPointInsertionLoss_Object = MibTableColumn
ifAmplifierRamanHighPointInsertionLoss = _IfAmplifierRamanHighPointInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 18),
    _IfAmplifierRamanHighPointInsertionLoss_Type()
)
ifAmplifierRamanHighPointInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanHighPointInsertionLoss.setStatus("current")
_IfAmplifierRamanRelatedAmplifierIndex_Type = Unsigned32
_IfAmplifierRamanRelatedAmplifierIndex_Object = MibTableColumn
ifAmplifierRamanRelatedAmplifierIndex = _IfAmplifierRamanRelatedAmplifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 19),
    _IfAmplifierRamanRelatedAmplifierIndex_Type()
)
ifAmplifierRamanRelatedAmplifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanRelatedAmplifierIndex.setStatus("current")
_IfAmplifierRamanSubrack_Type = Unsigned32
_IfAmplifierRamanSubrack_Object = MibTableColumn
ifAmplifierRamanSubrack = _IfAmplifierRamanSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 20),
    _IfAmplifierRamanSubrack_Type()
)
ifAmplifierRamanSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanSubrack.setStatus("current")
_IfAmplifierRamanSlot_Type = Unsigned32
_IfAmplifierRamanSlot_Object = MibTableColumn
ifAmplifierRamanSlot = _IfAmplifierRamanSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 21),
    _IfAmplifierRamanSlot_Type()
)
ifAmplifierRamanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanSlot.setStatus("current")
_IfAmplifierRamanActualGain_Type = Signed32WithNA
_IfAmplifierRamanActualGain_Object = MibTableColumn
ifAmplifierRamanActualGain = _IfAmplifierRamanActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 4, 1, 1, 22),
    _IfAmplifierRamanActualGain_Type()
)
ifAmplifierRamanActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierRamanActualGain.setStatus("current")
_IfAmplifierEdfaList_ObjectIdentity = ObjectIdentity
ifAmplifierEdfaList = _IfAmplifierEdfaList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5)
)
_IfAmplifierEdfaTable_Object = MibTable
ifAmplifierEdfaTable = _IfAmplifierEdfaTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ifAmplifierEdfaTable.setStatus("current")
_IfAmplifierEdfaEntry_Object = MibTableRow
ifAmplifierEdfaEntry = _IfAmplifierEdfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1)
)
ifAmplifierEdfaEntry.setIndexNames(
    (0, "LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaIndex"),
)
if mibBuilder.loadTexts:
    ifAmplifierEdfaEntry.setStatus("current")
_IfAmplifierEdfaIndex_Type = Unsigned32
_IfAmplifierEdfaIndex_Object = MibTableColumn
ifAmplifierEdfaIndex = _IfAmplifierEdfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 1),
    _IfAmplifierEdfaIndex_Type()
)
ifAmplifierEdfaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaIndex.setStatus("current")
_IfAmplifierEdfaName_Type = MgmtNameString
_IfAmplifierEdfaName_Object = MibTableColumn
ifAmplifierEdfaName = _IfAmplifierEdfaName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 2),
    _IfAmplifierEdfaName_Type()
)
ifAmplifierEdfaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaName.setStatus("current")
_IfAmplifierEdfaUId_Type = Unsigned32
_IfAmplifierEdfaUId_Object = MibTableColumn
ifAmplifierEdfaUId = _IfAmplifierEdfaUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 3),
    _IfAmplifierEdfaUId_Type()
)
ifAmplifierEdfaUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaUId.setStatus("current")


class _IfAmplifierEdfaWantedGainTilt_Type(Signed32WithNA):
    """Custom type ifAmplifierEdfaWantedGainTilt based on Signed32WithNA"""
    defaultValue = -10

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfAmplifierEdfaWantedGainTilt_Type.__name__ = "Signed32WithNA"
_IfAmplifierEdfaWantedGainTilt_Object = MibTableColumn
ifAmplifierEdfaWantedGainTilt = _IfAmplifierEdfaWantedGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 4),
    _IfAmplifierEdfaWantedGainTilt_Type()
)
ifAmplifierEdfaWantedGainTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierEdfaWantedGainTilt.setStatus("current")
_IfAmplifierEdfaTxPowerLimit_Type = Signed32WithNA
_IfAmplifierEdfaTxPowerLimit_Object = MibTableColumn
ifAmplifierEdfaTxPowerLimit = _IfAmplifierEdfaTxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 5),
    _IfAmplifierEdfaTxPowerLimit_Type()
)
ifAmplifierEdfaTxPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierEdfaTxPowerLimit.setStatus("current")


class _IfAmplifierEdfaPumpStatus_Type(Integer32):
    """Custom type ifAmplifierEdfaPumpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2147483646)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 2147483646))
    )


_IfAmplifierEdfaPumpStatus_Type.__name__ = "Integer32"
_IfAmplifierEdfaPumpStatus_Object = MibTableColumn
ifAmplifierEdfaPumpStatus = _IfAmplifierEdfaPumpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 6),
    _IfAmplifierEdfaPumpStatus_Type()
)
ifAmplifierEdfaPumpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaPumpStatus.setStatus("current")
_IfAmplifierEdfaBackReflectionPower_Type = Signed32WithNA
_IfAmplifierEdfaBackReflectionPower_Object = MibTableColumn
ifAmplifierEdfaBackReflectionPower = _IfAmplifierEdfaBackReflectionPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 7),
    _IfAmplifierEdfaBackReflectionPower_Type()
)
ifAmplifierEdfaBackReflectionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaBackReflectionPower.setStatus("current")
_IfAmplifierEdfaBackReflectionPowerRatio_Type = Signed32WithNA
_IfAmplifierEdfaBackReflectionPowerRatio_Object = MibTableColumn
ifAmplifierEdfaBackReflectionPowerRatio = _IfAmplifierEdfaBackReflectionPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 8),
    _IfAmplifierEdfaBackReflectionPowerRatio_Type()
)
ifAmplifierEdfaBackReflectionPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaBackReflectionPowerRatio.setStatus("current")
_IfAmplifierEdfaHighBackReflection_Type = FaultStatusWithNA
_IfAmplifierEdfaHighBackReflection_Object = MibTableColumn
ifAmplifierEdfaHighBackReflection = _IfAmplifierEdfaHighBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 9),
    _IfAmplifierEdfaHighBackReflection_Type()
)
ifAmplifierEdfaHighBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaHighBackReflection.setStatus("current")


class _IfAmplifierEdfaHighBackReflectionThld_Type(Signed32WithNA):
    """Custom type ifAmplifierEdfaHighBackReflectionThld based on Signed32WithNA"""
    defaultValue = 260

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 280),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfAmplifierEdfaHighBackReflectionThld_Type.__name__ = "Signed32WithNA"
_IfAmplifierEdfaHighBackReflectionThld_Object = MibTableColumn
ifAmplifierEdfaHighBackReflectionThld = _IfAmplifierEdfaHighBackReflectionThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 10),
    _IfAmplifierEdfaHighBackReflectionThld_Type()
)
ifAmplifierEdfaHighBackReflectionThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAmplifierEdfaHighBackReflectionThld.setStatus("current")
_IfAmplifierEdfaSaturation_Type = FaultStatusWithNA
_IfAmplifierEdfaSaturation_Object = MibTableColumn
ifAmplifierEdfaSaturation = _IfAmplifierEdfaSaturation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 11),
    _IfAmplifierEdfaSaturation_Type()
)
ifAmplifierEdfaSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaSaturation.setStatus("deprecated")
_IfAmplifierEdfaMonitorPortLoss_Type = Signed32WithNA
_IfAmplifierEdfaMonitorPortLoss_Object = MibTableColumn
ifAmplifierEdfaMonitorPortLoss = _IfAmplifierEdfaMonitorPortLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 12),
    _IfAmplifierEdfaMonitorPortLoss_Type()
)
ifAmplifierEdfaMonitorPortLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaMonitorPortLoss.setStatus("current")
_IfAmplifierEdfaRelatedAmplifierIndex_Type = Unsigned32
_IfAmplifierEdfaRelatedAmplifierIndex_Object = MibTableColumn
ifAmplifierEdfaRelatedAmplifierIndex = _IfAmplifierEdfaRelatedAmplifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 13),
    _IfAmplifierEdfaRelatedAmplifierIndex_Type()
)
ifAmplifierEdfaRelatedAmplifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaRelatedAmplifierIndex.setStatus("current")
_IfAmplifierEdfaSubrack_Type = Unsigned32
_IfAmplifierEdfaSubrack_Object = MibTableColumn
ifAmplifierEdfaSubrack = _IfAmplifierEdfaSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 14),
    _IfAmplifierEdfaSubrack_Type()
)
ifAmplifierEdfaSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaSubrack.setStatus("current")
_IfAmplifierEdfaSlot_Type = Unsigned32
_IfAmplifierEdfaSlot_Object = MibTableColumn
ifAmplifierEdfaSlot = _IfAmplifierEdfaSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 15),
    _IfAmplifierEdfaSlot_Type()
)
ifAmplifierEdfaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaSlot.setStatus("current")
_IfAmplifierEdfaPumpPower_Type = Signed32WithNA
_IfAmplifierEdfaPumpPower_Object = MibTableColumn
ifAmplifierEdfaPumpPower = _IfAmplifierEdfaPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 16),
    _IfAmplifierEdfaPumpPower_Type()
)
ifAmplifierEdfaPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaPumpPower.setStatus("current")
_IfAmplifierEdfaPumpCurrent_Type = Signed32WithNA
_IfAmplifierEdfaPumpCurrent_Object = MibTableColumn
ifAmplifierEdfaPumpCurrent = _IfAmplifierEdfaPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 17),
    _IfAmplifierEdfaPumpCurrent_Type()
)
ifAmplifierEdfaPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaPumpCurrent.setStatus("current")
_IfAmplifierEdfaActualGain_Type = Signed32WithNA
_IfAmplifierEdfaActualGain_Object = MibTableColumn
ifAmplifierEdfaActualGain = _IfAmplifierEdfaActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 2, 5, 1, 1, 18),
    _IfAmplifierEdfaActualGain_Type()
)
ifAmplifierEdfaActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAmplifierEdfaActualGain.setStatus("current")

# Managed Objects groups

ifAmplifierGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 1)
)
ifAmplifierGeneralGroupV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralConfigLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralStateLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierAmplifierTableSize"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierModuleTableSize"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierRamanTableSize"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierEdfaTableSize"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifAmplifierGeneralGroupV1.setStatus("current")

ifAmplifierAmplifierGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 2)
)
ifAmplifierAmplifierGroupV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierWantedGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierActualGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierAdminStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOperStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierMidStageLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSlot"))
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierGroupV1.setStatus("deprecated")

ifAmplifierModuleGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 3)
)
ifAmplifierModuleGroupV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleTemperature"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleInfo"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleHighModuleTemperature"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleHighPumpCurrent"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleHighPumpTemperature"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleCommunicationFailure"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleColdRestart"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleSlot"))
)
if mibBuilder.loadTexts:
    ifAmplifierModuleGroupV1.setStatus("current")

ifAmplifierRamanGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 4)
)
ifAmplifierRamanGroupV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanLineFiberType"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanWantedGainTilt"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanReceivedPowerLevel"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump1Power"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump1Status"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump2Power"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump2Status"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanTotalPumpPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanBackReflectionPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanBackReflectionPowerRatio"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighBackReflection"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighBackReflectionThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPointInsertionLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPointInsertionLossThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighPointInsertionLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanRelatedAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanSlot"))
)
if mibBuilder.loadTexts:
    ifAmplifierRamanGroupV1.setStatus("deprecated")

ifAmplifierEdfaGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 5)
)
ifAmplifierEdfaGroupV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaWantedGainTilt"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaTxPowerLimit"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPowerRatio"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflection"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflectionThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSaturation"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaMonitorPortLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaRelatedAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSlot"))
)
if mibBuilder.loadTexts:
    ifAmplifierEdfaGroupV1.setStatus("deprecated")

ifAmplifierAmplifierGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 6)
)
ifAmplifierAmplifierGroupV2.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierWantedGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierActualGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierAdminStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOperStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierMidStageLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOutputPowerFail"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSaturation"))
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierGroupV2.setStatus("deprecated")

ifAmplifierEdfaGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 7)
)
ifAmplifierEdfaGroupV2.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaWantedGainTilt"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaTxPowerLimit"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPowerRatio"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflection"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflectionThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaMonitorPortLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaRelatedAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpCurrent"))
)
if mibBuilder.loadTexts:
    ifAmplifierEdfaGroupV2.setStatus("deprecated")

ifAmplifierRamanGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 8)
)
ifAmplifierRamanGroupV2.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanLineFiberType"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanWantedGainTilt"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanReceivedPowerLevel"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump1Power"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump1Status"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump2Power"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPump2Status"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanTotalPumpPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanBackReflectionPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanBackReflectionPowerRatio"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighBackReflection"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighBackReflectionThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPointInsertionLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanPointInsertionLossThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanHighPointInsertionLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanRelatedAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanActualGain"))
)
if mibBuilder.loadTexts:
    ifAmplifierRamanGroupV2.setStatus("current")

ifAmplifierEdfaGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 9)
)
ifAmplifierEdfaGroupV3.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaWantedGainTilt"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaTxPowerLimit"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaBackReflectionPowerRatio"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflection"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaHighBackReflectionThld"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaMonitorPortLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaRelatedAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaPumpCurrent"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaActualGain"))
)
if mibBuilder.loadTexts:
    ifAmplifierEdfaGroupV3.setStatus("current")

ifAmplifierAmplifierGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 10)
)
ifAmplifierAmplifierGroupV3.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierWantedGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierActualGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierAdminStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOperStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierMidStageLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOutputPowerFail"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSaturation"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierFunctionalType"))
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierGroupV3.setStatus("deprecated")

ifAmplifierAmplifierGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 1, 11)
)
ifAmplifierAmplifierGroupV4.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierName"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierUId"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxPower"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierWantedGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierActualGain"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierAdminStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOperStatus"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierMidStageLoss"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierTxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierRxIfIndex"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSubrack"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSlot"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierOutputPowerFail"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierSaturation"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierFunctionalType"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierDescr"))
)
if mibBuilder.loadTexts:
    ifAmplifierAmplifierGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfAmplifierComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 2, 1)
)
lumIfAmplifierComplV1.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfAmplifierComplV1.setStatus(
        "deprecated"
    )

lumIfAmplifierComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 2, 2)
)
lumIfAmplifierComplV2.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierGroupV2"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfAmplifierComplV2.setStatus(
        "deprecated"
    )

lumIfAmplifierComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 2, 3)
)
lumIfAmplifierComplV3.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierGroupV3"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanGroupV2"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfAmplifierComplV3.setStatus(
        "deprecated"
    )

lumIfAmplifierComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65, 1, 2, 4)
)
lumIfAmplifierComplV4.setObjects(
      *(("LUM-IFAMPLIFIER-MIB", "ifAmplifierGeneralGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierAmplifierGroupV4"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierModuleGroupV1"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierRamanGroupV2"),
        ("LUM-IFAMPLIFIER-MIB", "ifAmplifierEdfaGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfAmplifierComplV4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFAMPLIFIER-MIB",
    **{"lumIfAmplifierMIBModule": lumIfAmplifierMIBModule,
       "lumIfAmplifierConfs": lumIfAmplifierConfs,
       "lumIfAmplifierGroups": lumIfAmplifierGroups,
       "ifAmplifierGeneralGroupV1": ifAmplifierGeneralGroupV1,
       "ifAmplifierAmplifierGroupV1": ifAmplifierAmplifierGroupV1,
       "ifAmplifierModuleGroupV1": ifAmplifierModuleGroupV1,
       "ifAmplifierRamanGroupV1": ifAmplifierRamanGroupV1,
       "ifAmplifierEdfaGroupV1": ifAmplifierEdfaGroupV1,
       "ifAmplifierAmplifierGroupV2": ifAmplifierAmplifierGroupV2,
       "ifAmplifierEdfaGroupV2": ifAmplifierEdfaGroupV2,
       "ifAmplifierRamanGroupV2": ifAmplifierRamanGroupV2,
       "ifAmplifierEdfaGroupV3": ifAmplifierEdfaGroupV3,
       "ifAmplifierAmplifierGroupV3": ifAmplifierAmplifierGroupV3,
       "ifAmplifierAmplifierGroupV4": ifAmplifierAmplifierGroupV4,
       "lumIfAmplifierCompl": lumIfAmplifierCompl,
       "lumIfAmplifierComplV1": lumIfAmplifierComplV1,
       "lumIfAmplifierComplV2": lumIfAmplifierComplV2,
       "lumIfAmplifierComplV3": lumIfAmplifierComplV3,
       "lumIfAmplifierComplV4": lumIfAmplifierComplV4,
       "lumIfAmplifierMIBObjects": lumIfAmplifierMIBObjects,
       "ifAmplifierGeneral": ifAmplifierGeneral,
       "ifAmplifierGeneralConfigLastChangeTime": ifAmplifierGeneralConfigLastChangeTime,
       "ifAmplifierGeneralStateLastChangeTime": ifAmplifierGeneralStateLastChangeTime,
       "ifAmplifierGeneralIfAmplifierAmplifierTableSize": ifAmplifierGeneralIfAmplifierAmplifierTableSize,
       "ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime": ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime,
       "ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime": ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime,
       "ifAmplifierGeneralIfAmplifierModuleTableSize": ifAmplifierGeneralIfAmplifierModuleTableSize,
       "ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime": ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime,
       "ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime": ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime,
       "ifAmplifierGeneralIfAmplifierRamanTableSize": ifAmplifierGeneralIfAmplifierRamanTableSize,
       "ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime": ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime,
       "ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime": ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime,
       "ifAmplifierGeneralIfAmplifierEdfaTableSize": ifAmplifierGeneralIfAmplifierEdfaTableSize,
       "ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime": ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime,
       "ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime": ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime,
       "ifAmplifierAmplifierList": ifAmplifierAmplifierList,
       "ifAmplifierAmplifierTable": ifAmplifierAmplifierTable,
       "ifAmplifierAmplifierEntry": ifAmplifierAmplifierEntry,
       "ifAmplifierAmplifierIndex": ifAmplifierAmplifierIndex,
       "ifAmplifierAmplifierName": ifAmplifierAmplifierName,
       "ifAmplifierAmplifierUId": ifAmplifierAmplifierUId,
       "ifAmplifierAmplifierRxPower": ifAmplifierAmplifierRxPower,
       "ifAmplifierAmplifierTxPower": ifAmplifierAmplifierTxPower,
       "ifAmplifierAmplifierWantedGain": ifAmplifierAmplifierWantedGain,
       "ifAmplifierAmplifierActualGain": ifAmplifierAmplifierActualGain,
       "ifAmplifierAmplifierAdminStatus": ifAmplifierAmplifierAdminStatus,
       "ifAmplifierAmplifierOperStatus": ifAmplifierAmplifierOperStatus,
       "ifAmplifierAmplifierMidStageLoss": ifAmplifierAmplifierMidStageLoss,
       "ifAmplifierAmplifierTxIfIndex": ifAmplifierAmplifierTxIfIndex,
       "ifAmplifierAmplifierRxIfIndex": ifAmplifierAmplifierRxIfIndex,
       "ifAmplifierAmplifierSubrack": ifAmplifierAmplifierSubrack,
       "ifAmplifierAmplifierSlot": ifAmplifierAmplifierSlot,
       "ifAmplifierAmplifierOutputPowerFail": ifAmplifierAmplifierOutputPowerFail,
       "ifAmplifierAmplifierSaturation": ifAmplifierAmplifierSaturation,
       "ifAmplifierAmplifierFunctionalType": ifAmplifierAmplifierFunctionalType,
       "ifAmplifierAmplifierDescr": ifAmplifierAmplifierDescr,
       "ifAmplifierModuleList": ifAmplifierModuleList,
       "ifAmplifierModuleTable": ifAmplifierModuleTable,
       "ifAmplifierModuleEntry": ifAmplifierModuleEntry,
       "ifAmplifierModuleIndex": ifAmplifierModuleIndex,
       "ifAmplifierModuleName": ifAmplifierModuleName,
       "ifAmplifierModuleUId": ifAmplifierModuleUId,
       "ifAmplifierModuleTemperature": ifAmplifierModuleTemperature,
       "ifAmplifierModuleInfo": ifAmplifierModuleInfo,
       "ifAmplifierModuleHighModuleTemperature": ifAmplifierModuleHighModuleTemperature,
       "ifAmplifierModuleHighPumpCurrent": ifAmplifierModuleHighPumpCurrent,
       "ifAmplifierModuleHighPumpTemperature": ifAmplifierModuleHighPumpTemperature,
       "ifAmplifierModuleCommunicationFailure": ifAmplifierModuleCommunicationFailure,
       "ifAmplifierModuleColdRestart": ifAmplifierModuleColdRestart,
       "ifAmplifierModuleSubrack": ifAmplifierModuleSubrack,
       "ifAmplifierModuleSlot": ifAmplifierModuleSlot,
       "ifAmplifierRamanList": ifAmplifierRamanList,
       "ifAmplifierRamanTable": ifAmplifierRamanTable,
       "ifAmplifierRamanEntry": ifAmplifierRamanEntry,
       "ifAmplifierRamanIndex": ifAmplifierRamanIndex,
       "ifAmplifierRamanName": ifAmplifierRamanName,
       "ifAmplifierRamanUId": ifAmplifierRamanUId,
       "ifAmplifierRamanLineFiberType": ifAmplifierRamanLineFiberType,
       "ifAmplifierRamanWantedGainTilt": ifAmplifierRamanWantedGainTilt,
       "ifAmplifierRamanReceivedPowerLevel": ifAmplifierRamanReceivedPowerLevel,
       "ifAmplifierRamanPump1Power": ifAmplifierRamanPump1Power,
       "ifAmplifierRamanPump1Status": ifAmplifierRamanPump1Status,
       "ifAmplifierRamanPump2Power": ifAmplifierRamanPump2Power,
       "ifAmplifierRamanPump2Status": ifAmplifierRamanPump2Status,
       "ifAmplifierRamanTotalPumpPower": ifAmplifierRamanTotalPumpPower,
       "ifAmplifierRamanBackReflectionPower": ifAmplifierRamanBackReflectionPower,
       "ifAmplifierRamanBackReflectionPowerRatio": ifAmplifierRamanBackReflectionPowerRatio,
       "ifAmplifierRamanHighBackReflection": ifAmplifierRamanHighBackReflection,
       "ifAmplifierRamanHighBackReflectionThld": ifAmplifierRamanHighBackReflectionThld,
       "ifAmplifierRamanPointInsertionLoss": ifAmplifierRamanPointInsertionLoss,
       "ifAmplifierRamanPointInsertionLossThld": ifAmplifierRamanPointInsertionLossThld,
       "ifAmplifierRamanHighPointInsertionLoss": ifAmplifierRamanHighPointInsertionLoss,
       "ifAmplifierRamanRelatedAmplifierIndex": ifAmplifierRamanRelatedAmplifierIndex,
       "ifAmplifierRamanSubrack": ifAmplifierRamanSubrack,
       "ifAmplifierRamanSlot": ifAmplifierRamanSlot,
       "ifAmplifierRamanActualGain": ifAmplifierRamanActualGain,
       "ifAmplifierEdfaList": ifAmplifierEdfaList,
       "ifAmplifierEdfaTable": ifAmplifierEdfaTable,
       "ifAmplifierEdfaEntry": ifAmplifierEdfaEntry,
       "ifAmplifierEdfaIndex": ifAmplifierEdfaIndex,
       "ifAmplifierEdfaName": ifAmplifierEdfaName,
       "ifAmplifierEdfaUId": ifAmplifierEdfaUId,
       "ifAmplifierEdfaWantedGainTilt": ifAmplifierEdfaWantedGainTilt,
       "ifAmplifierEdfaTxPowerLimit": ifAmplifierEdfaTxPowerLimit,
       "ifAmplifierEdfaPumpStatus": ifAmplifierEdfaPumpStatus,
       "ifAmplifierEdfaBackReflectionPower": ifAmplifierEdfaBackReflectionPower,
       "ifAmplifierEdfaBackReflectionPowerRatio": ifAmplifierEdfaBackReflectionPowerRatio,
       "ifAmplifierEdfaHighBackReflection": ifAmplifierEdfaHighBackReflection,
       "ifAmplifierEdfaHighBackReflectionThld": ifAmplifierEdfaHighBackReflectionThld,
       "ifAmplifierEdfaSaturation": ifAmplifierEdfaSaturation,
       "ifAmplifierEdfaMonitorPortLoss": ifAmplifierEdfaMonitorPortLoss,
       "ifAmplifierEdfaRelatedAmplifierIndex": ifAmplifierEdfaRelatedAmplifierIndex,
       "ifAmplifierEdfaSubrack": ifAmplifierEdfaSubrack,
       "ifAmplifierEdfaSlot": ifAmplifierEdfaSlot,
       "ifAmplifierEdfaPumpPower": ifAmplifierEdfaPumpPower,
       "ifAmplifierEdfaPumpCurrent": ifAmplifierEdfaPumpCurrent,
       "ifAmplifierEdfaActualGain": ifAmplifierEdfaActualGain}
)
