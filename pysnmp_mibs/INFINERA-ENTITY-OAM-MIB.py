_S='oamGroup'
_R='oamCBandSoakCapableFW'
_Q='oamRowStatus'
_P='oamGain'
_O='oamOperatingMode'
_N='oamTilt'
_M='oamRxDampSeqNum'
_L='oamLaunchPowerOffset'
_K='oamRxLastAmpDeviceCommitTs'
_J='oamRxAmpDeviceTarget'
_I='oamRxAmpDeviceSetpoint'
_H='oamProvisonedType'
_G='oamMoId'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-create'
_B='INFINERA-ENTITY-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType,InfnOAOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEqptType','InfnOAOperatingMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
oamMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,11))
_OamTable_Object=MibTable
oamTable=_OamTable_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1))
if mibBuilder.loadTexts:oamTable.setStatus(_A)
_OamEntry_Object=MibTableRow
oamEntry=_OamEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1))
oamEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oamEntry.setStatus(_A)
_OamMoId_Type=DisplayString
_OamMoId_Object=MibTableColumn
oamMoId=_OamMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,1),_OamMoId_Type())
oamMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:oamMoId.setStatus(_A)
_OamProvisonedType_Type=InfnEqptType
_OamProvisonedType_Object=MibTableColumn
oamProvisonedType=_OamProvisonedType_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,2),_OamProvisonedType_Type())
oamProvisonedType.setMaxAccess(_C)
if mibBuilder.loadTexts:oamProvisonedType.setStatus(_A)
_OamRxAmpDeviceSetpoint_Type=FloatTenths
_OamRxAmpDeviceSetpoint_Object=MibTableColumn
oamRxAmpDeviceSetpoint=_OamRxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,3),_OamRxAmpDeviceSetpoint_Type())
oamRxAmpDeviceSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:oamRxAmpDeviceSetpoint.setStatus(_A)
_OamRxAmpDeviceTarget_Type=FloatTenths
_OamRxAmpDeviceTarget_Object=MibTableColumn
oamRxAmpDeviceTarget=_OamRxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,4),_OamRxAmpDeviceTarget_Type())
oamRxAmpDeviceTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:oamRxAmpDeviceTarget.setStatus(_A)
_OamRxLastAmpDeviceCommitTs_Type=Integer32
_OamRxLastAmpDeviceCommitTs_Object=MibTableColumn
oamRxLastAmpDeviceCommitTs=_OamRxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,5),_OamRxLastAmpDeviceCommitTs_Type())
oamRxLastAmpDeviceCommitTs.setMaxAccess(_D)
if mibBuilder.loadTexts:oamRxLastAmpDeviceCommitTs.setStatus(_A)
_OamLaunchPowerOffset_Type=FloatTenths
_OamLaunchPowerOffset_Object=MibTableColumn
oamLaunchPowerOffset=_OamLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,6),_OamLaunchPowerOffset_Type())
oamLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:oamLaunchPowerOffset.setStatus(_A)
_OamRxDampSeqNum_Type=Integer32
_OamRxDampSeqNum_Object=MibTableColumn
oamRxDampSeqNum=_OamRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,7),_OamRxDampSeqNum_Type())
oamRxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:oamRxDampSeqNum.setStatus(_A)
_OamTilt_Type=FloatTenths
_OamTilt_Object=MibTableColumn
oamTilt=_OamTilt_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,8),_OamTilt_Type())
oamTilt.setMaxAccess(_C)
if mibBuilder.loadTexts:oamTilt.setStatus(_A)
_OamOperatingMode_Type=InfnOAOperatingMode
_OamOperatingMode_Object=MibTableColumn
oamOperatingMode=_OamOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,9),_OamOperatingMode_Type())
oamOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oamOperatingMode.setStatus(_A)
_OamGain_Type=FloatTenths
_OamGain_Object=MibTableColumn
oamGain=_OamGain_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,10),_OamGain_Type())
oamGain.setMaxAccess(_C)
if mibBuilder.loadTexts:oamGain.setStatus(_A)
_OamRowStatus_Type=RowStatus
_OamRowStatus_Object=MibTableColumn
oamRowStatus=_OamRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,11),_OamRowStatus_Type())
oamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oamRowStatus.setStatus(_A)
_OamCBandSoakCapableFW_Type=TruthValue
_OamCBandSoakCapableFW_Object=MibTableColumn
oamCBandSoakCapableFW=_OamCBandSoakCapableFW_Object((1,3,6,1,4,1,21296,2,2,2,1,11,1,1,12),_OamCBandSoakCapableFW_Type())
oamCBandSoakCapableFW.setMaxAccess(_D)
if mibBuilder.loadTexts:oamCBandSoakCapableFW.setStatus(_A)
_OamConformance_ObjectIdentity=ObjectIdentity
oamConformance=_OamConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,11,3))
_OamCompliances_ObjectIdentity=ObjectIdentity
oamCompliances=_OamCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,11,3,1))
_OamGroups_ObjectIdentity=ObjectIdentity
oamGroups=_OamGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,11,3,2))
oamGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,11,3,2,1))
oamGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:oamGroup.setStatus(_A)
oamCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,11,3,1,1))
oamCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:oamCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oamMIB':oamMIB,'oamTable':oamTable,'oamEntry':oamEntry,_G:oamMoId,_H:oamProvisonedType,_I:oamRxAmpDeviceSetpoint,_J:oamRxAmpDeviceTarget,_K:oamRxLastAmpDeviceCommitTs,_L:oamLaunchPowerOffset,_M:oamRxDampSeqNum,_N:oamTilt,_O:oamOperatingMode,_P:oamGain,_Q:oamRowStatus,_R:oamCBandSoakCapableFW,'oamConformance':oamConformance,'oamCompliances':oamCompliances,'oamCompliance':oamCompliance,'oamGroups':oamGroups,_S:oamGroup})