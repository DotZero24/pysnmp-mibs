# SNMP MIB module (ADTRAN-GENERIC-PSEUDOWIRE-CEM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:15 2025
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

(adGenPseudowireCEMAlarmProv,
 adGenPseudowireCEMAlarmsID,
 adGenPseudowireCEMEvents,
 adGenPseudowireCEMPhysicalPortIfIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB",
    "adGenPseudowireCEMAlarmProv",
    "adGenPseudowireCEMAlarmsID",
    "adGenPseudowireCEMEvents",
    "adGenPseudowireCEMPhysicalPortIfIndex")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPseudowireCEMAlarmModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 3, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmModuleIdentity.setRevisions(
        ("2018-11-20 17:00",
         "2014-07-01 17:00",
         "2012-05-18 11:20")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPseudowireCEMAlarmProvTable_Object = MibTable
adGenPseudowireCEMAlarmProvTable = _AdGenPseudowireCEMAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 7, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmProvTable.setStatus("current")
_AdGenPseudowireCEMAlarmProvTableEntry_Object = MibTableRow
adGenPseudowireCEMAlarmProvTableEntry = _AdGenPseudowireCEMAlarmProvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 7, 1, 1)
)
adGenPseudowireCEMAlarmProvTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmProvTableEntry.setStatus("current")
_AdGenPseudowireCEMFarEndLOSAlarmEnable_Type = TruthValue
_AdGenPseudowireCEMFarEndLOSAlarmEnable_Object = MibTableColumn
adGenPseudowireCEMFarEndLOSAlarmEnable = _AdGenPseudowireCEMFarEndLOSAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 7, 1, 1, 1),
    _AdGenPseudowireCEMFarEndLOSAlarmEnable_Type()
)
adGenPseudowireCEMFarEndLOSAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMFarEndLOSAlarmEnable.setStatus("current")

# Managed Objects groups


# Notification objects

adGenPseudowireCEMAlarmFarEndLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 1)
)
adGenPseudowireCEMAlarmFarEndLOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmFarEndLOSClear.setStatus(
        "current"
    )

adGenPseudowireCEMAlarmFarEndLOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 2)
)
adGenPseudowireCEMAlarmFarEndLOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmFarEndLOSActive.setStatus(
        "current"
    )

adGenPseudowireCEMAlarmNearEndLPSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 3)
)
adGenPseudowireCEMAlarmNearEndLPSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmNearEndLPSClear.setStatus(
        "current"
    )

adGenPseudowireCEMAlarmNearEndLPSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 4)
)
adGenPseudowireCEMAlarmNearEndLPSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmNearEndLPSActive.setStatus(
        "current"
    )

adGenPseudowireCEMAlarmFarEndLPSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 5)
)
adGenPseudowireCEMAlarmFarEndLPSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmFarEndLPSClear.setStatus(
        "current"
    )

adGenPseudowireCEMAlarmFarEndLPSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0, 6)
)
adGenPseudowireCEMAlarmFarEndLPSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPhysicalPortIfIndex"))
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMAlarmFarEndLPSActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-ALARM-MIB",
    **{"adGenPseudowireCEMAlarmFarEndLOSClear": adGenPseudowireCEMAlarmFarEndLOSClear,
       "adGenPseudowireCEMAlarmFarEndLOSActive": adGenPseudowireCEMAlarmFarEndLOSActive,
       "adGenPseudowireCEMAlarmNearEndLPSClear": adGenPseudowireCEMAlarmNearEndLPSClear,
       "adGenPseudowireCEMAlarmNearEndLPSActive": adGenPseudowireCEMAlarmNearEndLPSActive,
       "adGenPseudowireCEMAlarmFarEndLPSClear": adGenPseudowireCEMAlarmFarEndLPSClear,
       "adGenPseudowireCEMAlarmFarEndLPSActive": adGenPseudowireCEMAlarmFarEndLPSActive,
       "adGenPseudowireCEMAlarmProvTable": adGenPseudowireCEMAlarmProvTable,
       "adGenPseudowireCEMAlarmProvTableEntry": adGenPseudowireCEMAlarmProvTableEntry,
       "adGenPseudowireCEMFarEndLOSAlarmEnable": adGenPseudowireCEMFarEndLOSAlarmEnable,
       "adGenPseudowireCEMAlarmModuleIdentity": adGenPseudowireCEMAlarmModuleIdentity}
)
