# SNMP MIB module (CRESTRON-PROGRAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-PROGRAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:46 2025
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

(crestronControl,) = mibBuilder.importSymbols(
    "CRESTRON-ROOT-MIB",
    "crestronControl")

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

crestronProgram = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2)
)
if mibBuilder.loadTexts:
    crestronProgram.setRevisions(
        ("2003-08-18 12:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ProgramState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )



# MIB Managed Objects in the order of their OIDs

_CrestronProgAdmin_ObjectIdentity = ObjectIdentity
crestronProgAdmin = _CrestronProgAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 1)
)
_CrestronProgNotifications_ObjectIdentity = ObjectIdentity
crestronProgNotifications = _CrestronProgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 2)
)
_CrestronProgObjects_ObjectIdentity = ObjectIdentity
crestronProgObjects = _CrestronProgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3)
)
_CrestronProgMIBVersion_Type = Integer32
_CrestronProgMIBVersion_Object = MibScalar
crestronProgMIBVersion = _CrestronProgMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 1),
    _CrestronProgMIBVersion_Type()
)
crestronProgMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgMIBVersion.setStatus("current")
_CrestronProgInfo_ObjectIdentity = ObjectIdentity
crestronProgInfo = _CrestronProgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2)
)
_CrestronProgUptime_Type = Integer32
_CrestronProgUptime_Object = MibScalar
crestronProgUptime = _CrestronProgUptime_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 1),
    _CrestronProgUptime_Type()
)
crestronProgUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgUptime.setStatus("current")
_CrestronProgLabel_Type = DisplayString
_CrestronProgLabel_Object = MibScalar
crestronProgLabel = _CrestronProgLabel_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 2),
    _CrestronProgLabel_Type()
)
crestronProgLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgLabel.setStatus("current")
_CrestronProgSymbolCnt_Type = Integer32
_CrestronProgSymbolCnt_Object = MibScalar
crestronProgSymbolCnt = _CrestronProgSymbolCnt_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 3),
    _CrestronProgSymbolCnt_Type()
)
crestronProgSymbolCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgSymbolCnt.setStatus("current")
_CrestronProgFilename_Type = DisplayString
_CrestronProgFilename_Object = MibScalar
crestronProgFilename = _CrestronProgFilename_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 4),
    _CrestronProgFilename_Type()
)
crestronProgFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgFilename.setStatus("current")
_CrestronProgCompiledOn_Type = DisplayString
_CrestronProgCompiledOn_Object = MibScalar
crestronProgCompiledOn = _CrestronProgCompiledOn_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 5),
    _CrestronProgCompiledOn_Type()
)
crestronProgCompiledOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronProgCompiledOn.setStatus("current")
_CrestronProgState_Type = ProgramState
_CrestronProgState_Object = MibScalar
crestronProgState = _CrestronProgState_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 3, 2, 6),
    _CrestronProgState_Type()
)
crestronProgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronProgState.setStatus("current")
_CrestronProgConformance_ObjectIdentity = ObjectIdentity
crestronProgConformance = _CrestronProgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 5)
)
_CrestronProgCompliances_ObjectIdentity = ObjectIdentity
crestronProgCompliances = _CrestronProgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 1)
)
_CrestronProgGroups_ObjectIdentity = ObjectIdentity
crestronProgGroups = _CrestronProgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2)
)

# Managed Objects groups

crestronProgAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2, 1)
)
crestronProgAllObjects.setObjects(
      *(("CRESTRON-PROGRAM-MIB", "crestronProgMIBVersion"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgUptime"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgLabel"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgSymbolCnt"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgFilename"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgCompiledOn"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgState"))
)
if mibBuilder.loadTexts:
    crestronProgAllObjects.setStatus("current")


# Notification objects

crestronProgStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 2, 1)
)
crestronProgStateChangeTrap.setObjects(
      *(("CRESTRON-PROGRAM-MIB", "crestronProgLabel"),
        ("CRESTRON-PROGRAM-MIB", "crestronProgUptime"))
)
if mibBuilder.loadTexts:
    crestronProgStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups

crestronProgAllTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 2, 5, 2, 2)
)
crestronProgAllTraps.setObjects(
    ("CRESTRON-PROGRAM-MIB", "crestronProgStateChangeTrap")
)
if mibBuilder.loadTexts:
    crestronProgAllTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-PROGRAM-MIB",
    **{"ProgramState": ProgramState,
       "crestronProgram": crestronProgram,
       "crestronProgAdmin": crestronProgAdmin,
       "crestronProgNotifications": crestronProgNotifications,
       "crestronProgStateChangeTrap": crestronProgStateChangeTrap,
       "crestronProgObjects": crestronProgObjects,
       "crestronProgMIBVersion": crestronProgMIBVersion,
       "crestronProgInfo": crestronProgInfo,
       "crestronProgUptime": crestronProgUptime,
       "crestronProgLabel": crestronProgLabel,
       "crestronProgSymbolCnt": crestronProgSymbolCnt,
       "crestronProgFilename": crestronProgFilename,
       "crestronProgCompiledOn": crestronProgCompiledOn,
       "crestronProgState": crestronProgState,
       "crestronProgConformance": crestronProgConformance,
       "crestronProgCompliances": crestronProgCompliances,
       "crestronProgGroups": crestronProgGroups,
       "crestronProgAllObjects": crestronProgAllObjects,
       "crestronProgAllTraps": crestronProgAllTraps}
)
