# SNMP MIB module (PKTC-ECL-EN-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/PKTC-ECL-EN-SIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:18:35 2025
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

(pktcEclEnhancements,) = mibBuilder.importSymbols(
    "ECL-DEF-MIB",
    "pktcEclEnhancements")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pktcNcsEndPntConfigEntry,) = mibBuilder.importSymbols(
    "PKTC-EXCENTIS-SIG-MIB",
    "pktcNcsEndPntConfigEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEclEnSigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pktcEclEnSigMib.setRevisions(
        ("2007-05-25 00:00",
         "2005-01-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEnSigMibObjects_ObjectIdentity = ObjectIdentity
pktcEnSigMibObjects = _PktcEnSigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1)
)
_PktcEnSigDevConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnSigDevConfigObjects = _PktcEnSigDevConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 1)
)


class _PktcEnNcsMinimumDtmfPlayout_Type(Unsigned32):
    """Custom type pktcEnNcsMinimumDtmfPlayout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 100),
    )


_PktcEnNcsMinimumDtmfPlayout_Type.__name__ = "Unsigned32"
_PktcEnNcsMinimumDtmfPlayout_Object = MibScalar
pktcEnNcsMinimumDtmfPlayout = _PktcEnNcsMinimumDtmfPlayout_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 1, 1),
    _PktcEnNcsMinimumDtmfPlayout_Type()
)
pktcEnNcsMinimumDtmfPlayout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsMinimumDtmfPlayout.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsMinimumDtmfPlayout.setUnits("milliseconds")
_PktcEnNcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnNcsEndPntConfigObjects = _PktcEnNcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2)
)
_PktcEnNcsEndPntConfigTable_Object = MibTable
pktcEnNcsEndPntConfigTable = _PktcEnNcsEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntConfigTable.setStatus("current")
_PktcEnNcsEndPntConfigEntry_Object = MibTableRow
pktcEnNcsEndPntConfigEntry = _PktcEnNcsEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntConfigEntry.setStatus("current")


class _PktcEnNcsEndPntQuarantineState_Type(Integer32):
    """Custom type pktcEnNcsEndPntQuarantineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notification", 2),
          ("lockstep", 3),
          ("extendedlockstep", 4))
    )


_PktcEnNcsEndPntQuarantineState_Type.__name__ = "Integer32"
_PktcEnNcsEndPntQuarantineState_Object = MibTableColumn
pktcEnNcsEndPntQuarantineState = _PktcEnNcsEndPntQuarantineState_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1, 1, 1),
    _PktcEnNcsEndPntQuarantineState_Type()
)
pktcEnNcsEndPntQuarantineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntQuarantineState.setStatus("current")


class _PktcEnNcsEndPntHookState_Type(Integer32):
    """Custom type pktcEnNcsEndPntHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 1),
          ("onHookPlusNCSActivity", 2),
          ("offHook", 3))
    )


_PktcEnNcsEndPntHookState_Type.__name__ = "Integer32"
_PktcEnNcsEndPntHookState_Object = MibTableColumn
pktcEnNcsEndPntHookState = _PktcEnNcsEndPntHookState_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1, 1, 2),
    _PktcEnNcsEndPntHookState_Type()
)
pktcEnNcsEndPntHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntHookState.setStatus("current")


class _PktcEnNcsEndPntFaxDetection_Type(TruthValue):
    """Custom type pktcEnNcsEndPntFaxDetection based on TruthValue"""
    defaultValue = 2


_PktcEnNcsEndPntFaxDetection_Type.__name__ = "TruthValue"
_PktcEnNcsEndPntFaxDetection_Object = MibTableColumn
pktcEnNcsEndPntFaxDetection = _PktcEnNcsEndPntFaxDetection_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1, 1, 3),
    _PktcEnNcsEndPntFaxDetection_Type()
)
pktcEnNcsEndPntFaxDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntFaxDetection.setStatus("current")


class _PktcEnNcsEndPntStatusReportCtrl_Type(Integer32):
    """Custom type pktcEnNcsEndPntStatusReportCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("reportActualStatus", 2),
          ("reportEndPointAsActive", 3))
    )


_PktcEnNcsEndPntStatusReportCtrl_Type.__name__ = "Integer32"
_PktcEnNcsEndPntStatusReportCtrl_Object = MibTableColumn
pktcEnNcsEndPntStatusReportCtrl = _PktcEnNcsEndPntStatusReportCtrl_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 1, 1, 4),
    _PktcEnNcsEndPntStatusReportCtrl_Type()
)
pktcEnNcsEndPntStatusReportCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntStatusReportCtrl.setStatus("deprecated")
_PktcEnEndPntInfoTable_Object = MibTable
pktcEnEndPntInfoTable = _PktcEnEndPntInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pktcEnEndPntInfoTable.setStatus("current")
_PktcEnEndPntInfoEntry_Object = MibTableRow
pktcEnEndPntInfoEntry = _PktcEnEndPntInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1)
)
pktcEnEndPntInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEnEndPntInfoEntry.setStatus("current")


class _PktcEnEndPntFgnPotSupport_Type(Bits):
    """Custom type pktcEnEndPntFgnPotSupport based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotDetection", 0),
          ("hazardousFgnPotDetection", 1))
    )

_PktcEnEndPntFgnPotSupport_Type.__name__ = "Bits"
_PktcEnEndPntFgnPotSupport_Object = MibTableColumn
pktcEnEndPntFgnPotSupport = _PktcEnEndPntFgnPotSupport_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 1),
    _PktcEnEndPntFgnPotSupport_Type()
)
pktcEnEndPntFgnPotSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnPotSupport.setStatus("current")
_PktcEnEndPntFgnPotDescr_Type = SnmpAdminString
_PktcEnEndPntFgnPotDescr_Object = MibTableColumn
pktcEnEndPntFgnPotDescr = _PktcEnEndPntFgnPotDescr_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 2),
    _PktcEnEndPntFgnPotDescr_Type()
)
pktcEnEndPntFgnPotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnPotDescr.setStatus("current")


class _PktcEnEndPntClrFgnPotTsts_Type(Bits):
    """Custom type pktcEnEndPntClrFgnPotTsts based on Bits"""
    namedValues = NamedValues(
        *(("clrFgnPotentialResults", 0),
          ("clrHazardousPotResults", 1))
    )

_PktcEnEndPntClrFgnPotTsts_Type.__name__ = "Bits"
_PktcEnEndPntClrFgnPotTsts_Object = MibTableColumn
pktcEnEndPntClrFgnPotTsts = _PktcEnEndPntClrFgnPotTsts_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 3),
    _PktcEnEndPntClrFgnPotTsts_Type()
)
pktcEnEndPntClrFgnPotTsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnEndPntClrFgnPotTsts.setStatus("current")


class _PktcEnEndPntRunFgnPotTsts_Type(Bits):
    """Custom type pktcEnEndPntRunFgnPotTsts based on Bits"""
    namedValues = NamedValues(
        *(("runFgnPotentialTsts", 0),
          ("runHazardousPotTsts", 1))
    )

_PktcEnEndPntRunFgnPotTsts_Type.__name__ = "Bits"
_PktcEnEndPntRunFgnPotTsts_Object = MibTableColumn
pktcEnEndPntRunFgnPotTsts = _PktcEnEndPntRunFgnPotTsts_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 4),
    _PktcEnEndPntRunFgnPotTsts_Type()
)
pktcEnEndPntRunFgnPotTsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnEndPntRunFgnPotTsts.setStatus("current")


class _PktcEnEndPntFgnTestValidity_Type(Bits):
    """Custom type pktcEnEndPntFgnTestValidity based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotTstValidity", 0),
          ("hazardousPotTstValidity", 1))
    )

_PktcEnEndPntFgnTestValidity_Type.__name__ = "Bits"
_PktcEnEndPntFgnTestValidity_Object = MibTableColumn
pktcEnEndPntFgnTestValidity = _PktcEnEndPntFgnTestValidity_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 5),
    _PktcEnEndPntFgnTestValidity_Type()
)
pktcEnEndPntFgnTestValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnTestValidity.setStatus("current")


class _PktcEnEndPntFgnTestResults_Type(Bits):
    """Custom type pktcEnEndPntFgnTestResults based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotentialResults", 0),
          ("hazardousPotResults", 1))
    )

_PktcEnEndPntFgnTestResults_Type.__name__ = "Bits"
_PktcEnEndPntFgnTestResults_Object = MibTableColumn
pktcEnEndPntFgnTestResults = _PktcEnEndPntFgnTestResults_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 2, 1, 6),
    _PktcEnEndPntFgnTestResults_Type()
)
pktcEnEndPntFgnTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnTestResults.setStatus("current")
_PktcEnNcsEndPntLVMgmtTable_Object = MibTable
pktcEnNcsEndPntLVMgmtTable = _PktcEnNcsEndPntLVMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtTable.setStatus("current")
_PktcEnNcsEndPntLVMgmtEntry_Object = MibTableRow
pktcEnNcsEndPntLVMgmtEntry = _PktcEnNcsEndPntLVMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 3, 1)
)
pktcEnNcsEndPntLVMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtEntry.setStatus("current")


class _PktcEnNcsEndPntLVMgmtPolicy_Type(Integer32):
    """Custom type pktcEnNcsEndPntLVMgmtPolicy based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("voltageAtAllTimes", 1),
          ("voltageUnlessRFQAMabsent", 2),
          ("voltageBasedOnServiceOrTimers", 3),
          ("voltageBasedOnService", 4))
    )


_PktcEnNcsEndPntLVMgmtPolicy_Type.__name__ = "Integer32"
_PktcEnNcsEndPntLVMgmtPolicy_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtPolicy = _PktcEnNcsEndPntLVMgmtPolicy_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 3, 1, 1),
    _PktcEnNcsEndPntLVMgmtPolicy_Type()
)
pktcEnNcsEndPntLVMgmtPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtPolicy.setStatus("current")


class _PktcEnNcsEndPntLVMgmtResetTimer_Type(Unsigned32):
    """Custom type pktcEnNcsEndPntLVMgmtResetTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PktcEnNcsEndPntLVMgmtResetTimer_Type.__name__ = "Unsigned32"
_PktcEnNcsEndPntLVMgmtResetTimer_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtResetTimer = _PktcEnNcsEndPntLVMgmtResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 3, 1, 2),
    _PktcEnNcsEndPntLVMgmtResetTimer_Type()
)
pktcEnNcsEndPntLVMgmtResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtResetTimer.setUnits("minutes")


class _PktcEnNcsEndPntLVMgmtMaintTimer_Type(Unsigned32):
    """Custom type pktcEnNcsEndPntLVMgmtMaintTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PktcEnNcsEndPntLVMgmtMaintTimer_Type.__name__ = "Unsigned32"
_PktcEnNcsEndPntLVMgmtMaintTimer_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtMaintTimer = _PktcEnNcsEndPntLVMgmtMaintTimer_Object(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 2, 3, 1, 3),
    _PktcEnNcsEndPntLVMgmtMaintTimer_Type()
)
pktcEnNcsEndPntLVMgmtMaintTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtMaintTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtMaintTimer.setUnits("minutes")
_PktcEnSigEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnSigEndPntConfigObjects = _PktcEnSigEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 3)
)
_PktcEnDcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnDcsEndPntConfigObjects = _PktcEnDcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 1, 4)
)
_PktcEnSigNotificationPrefix_ObjectIdentity = ObjectIdentity
pktcEnSigNotificationPrefix = _PktcEnSigNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 2)
)
_PktcEnSigNotification_ObjectIdentity = ObjectIdentity
pktcEnSigNotification = _PktcEnSigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 2, 0)
)
_PktcEnSigConformance_ObjectIdentity = ObjectIdentity
pktcEnSigConformance = _PktcEnSigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3)
)
_PktcEnSigCompliances_ObjectIdentity = ObjectIdentity
pktcEnSigCompliances = _PktcEnSigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 1)
)
_PktcEnSigGroups_ObjectIdentity = ObjectIdentity
pktcEnSigGroups = _PktcEnSigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 2)
)
pktcNcsEndPntConfigEntry.registerAugmentions(
    ("PKTC-ECL-EN-SIG-MIB",
     "pktcEnNcsEndPntConfigEntry")
)
pktcEnNcsEndPntConfigEntry.setIndexNames(*pktcNcsEndPntConfigEntry.getIndexNames())

# Managed Objects groups

pktcEnSigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 2, 1)
)
pktcEnSigGroup.setObjects(
    ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsMinimumDtmfPlayout")
)
if mibBuilder.loadTexts:
    pktcEnSigGroup.setStatus("current")

pktcEnNcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 2, 2)
)
pktcEnNcsGroup.setObjects(
      *(("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntQuarantineState"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntHookState"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntFaxDetection"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntFgnPotSupport"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntFgnPotDescr"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntClrFgnPotTsts"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntRunFgnPotTsts"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntFgnTestValidity"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnEndPntFgnTestResults"))
)
if mibBuilder.loadTexts:
    pktcEnNcsGroup.setStatus("current")

pktcEnNcsLVMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 2, 3)
)
pktcEnNcsLVMgmtGroup.setObjects(
      *(("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtPolicy"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtResetTimer"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtMaintTimer"))
)
if mibBuilder.loadTexts:
    pktcEnNcsLVMgmtGroup.setStatus("current")

pktcEnNcsDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 2, 4)
)
pktcEnNcsDeprecatedGroup.setObjects(
    ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsEndPntStatusReportCtrl")
)
if mibBuilder.loadTexts:
    pktcEnNcsDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcSigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2, 3, 1, 1)
)
pktcSigBasicCompliance.setObjects(
      *(("PKTC-ECL-EN-SIG-MIB", "pktcEnSigGroup"),
        ("PKTC-ECL-EN-SIG-MIB", "pktcEnNcsGroup"))
)
if mibBuilder.loadTexts:
    pktcSigBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-ECL-EN-SIG-MIB",
    **{"pktcEclEnSigMib": pktcEclEnSigMib,
       "pktcEnSigMibObjects": pktcEnSigMibObjects,
       "pktcEnSigDevConfigObjects": pktcEnSigDevConfigObjects,
       "pktcEnNcsMinimumDtmfPlayout": pktcEnNcsMinimumDtmfPlayout,
       "pktcEnNcsEndPntConfigObjects": pktcEnNcsEndPntConfigObjects,
       "pktcEnNcsEndPntConfigTable": pktcEnNcsEndPntConfigTable,
       "pktcEnNcsEndPntConfigEntry": pktcEnNcsEndPntConfigEntry,
       "pktcEnNcsEndPntQuarantineState": pktcEnNcsEndPntQuarantineState,
       "pktcEnNcsEndPntHookState": pktcEnNcsEndPntHookState,
       "pktcEnNcsEndPntFaxDetection": pktcEnNcsEndPntFaxDetection,
       "pktcEnNcsEndPntStatusReportCtrl": pktcEnNcsEndPntStatusReportCtrl,
       "pktcEnEndPntInfoTable": pktcEnEndPntInfoTable,
       "pktcEnEndPntInfoEntry": pktcEnEndPntInfoEntry,
       "pktcEnEndPntFgnPotSupport": pktcEnEndPntFgnPotSupport,
       "pktcEnEndPntFgnPotDescr": pktcEnEndPntFgnPotDescr,
       "pktcEnEndPntClrFgnPotTsts": pktcEnEndPntClrFgnPotTsts,
       "pktcEnEndPntRunFgnPotTsts": pktcEnEndPntRunFgnPotTsts,
       "pktcEnEndPntFgnTestValidity": pktcEnEndPntFgnTestValidity,
       "pktcEnEndPntFgnTestResults": pktcEnEndPntFgnTestResults,
       "pktcEnNcsEndPntLVMgmtTable": pktcEnNcsEndPntLVMgmtTable,
       "pktcEnNcsEndPntLVMgmtEntry": pktcEnNcsEndPntLVMgmtEntry,
       "pktcEnNcsEndPntLVMgmtPolicy": pktcEnNcsEndPntLVMgmtPolicy,
       "pktcEnNcsEndPntLVMgmtResetTimer": pktcEnNcsEndPntLVMgmtResetTimer,
       "pktcEnNcsEndPntLVMgmtMaintTimer": pktcEnNcsEndPntLVMgmtMaintTimer,
       "pktcEnSigEndPntConfigObjects": pktcEnSigEndPntConfigObjects,
       "pktcEnDcsEndPntConfigObjects": pktcEnDcsEndPntConfigObjects,
       "pktcEnSigNotificationPrefix": pktcEnSigNotificationPrefix,
       "pktcEnSigNotification": pktcEnSigNotification,
       "pktcEnSigConformance": pktcEnSigConformance,
       "pktcEnSigCompliances": pktcEnSigCompliances,
       "pktcSigBasicCompliance": pktcSigBasicCompliance,
       "pktcEnSigGroups": pktcEnSigGroups,
       "pktcEnSigGroup": pktcEnSigGroup,
       "pktcEnNcsGroup": pktcEnNcsGroup,
       "pktcEnNcsLVMgmtGroup": pktcEnNcsLVMgmtGroup,
       "pktcEnNcsDeprecatedGroup": pktcEnNcsDeprecatedGroup}
)
