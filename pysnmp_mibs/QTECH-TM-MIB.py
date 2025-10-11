# SNMP MIB module (QTECH-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:14 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechTMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91)
)
if mibBuilder.loadTexts:
    qtechTMMIB.setRevisions(
        ("2010-12-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechTMMIBObjects_ObjectIdentity = ObjectIdentity
qtechTMMIBObjects = _QtechTMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1)
)
_QtechTMQosDramMIBObjects_ObjectIdentity = ObjectIdentity
qtechTMQosDramMIBObjects = _QtechTMQosDramMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1)
)
_QtechQosDramTable_Object = MibTable
qtechQosDramTable = _QtechQosDramTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechQosDramTable.setStatus("current")
_QtechQosDramEntry_Object = MibTableRow
qtechQosDramEntry = _QtechQosDramEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1, 1, 1)
)
qtechQosDramEntry.setIndexNames(
    (0, "QTECH-TM-MIB", "qtechQoSDramIndex"),
)
if mibBuilder.loadTexts:
    qtechQosDramEntry.setStatus("current")
_QtechQoSDramIndex_Type = Integer32
_QtechQoSDramIndex_Object = MibTableColumn
qtechQoSDramIndex = _QtechQoSDramIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1, 1, 1, 1),
    _QtechQoSDramIndex_Type()
)
qtechQoSDramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSDramIndex.setStatus("current")
_QtechQosDramTotal_Type = Integer32
_QtechQosDramTotal_Object = MibTableColumn
qtechQosDramTotal = _QtechQosDramTotal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1, 1, 1, 2),
    _QtechQosDramTotal_Type()
)
qtechQosDramTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQosDramTotal.setStatus("current")
_QtechQosDramCurUsed_Type = Integer32
_QtechQosDramCurUsed_Object = MibTableColumn
qtechQosDramCurUsed = _QtechQosDramCurUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 1, 1, 1, 3),
    _QtechQosDramCurUsed_Type()
)
qtechQosDramCurUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQosDramCurUsed.setStatus("current")
_QtechTMQosDropMIBObjects_ObjectIdentity = ObjectIdentity
qtechTMQosDropMIBObjects = _QtechTMQosDropMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2)
)
_QtechQosDropTable_Object = MibTable
qtechQosDropTable = _QtechQosDropTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechQosDropTable.setStatus("current")
_QtechQosDropEntry_Object = MibTableRow
qtechQosDropEntry = _QtechQosDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1)
)
qtechQosDropEntry.setIndexNames(
    (0, "QTECH-TM-MIB", "qtechQoSDropIndex"),
)
if mibBuilder.loadTexts:
    qtechQosDropEntry.setStatus("current")
_QtechQoSDropIndex_Type = Integer32
_QtechQoSDropIndex_Object = MibTableColumn
qtechQoSDropIndex = _QtechQoSDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 1),
    _QtechQoSDropIndex_Type()
)
qtechQoSDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSDropIndex.setStatus("current")
_QtechQoSTotalEnQue_Type = Integer32
_QtechQoSTotalEnQue_Object = MibTableColumn
qtechQoSTotalEnQue = _QtechQoSTotalEnQue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 2),
    _QtechQoSTotalEnQue_Type()
)
qtechQoSTotalEnQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSTotalEnQue.setStatus("current")
_QtechQoSTotalDeQue_Type = Integer32
_QtechQoSTotalDeQue_Object = MibTableColumn
qtechQoSTotalDeQue = _QtechQoSTotalDeQue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 3),
    _QtechQoSTotalDeQue_Type()
)
qtechQoSTotalDeQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSTotalDeQue.setStatus("current")
_QtechQoSEnQueDrop_Type = Integer32
_QtechQoSEnQueDrop_Object = MibTableColumn
qtechQoSEnQueDrop = _QtechQoSEnQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 4),
    _QtechQoSEnQueDrop_Type()
)
qtechQoSEnQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSEnQueDrop.setStatus("current")
_QtechQoSEnQueDropByBuf_Type = Integer32
_QtechQoSEnQueDropByBuf_Object = MibTableColumn
qtechQoSEnQueDropByBuf = _QtechQoSEnQueDropByBuf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 5),
    _QtechQoSEnQueDropByBuf_Type()
)
qtechQoSEnQueDropByBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSEnQueDropByBuf.setStatus("current")
_QtechQoSEnQueDropByBufDesc_Type = Integer32
_QtechQoSEnQueDropByBufDesc_Object = MibTableColumn
qtechQoSEnQueDropByBufDesc = _QtechQoSEnQueDropByBufDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 6),
    _QtechQoSEnQueDropByBufDesc_Type()
)
qtechQoSEnQueDropByBufDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSEnQueDropByBufDesc.setStatus("current")
_QtechQoSEnQueDropByOther_Type = Integer32
_QtechQoSEnQueDropByOther_Object = MibTableColumn
qtechQoSEnQueDropByOther = _QtechQoSEnQueDropByOther_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 7),
    _QtechQoSEnQueDropByOther_Type()
)
qtechQoSEnQueDropByOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSEnQueDropByOther.setStatus("current")
_QtechQoSDeQueDrop_Type = Integer32
_QtechQoSDeQueDrop_Object = MibTableColumn
qtechQoSDeQueDrop = _QtechQoSDeQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 8),
    _QtechQoSDeQueDrop_Type()
)
qtechQoSDeQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSDeQueDrop.setStatus("current")
_QtechQoSLastClearTime_Type = TimeTicks
_QtechQoSLastClearTime_Object = MibTableColumn
qtechQoSLastClearTime = _QtechQoSLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 2, 1, 1, 9),
    _QtechQoSLastClearTime_Type()
)
qtechQoSLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSLastClearTime.setStatus("current")
_QtechTMQosQueMIBObjects_ObjectIdentity = ObjectIdentity
qtechTMQosQueMIBObjects = _QtechTMQosQueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3)
)
_QtechQosQueTable_Object = MibTable
qtechQosQueTable = _QtechQosQueTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechQosQueTable.setStatus("current")
_QtechQosQueEntry_Object = MibTableRow
qtechQosQueEntry = _QtechQosQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1)
)
qtechQosQueEntry.setIndexNames(
    (0, "QTECH-TM-MIB", "qtechQoSIfIndex"),
    (0, "QTECH-TM-MIB", "qtechQoSIfChipIndex"),
    (0, "QTECH-TM-MIB", "qtechQoSIfChipQueIndex"),
)
if mibBuilder.loadTexts:
    qtechQosQueEntry.setStatus("current")
_QtechQoSIfIndex_Type = IfIndex
_QtechQoSIfIndex_Object = MibTableColumn
qtechQoSIfIndex = _QtechQoSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 1),
    _QtechQoSIfIndex_Type()
)
qtechQoSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfIndex.setStatus("current")


class _QtechQoSIfChipIndex_Type(Integer32):
    """Custom type qtechQoSIfChipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chip-0", 0),
          ("chip-1", 1))
    )


_QtechQoSIfChipIndex_Type.__name__ = "Integer32"
_QtechQoSIfChipIndex_Object = MibTableColumn
qtechQoSIfChipIndex = _QtechQoSIfChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 2),
    _QtechQoSIfChipIndex_Type()
)
qtechQoSIfChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipIndex.setStatus("current")


class _QtechQoSIfChipQueIndex_Type(Integer32):
    """Custom type qtechQoSIfChipQueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4),
          ("queue-5", 5),
          ("queue-6", 6),
          ("queue-7", 7),
          ("queue-8", 8))
    )


_QtechQoSIfChipQueIndex_Type.__name__ = "Integer32"
_QtechQoSIfChipQueIndex_Object = MibTableColumn
qtechQoSIfChipQueIndex = _QtechQoSIfChipQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 3),
    _QtechQoSIfChipQueIndex_Type()
)
qtechQoSIfChipQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipQueIndex.setStatus("current")
_QtechQoSIfChipMax_Type = Integer32
_QtechQoSIfChipMax_Object = MibTableColumn
qtechQoSIfChipMax = _QtechQoSIfChipMax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 4),
    _QtechQoSIfChipMax_Type()
)
qtechQoSIfChipMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipMax.setStatus("current")
_QtechQoSIfChipCur_Type = Integer32
_QtechQoSIfChipCur_Object = MibTableColumn
qtechQoSIfChipCur = _QtechQoSIfChipCur_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 5),
    _QtechQoSIfChipCur_Type()
)
qtechQoSIfChipCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipCur.setStatus("current")
_QtechQoSIfChipPeak_Type = Integer32
_QtechQoSIfChipPeak_Object = MibTableColumn
qtechQoSIfChipPeak = _QtechQoSIfChipPeak_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 6),
    _QtechQoSIfChipPeak_Type()
)
qtechQoSIfChipPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipPeak.setStatus("current")
_QtechQoSIfChipRate_Type = Integer32
_QtechQoSIfChipRate_Object = MibTableColumn
qtechQoSIfChipRate = _QtechQoSIfChipRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 7),
    _QtechQoSIfChipRate_Type()
)
qtechQoSIfChipRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipRate.setStatus("current")
_QtechQoSIfChipTime_Type = TimeTicks
_QtechQoSIfChipTime_Object = MibTableColumn
qtechQoSIfChipTime = _QtechQoSIfChipTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 1, 3, 1, 1, 8),
    _QtechQoSIfChipTime_Type()
)
qtechQoSIfChipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSIfChipTime.setStatus("current")
_QtechTMMIBConformance_ObjectIdentity = ObjectIdentity
qtechTMMIBConformance = _QtechTMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 2)
)
_QtechTMMIBCompliances_ObjectIdentity = ObjectIdentity
qtechTMMIBCompliances = _QtechTMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 2, 1)
)
_QtechTMMIBGroups_ObjectIdentity = ObjectIdentity
qtechTMMIBGroups = _QtechTMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 2, 2)
)

# Managed Objects groups

qtechTMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 2, 2, 1)
)
qtechTMMIBGroup.setObjects(
      *(("QTECH-TM-MIB", "qtechQoSDramIndex"),
        ("QTECH-TM-MIB", "qtechQosDramTotal"),
        ("QTECH-TM-MIB", "qtechQosDramCurUsed"),
        ("QTECH-TM-MIB", "qtechQoSDropIndex"),
        ("QTECH-TM-MIB", "qtechQoSTotalEnQue"),
        ("QTECH-TM-MIB", "qtechQoSTotalDeQue"),
        ("QTECH-TM-MIB", "qtechQoSEnQueDrop"),
        ("QTECH-TM-MIB", "qtechQoSEnQueDropByBuf"),
        ("QTECH-TM-MIB", "qtechQoSEnQueDropByBufDesc"),
        ("QTECH-TM-MIB", "qtechQoSEnQueDropByOther"),
        ("QTECH-TM-MIB", "qtechQoSDeQueDrop"),
        ("QTECH-TM-MIB", "qtechQoSLastClearTime"),
        ("QTECH-TM-MIB", "qtechQoSIfIndex"),
        ("QTECH-TM-MIB", "qtechQoSIfChipIndex"),
        ("QTECH-TM-MIB", "qtechQoSIfChipQueIndex"),
        ("QTECH-TM-MIB", "qtechQoSIfChipMax"),
        ("QTECH-TM-MIB", "qtechQoSIfChipCur"),
        ("QTECH-TM-MIB", "qtechQoSIfChipPeak"),
        ("QTECH-TM-MIB", "qtechQoSIfChipRate"),
        ("QTECH-TM-MIB", "qtechQoSIfChipTime"))
)
if mibBuilder.loadTexts:
    qtechTMMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechTMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 91, 2, 1, 1)
)
qtechTMMIBCompliance.setObjects(
    ("QTECH-TM-MIB", "qtechTMMIBGroup")
)
if mibBuilder.loadTexts:
    qtechTMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TM-MIB",
    **{"qtechTMMIB": qtechTMMIB,
       "qtechTMMIBObjects": qtechTMMIBObjects,
       "qtechTMQosDramMIBObjects": qtechTMQosDramMIBObjects,
       "qtechQosDramTable": qtechQosDramTable,
       "qtechQosDramEntry": qtechQosDramEntry,
       "qtechQoSDramIndex": qtechQoSDramIndex,
       "qtechQosDramTotal": qtechQosDramTotal,
       "qtechQosDramCurUsed": qtechQosDramCurUsed,
       "qtechTMQosDropMIBObjects": qtechTMQosDropMIBObjects,
       "qtechQosDropTable": qtechQosDropTable,
       "qtechQosDropEntry": qtechQosDropEntry,
       "qtechQoSDropIndex": qtechQoSDropIndex,
       "qtechQoSTotalEnQue": qtechQoSTotalEnQue,
       "qtechQoSTotalDeQue": qtechQoSTotalDeQue,
       "qtechQoSEnQueDrop": qtechQoSEnQueDrop,
       "qtechQoSEnQueDropByBuf": qtechQoSEnQueDropByBuf,
       "qtechQoSEnQueDropByBufDesc": qtechQoSEnQueDropByBufDesc,
       "qtechQoSEnQueDropByOther": qtechQoSEnQueDropByOther,
       "qtechQoSDeQueDrop": qtechQoSDeQueDrop,
       "qtechQoSLastClearTime": qtechQoSLastClearTime,
       "qtechTMQosQueMIBObjects": qtechTMQosQueMIBObjects,
       "qtechQosQueTable": qtechQosQueTable,
       "qtechQosQueEntry": qtechQosQueEntry,
       "qtechQoSIfIndex": qtechQoSIfIndex,
       "qtechQoSIfChipIndex": qtechQoSIfChipIndex,
       "qtechQoSIfChipQueIndex": qtechQoSIfChipQueIndex,
       "qtechQoSIfChipMax": qtechQoSIfChipMax,
       "qtechQoSIfChipCur": qtechQoSIfChipCur,
       "qtechQoSIfChipPeak": qtechQoSIfChipPeak,
       "qtechQoSIfChipRate": qtechQoSIfChipRate,
       "qtechQoSIfChipTime": qtechQoSIfChipTime,
       "qtechTMMIBConformance": qtechTMMIBConformance,
       "qtechTMMIBCompliances": qtechTMMIBCompliances,
       "qtechTMMIBCompliance": qtechTMMIBCompliance,
       "qtechTMMIBGroups": qtechTMMIBGroups,
       "qtechTMMIBGroup": qtechTMMIBGroup}
)
