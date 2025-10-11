# SNMP MIB module (IPE-TERM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-TERM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:44 2025
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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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



class OffOnValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("off", 1),
          ("on", 2))
    )



class SeverityValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("indetermine", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsTermCardGroup_ObjectIdentity = ObjectIdentity
asTermCardGroup = _AsTermCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36)
)
_AsTermCardTable_Object = MibTable
asTermCardTable = _AsTermCardTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1)
)
if mibBuilder.loadTexts:
    asTermCardTable.setStatus("current")
_AsTermCardEntry_Object = MibTableRow
asTermCardEntry = _AsTermCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1)
)
asTermCardEntry.setIndexNames(
    (0, "IPE-TERM-MIB", "asTermCardIndex"),
)
if mibBuilder.loadTexts:
    asTermCardEntry.setStatus("current")
_AsTermCardIndex_Type = Integer32
_AsTermCardIndex_Object = MibTableColumn
asTermCardIndex = _AsTermCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 1),
    _AsTermCardIndex_Type()
)
asTermCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asTermCardIndex.setStatus("current")
_AsTermCardNEAddress_Type = IpAddress
_AsTermCardNEAddress_Object = MibTableColumn
asTermCardNEAddress = _AsTermCardNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 2),
    _AsTermCardNEAddress_Type()
)
asTermCardNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asTermCardNEAddress.setStatus("current")
_TermAlarm_Type = SeverityValue
_TermAlarm_Object = MibTableColumn
termAlarm = _TermAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 3),
    _TermAlarm_Type()
)
termAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termAlarm.setStatus("current")
_TermComFailAlarm_Type = SeverityValue
_TermComFailAlarm_Object = MibTableColumn
termComFailAlarm = _TermComFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 4),
    _TermComFailAlarm_Type()
)
termComFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termComFailAlarm.setStatus("current")
_TermUnequipped_Type = SeverityValue
_TermUnequipped_Object = MibTableColumn
termUnequipped = _TermUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 5),
    _TermUnequipped_Type()
)
termUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termUnequipped.setStatus("current")
_TermTypeMismatch_Type = SeverityValue
_TermTypeMismatch_Object = MibTableColumn
termTypeMismatch = _TermTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 6),
    _TermTypeMismatch_Type()
)
termTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termTypeMismatch.setStatus("current")
_TermCardChange_Type = OffOnValue
_TermCardChange_Object = MibTableColumn
termCardChange = _TermCardChange_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 7),
    _TermCardChange_Type()
)
termCardChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termCardChange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-TERM-MIB",
    **{"OffOnValue": OffOnValue,
       "SeverityValue": SeverityValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asTermCardGroup": asTermCardGroup,
       "asTermCardTable": asTermCardTable,
       "asTermCardEntry": asTermCardEntry,
       "asTermCardIndex": asTermCardIndex,
       "asTermCardNEAddress": asTermCardNEAddress,
       "termAlarm": termAlarm,
       "termComFailAlarm": termComFailAlarm,
       "termUnequipped": termUnequipped,
       "termTypeMismatch": termTypeMismatch,
       "termCardChange": termCardChange}
)
