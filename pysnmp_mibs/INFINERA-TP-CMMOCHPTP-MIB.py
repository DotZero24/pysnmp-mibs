_V='cmmOchPtpGroup'
_U='cmmOchPtpModulationCatagory'
_T='cmmOchPtpPowerControlLoop'
_S='cmmOchPtpTargetPowerOffset'
_R='cmmOchPtpInterfaceType'
_Q='cmmOchPtpWavelengthDetectedState'
_P='cmmOchPtpDiscoveredWavelength'
_O='cmmOchPtpDiscoveredOchPortId'
_N='cmmOchPtpProvisionedOchPort'
_M='cmmOchPtpPmHistStatsEnable'
_L='cmmOchPtpProvisionedOchOWPortId'
_K='Integer32'
_J='InfnPmHistStatsControl'
_I='InfnModulationCategory'
_H='InfnEnableDisableType'
_G='FloatHundredths'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-CMMOCHPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnEnableDisableType,InfnModulationCategory,InfnPmHistStatsControl,InfnServiceType,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB',_G,_H,_I,_J,'InfnServiceType','InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cmmOchPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,29))
if mibBuilder.loadTexts:cmmOchPtpMIB.setRevisions(('2008-10-20 00:00',))
_CmmOchPtpTable_Object=MibTable
cmmOchPtpTable=_CmmOchPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1))
if mibBuilder.loadTexts:cmmOchPtpTable.setStatus(_A)
_CmmOchPtpEntry_Object=MibTableRow
cmmOchPtpEntry=_CmmOchPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1))
cmmOchPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cmmOchPtpEntry.setStatus(_A)
_CmmOchPtpProvisionedOchOWPortId_Type=Integer32
_CmmOchPtpProvisionedOchOWPortId_Object=MibTableColumn
cmmOchPtpProvisionedOchOWPortId=_CmmOchPtpProvisionedOchOWPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,1),_CmmOchPtpProvisionedOchOWPortId_Type())
cmmOchPtpProvisionedOchOWPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpProvisionedOchOWPortId.setStatus(_A)
class _CmmOchPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_CmmOchPtpPmHistStatsEnable_Type.__name__=_J
_CmmOchPtpPmHistStatsEnable_Object=MibTableColumn
cmmOchPtpPmHistStatsEnable=_CmmOchPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,2),_CmmOchPtpPmHistStatsEnable_Type())
cmmOchPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOchPtpPmHistStatsEnable.setStatus(_A)
_CmmOchPtpProvisionedOchPort_Type=DisplayString
_CmmOchPtpProvisionedOchPort_Object=MibTableColumn
cmmOchPtpProvisionedOchPort=_CmmOchPtpProvisionedOchPort_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,3),_CmmOchPtpProvisionedOchPort_Type())
cmmOchPtpProvisionedOchPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOchPtpProvisionedOchPort.setStatus(_A)
_CmmOchPtpDiscoveredOchPortId_Type=DisplayString
_CmmOchPtpDiscoveredOchPortId_Object=MibTableColumn
cmmOchPtpDiscoveredOchPortId=_CmmOchPtpDiscoveredOchPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,4),_CmmOchPtpDiscoveredOchPortId_Type())
cmmOchPtpDiscoveredOchPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpDiscoveredOchPortId.setStatus(_A)
_CmmOchPtpDiscoveredWavelength_Type=FloatHundredths
_CmmOchPtpDiscoveredWavelength_Object=MibTableColumn
cmmOchPtpDiscoveredWavelength=_CmmOchPtpDiscoveredWavelength_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,5),_CmmOchPtpDiscoveredWavelength_Type())
cmmOchPtpDiscoveredWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpDiscoveredWavelength.setStatus(_A)
class _CmmOchPtpWavelengthDetectedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('notStarted',2),('failed',3),('notValid',4),('shutdown',5),('inprogress',6),('completed',7)))
_CmmOchPtpWavelengthDetectedState_Type.__name__=_K
_CmmOchPtpWavelengthDetectedState_Object=MibTableColumn
cmmOchPtpWavelengthDetectedState=_CmmOchPtpWavelengthDetectedState_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,6),_CmmOchPtpWavelengthDetectedState_Type())
cmmOchPtpWavelengthDetectedState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpWavelengthDetectedState.setStatus(_A)
_CmmOchPtpInterfaceType_Type=InfnWaveInterfaceType
_CmmOchPtpInterfaceType_Object=MibTableColumn
cmmOchPtpInterfaceType=_CmmOchPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,7),_CmmOchPtpInterfaceType_Type())
cmmOchPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOchPtpInterfaceType.setStatus(_A)
class _CmmOchPtpTargetPowerOffset_Type(FloatHundredths):defaultValue=0
_CmmOchPtpTargetPowerOffset_Type.__name__=_G
_CmmOchPtpTargetPowerOffset_Object=MibTableColumn
cmmOchPtpTargetPowerOffset=_CmmOchPtpTargetPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,8),_CmmOchPtpTargetPowerOffset_Type())
cmmOchPtpTargetPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpTargetPowerOffset.setStatus(_A)
class _CmmOchPtpPowerControlLoop_Type(InfnEnableDisableType):defaultValue=2
_CmmOchPtpPowerControlLoop_Type.__name__=_H
_CmmOchPtpPowerControlLoop_Object=MibTableColumn
cmmOchPtpPowerControlLoop=_CmmOchPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,9),_CmmOchPtpPowerControlLoop_Type())
cmmOchPtpPowerControlLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOchPtpPowerControlLoop.setStatus(_A)
class _CmmOchPtpModulationCatagory_Type(InfnModulationCategory):defaultValue=1
_CmmOchPtpModulationCatagory_Type.__name__=_I
_CmmOchPtpModulationCatagory_Object=MibTableColumn
cmmOchPtpModulationCatagory=_CmmOchPtpModulationCatagory_Object((1,3,6,1,4,1,21296,2,2,2,2,29,1,1,10),_CmmOchPtpModulationCatagory_Type())
cmmOchPtpModulationCatagory.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmOchPtpModulationCatagory.setStatus(_A)
_CmmOchPtpConformance_ObjectIdentity=ObjectIdentity
cmmOchPtpConformance=_CmmOchPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,29,3))
_CmmOchPtpCompliances_ObjectIdentity=ObjectIdentity
cmmOchPtpCompliances=_CmmOchPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,29,3,1))
_CmmOchPtpGroups_ObjectIdentity=ObjectIdentity
cmmOchPtpGroups=_CmmOchPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,29,3,2))
cmmOchPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,29,3,2,1))
cmmOchPtpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cmmOchPtpGroup.setStatus(_A)
cmmOchPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,29,3,1,1))
cmmOchPtpCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:cmmOchPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmOchPtpMIB':cmmOchPtpMIB,'cmmOchPtpTable':cmmOchPtpTable,'cmmOchPtpEntry':cmmOchPtpEntry,_L:cmmOchPtpProvisionedOchOWPortId,_M:cmmOchPtpPmHistStatsEnable,_N:cmmOchPtpProvisionedOchPort,_O:cmmOchPtpDiscoveredOchPortId,_P:cmmOchPtpDiscoveredWavelength,_Q:cmmOchPtpWavelengthDetectedState,_R:cmmOchPtpInterfaceType,_S:cmmOchPtpTargetPowerOffset,_T:cmmOchPtpPowerControlLoop,_U:cmmOchPtpModulationCatagory,'cmmOchPtpConformance':cmmOchPtpConformance,'cmmOchPtpCompliances':cmmOchPtpCompliances,'cmmOchPtpCompliance':cmmOchPtpCompliance,'cmmOchPtpGroups':cmmOchPtpGroups,_V:cmmOchPtpGroup})