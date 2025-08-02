_V='mrNetMgmtTrapClientIndex'
_U='permanent'
_T='invalid'
_S='mrNetMgmtSetClientIndex'
_R='mrStackUnitIndex'
_Q='mrSupervisorLogIndex'
_P='noClear'
_O='noReset'
_N='NotificationType'
_M='obsolete'
_L='disabled'
_K='enabled'
_J='CISCO-FASTHUB-MIB'
_I='sysName'
_H='SNMPv2-MIB'
_G='false'
_F='true'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class VisualLEDMap(OctetString):0
_CiscoFastHubMIB_ObjectIdentity=ObjectIdentity
ciscoFastHubMIB=_CiscoFastHubMIB_ObjectIdentity((1,3,6,1,4,1,9,2,11))
_CiscoFastHubMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFastHubMIBObjects=_CiscoFastHubMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,2,11,1))
_MrStack_ObjectIdentity=ObjectIdentity
mrStack=_MrStack_ObjectIdentity((1,3,6,1,4,1,9,2,11,1,1))
_MrStackUnitCapacity_Type=Integer32
_MrStackUnitCapacity_Object=MibScalar
mrStackUnitCapacity=_MrStackUnitCapacity_Object((1,3,6,1,4,1,9,2,11,1,1,1),_MrStackUnitCapacity_Type())
mrStackUnitCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitCapacity.setStatus(_A)
_MrStackNumberOfUnitsPresent_Type=Integer32
_MrStackNumberOfUnitsPresent_Object=MibScalar
mrStackNumberOfUnitsPresent=_MrStackNumberOfUnitsPresent_Object((1,3,6,1,4,1,9,2,11,1,1,2),_MrStackNumberOfUnitsPresent_Type())
mrStackNumberOfUnitsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackNumberOfUnitsPresent.setStatus(_A)
_MrStackSelectPrimarySupervisorUnit_Type=Integer32
_MrStackSelectPrimarySupervisorUnit_Object=MibScalar
mrStackSelectPrimarySupervisorUnit=_MrStackSelectPrimarySupervisorUnit_Object((1,3,6,1,4,1,9,2,11,1,1,3),_MrStackSelectPrimarySupervisorUnit_Type())
mrStackSelectPrimarySupervisorUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:mrStackSelectPrimarySupervisorUnit.setStatus(_A)
class _MrStackPOSTSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('abbreviated',2)))
_MrStackPOSTSelect_Type.__name__=_D
_MrStackPOSTSelect_Object=MibScalar
mrStackPOSTSelect=_MrStackPOSTSelect_Object((1,3,6,1,4,1,9,2,11,1,1,4),_MrStackPOSTSelect_Type())
mrStackPOSTSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:mrStackPOSTSelect.setStatus(_A)
class _MrStackReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_O,2)))
_MrStackReset_Type.__name__=_D
_MrStackReset_Object=MibScalar
mrStackReset=_MrStackReset_Object((1,3,6,1,4,1,9,2,11,1,1,5),_MrStackReset_Type())
mrStackReset.setMaxAccess(_C)
if mibBuilder.loadTexts:mrStackReset.setStatus(_A)
class _MrStackDefaultReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_O,2)))
_MrStackDefaultReset_Type.__name__=_D
_MrStackDefaultReset_Object=MibScalar
mrStackDefaultReset=_MrStackDefaultReset_Object((1,3,6,1,4,1,9,2,11,1,1,6),_MrStackDefaultReset_Type())
mrStackDefaultReset.setMaxAccess(_C)
if mibBuilder.loadTexts:mrStackDefaultReset.setStatus(_A)
class _MrStackClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_P,2)))
_MrStackClearStatistics_Type.__name__=_D
_MrStackClearStatistics_Object=MibScalar
mrStackClearStatistics=_MrStackClearStatistics_Object((1,3,6,1,4,1,9,2,11,1,1,7),_MrStackClearStatistics_Type())
mrStackClearStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:mrStackClearStatistics.setStatus(_M)
_MrStackShortJabberLoopCorrections_Type=Counter32
_MrStackShortJabberLoopCorrections_Object=MibScalar
mrStackShortJabberLoopCorrections=_MrStackShortJabberLoopCorrections_Object((1,3,6,1,4,1,9,2,11,1,1,8),_MrStackShortJabberLoopCorrections_Type())
mrStackShortJabberLoopCorrections.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackShortJabberLoopCorrections.setStatus(_A)
_MrSupervisorLog_ObjectIdentity=ObjectIdentity
mrSupervisorLog=_MrSupervisorLog_ObjectIdentity((1,3,6,1,4,1,9,2,11,1,2))
class _MrSupervisorLogTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_P,2)))
_MrSupervisorLogTableClear_Type.__name__=_D
_MrSupervisorLogTableClear_Object=MibScalar
mrSupervisorLogTableClear=_MrSupervisorLogTableClear_Object((1,3,6,1,4,1,9,2,11,1,2,1),_MrSupervisorLogTableClear_Type())
mrSupervisorLogTableClear.setMaxAccess(_C)
if mibBuilder.loadTexts:mrSupervisorLogTableClear.setStatus(_A)
_MrSupervisorLogTable_Object=MibTable
mrSupervisorLogTable=_MrSupervisorLogTable_Object((1,3,6,1,4,1,9,2,11,1,2,2))
if mibBuilder.loadTexts:mrSupervisorLogTable.setStatus(_A)
_MrSupervisorLogEntry_Object=MibTableRow
mrSupervisorLogEntry=_MrSupervisorLogEntry_Object((1,3,6,1,4,1,9,2,11,1,2,2,1))
mrSupervisorLogEntry.setIndexNames((0,_J,_Q))
if mibBuilder.loadTexts:mrSupervisorLogEntry.setStatus(_A)
_MrSupervisorLogIndex_Type=Integer32
_MrSupervisorLogIndex_Object=MibTableColumn
mrSupervisorLogIndex=_MrSupervisorLogIndex_Object((1,3,6,1,4,1,9,2,11,1,2,2,1,1),_MrSupervisorLogIndex_Type())
mrSupervisorLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrSupervisorLogIndex.setStatus(_A)
_MrSupervisorLogTime_Type=DisplayString
_MrSupervisorLogTime_Object=MibTableColumn
mrSupervisorLogTime=_MrSupervisorLogTime_Object((1,3,6,1,4,1,9,2,11,1,2,2,1,2),_MrSupervisorLogTime_Type())
mrSupervisorLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mrSupervisorLogTime.setStatus(_M)
_MrSupervisorLogInfo_Type=DisplayString
_MrSupervisorLogInfo_Object=MibTableColumn
mrSupervisorLogInfo=_MrSupervisorLogInfo_Object((1,3,6,1,4,1,9,2,11,1,2,2,1,3),_MrSupervisorLogInfo_Type())
mrSupervisorLogInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mrSupervisorLogInfo.setStatus(_A)
_MrSupervisorLogRelativeTime_Type=TimeTicks
_MrSupervisorLogRelativeTime_Object=MibTableColumn
mrSupervisorLogRelativeTime=_MrSupervisorLogRelativeTime_Object((1,3,6,1,4,1,9,2,11,1,2,2,1,4),_MrSupervisorLogRelativeTime_Type())
mrSupervisorLogRelativeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mrSupervisorLogRelativeTime.setStatus(_A)
_MrStackUnit_ObjectIdentity=ObjectIdentity
mrStackUnit=_MrStackUnit_ObjectIdentity((1,3,6,1,4,1,9,2,11,1,3))
_MrStackUnitTable_Object=MibTable
mrStackUnitTable=_MrStackUnitTable_Object((1,3,6,1,4,1,9,2,11,1,3,1))
if mibBuilder.loadTexts:mrStackUnitTable.setStatus(_A)
_MrStackUnitEntry_Object=MibTableRow
mrStackUnitEntry=_MrStackUnitEntry_Object((1,3,6,1,4,1,9,2,11,1,3,1,1))
mrStackUnitEntry.setIndexNames((0,_J,_R))
if mibBuilder.loadTexts:mrStackUnitEntry.setStatus(_A)
_MrStackUnitIndex_Type=Integer32
_MrStackUnitIndex_Object=MibTableColumn
mrStackUnitIndex=_MrStackUnitIndex_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,1),_MrStackUnitIndex_Type())
mrStackUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitIndex.setStatus(_A)
class _MrStackUnitPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitPresent_Type.__name__=_D
_MrStackUnitPresent_Object=MibTableColumn
mrStackUnitPresent=_MrStackUnitPresent_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,2),_MrStackUnitPresent_Type())
mrStackUnitPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitPresent.setStatus(_A)
_MrStackUnitFirstGroupIndex_Type=Integer32
_MrStackUnitFirstGroupIndex_Object=MibTableColumn
mrStackUnitFirstGroupIndex=_MrStackUnitFirstGroupIndex_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,3),_MrStackUnitFirstGroupIndex_Type())
mrStackUnitFirstGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitFirstGroupIndex.setStatus(_A)
_MrStackUnitLastGroupIndex_Type=Integer32
_MrStackUnitLastGroupIndex_Object=MibTableColumn
mrStackUnitLastGroupIndex=_MrStackUnitLastGroupIndex_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,4),_MrStackUnitLastGroupIndex_Type())
mrStackUnitLastGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitLastGroupIndex.setStatus(_A)
class _MrStackUnitSupervisorPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitSupervisorPresent_Type.__name__=_D
_MrStackUnitSupervisorPresent_Object=MibTableColumn
mrStackUnitSupervisorPresent=_MrStackUnitSupervisorPresent_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,5),_MrStackUnitSupervisorPresent_Type())
mrStackUnitSupervisorPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorPresent.setStatus(_A)
_MrStackUnitSupervisorMajorVersion_Type=Integer32
_MrStackUnitSupervisorMajorVersion_Object=MibTableColumn
mrStackUnitSupervisorMajorVersion=_MrStackUnitSupervisorMajorVersion_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,6),_MrStackUnitSupervisorMajorVersion_Type())
mrStackUnitSupervisorMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorMajorVersion.setStatus(_A)
_MrStackUnitSupervisorMinorVersion_Type=Integer32
_MrStackUnitSupervisorMinorVersion_Object=MibTableColumn
mrStackUnitSupervisorMinorVersion=_MrStackUnitSupervisorMinorVersion_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,7),_MrStackUnitSupervisorMinorVersion_Type())
mrStackUnitSupervisorMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorMinorVersion.setStatus(_A)
_MrStackUnitSupervisorBootstrapMajorVersion_Type=Integer32
_MrStackUnitSupervisorBootstrapMajorVersion_Object=MibTableColumn
mrStackUnitSupervisorBootstrapMajorVersion=_MrStackUnitSupervisorBootstrapMajorVersion_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,8),_MrStackUnitSupervisorBootstrapMajorVersion_Type())
mrStackUnitSupervisorBootstrapMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorBootstrapMajorVersion.setStatus(_A)
_MrStackUnitSupervisorBootstrapMinorVersion_Type=Integer32
_MrStackUnitSupervisorBootstrapMinorVersion_Object=MibTableColumn
mrStackUnitSupervisorBootstrapMinorVersion=_MrStackUnitSupervisorBootstrapMinorVersion_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,9),_MrStackUnitSupervisorBootstrapMinorVersion_Type())
mrStackUnitSupervisorBootstrapMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorBootstrapMinorVersion.setStatus(_A)
_MrStackUnitPOSTResult_Type=OctetString
_MrStackUnitPOSTResult_Object=MibTableColumn
mrStackUnitPOSTResult=_MrStackUnitPOSTResult_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,10),_MrStackUnitPOSTResult_Type())
mrStackUnitPOSTResult.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitPOSTResult.setStatus(_A)
class _MrStackUnitSupervisorIsPrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitSupervisorIsPrimary_Type.__name__=_D
_MrStackUnitSupervisorIsPrimary_Object=MibTableColumn
mrStackUnitSupervisorIsPrimary=_MrStackUnitSupervisorIsPrimary_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,11),_MrStackUnitSupervisorIsPrimary_Type())
mrStackUnitSupervisorIsPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSupervisorIsPrimary.setStatus(_A)
class _MrStackUnitExpansionModulePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitExpansionModulePresent_Type.__name__=_D
_MrStackUnitExpansionModulePresent_Object=MibTableColumn
mrStackUnitExpansionModulePresent=_MrStackUnitExpansionModulePresent_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,12),_MrStackUnitExpansionModulePresent_Type())
mrStackUnitExpansionModulePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitExpansionModulePresent.setStatus(_A)
class _MrStackUnitPortVisualIndicatorSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('portStatus',1),('unitNumber',2),('utilization',3)))
_MrStackUnitPortVisualIndicatorSelect_Type.__name__=_D
_MrStackUnitPortVisualIndicatorSelect_Object=MibTableColumn
mrStackUnitPortVisualIndicatorSelect=_MrStackUnitPortVisualIndicatorSelect_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,13),_MrStackUnitPortVisualIndicatorSelect_Type())
mrStackUnitPortVisualIndicatorSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitPortVisualIndicatorSelect.setStatus(_A)
_MrStackUnitBasePortVisualIndicatorGreenMap_Type=VisualLEDMap
_MrStackUnitBasePortVisualIndicatorGreenMap_Object=MibTableColumn
mrStackUnitBasePortVisualIndicatorGreenMap=_MrStackUnitBasePortVisualIndicatorGreenMap_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,14),_MrStackUnitBasePortVisualIndicatorGreenMap_Type())
mrStackUnitBasePortVisualIndicatorGreenMap.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitBasePortVisualIndicatorGreenMap.setStatus(_A)
_MrStackUnitBasePortVisualIndicatorAmberMap_Type=VisualLEDMap
_MrStackUnitBasePortVisualIndicatorAmberMap_Object=MibTableColumn
mrStackUnitBasePortVisualIndicatorAmberMap=_MrStackUnitBasePortVisualIndicatorAmberMap_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,15),_MrStackUnitBasePortVisualIndicatorAmberMap_Type())
mrStackUnitBasePortVisualIndicatorAmberMap.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitBasePortVisualIndicatorAmberMap.setStatus(_A)
_MrStackUnitExpansionPortVisualIndicatorGreenMap_Type=VisualLEDMap
_MrStackUnitExpansionPortVisualIndicatorGreenMap_Object=MibTableColumn
mrStackUnitExpansionPortVisualIndicatorGreenMap=_MrStackUnitExpansionPortVisualIndicatorGreenMap_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,16),_MrStackUnitExpansionPortVisualIndicatorGreenMap_Type())
mrStackUnitExpansionPortVisualIndicatorGreenMap.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitExpansionPortVisualIndicatorGreenMap.setStatus(_A)
_MrStackUnitExpansionPortVisualIndicatorAmberMap_Type=VisualLEDMap
_MrStackUnitExpansionPortVisualIndicatorAmberMap_Object=MibTableColumn
mrStackUnitExpansionPortVisualIndicatorAmberMap=_MrStackUnitExpansionPortVisualIndicatorAmberMap_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,17),_MrStackUnitExpansionPortVisualIndicatorAmberMap_Type())
mrStackUnitExpansionPortVisualIndicatorAmberMap.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitExpansionPortVisualIndicatorAmberMap.setStatus(_A)
class _MrStackUnitActivityVisualIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitActivityVisualIndicator_Type.__name__=_D
_MrStackUnitActivityVisualIndicator_Object=MibTableColumn
mrStackUnitActivityVisualIndicator=_MrStackUnitActivityVisualIndicator_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,18),_MrStackUnitActivityVisualIndicator_Type())
mrStackUnitActivityVisualIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitActivityVisualIndicator.setStatus(_A)
class _MrStackUnitCollisionVisualIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MrStackUnitCollisionVisualIndicator_Type.__name__=_D
_MrStackUnitCollisionVisualIndicator_Object=MibTableColumn
mrStackUnitCollisionVisualIndicator=_MrStackUnitCollisionVisualIndicator_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,19),_MrStackUnitCollisionVisualIndicator_Type())
mrStackUnitCollisionVisualIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitCollisionVisualIndicator.setStatus(_A)
class _MrStackUnitRPSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notPresent',1),('connectedFunctional',2),('connectedNotFunctional',3),('functionalPrimaryFailed',4)))
_MrStackUnitRPSStatus_Type.__name__=_D
_MrStackUnitRPSStatus_Object=MibTableColumn
mrStackUnitRPSStatus=_MrStackUnitRPSStatus_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,20),_MrStackUnitRPSStatus_Type())
mrStackUnitRPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitRPSStatus.setStatus(_A)
class _MrStackUnitRPSVisualIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('green',2),('amber',3)))
_MrStackUnitRPSVisualIndicator_Type.__name__=_D
_MrStackUnitRPSVisualIndicator_Object=MibTableColumn
mrStackUnitRPSVisualIndicator=_MrStackUnitRPSVisualIndicator_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,21),_MrStackUnitRPSVisualIndicator_Type())
mrStackUnitRPSVisualIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitRPSVisualIndicator.setStatus(_A)
_MrStackUnitSerialNumber_Type=DisplayString
_MrStackUnitSerialNumber_Object=MibTableColumn
mrStackUnitSerialNumber=_MrStackUnitSerialNumber_Object((1,3,6,1,4,1,9,2,11,1,3,1,1,22),_MrStackUnitSerialNumber_Type())
mrStackUnitSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mrStackUnitSerialNumber.setStatus(_A)
_MrNetMgmt_ObjectIdentity=ObjectIdentity
mrNetMgmt=_MrNetMgmt_ObjectIdentity((1,3,6,1,4,1,9,2,11,1,4))
_MrNetMgmtIpAddress_Type=IpAddress
_MrNetMgmtIpAddress_Object=MibScalar
mrNetMgmtIpAddress=_MrNetMgmtIpAddress_Object((1,3,6,1,4,1,9,2,11,1,4,1),_MrNetMgmtIpAddress_Type())
mrNetMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtIpAddress.setStatus(_A)
_MrNetMgmtIpSubnetMask_Type=IpAddress
_MrNetMgmtIpSubnetMask_Object=MibScalar
mrNetMgmtIpSubnetMask=_MrNetMgmtIpSubnetMask_Object((1,3,6,1,4,1,9,2,11,1,4,2),_MrNetMgmtIpSubnetMask_Type())
mrNetMgmtIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtIpSubnetMask.setStatus(_A)
_MrNetMgmtDefaultGateway_Type=IpAddress
_MrNetMgmtDefaultGateway_Object=MibScalar
mrNetMgmtDefaultGateway=_MrNetMgmtDefaultGateway_Object((1,3,6,1,4,1,9,2,11,1,4,3),_MrNetMgmtDefaultGateway_Type())
mrNetMgmtDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtDefaultGateway.setStatus(_A)
class _MrNetMgmtEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_MrNetMgmtEnableAuthenTraps_Type.__name__=_D
_MrNetMgmtEnableAuthenTraps_Object=MibScalar
mrNetMgmtEnableAuthenTraps=_MrNetMgmtEnableAuthenTraps_Object((1,3,6,1,4,1,9,2,11,1,4,4),_MrNetMgmtEnableAuthenTraps_Type())
mrNetMgmtEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtEnableAuthenTraps.setStatus(_A)
class _MrNetMgmtEnableRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_MrNetMgmtEnableRIP_Type.__name__=_D
_MrNetMgmtEnableRIP_Object=MibScalar
mrNetMgmtEnableRIP=_MrNetMgmtEnableRIP_Object((1,3,6,1,4,1,9,2,11,1,4,6),_MrNetMgmtEnableRIP_Type())
mrNetMgmtEnableRIP.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtEnableRIP.setStatus(_A)
class _MrNetMgmtConsoleInactTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_MrNetMgmtConsoleInactTime_Type.__name__=_D
_MrNetMgmtConsoleInactTime_Object=MibScalar
mrNetMgmtConsoleInactTime=_MrNetMgmtConsoleInactTime_Object((1,3,6,1,4,1,9,2,11,1,4,7),_MrNetMgmtConsoleInactTime_Type())
mrNetMgmtConsoleInactTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtConsoleInactTime.setStatus(_A)
class _MrNetMgmtConsolePasswordThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_MrNetMgmtConsolePasswordThreshold_Type.__name__=_D
_MrNetMgmtConsolePasswordThreshold_Object=MibScalar
mrNetMgmtConsolePasswordThreshold=_MrNetMgmtConsolePasswordThreshold_Object((1,3,6,1,4,1,9,2,11,1,4,8),_MrNetMgmtConsolePasswordThreshold_Type())
mrNetMgmtConsolePasswordThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtConsolePasswordThreshold.setStatus(_A)
class _MrNetMgmtConsoleSilentTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_MrNetMgmtConsoleSilentTime_Type.__name__=_D
_MrNetMgmtConsoleSilentTime_Object=MibScalar
mrNetMgmtConsoleSilentTime=_MrNetMgmtConsoleSilentTime_Object((1,3,6,1,4,1,9,2,11,1,4,9),_MrNetMgmtConsoleSilentTime_Type())
mrNetMgmtConsoleSilentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtConsoleSilentTime.setStatus(_A)
class _MrNetMgmtModemInitString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_MrNetMgmtModemInitString_Type.__name__=_E
_MrNetMgmtModemInitString_Object=MibScalar
mrNetMgmtModemInitString=_MrNetMgmtModemInitString_Object((1,3,6,1,4,1,9,2,11,1,4,10),_MrNetMgmtModemInitString_Type())
mrNetMgmtModemInitString.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtModemInitString.setStatus(_A)
class _MrNetMgmtModemDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_MrNetMgmtModemDialString_Type.__name__=_E
_MrNetMgmtModemDialString_Object=MibScalar
mrNetMgmtModemDialString=_MrNetMgmtModemDialString_Object((1,3,6,1,4,1,9,2,11,1,4,11),_MrNetMgmtModemDialString_Type())
mrNetMgmtModemDialString.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtModemDialString.setStatus(_A)
class _MrNetMgmtModemDialDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_MrNetMgmtModemDialDelay_Type.__name__=_D
_MrNetMgmtModemDialDelay_Object=MibScalar
mrNetMgmtModemDialDelay=_MrNetMgmtModemDialDelay_Object((1,3,6,1,4,1,9,2,11,1,4,12),_MrNetMgmtModemDialDelay_Type())
mrNetMgmtModemDialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtModemDialDelay.setStatus(_A)
class _MrNetMgmtModemAutoAnswer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_MrNetMgmtModemAutoAnswer_Type.__name__=_D
_MrNetMgmtModemAutoAnswer_Object=MibScalar
mrNetMgmtModemAutoAnswer=_MrNetMgmtModemAutoAnswer_Object((1,3,6,1,4,1,9,2,11,1,4,13),_MrNetMgmtModemAutoAnswer_Type())
mrNetMgmtModemAutoAnswer.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtModemAutoAnswer.setStatus(_A)
_MrNetMgmtDomainServer1IpAddress_Type=IpAddress
_MrNetMgmtDomainServer1IpAddress_Object=MibScalar
mrNetMgmtDomainServer1IpAddress=_MrNetMgmtDomainServer1IpAddress_Object((1,3,6,1,4,1,9,2,11,1,4,14),_MrNetMgmtDomainServer1IpAddress_Type())
mrNetMgmtDomainServer1IpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtDomainServer1IpAddress.setStatus(_A)
_MrNetMgmtDomainServer2IpAddress_Type=IpAddress
_MrNetMgmtDomainServer2IpAddress_Object=MibScalar
mrNetMgmtDomainServer2IpAddress=_MrNetMgmtDomainServer2IpAddress_Object((1,3,6,1,4,1,9,2,11,1,4,15),_MrNetMgmtDomainServer2IpAddress_Type())
mrNetMgmtDomainServer2IpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtDomainServer2IpAddress.setStatus(_A)
class _MrNetMgmtDefaultSearchDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MrNetMgmtDefaultSearchDomain_Type.__name__=_E
_MrNetMgmtDefaultSearchDomain_Object=MibScalar
mrNetMgmtDefaultSearchDomain=_MrNetMgmtDefaultSearchDomain_Object((1,3,6,1,4,1,9,2,11,1,4,16),_MrNetMgmtDefaultSearchDomain_Type())
mrNetMgmtDefaultSearchDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtDefaultSearchDomain.setStatus(_A)
_MrNetMgmtSetClientTable_Object=MibTable
mrNetMgmtSetClientTable=_MrNetMgmtSetClientTable_Object((1,3,6,1,4,1,9,2,11,1,4,17))
if mibBuilder.loadTexts:mrNetMgmtSetClientTable.setStatus(_A)
_MrNetMgmtSetClientEntry_Object=MibTableRow
mrNetMgmtSetClientEntry=_MrNetMgmtSetClientEntry_Object((1,3,6,1,4,1,9,2,11,1,4,17,1))
mrNetMgmtSetClientEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:mrNetMgmtSetClientEntry.setStatus(_A)
class _MrNetMgmtSetClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_MrNetMgmtSetClientIndex_Type.__name__=_D
_MrNetMgmtSetClientIndex_Object=MibTableColumn
mrNetMgmtSetClientIndex=_MrNetMgmtSetClientIndex_Object((1,3,6,1,4,1,9,2,11,1,4,17,1,1),_MrNetMgmtSetClientIndex_Type())
mrNetMgmtSetClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrNetMgmtSetClientIndex.setStatus(_A)
_MrNetMgmtSetClientName_Type=DisplayString
_MrNetMgmtSetClientName_Object=MibTableColumn
mrNetMgmtSetClientName=_MrNetMgmtSetClientName_Object((1,3,6,1,4,1,9,2,11,1,4,17,1,2),_MrNetMgmtSetClientName_Type())
mrNetMgmtSetClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtSetClientName.setStatus(_A)
class _MrNetMgmtSetClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_T,2),(_U,3)))
_MrNetMgmtSetClientStatus_Type.__name__=_D
_MrNetMgmtSetClientStatus_Object=MibTableColumn
mrNetMgmtSetClientStatus=_MrNetMgmtSetClientStatus_Object((1,3,6,1,4,1,9,2,11,1,4,17,1,3),_MrNetMgmtSetClientStatus_Type())
mrNetMgmtSetClientStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtSetClientStatus.setStatus(_A)
_MrNetMgmtTrapClientTable_Object=MibTable
mrNetMgmtTrapClientTable=_MrNetMgmtTrapClientTable_Object((1,3,6,1,4,1,9,2,11,1,4,18))
if mibBuilder.loadTexts:mrNetMgmtTrapClientTable.setStatus(_A)
_MrNetMgmtTrapClientEntry_Object=MibTableRow
mrNetMgmtTrapClientEntry=_MrNetMgmtTrapClientEntry_Object((1,3,6,1,4,1,9,2,11,1,4,18,1))
mrNetMgmtTrapClientEntry.setIndexNames((0,_J,_V))
if mibBuilder.loadTexts:mrNetMgmtTrapClientEntry.setStatus(_A)
class _MrNetMgmtTrapClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_MrNetMgmtTrapClientIndex_Type.__name__=_D
_MrNetMgmtTrapClientIndex_Object=MibTableColumn
mrNetMgmtTrapClientIndex=_MrNetMgmtTrapClientIndex_Object((1,3,6,1,4,1,9,2,11,1,4,18,1,1),_MrNetMgmtTrapClientIndex_Type())
mrNetMgmtTrapClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mrNetMgmtTrapClientIndex.setStatus(_A)
_MrNetMgmtTrapClientName_Type=DisplayString
_MrNetMgmtTrapClientName_Object=MibTableColumn
mrNetMgmtTrapClientName=_MrNetMgmtTrapClientName_Object((1,3,6,1,4,1,9,2,11,1,4,18,1,2),_MrNetMgmtTrapClientName_Type())
mrNetMgmtTrapClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtTrapClientName.setStatus(_A)
class _MrNetMgmtTrapClientComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MrNetMgmtTrapClientComm_Type.__name__=_E
_MrNetMgmtTrapClientComm_Object=MibTableColumn
mrNetMgmtTrapClientComm=_MrNetMgmtTrapClientComm_Object((1,3,6,1,4,1,9,2,11,1,4,18,1,3),_MrNetMgmtTrapClientComm_Type())
mrNetMgmtTrapClientComm.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtTrapClientComm.setStatus(_A)
class _MrNetMgmtTrapClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_T,2),(_U,3)))
_MrNetMgmtTrapClientStatus_Type.__name__=_D
_MrNetMgmtTrapClientStatus_Object=MibTableColumn
mrNetMgmtTrapClientStatus=_MrNetMgmtTrapClientStatus_Object((1,3,6,1,4,1,9,2,11,1,4,18,1,4),_MrNetMgmtTrapClientStatus_Type())
mrNetMgmtTrapClientStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrNetMgmtTrapClientStatus.setStatus(_A)
_MrUpgrade_ObjectIdentity=ObjectIdentity
mrUpgrade=_MrUpgrade_ObjectIdentity((1,3,6,1,4,1,9,2,11,1,5))
_MrUpgradeFlashSize_Type=Integer32
_MrUpgradeFlashSize_Object=MibScalar
mrUpgradeFlashSize=_MrUpgradeFlashSize_Object((1,3,6,1,4,1,9,2,11,1,5,1),_MrUpgradeFlashSize_Type())
mrUpgradeFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mrUpgradeFlashSize.setStatus(_A)
class _MrUpgradeLastUpgradeTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_MrUpgradeLastUpgradeTime_Type.__name__=_E
_MrUpgradeLastUpgradeTime_Object=MibScalar
mrUpgradeLastUpgradeTime=_MrUpgradeLastUpgradeTime_Object((1,3,6,1,4,1,9,2,11,1,5,2),_MrUpgradeLastUpgradeTime_Type())
mrUpgradeLastUpgradeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mrUpgradeLastUpgradeTime.setStatus(_M)
_MrUpgradeLastUpgradeSource_Type=DisplayString
_MrUpgradeLastUpgradeSource_Object=MibScalar
mrUpgradeLastUpgradeSource=_MrUpgradeLastUpgradeSource_Object((1,3,6,1,4,1,9,2,11,1,5,3),_MrUpgradeLastUpgradeSource_Type())
mrUpgradeLastUpgradeSource.setMaxAccess(_B)
if mibBuilder.loadTexts:mrUpgradeLastUpgradeSource.setStatus(_A)
class _MrUpgradeLastUpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('inProgress',2),('success',3),('failure',4)))
_MrUpgradeLastUpgradeStatus_Type.__name__=_D
_MrUpgradeLastUpgradeStatus_Object=MibScalar
mrUpgradeLastUpgradeStatus=_MrUpgradeLastUpgradeStatus_Object((1,3,6,1,4,1,9,2,11,1,5,4),_MrUpgradeLastUpgradeStatus_Type())
mrUpgradeLastUpgradeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mrUpgradeLastUpgradeStatus.setStatus(_A)
_MrUpgradeTFTPServerAddress_Type=DisplayString
_MrUpgradeTFTPServerAddress_Object=MibScalar
mrUpgradeTFTPServerAddress=_MrUpgradeTFTPServerAddress_Object((1,3,6,1,4,1,9,2,11,1,5,5),_MrUpgradeTFTPServerAddress_Type())
mrUpgradeTFTPServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mrUpgradeTFTPServerAddress.setStatus(_A)
class _MrUpgradeTFTPLoadFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_MrUpgradeTFTPLoadFilename_Type.__name__=_E
_MrUpgradeTFTPLoadFilename_Object=MibScalar
mrUpgradeTFTPLoadFilename=_MrUpgradeTFTPLoadFilename_Object((1,3,6,1,4,1,9,2,11,1,5,6),_MrUpgradeTFTPLoadFilename_Type())
mrUpgradeTFTPLoadFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:mrUpgradeTFTPLoadFilename.setStatus(_A)
class _MrUpgradeTFTPInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upgrade',1),('noUpgrade',2)))
_MrUpgradeTFTPInitiate_Type.__name__=_D
_MrUpgradeTFTPInitiate_Object=MibScalar
mrUpgradeTFTPInitiate=_MrUpgradeTFTPInitiate_Object((1,3,6,1,4,1,9,2,11,1,5,7),_MrUpgradeTFTPInitiate_Type())
mrUpgradeTFTPInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:mrUpgradeTFTPInitiate.setStatus(_A)
class _MrUpgradeTFTPAccept_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_MrUpgradeTFTPAccept_Type.__name__=_D
_MrUpgradeTFTPAccept_Object=MibScalar
mrUpgradeTFTPAccept=_MrUpgradeTFTPAccept_Object((1,3,6,1,4,1,9,2,11,1,5,8),_MrUpgradeTFTPAccept_Type())
mrUpgradeTFTPAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:mrUpgradeTFTPAccept.setStatus(_A)
logonIntruder=NotificationType((1,3,6,1,4,1,9,2,11,1,0,0))
logonIntruder.setObjects((_H,_I))
if mibBuilder.loadTexts:logonIntruder.setStatus('')
hubStackDiagnostic=NotificationType((1,3,6,1,4,1,9,2,11,1,0,1))
hubStackDiagnostic.setObjects((_H,_I))
if mibBuilder.loadTexts:hubStackDiagnostic.setStatus('')
rpsFailed=NotificationType((1,3,6,1,4,1,9,2,11,1,0,2))
rpsFailed.setObjects((_H,_I))
if mibBuilder.loadTexts:rpsFailed.setStatus('')
ipAddressChange=NotificationType((1,3,6,1,4,1,9,2,11,1,0,3))
ipAddressChange.setObjects((_H,_I))
if mibBuilder.loadTexts:ipAddressChange.setStatus('')
mibBuilder.exportSymbols(_J,**{'VisualLEDMap':VisualLEDMap,'ciscoFastHubMIB':ciscoFastHubMIB,'ciscoFastHubMIBObjects':ciscoFastHubMIBObjects,'logonIntruder':logonIntruder,'hubStackDiagnostic':hubStackDiagnostic,'rpsFailed':rpsFailed,'ipAddressChange':ipAddressChange,'mrStack':mrStack,'mrStackUnitCapacity':mrStackUnitCapacity,'mrStackNumberOfUnitsPresent':mrStackNumberOfUnitsPresent,'mrStackSelectPrimarySupervisorUnit':mrStackSelectPrimarySupervisorUnit,'mrStackPOSTSelect':mrStackPOSTSelect,'mrStackReset':mrStackReset,'mrStackDefaultReset':mrStackDefaultReset,'mrStackClearStatistics':mrStackClearStatistics,'mrStackShortJabberLoopCorrections':mrStackShortJabberLoopCorrections,'mrSupervisorLog':mrSupervisorLog,'mrSupervisorLogTableClear':mrSupervisorLogTableClear,'mrSupervisorLogTable':mrSupervisorLogTable,'mrSupervisorLogEntry':mrSupervisorLogEntry,_Q:mrSupervisorLogIndex,'mrSupervisorLogTime':mrSupervisorLogTime,'mrSupervisorLogInfo':mrSupervisorLogInfo,'mrSupervisorLogRelativeTime':mrSupervisorLogRelativeTime,'mrStackUnit':mrStackUnit,'mrStackUnitTable':mrStackUnitTable,'mrStackUnitEntry':mrStackUnitEntry,_R:mrStackUnitIndex,'mrStackUnitPresent':mrStackUnitPresent,'mrStackUnitFirstGroupIndex':mrStackUnitFirstGroupIndex,'mrStackUnitLastGroupIndex':mrStackUnitLastGroupIndex,'mrStackUnitSupervisorPresent':mrStackUnitSupervisorPresent,'mrStackUnitSupervisorMajorVersion':mrStackUnitSupervisorMajorVersion,'mrStackUnitSupervisorMinorVersion':mrStackUnitSupervisorMinorVersion,'mrStackUnitSupervisorBootstrapMajorVersion':mrStackUnitSupervisorBootstrapMajorVersion,'mrStackUnitSupervisorBootstrapMinorVersion':mrStackUnitSupervisorBootstrapMinorVersion,'mrStackUnitPOSTResult':mrStackUnitPOSTResult,'mrStackUnitSupervisorIsPrimary':mrStackUnitSupervisorIsPrimary,'mrStackUnitExpansionModulePresent':mrStackUnitExpansionModulePresent,'mrStackUnitPortVisualIndicatorSelect':mrStackUnitPortVisualIndicatorSelect,'mrStackUnitBasePortVisualIndicatorGreenMap':mrStackUnitBasePortVisualIndicatorGreenMap,'mrStackUnitBasePortVisualIndicatorAmberMap':mrStackUnitBasePortVisualIndicatorAmberMap,'mrStackUnitExpansionPortVisualIndicatorGreenMap':mrStackUnitExpansionPortVisualIndicatorGreenMap,'mrStackUnitExpansionPortVisualIndicatorAmberMap':mrStackUnitExpansionPortVisualIndicatorAmberMap,'mrStackUnitActivityVisualIndicator':mrStackUnitActivityVisualIndicator,'mrStackUnitCollisionVisualIndicator':mrStackUnitCollisionVisualIndicator,'mrStackUnitRPSStatus':mrStackUnitRPSStatus,'mrStackUnitRPSVisualIndicator':mrStackUnitRPSVisualIndicator,'mrStackUnitSerialNumber':mrStackUnitSerialNumber,'mrNetMgmt':mrNetMgmt,'mrNetMgmtIpAddress':mrNetMgmtIpAddress,'mrNetMgmtIpSubnetMask':mrNetMgmtIpSubnetMask,'mrNetMgmtDefaultGateway':mrNetMgmtDefaultGateway,'mrNetMgmtEnableAuthenTraps':mrNetMgmtEnableAuthenTraps,'mrNetMgmtEnableRIP':mrNetMgmtEnableRIP,'mrNetMgmtConsoleInactTime':mrNetMgmtConsoleInactTime,'mrNetMgmtConsolePasswordThreshold':mrNetMgmtConsolePasswordThreshold,'mrNetMgmtConsoleSilentTime':mrNetMgmtConsoleSilentTime,'mrNetMgmtModemInitString':mrNetMgmtModemInitString,'mrNetMgmtModemDialString':mrNetMgmtModemDialString,'mrNetMgmtModemDialDelay':mrNetMgmtModemDialDelay,'mrNetMgmtModemAutoAnswer':mrNetMgmtModemAutoAnswer,'mrNetMgmtDomainServer1IpAddress':mrNetMgmtDomainServer1IpAddress,'mrNetMgmtDomainServer2IpAddress':mrNetMgmtDomainServer2IpAddress,'mrNetMgmtDefaultSearchDomain':mrNetMgmtDefaultSearchDomain,'mrNetMgmtSetClientTable':mrNetMgmtSetClientTable,'mrNetMgmtSetClientEntry':mrNetMgmtSetClientEntry,_S:mrNetMgmtSetClientIndex,'mrNetMgmtSetClientName':mrNetMgmtSetClientName,'mrNetMgmtSetClientStatus':mrNetMgmtSetClientStatus,'mrNetMgmtTrapClientTable':mrNetMgmtTrapClientTable,'mrNetMgmtTrapClientEntry':mrNetMgmtTrapClientEntry,_V:mrNetMgmtTrapClientIndex,'mrNetMgmtTrapClientName':mrNetMgmtTrapClientName,'mrNetMgmtTrapClientComm':mrNetMgmtTrapClientComm,'mrNetMgmtTrapClientStatus':mrNetMgmtTrapClientStatus,'mrUpgrade':mrUpgrade,'mrUpgradeFlashSize':mrUpgradeFlashSize,'mrUpgradeLastUpgradeTime':mrUpgradeLastUpgradeTime,'mrUpgradeLastUpgradeSource':mrUpgradeLastUpgradeSource,'mrUpgradeLastUpgradeStatus':mrUpgradeLastUpgradeStatus,'mrUpgradeTFTPServerAddress':mrUpgradeTFTPServerAddress,'mrUpgradeTFTPLoadFilename':mrUpgradeTFTPLoadFilename,'mrUpgradeTFTPInitiate':mrUpgradeTFTPInitiate,'mrUpgradeTFTPAccept':mrUpgradeTFTPAccept})