# SNMP MIB module (FS-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:24 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
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

fsTMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91)
)
if mibBuilder.loadTexts:
    fsTMMIB.setRevisions(
        ("2010-12-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTMMIBObjects_ObjectIdentity = ObjectIdentity
fsTMMIBObjects = _FsTMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1)
)
_FsTMQosDramMIBObjects_ObjectIdentity = ObjectIdentity
fsTMQosDramMIBObjects = _FsTMQosDramMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1)
)
_FsQosDramTable_Object = MibTable
fsQosDramTable = _FsQosDramTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsQosDramTable.setStatus("current")
_FsQosDramEntry_Object = MibTableRow
fsQosDramEntry = _FsQosDramEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1, 1, 1)
)
fsQosDramEntry.setIndexNames(
    (0, "FS-TM-MIB", "fsQoSDramIndex"),
)
if mibBuilder.loadTexts:
    fsQosDramEntry.setStatus("current")
_FsQoSDramIndex_Type = Integer32
_FsQoSDramIndex_Object = MibTableColumn
fsQoSDramIndex = _FsQoSDramIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1, 1, 1, 1),
    _FsQoSDramIndex_Type()
)
fsQoSDramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSDramIndex.setStatus("current")
_FsQosDramTotal_Type = Integer32
_FsQosDramTotal_Object = MibTableColumn
fsQosDramTotal = _FsQosDramTotal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1, 1, 1, 2),
    _FsQosDramTotal_Type()
)
fsQosDramTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQosDramTotal.setStatus("current")
_FsQosDramCurUsed_Type = Integer32
_FsQosDramCurUsed_Object = MibTableColumn
fsQosDramCurUsed = _FsQosDramCurUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 1, 1, 1, 3),
    _FsQosDramCurUsed_Type()
)
fsQosDramCurUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQosDramCurUsed.setStatus("current")
_FsTMQosDropMIBObjects_ObjectIdentity = ObjectIdentity
fsTMQosDropMIBObjects = _FsTMQosDropMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2)
)
_FsQosDropTable_Object = MibTable
fsQosDropTable = _FsQosDropTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsQosDropTable.setStatus("current")
_FsQosDropEntry_Object = MibTableRow
fsQosDropEntry = _FsQosDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1)
)
fsQosDropEntry.setIndexNames(
    (0, "FS-TM-MIB", "fsQoSDropIndex"),
)
if mibBuilder.loadTexts:
    fsQosDropEntry.setStatus("current")
_FsQoSDropIndex_Type = Integer32
_FsQoSDropIndex_Object = MibTableColumn
fsQoSDropIndex = _FsQoSDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 1),
    _FsQoSDropIndex_Type()
)
fsQoSDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSDropIndex.setStatus("current")
_FsQoSTotalEnQue_Type = Integer32
_FsQoSTotalEnQue_Object = MibTableColumn
fsQoSTotalEnQue = _FsQoSTotalEnQue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 2),
    _FsQoSTotalEnQue_Type()
)
fsQoSTotalEnQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSTotalEnQue.setStatus("current")
_FsQoSTotalDeQue_Type = Integer32
_FsQoSTotalDeQue_Object = MibTableColumn
fsQoSTotalDeQue = _FsQoSTotalDeQue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 3),
    _FsQoSTotalDeQue_Type()
)
fsQoSTotalDeQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSTotalDeQue.setStatus("current")
_FsQoSEnQueDrop_Type = Integer32
_FsQoSEnQueDrop_Object = MibTableColumn
fsQoSEnQueDrop = _FsQoSEnQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 4),
    _FsQoSEnQueDrop_Type()
)
fsQoSEnQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSEnQueDrop.setStatus("current")
_FsQoSEnQueDropByBuf_Type = Integer32
_FsQoSEnQueDropByBuf_Object = MibTableColumn
fsQoSEnQueDropByBuf = _FsQoSEnQueDropByBuf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 5),
    _FsQoSEnQueDropByBuf_Type()
)
fsQoSEnQueDropByBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSEnQueDropByBuf.setStatus("current")
_FsQoSEnQueDropByBufDesc_Type = Integer32
_FsQoSEnQueDropByBufDesc_Object = MibTableColumn
fsQoSEnQueDropByBufDesc = _FsQoSEnQueDropByBufDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 6),
    _FsQoSEnQueDropByBufDesc_Type()
)
fsQoSEnQueDropByBufDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSEnQueDropByBufDesc.setStatus("current")
_FsQoSEnQueDropByOther_Type = Integer32
_FsQoSEnQueDropByOther_Object = MibTableColumn
fsQoSEnQueDropByOther = _FsQoSEnQueDropByOther_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 7),
    _FsQoSEnQueDropByOther_Type()
)
fsQoSEnQueDropByOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSEnQueDropByOther.setStatus("current")
_FsQoSDeQueDrop_Type = Integer32
_FsQoSDeQueDrop_Object = MibTableColumn
fsQoSDeQueDrop = _FsQoSDeQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 8),
    _FsQoSDeQueDrop_Type()
)
fsQoSDeQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSDeQueDrop.setStatus("current")
_FsQoSLastClearTime_Type = TimeTicks
_FsQoSLastClearTime_Object = MibTableColumn
fsQoSLastClearTime = _FsQoSLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 2, 1, 1, 9),
    _FsQoSLastClearTime_Type()
)
fsQoSLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSLastClearTime.setStatus("current")
_FsTMQosQueMIBObjects_ObjectIdentity = ObjectIdentity
fsTMQosQueMIBObjects = _FsTMQosQueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3)
)
_FsQosQueTable_Object = MibTable
fsQosQueTable = _FsQosQueTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsQosQueTable.setStatus("current")
_FsQosQueEntry_Object = MibTableRow
fsQosQueEntry = _FsQosQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1)
)
fsQosQueEntry.setIndexNames(
    (0, "FS-TM-MIB", "fsQoSIfIndex"),
    (0, "FS-TM-MIB", "fsQoSIfChipIndex"),
    (0, "FS-TM-MIB", "fsQoSIfChipQueIndex"),
)
if mibBuilder.loadTexts:
    fsQosQueEntry.setStatus("current")
_FsQoSIfIndex_Type = IfIndex
_FsQoSIfIndex_Object = MibTableColumn
fsQoSIfIndex = _FsQoSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 1),
    _FsQoSIfIndex_Type()
)
fsQoSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfIndex.setStatus("current")


class _FsQoSIfChipIndex_Type(Integer32):
    """Custom type fsQoSIfChipIndex based on Integer32"""
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


_FsQoSIfChipIndex_Type.__name__ = "Integer32"
_FsQoSIfChipIndex_Object = MibTableColumn
fsQoSIfChipIndex = _FsQoSIfChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 2),
    _FsQoSIfChipIndex_Type()
)
fsQoSIfChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipIndex.setStatus("current")


class _FsQoSIfChipQueIndex_Type(Integer32):
    """Custom type fsQoSIfChipQueIndex based on Integer32"""
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


_FsQoSIfChipQueIndex_Type.__name__ = "Integer32"
_FsQoSIfChipQueIndex_Object = MibTableColumn
fsQoSIfChipQueIndex = _FsQoSIfChipQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 3),
    _FsQoSIfChipQueIndex_Type()
)
fsQoSIfChipQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipQueIndex.setStatus("current")
_FsQoSIfChipMax_Type = Integer32
_FsQoSIfChipMax_Object = MibTableColumn
fsQoSIfChipMax = _FsQoSIfChipMax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 4),
    _FsQoSIfChipMax_Type()
)
fsQoSIfChipMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipMax.setStatus("current")
_FsQoSIfChipCur_Type = Integer32
_FsQoSIfChipCur_Object = MibTableColumn
fsQoSIfChipCur = _FsQoSIfChipCur_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 5),
    _FsQoSIfChipCur_Type()
)
fsQoSIfChipCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipCur.setStatus("current")
_FsQoSIfChipPeak_Type = Integer32
_FsQoSIfChipPeak_Object = MibTableColumn
fsQoSIfChipPeak = _FsQoSIfChipPeak_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 6),
    _FsQoSIfChipPeak_Type()
)
fsQoSIfChipPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipPeak.setStatus("current")
_FsQoSIfChipRate_Type = Integer32
_FsQoSIfChipRate_Object = MibTableColumn
fsQoSIfChipRate = _FsQoSIfChipRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 7),
    _FsQoSIfChipRate_Type()
)
fsQoSIfChipRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipRate.setStatus("current")
_FsQoSIfChipTime_Type = TimeTicks
_FsQoSIfChipTime_Object = MibTableColumn
fsQoSIfChipTime = _FsQoSIfChipTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 1, 3, 1, 1, 8),
    _FsQoSIfChipTime_Type()
)
fsQoSIfChipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSIfChipTime.setStatus("current")
_FsTMMIBConformance_ObjectIdentity = ObjectIdentity
fsTMMIBConformance = _FsTMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 2)
)
_FsTMMIBCompliances_ObjectIdentity = ObjectIdentity
fsTMMIBCompliances = _FsTMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 2, 1)
)
_FsTMMIBGroups_ObjectIdentity = ObjectIdentity
fsTMMIBGroups = _FsTMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 2, 2)
)

# Managed Objects groups

fsTMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 2, 2, 1)
)
fsTMMIBGroup.setObjects(
      *(("FS-TM-MIB", "fsQoSDramIndex"),
        ("FS-TM-MIB", "fsQosDramTotal"),
        ("FS-TM-MIB", "fsQosDramCurUsed"),
        ("FS-TM-MIB", "fsQoSDropIndex"),
        ("FS-TM-MIB", "fsQoSTotalEnQue"),
        ("FS-TM-MIB", "fsQoSTotalDeQue"),
        ("FS-TM-MIB", "fsQoSEnQueDrop"),
        ("FS-TM-MIB", "fsQoSEnQueDropByBuf"),
        ("FS-TM-MIB", "fsQoSEnQueDropByBufDesc"),
        ("FS-TM-MIB", "fsQoSEnQueDropByOther"),
        ("FS-TM-MIB", "fsQoSDeQueDrop"),
        ("FS-TM-MIB", "fsQoSLastClearTime"),
        ("FS-TM-MIB", "fsQoSIfIndex"),
        ("FS-TM-MIB", "fsQoSIfChipIndex"),
        ("FS-TM-MIB", "fsQoSIfChipQueIndex"),
        ("FS-TM-MIB", "fsQoSIfChipMax"),
        ("FS-TM-MIB", "fsQoSIfChipCur"),
        ("FS-TM-MIB", "fsQoSIfChipPeak"),
        ("FS-TM-MIB", "fsQoSIfChipRate"),
        ("FS-TM-MIB", "fsQoSIfChipTime"))
)
if mibBuilder.loadTexts:
    fsTMMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsTMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 91, 2, 1, 1)
)
fsTMMIBCompliance.setObjects(
    ("FS-TM-MIB", "fsTMMIBGroup")
)
if mibBuilder.loadTexts:
    fsTMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TM-MIB",
    **{"fsTMMIB": fsTMMIB,
       "fsTMMIBObjects": fsTMMIBObjects,
       "fsTMQosDramMIBObjects": fsTMQosDramMIBObjects,
       "fsQosDramTable": fsQosDramTable,
       "fsQosDramEntry": fsQosDramEntry,
       "fsQoSDramIndex": fsQoSDramIndex,
       "fsQosDramTotal": fsQosDramTotal,
       "fsQosDramCurUsed": fsQosDramCurUsed,
       "fsTMQosDropMIBObjects": fsTMQosDropMIBObjects,
       "fsQosDropTable": fsQosDropTable,
       "fsQosDropEntry": fsQosDropEntry,
       "fsQoSDropIndex": fsQoSDropIndex,
       "fsQoSTotalEnQue": fsQoSTotalEnQue,
       "fsQoSTotalDeQue": fsQoSTotalDeQue,
       "fsQoSEnQueDrop": fsQoSEnQueDrop,
       "fsQoSEnQueDropByBuf": fsQoSEnQueDropByBuf,
       "fsQoSEnQueDropByBufDesc": fsQoSEnQueDropByBufDesc,
       "fsQoSEnQueDropByOther": fsQoSEnQueDropByOther,
       "fsQoSDeQueDrop": fsQoSDeQueDrop,
       "fsQoSLastClearTime": fsQoSLastClearTime,
       "fsTMQosQueMIBObjects": fsTMQosQueMIBObjects,
       "fsQosQueTable": fsQosQueTable,
       "fsQosQueEntry": fsQosQueEntry,
       "fsQoSIfIndex": fsQoSIfIndex,
       "fsQoSIfChipIndex": fsQoSIfChipIndex,
       "fsQoSIfChipQueIndex": fsQoSIfChipQueIndex,
       "fsQoSIfChipMax": fsQoSIfChipMax,
       "fsQoSIfChipCur": fsQoSIfChipCur,
       "fsQoSIfChipPeak": fsQoSIfChipPeak,
       "fsQoSIfChipRate": fsQoSIfChipRate,
       "fsQoSIfChipTime": fsQoSIfChipTime,
       "fsTMMIBConformance": fsTMMIBConformance,
       "fsTMMIBCompliances": fsTMMIBCompliances,
       "fsTMMIBCompliance": fsTMMIBCompliance,
       "fsTMMIBGroups": fsTMMIBGroups,
       "fsTMMIBGroup": fsTMMIBGroup}
)
