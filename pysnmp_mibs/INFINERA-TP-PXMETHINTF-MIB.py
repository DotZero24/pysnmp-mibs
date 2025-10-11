# SNMP MIB module (INFINERA-TP-PXMETHINTF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMETHINTF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:33 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatHundredths,
 FloatTenths,
 InfnAcceptableFrameType,
 InfnEnableDisableType,
 InfnLoopbackBehavior,
 InfnPXMInterfaceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnAcceptableFrameType",
    "InfnEnableDisableType",
    "InfnLoopbackBehavior",
    "InfnPXMInterfaceType")

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

pxmEthIntfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76)
)
if mibBuilder.loadTexts:
    pxmEthIntfMIB.setRevisions(
        ("2016-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmEthIntfTable_Object = MibTable
pxmEthIntfTable = _PxmEthIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1)
)
if mibBuilder.loadTexts:
    pxmEthIntfTable.setStatus("current")
_PxmEthIntfEntry_Object = MibTableRow
pxmEthIntfEntry = _PxmEthIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1)
)
pxmEthIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmEthIntfEntry.setStatus("current")
_PxmEthIntfMTUSize_Type = Integer32
_PxmEthIntfMTUSize_Object = MibTableColumn
pxmEthIntfMTUSize = _PxmEthIntfMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 1),
    _PxmEthIntfMTUSize_Type()
)
pxmEthIntfMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfMTUSize.setStatus("current")
_PxmEthIntfInterfaceType_Type = InfnPXMInterfaceType
_PxmEthIntfInterfaceType_Object = MibTableColumn
pxmEthIntfInterfaceType = _PxmEthIntfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 2),
    _PxmEthIntfInterfaceType_Type()
)
pxmEthIntfInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfInterfaceType.setStatus("current")
_PxmEthIntfOuterTPID_Type = Integer32
_PxmEthIntfOuterTPID_Object = MibTableColumn
pxmEthIntfOuterTPID = _PxmEthIntfOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 3),
    _PxmEthIntfOuterTPID_Type()
)
pxmEthIntfOuterTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfOuterTPID.setStatus("current")
_PxmEthIntfInnerTPID_Type = Integer32
_PxmEthIntfInnerTPID_Object = MibTableColumn
pxmEthIntfInnerTPID = _PxmEthIntfInnerTPID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 4),
    _PxmEthIntfInnerTPID_Type()
)
pxmEthIntfInnerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfInnerTPID.setStatus("current")
_PxmEthIntfDefaultVLANID_Type = Integer32
_PxmEthIntfDefaultVLANID_Object = MibTableColumn
pxmEthIntfDefaultVLANID = _PxmEthIntfDefaultVLANID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 5),
    _PxmEthIntfDefaultVLANID_Type()
)
pxmEthIntfDefaultVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfDefaultVLANID.setStatus("current")
_PxmEthIntfDefaultPriority_Type = Integer32
_PxmEthIntfDefaultPriority_Object = MibTableColumn
pxmEthIntfDefaultPriority = _PxmEthIntfDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 6),
    _PxmEthIntfDefaultPriority_Type()
)
pxmEthIntfDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfDefaultPriority.setStatus("current")
_PxmEthIntfIngressTrafficClass_Type = Integer32
_PxmEthIntfIngressTrafficClass_Object = MibTableColumn
pxmEthIntfIngressTrafficClass = _PxmEthIntfIngressTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 7),
    _PxmEthIntfIngressTrafficClass_Type()
)
pxmEthIntfIngressTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfIngressTrafficClass.setStatus("current")
_PxmEthIntfFacTestSignalGen_Type = InfnEnableDisableType
_PxmEthIntfFacTestSignalGen_Object = MibTableColumn
pxmEthIntfFacTestSignalGen = _PxmEthIntfFacTestSignalGen_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 8),
    _PxmEthIntfFacTestSignalGen_Type()
)
pxmEthIntfFacTestSignalGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfFacTestSignalGen.setStatus("current")
_PxmEthIntfFacTestSignalMon_Type = InfnEnableDisableType
_PxmEthIntfFacTestSignalMon_Object = MibTableColumn
pxmEthIntfFacTestSignalMon = _PxmEthIntfFacTestSignalMon_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 9),
    _PxmEthIntfFacTestSignalMon_Type()
)
pxmEthIntfFacTestSignalMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfFacTestSignalMon.setStatus("current")
_PxmEthIntfTerminalTestSignalGen_Type = InfnEnableDisableType
_PxmEthIntfTerminalTestSignalGen_Object = MibTableColumn
pxmEthIntfTerminalTestSignalGen = _PxmEthIntfTerminalTestSignalGen_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 10),
    _PxmEthIntfTerminalTestSignalGen_Type()
)
pxmEthIntfTerminalTestSignalGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfTerminalTestSignalGen.setStatus("current")
_PxmEthIntfTerminalTestSignalMon_Type = InfnEnableDisableType
_PxmEthIntfTerminalTestSignalMon_Object = MibTableColumn
pxmEthIntfTerminalTestSignalMon = _PxmEthIntfTerminalTestSignalMon_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 11),
    _PxmEthIntfTerminalTestSignalMon_Type()
)
pxmEthIntfTerminalTestSignalMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfTerminalTestSignalMon.setStatus("current")
_PxmEthIntfInterfaceRate_Type = Integer32
_PxmEthIntfInterfaceRate_Object = MibTableColumn
pxmEthIntfInterfaceRate = _PxmEthIntfInterfaceRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 12),
    _PxmEthIntfInterfaceRate_Type()
)
pxmEthIntfInterfaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfInterfaceRate.setStatus("current")
_PxmEthIntfAcceptableFrameType_Type = InfnAcceptableFrameType
_PxmEthIntfAcceptableFrameType_Object = MibTableColumn
pxmEthIntfAcceptableFrameType = _PxmEthIntfAcceptableFrameType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 13),
    _PxmEthIntfAcceptableFrameType_Type()
)
pxmEthIntfAcceptableFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfAcceptableFrameType.setStatus("current")
_PxmEthIntfOverBookingFactor_Type = FloatTenths
_PxmEthIntfOverBookingFactor_Object = MibTableColumn
pxmEthIntfOverBookingFactor = _PxmEthIntfOverBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 14),
    _PxmEthIntfOverBookingFactor_Type()
)
pxmEthIntfOverBookingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfOverBookingFactor.setStatus("current")
_PxmEthIntfMaxReservableBW_Type = FloatHundredths
_PxmEthIntfMaxReservableBW_Object = MibTableColumn
pxmEthIntfMaxReservableBW = _PxmEthIntfMaxReservableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 15),
    _PxmEthIntfMaxReservableBW_Type()
)
pxmEthIntfMaxReservableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfMaxReservableBW.setStatus("current")
_PxmEthIntfAvailableBW_Type = FloatHundredths
_PxmEthIntfAvailableBW_Object = MibTableColumn
pxmEthIntfAvailableBW = _PxmEthIntfAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 16),
    _PxmEthIntfAvailableBW_Type()
)
pxmEthIntfAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfAvailableBW.setStatus("current")
_PxmEthIntfLoopbackBehavior_Type = InfnLoopbackBehavior
_PxmEthIntfLoopbackBehavior_Object = MibTableColumn
pxmEthIntfLoopbackBehavior = _PxmEthIntfLoopbackBehavior_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 17),
    _PxmEthIntfLoopbackBehavior_Type()
)
pxmEthIntfLoopbackBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfLoopbackBehavior.setStatus("current")
_PxmEthIntfMacAddress_Type = DisplayString
_PxmEthIntfMacAddress_Object = MibTableColumn
pxmEthIntfMacAddress = _PxmEthIntfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 18),
    _PxmEthIntfMacAddress_Type()
)
pxmEthIntfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEthIntfMacAddress.setStatus("current")
_PxmEthIntfCSFAsTDATrigger_Type = InfnEnableDisableType
_PxmEthIntfCSFAsTDATrigger_Object = MibTableColumn
pxmEthIntfCSFAsTDATrigger = _PxmEthIntfCSFAsTDATrigger_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 1, 1, 19),
    _PxmEthIntfCSFAsTDATrigger_Type()
)
pxmEthIntfCSFAsTDATrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmEthIntfCSFAsTDATrigger.setStatus("current")
_PxmEthIntfConformance_ObjectIdentity = ObjectIdentity
pxmEthIntfConformance = _PxmEthIntfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 3)
)
_PxmEthIntfCompliances_ObjectIdentity = ObjectIdentity
pxmEthIntfCompliances = _PxmEthIntfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 3, 1)
)
_PxmEthIntfGroups_ObjectIdentity = ObjectIdentity
pxmEthIntfGroups = _PxmEthIntfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 3, 2)
)

# Managed Objects groups

pxmEthIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 3, 2, 1)
)
pxmEthIntfGroup.setObjects(
      *(("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfMTUSize"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfInterfaceType"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfOuterTPID"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfInnerTPID"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfDefaultVLANID"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfDefaultPriority"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfIngressTrafficClass"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfFacTestSignalGen"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfFacTestSignalMon"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfTerminalTestSignalGen"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfTerminalTestSignalMon"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfInterfaceRate"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfAcceptableFrameType"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfOverBookingFactor"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfMaxReservableBW"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfAvailableBW"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfLoopbackBehavior"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfMacAddress"),
        ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfCSFAsTDATrigger"))
)
if mibBuilder.loadTexts:
    pxmEthIntfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmEthIntfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 76, 3, 1, 1)
)
pxmEthIntfCompliance.setObjects(
    ("INFINERA-TP-PXMETHINTF-MIB", "pxmEthIntfGroup")
)
if mibBuilder.loadTexts:
    pxmEthIntfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMETHINTF-MIB",
    **{"pxmEthIntfMIB": pxmEthIntfMIB,
       "pxmEthIntfTable": pxmEthIntfTable,
       "pxmEthIntfEntry": pxmEthIntfEntry,
       "pxmEthIntfMTUSize": pxmEthIntfMTUSize,
       "pxmEthIntfInterfaceType": pxmEthIntfInterfaceType,
       "pxmEthIntfOuterTPID": pxmEthIntfOuterTPID,
       "pxmEthIntfInnerTPID": pxmEthIntfInnerTPID,
       "pxmEthIntfDefaultVLANID": pxmEthIntfDefaultVLANID,
       "pxmEthIntfDefaultPriority": pxmEthIntfDefaultPriority,
       "pxmEthIntfIngressTrafficClass": pxmEthIntfIngressTrafficClass,
       "pxmEthIntfFacTestSignalGen": pxmEthIntfFacTestSignalGen,
       "pxmEthIntfFacTestSignalMon": pxmEthIntfFacTestSignalMon,
       "pxmEthIntfTerminalTestSignalGen": pxmEthIntfTerminalTestSignalGen,
       "pxmEthIntfTerminalTestSignalMon": pxmEthIntfTerminalTestSignalMon,
       "pxmEthIntfInterfaceRate": pxmEthIntfInterfaceRate,
       "pxmEthIntfAcceptableFrameType": pxmEthIntfAcceptableFrameType,
       "pxmEthIntfOverBookingFactor": pxmEthIntfOverBookingFactor,
       "pxmEthIntfMaxReservableBW": pxmEthIntfMaxReservableBW,
       "pxmEthIntfAvailableBW": pxmEthIntfAvailableBW,
       "pxmEthIntfLoopbackBehavior": pxmEthIntfLoopbackBehavior,
       "pxmEthIntfMacAddress": pxmEthIntfMacAddress,
       "pxmEthIntfCSFAsTDATrigger": pxmEthIntfCSFAsTDATrigger,
       "pxmEthIntfConformance": pxmEthIntfConformance,
       "pxmEthIntfCompliances": pxmEthIntfCompliances,
       "pxmEthIntfCompliance": pxmEthIntfCompliance,
       "pxmEthIntfGroups": pxmEthIntfGroups,
       "pxmEthIntfGroup": pxmEthIntfGroup}
)
