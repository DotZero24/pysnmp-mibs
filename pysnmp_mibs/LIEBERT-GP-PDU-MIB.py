_AE='lgpPduAuxSensorOrderIndex'
_AD='alarm-when-open'
_AC='lgpPduAuxMeasSensorMeasurementIndex'
_AB='lgpPduAuxMeasSensorIndex'
_AA='temperature'
_A9='lgpPduAuxSensorIndex'
_A8='cycle-power'
_A7='lgpPduRcpEntryIndex'
_A6='lgpPduRbLineEntryIndex'
_A5='unknown-line-line'
_A4='unknown-line-neutral'
_A3='line-3-line-1'
_A2='line-2-line-3'
_A1='line-1-line-2'
_A0='current-measurement-and-control'
_z='current-measurement-only'
_y='control-only'
_x='measurement-and-control'
_w='measurement-only'
_v='no-optional-capabilities'
_u='nema-L6-30R-30-Amp'
_t='cee-7-type-E-schuko'
_s='iec-C19-sheet-J-16-Amp'
_r='iec-C13-sheet-F-10-Amp'
_q='nema-5-20R-20-Amp'
_p='phase3'
_o='phase2'
_n='phase1'
_m='lgpPduPsLineEntryIndex'
_l='0.001 Amp-AC-RMS'
_k='lgpPduRcpGroupIndex'
_j='0.01 Amp-AC-RMS'
_i='Volts-AC-RMS'
_h='0.1 Volts-AC-RMS'
_g='0.1 Kilowatt-Hour'
_f='lgpPduPsEntryIndex'
_e='enable'
_d='disabled'
_c='no-action'
_b='on'
_a='off'
_Z='0.1 VoltRMS'
_Y='lgpPduRbEntryIndex'
_X='0.1 Percent'
_W='0.1 Amps-AC-RMS'
_V='VoltRMS'
_U='Seconds'
_T='0.1 Pascal'
_S='0.01 Amps-AC-RMS'
_R='0.01 Power Factor'
_Q='VoltAmp'
_P='0.1 Amp-AC-RMS'
_O='Watt'
_N='0.1 percent Relative Humidity'
_M='0.1 degrees Celsius'
_L='0.1 degrees Fahrenheit'
_K='lgpPduEntryIndex'
_J='Count'
_I='not-specified'
_H='not-accessible'
_G='Percent'
_F='LIEBERT-GP-PDU-MIB'
_E='Integer32'
_D='deprecated'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpPdu,liebertPduModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpPdu','liebertPduModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertGlobalProductsPduModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,9,1))
if mibBuilder.loadTexts:liebertGlobalProductsPduModule.setRevisions(('2008-07-02 00:00',))
_LgpPduGlobalData_ObjectIdentity=ObjectIdentity
lgpPduGlobalData=_LgpPduGlobalData_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,5))
if mibBuilder.loadTexts:lgpPduGlobalData.setStatus(_A)
class _LgpPduEntrySWOverTemperatureProtectionConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('local',0),('array',1)))
_LgpPduEntrySWOverTemperatureProtectionConfig_Type.__name__=_E
_LgpPduEntrySWOverTemperatureProtectionConfig_Object=MibScalar
lgpPduEntrySWOverTemperatureProtectionConfig=_LgpPduEntrySWOverTemperatureProtectionConfig_Object((1,3,6,1,4,1,476,1,42,3,8,5,5),_LgpPduEntrySWOverTemperatureProtectionConfig_Type())
lgpPduEntrySWOverTemperatureProtectionConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntrySWOverTemperatureProtectionConfig.setStatus(_A)
_LgpPduEntrySWOverTemperatureProtectionDelay_Type=Unsigned32
_LgpPduEntrySWOverTemperatureProtectionDelay_Object=MibScalar
lgpPduEntrySWOverTemperatureProtectionDelay=_LgpPduEntrySWOverTemperatureProtectionDelay_Object((1,3,6,1,4,1,476,1,42,3,8,5,10),_LgpPduEntrySWOverTemperatureProtectionDelay_Type())
lgpPduEntrySWOverTemperatureProtectionDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntrySWOverTemperatureProtectionDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPduEntrySWOverTemperatureProtectionDelay.setUnits(_U)
_LgpPduCluster_ObjectIdentity=ObjectIdentity
lgpPduCluster=_LgpPduCluster_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,10))
if mibBuilder.loadTexts:lgpPduCluster.setStatus(_A)
_LgpPduGrpSysStatus_Type=Unsigned32
_LgpPduGrpSysStatus_Object=MibScalar
lgpPduGrpSysStatus=_LgpPduGrpSysStatus_Object((1,3,6,1,4,1,476,1,42,3,8,10,5),_LgpPduGrpSysStatus_Type())
lgpPduGrpSysStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduGrpSysStatus.setStatus(_A)
_LgpPduTableCount_Type=Unsigned32
_LgpPduTableCount_Object=MibScalar
lgpPduTableCount=_LgpPduTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,19),_LgpPduTableCount_Type())
lgpPduTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduTableCount.setUnits(_J)
_LgpPduTable_Object=MibTable
lgpPduTable=_LgpPduTable_Object((1,3,6,1,4,1,476,1,42,3,8,20))
if mibBuilder.loadTexts:lgpPduTable.setStatus(_A)
_LgpPduEntry_Object=MibTableRow
lgpPduEntry=_LgpPduEntry_Object((1,3,6,1,4,1,476,1,42,3,8,20,1))
lgpPduEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:lgpPduEntry.setStatus(_A)
_LgpPduEntryIndex_Type=Unsigned32
_LgpPduEntryIndex_Object=MibTableColumn
lgpPduEntryIndex=_LgpPduEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,1),_LgpPduEntryIndex_Type())
lgpPduEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduEntryIndex.setStatus(_A)
_LgpPduEntryId_Type=Unsigned32
_LgpPduEntryId_Object=MibTableColumn
lgpPduEntryId=_LgpPduEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,5),_LgpPduEntryId_Type())
lgpPduEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntryId.setStatus(_A)
_LgpPduEntryUsrLabel_Type=DisplayString
_LgpPduEntryUsrLabel_Object=MibTableColumn
lgpPduEntryUsrLabel=_LgpPduEntryUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,10),_LgpPduEntryUsrLabel_Type())
lgpPduEntryUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntryUsrLabel.setStatus(_A)
_LgpPduEntrySysAssignLabel_Type=DisplayString
_LgpPduEntrySysAssignLabel_Object=MibTableColumn
lgpPduEntrySysAssignLabel=_LgpPduEntrySysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,15),_LgpPduEntrySysAssignLabel_Type())
lgpPduEntrySysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntrySysAssignLabel.setStatus(_A)
_LgpPduEntryPositionRelative_Type=Unsigned32
_LgpPduEntryPositionRelative_Object=MibTableColumn
lgpPduEntryPositionRelative=_LgpPduEntryPositionRelative_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,20),_LgpPduEntryPositionRelative_Type())
lgpPduEntryPositionRelative.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntryPositionRelative.setStatus(_A)
if mibBuilder.loadTexts:lgpPduEntryPositionRelative.setUnits(_J)
_LgpPduEntrySysStatus_Type=Unsigned32
_LgpPduEntrySysStatus_Object=MibTableColumn
lgpPduEntrySysStatus=_LgpPduEntrySysStatus_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,25),_LgpPduEntrySysStatus_Type())
lgpPduEntrySysStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntrySysStatus.setStatus(_A)
_LgpPduEntryUsrTag1_Type=DisplayString
_LgpPduEntryUsrTag1_Object=MibTableColumn
lgpPduEntryUsrTag1=_LgpPduEntryUsrTag1_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,35),_LgpPduEntryUsrTag1_Type())
lgpPduEntryUsrTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntryUsrTag1.setStatus(_A)
_LgpPduEntryUsrTag2_Type=DisplayString
_LgpPduEntryUsrTag2_Object=MibTableColumn
lgpPduEntryUsrTag2=_LgpPduEntryUsrTag2_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,40),_LgpPduEntryUsrTag2_Type())
lgpPduEntryUsrTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntryUsrTag2.setStatus(_A)
_LgpPduEntrySerialNumber_Type=DisplayString
_LgpPduEntrySerialNumber_Object=MibTableColumn
lgpPduEntrySerialNumber=_LgpPduEntrySerialNumber_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,45),_LgpPduEntrySerialNumber_Type())
lgpPduEntrySerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntrySerialNumber.setStatus(_A)
_LgpPduEntryRbCount_Type=Unsigned32
_LgpPduEntryRbCount_Object=MibTableColumn
lgpPduEntryRbCount=_LgpPduEntryRbCount_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,50),_LgpPduEntryRbCount_Type())
lgpPduEntryRbCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduEntryRbCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduEntryRbCount.setUnits(_J)
class _LgpPduEntrySWOverCurrentProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_e,1)))
_LgpPduEntrySWOverCurrentProtection_Type.__name__=_E
_LgpPduEntrySWOverCurrentProtection_Object=MibTableColumn
lgpPduEntrySWOverCurrentProtection=_LgpPduEntrySWOverCurrentProtection_Object((1,3,6,1,4,1,476,1,42,3,8,20,1,55),_LgpPduEntrySWOverCurrentProtection_Type())
lgpPduEntrySWOverCurrentProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduEntrySWOverCurrentProtection.setStatus(_A)
_LgpPduPowerSource_ObjectIdentity=ObjectIdentity
lgpPduPowerSource=_LgpPduPowerSource_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,30))
if mibBuilder.loadTexts:lgpPduPowerSource.setStatus(_A)
_LgpPduPsTableCount_Type=Unsigned32
_LgpPduPsTableCount_Object=MibScalar
lgpPduPsTableCount=_LgpPduPsTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,30,19),_LgpPduPsTableCount_Type())
lgpPduPsTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsTableCount.setUnits(_J)
_LgpPduPsTable_Object=MibTable
lgpPduPsTable=_LgpPduPsTable_Object((1,3,6,1,4,1,476,1,42,3,8,30,20))
if mibBuilder.loadTexts:lgpPduPsTable.setStatus(_A)
_LgpPduPsEntry_Object=MibTableRow
lgpPduPsEntry=_LgpPduPsEntry_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1))
lgpPduPsEntry.setIndexNames((0,_F,_K),(0,_F,_f))
if mibBuilder.loadTexts:lgpPduPsEntry.setStatus(_A)
_LgpPduPsEntryIndex_Type=Unsigned32
_LgpPduPsEntryIndex_Object=MibTableColumn
lgpPduPsEntryIndex=_LgpPduPsEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,5),_LgpPduPsEntryIndex_Type())
lgpPduPsEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduPsEntryIndex.setStatus(_A)
_LgpPduPsEntryId_Type=Unsigned32
_LgpPduPsEntryId_Object=MibTableColumn
lgpPduPsEntryId=_LgpPduPsEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,10),_LgpPduPsEntryId_Type())
lgpPduPsEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryId.setStatus(_A)
_LgpPduPsEntrySysAssignLabel_Type=DisplayString
_LgpPduPsEntrySysAssignLabel_Object=MibTableColumn
lgpPduPsEntrySysAssignLabel=_LgpPduPsEntrySysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,15),_LgpPduPsEntrySysAssignLabel_Type())
lgpPduPsEntrySysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntrySysAssignLabel.setStatus(_A)
_LgpPduPsEntryModel_Type=DisplayString
_LgpPduPsEntryModel_Object=MibTableColumn
lgpPduPsEntryModel=_LgpPduPsEntryModel_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,20),_LgpPduPsEntryModel_Type())
lgpPduPsEntryModel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryModel.setStatus(_A)
class _LgpPduPsEntryWiringType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),('single-phase-3-wire-L1-N-PE',1),('two-phase-3-wire-L1-L2-PE',2),('three-phase-4-wire-L1-L2-L3-PE',3),('three-phase-5-wire-L1-L2-L3-N-PE',4),('two-phase-4-wire-L1-L2-N-PE',5)))
_LgpPduPsEntryWiringType_Type.__name__=_E
_LgpPduPsEntryWiringType_Object=MibTableColumn
lgpPduPsEntryWiringType=_LgpPduPsEntryWiringType_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,25),_LgpPduPsEntryWiringType_Type())
lgpPduPsEntryWiringType.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryWiringType.setStatus(_A)
_LgpPduPsEntryEpInputRated_Type=Unsigned32
_LgpPduPsEntryEpInputRated_Object=MibTableColumn
lgpPduPsEntryEpInputRated=_LgpPduPsEntryEpInputRated_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,30),_LgpPduPsEntryEpInputRated_Type())
lgpPduPsEntryEpInputRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryEpInputRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEpInputRated.setUnits(_V)
_LgpPduPsEntryEcInputRated_Type=Unsigned32
_LgpPduPsEntryEcInputRated_Object=MibTableColumn
lgpPduPsEntryEcInputRated=_LgpPduPsEntryEcInputRated_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,35),_LgpPduPsEntryEcInputRated_Type())
lgpPduPsEntryEcInputRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryEcInputRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcInputRated.setUnits(_P)
_LgpPduPsEntryFreqRated_Type=Unsigned32
_LgpPduPsEntryFreqRated_Object=MibTableColumn
lgpPduPsEntryFreqRated=_LgpPduPsEntryFreqRated_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,40),_LgpPduPsEntryFreqRated_Type())
lgpPduPsEntryFreqRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryFreqRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryFreqRated.setUnits('Hertz')
_LgpPduPsEntryEnergyAccum_Type=Unsigned32
_LgpPduPsEntryEnergyAccum_Object=MibTableColumn
lgpPduPsEntryEnergyAccum=_LgpPduPsEntryEnergyAccum_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,50),_LgpPduPsEntryEnergyAccum_Type())
lgpPduPsEntryEnergyAccum.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryEnergyAccum.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEnergyAccum.setUnits(_g)
_LgpPduPsEntrySerialNum_Type=DisplayString
_LgpPduPsEntrySerialNum_Object=MibTableColumn
lgpPduPsEntrySerialNum=_LgpPduPsEntrySerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,55),_LgpPduPsEntrySerialNum_Type())
lgpPduPsEntrySerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntrySerialNum.setStatus(_A)
_LgpPduPsEntryFirmwareVersion_Type=DisplayString
_LgpPduPsEntryFirmwareVersion_Object=MibTableColumn
lgpPduPsEntryFirmwareVersion=_LgpPduPsEntryFirmwareVersion_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,60),_LgpPduPsEntryFirmwareVersion_Type())
lgpPduPsEntryFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryFirmwareVersion.setStatus(_A)
_LgpPduPsEntryPwrTotal_Type=Unsigned32
_LgpPduPsEntryPwrTotal_Object=MibTableColumn
lgpPduPsEntryPwrTotal=_LgpPduPsEntryPwrTotal_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,65),_LgpPduPsEntryPwrTotal_Type())
lgpPduPsEntryPwrTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryPwrTotal.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryPwrTotal.setUnits(_O)
_LgpPduPsEntryEcNeutral_Type=Unsigned32
_LgpPduPsEntryEcNeutral_Object=MibTableColumn
lgpPduPsEntryEcNeutral=_LgpPduPsEntryEcNeutral_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,70),_LgpPduPsEntryEcNeutral_Type())
lgpPduPsEntryEcNeutral.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutral.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutral.setUnits(_P)
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Type=Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Object=MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrWarn=_LgpPduPsEntryEcNeutralThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,75),_LgpPduPsEntryEcNeutralThrshldOvrWarn_Type())
lgpPduPsEntryEcNeutralThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutralThrshldOvrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutralThrshldOvrWarn.setUnits(_G)
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type=Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object=MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrAlarm=_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,80),_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type())
lgpPduPsEntryEcNeutralThrshldOvrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutralThrshldOvrAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcNeutralThrshldOvrAlarm.setUnits(_G)
_LgpPduPsEntryUnbalancedLoadThrshldAlarm_Type=Unsigned32
_LgpPduPsEntryUnbalancedLoadThrshldAlarm_Object=MibTableColumn
lgpPduPsEntryUnbalancedLoadThrshldAlarm=_LgpPduPsEntryUnbalancedLoadThrshldAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,85),_LgpPduPsEntryUnbalancedLoadThrshldAlarm_Type())
lgpPduPsEntryUnbalancedLoadThrshldAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryUnbalancedLoadThrshldAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryUnbalancedLoadThrshldAlarm.setUnits(_G)
_LgpPduPsEntryApTotal_Type=Unsigned32
_LgpPduPsEntryApTotal_Object=MibTableColumn
lgpPduPsEntryApTotal=_LgpPduPsEntryApTotal_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,90),_LgpPduPsEntryApTotal_Type())
lgpPduPsEntryApTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryApTotal.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryApTotal.setUnits(_Q)
_LgpPduPsEntryPfTotal_Type=Integer32
_LgpPduPsEntryPfTotal_Object=MibTableColumn
lgpPduPsEntryPfTotal=_LgpPduPsEntryPfTotal_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,95),_LgpPduPsEntryPfTotal_Type())
lgpPduPsEntryPfTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryPfTotal.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryPfTotal.setUnits(_R)
_LgpPduPsEntryEcResidual_Type=Unsigned32
_LgpPduPsEntryEcResidual_Object=MibTableColumn
lgpPduPsEntryEcResidual=_LgpPduPsEntryEcResidual_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,100),_LgpPduPsEntryEcResidual_Type())
lgpPduPsEntryEcResidual.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsEntryEcResidual.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcResidual.setUnits(_l)
_LgpPduPsEntryEcResidualThrshldOvrAlarm_Type=Unsigned32
_LgpPduPsEntryEcResidualThrshldOvrAlarm_Object=MibTableColumn
lgpPduPsEntryEcResidualThrshldOvrAlarm=_LgpPduPsEntryEcResidualThrshldOvrAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,20,1,105),_LgpPduPsEntryEcResidualThrshldOvrAlarm_Type())
lgpPduPsEntryEcResidualThrshldOvrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsEntryEcResidualThrshldOvrAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsEntryEcResidualThrshldOvrAlarm.setUnits(_l)
_LgpPduPsLineTable_Object=MibTable
lgpPduPsLineTable=_LgpPduPsLineTable_Object((1,3,6,1,4,1,476,1,42,3,8,30,40))
if mibBuilder.loadTexts:lgpPduPsLineTable.setStatus(_A)
_LgpPduPsLineEntry_Object=MibTableRow
lgpPduPsLineEntry=_LgpPduPsLineEntry_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1))
lgpPduPsLineEntry.setIndexNames((0,_F,_K),(0,_F,_f),(0,_F,_m))
if mibBuilder.loadTexts:lgpPduPsLineEntry.setStatus(_A)
_LgpPduPsLineEntryIndex_Type=Unsigned32
_LgpPduPsLineEntryIndex_Object=MibTableColumn
lgpPduPsLineEntryIndex=_LgpPduPsLineEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,5),_LgpPduPsLineEntryIndex_Type())
lgpPduPsLineEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduPsLineEntryIndex.setStatus(_A)
_LgpPduPsLineEntryId_Type=Unsigned32
_LgpPduPsLineEntryId_Object=MibTableColumn
lgpPduPsLineEntryId=_LgpPduPsLineEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,10),_LgpPduPsLineEntryId_Type())
lgpPduPsLineEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryId.setStatus(_A)
class _LgpPduPsLineEntryLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_o,2),(_p,3)))
_LgpPduPsLineEntryLine_Type.__name__=_E
_LgpPduPsLineEntryLine_Object=MibTableColumn
lgpPduPsLineEntryLine=_LgpPduPsLineEntryLine_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,15),_LgpPduPsLineEntryLine_Type())
lgpPduPsLineEntryLine.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryLine.setStatus(_A)
_LgpPduPsLineEntryEpLNTenths_Type=Unsigned32
_LgpPduPsLineEntryEpLNTenths_Object=MibTableColumn
lgpPduPsLineEntryEpLNTenths=_LgpPduPsLineEntryEpLNTenths_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,19),_LgpPduPsLineEntryEpLNTenths_Type())
lgpPduPsLineEntryEpLNTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLNTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLNTenths.setUnits(_h)
_LgpPduPsLineEntryEpLN_Type=Unsigned32
_LgpPduPsLineEntryEpLN_Object=MibTableColumn
lgpPduPsLineEntryEpLN=_LgpPduPsLineEntryEpLN_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,20),_LgpPduPsLineEntryEpLN_Type())
lgpPduPsLineEntryEpLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLN.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLN.setUnits(_i)
_LgpPduPsLineEntryEc_Type=Unsigned32
_LgpPduPsLineEntryEc_Object=MibTableColumn
lgpPduPsLineEntryEc=_LgpPduPsLineEntryEc_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,21),_LgpPduPsLineEntryEc_Type())
lgpPduPsLineEntryEc.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEc.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEc.setUnits(_W)
_LgpPduPsLineEntryEcHundredths_Type=Unsigned32
_LgpPduPsLineEntryEcHundredths_Object=MibTableColumn
lgpPduPsLineEntryEcHundredths=_LgpPduPsLineEntryEcHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,22),_LgpPduPsLineEntryEcHundredths_Type())
lgpPduPsLineEntryEcHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcHundredths.setUnits(_S)
_LgpPduPsLineEntryEcThrshldUndrAlarm_Type=Unsigned32
_LgpPduPsLineEntryEcThrshldUndrAlarm_Object=MibTableColumn
lgpPduPsLineEntryEcThrshldUndrAlarm=_LgpPduPsLineEntryEcThrshldUndrAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,35),_LgpPduPsLineEntryEcThrshldUndrAlarm_Type())
lgpPduPsLineEntryEcThrshldUndrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldUndrAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldUndrAlarm.setUnits(_G)
_LgpPduPsLineEntryEcThrshldOvrWarn_Type=Unsigned32
_LgpPduPsLineEntryEcThrshldOvrWarn_Object=MibTableColumn
lgpPduPsLineEntryEcThrshldOvrWarn=_LgpPduPsLineEntryEcThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,36),_LgpPduPsLineEntryEcThrshldOvrWarn_Type())
lgpPduPsLineEntryEcThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldOvrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldOvrWarn.setUnits(_G)
_LgpPduPsLineEntryEcThrshldOvrAlarm_Type=Unsigned32
_LgpPduPsLineEntryEcThrshldOvrAlarm_Object=MibTableColumn
lgpPduPsLineEntryEcThrshldOvrAlarm=_LgpPduPsLineEntryEcThrshldOvrAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,37),_LgpPduPsLineEntryEcThrshldOvrAlarm_Type())
lgpPduPsLineEntryEcThrshldOvrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldOvrAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcThrshldOvrAlarm.setUnits(_G)
_LgpPduPsLineEntryEcAvailBeforeAlarm_Type=Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarm_Object=MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarm=_LgpPduPsLineEntryEcAvailBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,38),_LgpPduPsLineEntryEcAvailBeforeAlarm_Type())
lgpPduPsLineEntryEcAvailBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcAvailBeforeAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcAvailBeforeAlarm.setUnits(_W)
_LgpPduPsLineEntryEcUsedBeforeAlarm_Type=Unsigned32
_LgpPduPsLineEntryEcUsedBeforeAlarm_Object=MibTableColumn
lgpPduPsLineEntryEcUsedBeforeAlarm=_LgpPduPsLineEntryEcUsedBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,39),_LgpPduPsLineEntryEcUsedBeforeAlarm_Type())
lgpPduPsLineEntryEcUsedBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcUsedBeforeAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcUsedBeforeAlarm.setUnits(_X)
_LgpPduPsLineEntryEpLL_Type=Unsigned32
_LgpPduPsLineEntryEpLL_Object=MibTableColumn
lgpPduPsLineEntryEpLL=_LgpPduPsLineEntryEpLL_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,60),_LgpPduPsLineEntryEpLL_Type())
lgpPduPsLineEntryEpLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLL.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLL.setUnits(_i)
_LgpPduPsLineEntryEpLLTenths_Type=Unsigned32
_LgpPduPsLineEntryEpLLTenths_Object=MibTableColumn
lgpPduPsLineEntryEpLLTenths=_LgpPduPsLineEntryEpLLTenths_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,61),_LgpPduPsLineEntryEpLLTenths_Type())
lgpPduPsLineEntryEpLLTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLLTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEpLLTenths.setUnits(_h)
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type=Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object=MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths=_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,62),_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type())
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setUnits(_S)
_LgpPduPsLineEntryPwrLN_Type=Unsigned32
_LgpPduPsLineEntryPwrLN_Object=MibTableColumn
lgpPduPsLineEntryPwrLN=_LgpPduPsLineEntryPwrLN_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,63),_LgpPduPsLineEntryPwrLN_Type())
lgpPduPsLineEntryPwrLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryPwrLN.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryPwrLN.setUnits(_O)
_LgpPduPsLineEntryPwrLL_Type=Unsigned32
_LgpPduPsLineEntryPwrLL_Object=MibTableColumn
lgpPduPsLineEntryPwrLL=_LgpPduPsLineEntryPwrLL_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,64),_LgpPduPsLineEntryPwrLL_Type())
lgpPduPsLineEntryPwrLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryPwrLL.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryPwrLL.setUnits(_O)
_LgpPduPsLineEntryApLN_Type=Unsigned32
_LgpPduPsLineEntryApLN_Object=MibTableColumn
lgpPduPsLineEntryApLN=_LgpPduPsLineEntryApLN_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,65),_LgpPduPsLineEntryApLN_Type())
lgpPduPsLineEntryApLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryApLN.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryApLN.setUnits(_Q)
_LgpPduPsLineEntryApLL_Type=Unsigned32
_LgpPduPsLineEntryApLL_Object=MibTableColumn
lgpPduPsLineEntryApLL=_LgpPduPsLineEntryApLL_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,66),_LgpPduPsLineEntryApLL_Type())
lgpPduPsLineEntryApLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryApLL.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryApLL.setUnits(_Q)
_LgpPduPsLineEntryPfLN_Type=Integer32
_LgpPduPsLineEntryPfLN_Object=MibTableColumn
lgpPduPsLineEntryPfLN=_LgpPduPsLineEntryPfLN_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,67),_LgpPduPsLineEntryPfLN_Type())
lgpPduPsLineEntryPfLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryPfLN.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryPfLN.setUnits(_R)
_LgpPduPsLineEntryPfLL_Type=Integer32
_LgpPduPsLineEntryPfLL_Object=MibTableColumn
lgpPduPsLineEntryPfLL=_LgpPduPsLineEntryPfLL_Object((1,3,6,1,4,1,476,1,42,3,8,30,40,1,68),_LgpPduPsLineEntryPfLL_Type())
lgpPduPsLineEntryPfLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduPsLineEntryPfLL.setStatus(_A)
if mibBuilder.loadTexts:lgpPduPsLineEntryPfLL.setUnits(_R)
_LgpPduReceptacleBranch_ObjectIdentity=ObjectIdentity
lgpPduReceptacleBranch=_LgpPduReceptacleBranch_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,40))
if mibBuilder.loadTexts:lgpPduReceptacleBranch.setStatus(_A)
_LgpPduRbTableCount_Type=Unsigned32
_LgpPduRbTableCount_Object=MibScalar
lgpPduRbTableCount=_LgpPduRbTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,40,19),_LgpPduRbTableCount_Type())
lgpPduRbTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbTableCount.setUnits(_J)
_LgpPduRbTable_Object=MibTable
lgpPduRbTable=_LgpPduRbTable_Object((1,3,6,1,4,1,476,1,42,3,8,40,20))
if mibBuilder.loadTexts:lgpPduRbTable.setStatus(_A)
_LgpPduRbEntry_Object=MibTableRow
lgpPduRbEntry=_LgpPduRbEntry_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1))
lgpPduRbEntry.setIndexNames((0,_F,_K),(0,_F,_Y))
if mibBuilder.loadTexts:lgpPduRbEntry.setStatus(_A)
_LgpPduRbEntryIndex_Type=Unsigned32
_LgpPduRbEntryIndex_Object=MibTableColumn
lgpPduRbEntryIndex=_LgpPduRbEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,1),_LgpPduRbEntryIndex_Type())
lgpPduRbEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduRbEntryIndex.setStatus(_A)
_LgpPduRbEntryId_Type=Unsigned32
_LgpPduRbEntryId_Object=MibTableColumn
lgpPduRbEntryId=_LgpPduRbEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,5),_LgpPduRbEntryId_Type())
lgpPduRbEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryId.setStatus(_A)
_LgpPduRbEntryUsrLabel_Type=DisplayString
_LgpPduRbEntryUsrLabel_Object=MibTableColumn
lgpPduRbEntryUsrLabel=_LgpPduRbEntryUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,8),_LgpPduRbEntryUsrLabel_Type())
lgpPduRbEntryUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryUsrLabel.setStatus(_A)
_LgpPduRbEntrySysAssignLabel_Type=DisplayString
_LgpPduRbEntrySysAssignLabel_Object=MibTableColumn
lgpPduRbEntrySysAssignLabel=_LgpPduRbEntrySysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,20),_LgpPduRbEntrySysAssignLabel_Type())
lgpPduRbEntrySysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntrySysAssignLabel.setStatus(_A)
_LgpPduRbEntryPositionRelative_Type=Unsigned32
_LgpPduRbEntryPositionRelative_Object=MibTableColumn
lgpPduRbEntryPositionRelative=_LgpPduRbEntryPositionRelative_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,25),_LgpPduRbEntryPositionRelative_Type())
lgpPduRbEntryPositionRelative.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryPositionRelative.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryPositionRelative.setUnits(_J)
_LgpPduRbEntrySerialNum_Type=DisplayString
_LgpPduRbEntrySerialNum_Object=MibTableColumn
lgpPduRbEntrySerialNum=_LgpPduRbEntrySerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,30),_LgpPduRbEntrySerialNum_Type())
lgpPduRbEntrySerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntrySerialNum.setStatus(_A)
_LgpPduRbEntryModel_Type=DisplayString
_LgpPduRbEntryModel_Object=MibTableColumn
lgpPduRbEntryModel=_LgpPduRbEntryModel_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,35),_LgpPduRbEntryModel_Type())
lgpPduRbEntryModel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryModel.setStatus(_A)
_LgpPduRbEntryFirmwareVersion_Type=DisplayString
_LgpPduRbEntryFirmwareVersion_Object=MibTableColumn
lgpPduRbEntryFirmwareVersion=_LgpPduRbEntryFirmwareVersion_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,40),_LgpPduRbEntryFirmwareVersion_Type())
lgpPduRbEntryFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryFirmwareVersion.setStatus(_A)
_LgpPduRbEntryUsrTag1_Type=DisplayString
_LgpPduRbEntryUsrTag1_Object=MibTableColumn
lgpPduRbEntryUsrTag1=_LgpPduRbEntryUsrTag1_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,41),_LgpPduRbEntryUsrTag1_Type())
lgpPduRbEntryUsrTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryUsrTag1.setStatus(_A)
_LgpPduRbEntryUsrTag2_Type=DisplayString
_LgpPduRbEntryUsrTag2_Object=MibTableColumn
lgpPduRbEntryUsrTag2=_LgpPduRbEntryUsrTag2_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,42),_LgpPduRbEntryUsrTag2_Type())
lgpPduRbEntryUsrTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryUsrTag2.setStatus(_A)
class _LgpPduRbEntryReceptacleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,0),(_q,1),(_r,2),(_s,3),('iec-C13-sheet-F-10-Amp-and-iec-C19-sheet-J-16-Amp',4),('nema-5-20R-20-Amp-and-iec-C13-sheet-F-10-Amp',5),('nema-5-20R-20-Amp-and-iec-C19-sheet-J-16-Amp',6),(_t,7),(_u,8)))
_LgpPduRbEntryReceptacleType_Type.__name__=_E
_LgpPduRbEntryReceptacleType_Object=MibTableColumn
lgpPduRbEntryReceptacleType=_LgpPduRbEntryReceptacleType_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,45),_LgpPduRbEntryReceptacleType_Type())
lgpPduRbEntryReceptacleType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryReceptacleType.setStatus(_A)
class _LgpPduRbEntryCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),(_A0,6)))
_LgpPduRbEntryCapabilities_Type.__name__=_E
_LgpPduRbEntryCapabilities_Object=MibTableColumn
lgpPduRbEntryCapabilities=_LgpPduRbEntryCapabilities_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,50),_LgpPduRbEntryCapabilities_Type())
lgpPduRbEntryCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryCapabilities.setStatus(_A)
class _LgpPduRbEntryLineSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,0),('line-1-neutral',1),('line-2-neutral',2),('line-3-neutral',3),(_A1,4),(_A2,5),(_A3,6),('line-1-line-2-and-line-1-neutral',7),('line-2-line-3-and-line-2-neutral',8),('line-3-line-1-and-line-3-neutral',9),(_A4,10),(_A5,11)))
_LgpPduRbEntryLineSource_Type.__name__=_E
_LgpPduRbEntryLineSource_Object=MibTableColumn
lgpPduRbEntryLineSource=_LgpPduRbEntryLineSource_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,55),_LgpPduRbEntryLineSource_Type())
lgpPduRbEntryLineSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryLineSource.setStatus(_A)
_LgpPduRbEntryRcpCount_Type=Unsigned32
_LgpPduRbEntryRcpCount_Object=MibTableColumn
lgpPduRbEntryRcpCount=_LgpPduRbEntryRcpCount_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,60),_LgpPduRbEntryRcpCount_Type())
lgpPduRbEntryRcpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryRcpCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryRcpCount.setUnits(_J)
_LgpPduRbEntryEpRated_Type=Unsigned32
_LgpPduRbEntryEpRated_Object=MibTableColumn
lgpPduRbEntryEpRated=_LgpPduRbEntryEpRated_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,70),_LgpPduRbEntryEpRated_Type())
lgpPduRbEntryEpRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEpRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEpRated.setUnits(_V)
_LgpPduRbEntryEcRated_Type=Unsigned32
_LgpPduRbEntryEcRated_Object=MibTableColumn
lgpPduRbEntryEcRated=_LgpPduRbEntryEcRated_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,75),_LgpPduRbEntryEcRated_Type())
lgpPduRbEntryEcRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEcRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcRated.setUnits(_P)
_LgpPduRbEntryFreqRated_Type=Unsigned32
_LgpPduRbEntryFreqRated_Object=MibTableColumn
lgpPduRbEntryFreqRated=_LgpPduRbEntryFreqRated_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,80),_LgpPduRbEntryFreqRated_Type())
lgpPduRbEntryFreqRated.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryFreqRated.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryFreqRated.setUnits('Hertz')
_LgpPduRbEntryEnergyAccum_Type=Unsigned32
_LgpPduRbEntryEnergyAccum_Object=MibTableColumn
lgpPduRbEntryEnergyAccum=_LgpPduRbEntryEnergyAccum_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,85),_LgpPduRbEntryEnergyAccum_Type())
lgpPduRbEntryEnergyAccum.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryEnergyAccum.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEnergyAccum.setUnits(_g)
_LgpPduRbEntryEpLNTenths_Type=Unsigned32
_LgpPduRbEntryEpLNTenths_Object=MibTableColumn
lgpPduRbEntryEpLNTenths=_LgpPduRbEntryEpLNTenths_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,100),_LgpPduRbEntryEpLNTenths_Type())
lgpPduRbEntryEpLNTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEpLNTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEpLNTenths.setUnits(_Z)
_LgpPduRbEntryPwr_Type=Unsigned32
_LgpPduRbEntryPwr_Object=MibTableColumn
lgpPduRbEntryPwr=_LgpPduRbEntryPwr_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,115),_LgpPduRbEntryPwr_Type())
lgpPduRbEntryPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryPwr.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryPwr.setUnits(_O)
_LgpPduRbEntryAp_Type=Unsigned32
_LgpPduRbEntryAp_Object=MibTableColumn
lgpPduRbEntryAp=_LgpPduRbEntryAp_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,120),_LgpPduRbEntryAp_Type())
lgpPduRbEntryAp.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryAp.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryAp.setUnits(_Q)
_LgpPduRbEntryPf_Type=Integer32
_LgpPduRbEntryPf_Object=MibTableColumn
lgpPduRbEntryPf=_LgpPduRbEntryPf_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,125),_LgpPduRbEntryPf_Type())
lgpPduRbEntryPf.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryPf.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryPf.setUnits(_R)
_LgpPduRbEntryEcHundredths_Type=Unsigned32
_LgpPduRbEntryEcHundredths_Object=MibTableColumn
lgpPduRbEntryEcHundredths=_LgpPduRbEntryEcHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,130),_LgpPduRbEntryEcHundredths_Type())
lgpPduRbEntryEcHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEcHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcHundredths.setUnits(_j)
_LgpPduRbEntryEcThrshldUndrAlm_Type=Unsigned32
_LgpPduRbEntryEcThrshldUndrAlm_Object=MibTableColumn
lgpPduRbEntryEcThrshldUndrAlm=_LgpPduRbEntryEcThrshldUndrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,135),_LgpPduRbEntryEcThrshldUndrAlm_Type())
lgpPduRbEntryEcThrshldUndrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldUndrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldUndrAlm.setUnits(_G)
_LgpPduRbEntryEcThrshldOvrWarn_Type=Unsigned32
_LgpPduRbEntryEcThrshldOvrWarn_Object=MibTableColumn
lgpPduRbEntryEcThrshldOvrWarn=_LgpPduRbEntryEcThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,140),_LgpPduRbEntryEcThrshldOvrWarn_Type())
lgpPduRbEntryEcThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldOvrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldOvrWarn.setUnits(_G)
_LgpPduRbEntryEcThrshldOvrAlm_Type=Unsigned32
_LgpPduRbEntryEcThrshldOvrAlm_Object=MibTableColumn
lgpPduRbEntryEcThrshldOvrAlm=_LgpPduRbEntryEcThrshldOvrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,145),_LgpPduRbEntryEcThrshldOvrAlm_Type())
lgpPduRbEntryEcThrshldOvrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldOvrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcThrshldOvrAlm.setUnits(_G)
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type=Unsigned32
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object=MibTableColumn
lgpPduRbEntryEcAvailBeforeAlarmHundredths=_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,150),_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type())
lgpPduRbEntryEcAvailBeforeAlarmHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEcAvailBeforeAlarmHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcAvailBeforeAlarmHundredths.setUnits(_S)
_LgpPduRbEntryEcUsedBeforeAlarm_Type=Unsigned32
_LgpPduRbEntryEcUsedBeforeAlarm_Object=MibTableColumn
lgpPduRbEntryEcUsedBeforeAlarm=_LgpPduRbEntryEcUsedBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,160),_LgpPduRbEntryEcUsedBeforeAlarm_Type())
lgpPduRbEntryEcUsedBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEcUsedBeforeAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEcUsedBeforeAlarm.setUnits(_X)
_LgpPduRbEntryEpLLTenths_Type=Unsigned32
_LgpPduRbEntryEpLLTenths_Object=MibTableColumn
lgpPduRbEntryEpLLTenths=_LgpPduRbEntryEpLLTenths_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,170),_LgpPduRbEntryEpLLTenths_Type())
lgpPduRbEntryEpLLTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbEntryEpLLTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRbEntryEpLLTenths.setUnits(_Z)
class _LgpPduRbEntrySwOverCurrentProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),(_e,1)))
_LgpPduRbEntrySwOverCurrentProtection_Type.__name__=_E
_LgpPduRbEntrySwOverCurrentProtection_Object=MibTableColumn
lgpPduRbEntrySwOverCurrentProtection=_LgpPduRbEntrySwOverCurrentProtection_Object((1,3,6,1,4,1,476,1,42,3,8,40,20,1,175),_LgpPduRbEntrySwOverCurrentProtection_Type())
lgpPduRbEntrySwOverCurrentProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbEntrySwOverCurrentProtection.setStatus(_A)
_LgpPduRbLineTable_Object=MibTable
lgpPduRbLineTable=_LgpPduRbLineTable_Object((1,3,6,1,4,1,476,1,42,3,8,40,40))
if mibBuilder.loadTexts:lgpPduRbLineTable.setStatus(_D)
_LgpPduRbLineEntry_Object=MibTableRow
lgpPduRbLineEntry=_LgpPduRbLineEntry_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1))
lgpPduRbLineEntry.setIndexNames((0,_F,_K),(0,_F,_Y),(0,_F,_A6))
if mibBuilder.loadTexts:lgpPduRbLineEntry.setStatus(_D)
_LgpPduRbLineEntryIndex_Type=Unsigned32
_LgpPduRbLineEntryIndex_Object=MibTableColumn
lgpPduRbLineEntryIndex=_LgpPduRbLineEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,1),_LgpPduRbLineEntryIndex_Type())
lgpPduRbLineEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduRbLineEntryIndex.setStatus(_D)
_LgpPduRbLineEntryId_Type=Unsigned32
_LgpPduRbLineEntryId_Object=MibTableColumn
lgpPduRbLineEntryId=_LgpPduRbLineEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,5),_LgpPduRbLineEntryId_Type())
lgpPduRbLineEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryId.setStatus(_D)
class _LgpPduRbLineEntryLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_o,2),(_p,3)))
_LgpPduRbLineEntryLine_Type.__name__=_E
_LgpPduRbLineEntryLine_Object=MibTableColumn
lgpPduRbLineEntryLine=_LgpPduRbLineEntryLine_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,10),_LgpPduRbLineEntryLine_Type())
lgpPduRbLineEntryLine.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryLine.setStatus(_D)
_LgpPduRbLineEntryEpLNTenths_Type=Unsigned32
_LgpPduRbLineEntryEpLNTenths_Object=MibTableColumn
lgpPduRbLineEntryEpLNTenths=_LgpPduRbLineEntryEpLNTenths_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,19),_LgpPduRbLineEntryEpLNTenths_Type())
lgpPduRbLineEntryEpLNTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLNTenths.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLNTenths.setUnits(_Z)
_LgpPduRbLineEntryEpLN_Type=Unsigned32
_LgpPduRbLineEntryEpLN_Object=MibTableColumn
lgpPduRbLineEntryEpLN=_LgpPduRbLineEntryEpLN_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,20),_LgpPduRbLineEntryEpLN_Type())
lgpPduRbLineEntryEpLN.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLN.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLN.setUnits(_V)
_LgpPduRbLineEntryEc_Type=Unsigned32
_LgpPduRbLineEntryEc_Object=MibTableColumn
lgpPduRbLineEntryEc=_LgpPduRbLineEntryEc_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,21),_LgpPduRbLineEntryEc_Type())
lgpPduRbLineEntryEc.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEc.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEc.setUnits(_P)
_LgpPduRbLineEntryPwr_Type=Unsigned32
_LgpPduRbLineEntryPwr_Object=MibTableColumn
lgpPduRbLineEntryPwr=_LgpPduRbLineEntryPwr_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,22),_LgpPduRbLineEntryPwr_Type())
lgpPduRbLineEntryPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryPwr.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryPwr.setUnits(_O)
_LgpPduRbLineEntryAp_Type=Unsigned32
_LgpPduRbLineEntryAp_Object=MibTableColumn
lgpPduRbLineEntryAp=_LgpPduRbLineEntryAp_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,23),_LgpPduRbLineEntryAp_Type())
lgpPduRbLineEntryAp.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryAp.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryAp.setUnits(_Q)
_LgpPduRbLineEntryPf_Type=Integer32
_LgpPduRbLineEntryPf_Object=MibTableColumn
lgpPduRbLineEntryPf=_LgpPduRbLineEntryPf_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,24),_LgpPduRbLineEntryPf_Type())
lgpPduRbLineEntryPf.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryPf.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryPf.setUnits(_R)
_LgpPduRbLineEntryEcHundredths_Type=Unsigned32
_LgpPduRbLineEntryEcHundredths_Object=MibTableColumn
lgpPduRbLineEntryEcHundredths=_LgpPduRbLineEntryEcHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,25),_LgpPduRbLineEntryEcHundredths_Type())
lgpPduRbLineEntryEcHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcHundredths.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcHundredths.setUnits(_j)
_LgpPduRbLineEntryEcThrshldUndrAlm_Type=Unsigned32
_LgpPduRbLineEntryEcThrshldUndrAlm_Object=MibTableColumn
lgpPduRbLineEntryEcThrshldUndrAlm=_LgpPduRbLineEntryEcThrshldUndrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,35),_LgpPduRbLineEntryEcThrshldUndrAlm_Type())
lgpPduRbLineEntryEcThrshldUndrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldUndrAlm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldUndrAlm.setUnits(_G)
_LgpPduRbLineEntryEcThrshldOvrWarn_Type=Unsigned32
_LgpPduRbLineEntryEcThrshldOvrWarn_Object=MibTableColumn
lgpPduRbLineEntryEcThrshldOvrWarn=_LgpPduRbLineEntryEcThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,36),_LgpPduRbLineEntryEcThrshldOvrWarn_Type())
lgpPduRbLineEntryEcThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldOvrWarn.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldOvrWarn.setUnits(_G)
_LgpPduRbLineEntryEcThrshldOvrAlm_Type=Unsigned32
_LgpPduRbLineEntryEcThrshldOvrAlm_Object=MibTableColumn
lgpPduRbLineEntryEcThrshldOvrAlm=_LgpPduRbLineEntryEcThrshldOvrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,37),_LgpPduRbLineEntryEcThrshldOvrAlm_Type())
lgpPduRbLineEntryEcThrshldOvrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldOvrAlm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcThrshldOvrAlm.setUnits(_G)
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type=Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object=MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths=_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,39),_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type())
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setUnits(_S)
_LgpPduRbLineEntryEcAvailBeforeAlarm_Type=Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarm_Object=MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarm=_LgpPduRbLineEntryEcAvailBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,40),_LgpPduRbLineEntryEcAvailBeforeAlarm_Type())
lgpPduRbLineEntryEcAvailBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcAvailBeforeAlarm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcAvailBeforeAlarm.setUnits(_W)
_LgpPduRbLineEntryEcUsedBeforeAlarm_Type=Unsigned32
_LgpPduRbLineEntryEcUsedBeforeAlarm_Object=MibTableColumn
lgpPduRbLineEntryEcUsedBeforeAlarm=_LgpPduRbLineEntryEcUsedBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,41),_LgpPduRbLineEntryEcUsedBeforeAlarm_Type())
lgpPduRbLineEntryEcUsedBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcUsedBeforeAlarm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEcUsedBeforeAlarm.setUnits(_X)
_LgpPduRbLineEntryEpLL_Type=Unsigned32
_LgpPduRbLineEntryEpLL_Object=MibTableColumn
lgpPduRbLineEntryEpLL=_LgpPduRbLineEntryEpLL_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,60),_LgpPduRbLineEntryEpLL_Type())
lgpPduRbLineEntryEpLL.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLL.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLL.setUnits(_V)
_LgpPduRbLineEntryEpLLTenths_Type=Unsigned32
_LgpPduRbLineEntryEpLLTenths_Object=MibTableColumn
lgpPduRbLineEntryEpLLTenths=_LgpPduRbLineEntryEpLLTenths_Object((1,3,6,1,4,1,476,1,42,3,8,40,40,1,61),_LgpPduRbLineEntryEpLLTenths_Type())
lgpPduRbLineEntryEpLLTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLLTenths.setStatus(_D)
if mibBuilder.loadTexts:lgpPduRbLineEntryEpLLTenths.setUnits(_Z)
_LgpPduReceptacle_ObjectIdentity=ObjectIdentity
lgpPduReceptacle=_LgpPduReceptacle_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,50))
if mibBuilder.loadTexts:lgpPduReceptacle.setStatus(_A)
_LgpPduRcpTableCount_Type=Unsigned32
_LgpPduRcpTableCount_Object=MibScalar
lgpPduRcpTableCount=_LgpPduRcpTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,50,19),_LgpPduRcpTableCount_Type())
lgpPduRcpTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpTableCount.setUnits(_J)
_LgpPduRcpTable_Object=MibTable
lgpPduRcpTable=_LgpPduRcpTable_Object((1,3,6,1,4,1,476,1,42,3,8,50,20))
if mibBuilder.loadTexts:lgpPduRcpTable.setStatus(_A)
_LgpPduRcpEntry_Object=MibTableRow
lgpPduRcpEntry=_LgpPduRcpEntry_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1))
lgpPduRcpEntry.setIndexNames((0,_F,_K),(0,_F,_Y),(0,_F,_A7))
if mibBuilder.loadTexts:lgpPduRcpEntry.setStatus(_A)
_LgpPduRcpEntryIndex_Type=Unsigned32
_LgpPduRcpEntryIndex_Object=MibTableColumn
lgpPduRcpEntryIndex=_LgpPduRcpEntryIndex_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,1),_LgpPduRcpEntryIndex_Type())
lgpPduRcpEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduRcpEntryIndex.setStatus(_A)
_LgpPduRcpEntryId_Type=Unsigned32
_LgpPduRcpEntryId_Object=MibTableColumn
lgpPduRcpEntryId=_LgpPduRcpEntryId_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,5),_LgpPduRcpEntryId_Type())
lgpPduRcpEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryId.setStatus(_A)
_LgpPduRcpEntryUsrLabel_Type=DisplayString
_LgpPduRcpEntryUsrLabel_Object=MibTableColumn
lgpPduRcpEntryUsrLabel=_LgpPduRcpEntryUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,10),_LgpPduRcpEntryUsrLabel_Type())
lgpPduRcpEntryUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryUsrLabel.setStatus(_A)
_LgpPduRcpEntryUsrTag1_Type=DisplayString
_LgpPduRcpEntryUsrTag1_Object=MibTableColumn
lgpPduRcpEntryUsrTag1=_LgpPduRcpEntryUsrTag1_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,15),_LgpPduRcpEntryUsrTag1_Type())
lgpPduRcpEntryUsrTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryUsrTag1.setStatus(_A)
_LgpPduRcpEntryUsrTag2_Type=DisplayString
_LgpPduRcpEntryUsrTag2_Object=MibTableColumn
lgpPduRcpEntryUsrTag2=_LgpPduRcpEntryUsrTag2_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,20),_LgpPduRcpEntryUsrTag2_Type())
lgpPduRcpEntryUsrTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryUsrTag2.setStatus(_A)
_LgpPduRcpEntrySysAssignLabel_Type=DisplayString
_LgpPduRcpEntrySysAssignLabel_Object=MibTableColumn
lgpPduRcpEntrySysAssignLabel=_LgpPduRcpEntrySysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,25),_LgpPduRcpEntrySysAssignLabel_Type())
lgpPduRcpEntrySysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntrySysAssignLabel.setStatus(_A)
_LgpPduRcpEntryPosition_Type=Unsigned32
_LgpPduRcpEntryPosition_Object=MibTableColumn
lgpPduRcpEntryPosition=_LgpPduRcpEntryPosition_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,30),_LgpPduRcpEntryPosition_Type())
lgpPduRcpEntryPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryPosition.setStatus(_A)
class _LgpPduRcpEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,7,8)));namedValues=NamedValues(*((_I,0),(_q,1),(_r,2),(_s,3),(_t,7),(_u,8)))
_LgpPduRcpEntryType_Type.__name__=_E
_LgpPduRcpEntryType_Object=MibTableColumn
lgpPduRcpEntryType=_LgpPduRcpEntryType_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,40),_LgpPduRcpEntryType_Type())
lgpPduRcpEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryType.setStatus(_A)
class _LgpPduRcpEntryLineSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,0),('line-1-N',1),('line-2-N',2),('line-3-N',3),(_A1,4),(_A2,5),(_A3,6),(_A4,7),(_A5,8)))
_LgpPduRcpEntryLineSource_Type.__name__=_E
_LgpPduRcpEntryLineSource_Object=MibTableColumn
lgpPduRcpEntryLineSource=_LgpPduRcpEntryLineSource_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,45),_LgpPduRcpEntryLineSource_Type())
lgpPduRcpEntryLineSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryLineSource.setStatus(_A)
class _LgpPduRcpEntryCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),(_A0,6)))
_LgpPduRcpEntryCapabilities_Type.__name__=_E
_LgpPduRcpEntryCapabilities_Object=MibTableColumn
lgpPduRcpEntryCapabilities=_LgpPduRcpEntryCapabilities_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,50),_LgpPduRcpEntryCapabilities_Type())
lgpPduRcpEntryCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryCapabilities.setStatus(_A)
_LgpPduRcpEntryEp_Type=Unsigned32
_LgpPduRcpEntryEp_Object=MibTableColumn
lgpPduRcpEntryEp=_LgpPduRcpEntryEp_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,55),_LgpPduRcpEntryEp_Type())
lgpPduRcpEntryEp.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEp.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEp.setUnits(_i)
_LgpPduRcpEntryEpTenths_Type=Unsigned32
_LgpPduRcpEntryEpTenths_Object=MibTableColumn
lgpPduRcpEntryEpTenths=_LgpPduRcpEntryEpTenths_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,56),_LgpPduRcpEntryEpTenths_Type())
lgpPduRcpEntryEpTenths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEpTenths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEpTenths.setUnits(_h)
_LgpPduRcpEntryEc_Type=Unsigned32
_LgpPduRcpEntryEc_Object=MibTableColumn
lgpPduRcpEntryEc=_LgpPduRcpEntryEc_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,60),_LgpPduRcpEntryEc_Type())
lgpPduRcpEntryEc.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEc.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEc.setUnits(_P)
_LgpPduRcpEntryEcHundredths_Type=Unsigned32
_LgpPduRcpEntryEcHundredths_Object=MibTableColumn
lgpPduRcpEntryEcHundredths=_LgpPduRcpEntryEcHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,61),_LgpPduRcpEntryEcHundredths_Type())
lgpPduRcpEntryEcHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEcHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcHundredths.setUnits(_j)
_LgpPduRcpEntryPwrOut_Type=Unsigned32
_LgpPduRcpEntryPwrOut_Object=MibTableColumn
lgpPduRcpEntryPwrOut=_LgpPduRcpEntryPwrOut_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,65),_LgpPduRcpEntryPwrOut_Type())
lgpPduRcpEntryPwrOut.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrOut.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrOut.setUnits(_O)
_LgpPduRcpEntryApOut_Type=Unsigned32
_LgpPduRcpEntryApOut_Object=MibTableColumn
lgpPduRcpEntryApOut=_LgpPduRcpEntryApOut_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,70),_LgpPduRcpEntryApOut_Type())
lgpPduRcpEntryApOut.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryApOut.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryApOut.setUnits('Volt-Amp-RMS')
_LgpPduRcpEntryPf_Type=Unsigned32
_LgpPduRcpEntryPf_Object=MibTableColumn
lgpPduRcpEntryPf=_LgpPduRcpEntryPf_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,75),_LgpPduRcpEntryPf_Type())
lgpPduRcpEntryPf.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryPf.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryPf.setUnits('.01 Power Factor')
_LgpPduRcpEntryFreq_Type=Unsigned32
_LgpPduRcpEntryFreq_Object=MibTableColumn
lgpPduRcpEntryFreq=_LgpPduRcpEntryFreq_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,80),_LgpPduRcpEntryFreq_Type())
lgpPduRcpEntryFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryFreq.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryFreq.setUnits('0.1 Hertz')
_LgpPduRcpEntryEnergyAccum_Type=Unsigned32
_LgpPduRcpEntryEnergyAccum_Object=MibTableColumn
lgpPduRcpEntryEnergyAccum=_LgpPduRcpEntryEnergyAccum_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,85),_LgpPduRcpEntryEnergyAccum_Type())
lgpPduRcpEntryEnergyAccum.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryEnergyAccum.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEnergyAccum.setUnits(_g)
_LgpPduRcpEntryPwrOnDelay_Type=Unsigned32
_LgpPduRcpEntryPwrOnDelay_Object=MibTableColumn
lgpPduRcpEntryPwrOnDelay=_LgpPduRcpEntryPwrOnDelay_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,90),_LgpPduRcpEntryPwrOnDelay_Type())
lgpPduRcpEntryPwrOnDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrOnDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrOnDelay.setUnits(_U)
class _LgpPduRcpEntryPwrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),(_a,1),(_b,2),('off-pending-on-delay',3)))
_LgpPduRcpEntryPwrState_Type.__name__=_E
_LgpPduRcpEntryPwrState_Object=MibTableColumn
lgpPduRcpEntryPwrState=_LgpPduRcpEntryPwrState_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,95),_LgpPduRcpEntryPwrState_Type())
lgpPduRcpEntryPwrState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrState.setStatus(_A)
class _LgpPduRcpEntryPwrUpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),(_a,2),('last-state',3)))
_LgpPduRcpEntryPwrUpState_Type.__name__=_E
_LgpPduRcpEntryPwrUpState_Object=MibTableColumn
lgpPduRcpEntryPwrUpState=_LgpPduRcpEntryPwrUpState_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,96),_LgpPduRcpEntryPwrUpState_Type())
lgpPduRcpEntryPwrUpState.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryPwrUpState.setStatus(_A)
class _LgpPduRcpEntryControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_a,0),(_b,1),(_A8,2)))
_LgpPduRcpEntryControl_Type.__name__=_E
_LgpPduRcpEntryControl_Object=MibTableColumn
lgpPduRcpEntryControl=_LgpPduRcpEntryControl_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,100),_LgpPduRcpEntryControl_Type())
lgpPduRcpEntryControl.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryControl.setStatus(_A)
class _LgpPduRcpEntryControlLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('unlocked',1),('locked',2)))
_LgpPduRcpEntryControlLock_Type.__name__=_E
_LgpPduRcpEntryControlLock_Object=MibTableColumn
lgpPduRcpEntryControlLock=_LgpPduRcpEntryControlLock_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,105),_LgpPduRcpEntryControlLock_Type())
lgpPduRcpEntryControlLock.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryControlLock.setStatus(_A)
_LgpPduRcpEntryEcThrshldUnderAlarm_Type=Unsigned32
_LgpPduRcpEntryEcThrshldUnderAlarm_Object=MibTableColumn
lgpPduRcpEntryEcThrshldUnderAlarm=_LgpPduRcpEntryEcThrshldUnderAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,150),_LgpPduRcpEntryEcThrshldUnderAlarm_Type())
lgpPduRcpEntryEcThrshldUnderAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldUnderAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldUnderAlarm.setUnits(_G)
_LgpPduRcpEntryEcThrshldOverWarn_Type=Unsigned32
_LgpPduRcpEntryEcThrshldOverWarn_Object=MibTableColumn
lgpPduRcpEntryEcThrshldOverWarn=_LgpPduRcpEntryEcThrshldOverWarn_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,151),_LgpPduRcpEntryEcThrshldOverWarn_Type())
lgpPduRcpEntryEcThrshldOverWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldOverWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldOverWarn.setUnits(_G)
_LgpPduRcpEntryEcThrshldOverAlarm_Type=Unsigned32
_LgpPduRcpEntryEcThrshldOverAlarm_Object=MibTableColumn
lgpPduRcpEntryEcThrshldOverAlarm=_LgpPduRcpEntryEcThrshldOverAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,152),_LgpPduRcpEntryEcThrshldOverAlarm_Type())
lgpPduRcpEntryEcThrshldOverAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldOverAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcThrshldOverAlarm.setUnits(_G)
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type=Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object=MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarmHundredths=_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,159),_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type())
lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setUnits(_S)
_LgpPduRcpEntryEcAvailBeforeAlarm_Type=Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarm_Object=MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarm=_LgpPduRcpEntryEcAvailBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,160),_LgpPduRcpEntryEcAvailBeforeAlarm_Type())
lgpPduRcpEntryEcAvailBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEcAvailBeforeAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcAvailBeforeAlarm.setUnits(_W)
_LgpPduRcpEntryEcUsedBeforeAlarm_Type=Unsigned32
_LgpPduRcpEntryEcUsedBeforeAlarm_Object=MibTableColumn
lgpPduRcpEntryEcUsedBeforeAlarm=_LgpPduRcpEntryEcUsedBeforeAlarm_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,161),_LgpPduRcpEntryEcUsedBeforeAlarm_Type())
lgpPduRcpEntryEcUsedBeforeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEcUsedBeforeAlarm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcUsedBeforeAlarm.setUnits(_X)
_LgpPduRcpEntryEcCrestFactor_Type=Unsigned32
_LgpPduRcpEntryEcCrestFactor_Object=MibTableColumn
lgpPduRcpEntryEcCrestFactor=_LgpPduRcpEntryEcCrestFactor_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,162),_LgpPduRcpEntryEcCrestFactor_Type())
lgpPduRcpEntryEcCrestFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryEcCrestFactor.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryEcCrestFactor.setUnits('0.01')
class _LgpPduRcpEntryBlinkLED_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('blinkLED',2)))
_LgpPduRcpEntryBlinkLED_Type.__name__=_E
_LgpPduRcpEntryBlinkLED_Object=MibTableColumn
lgpPduRcpEntryBlinkLED=_LgpPduRcpEntryBlinkLED_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,200),_LgpPduRcpEntryBlinkLED_Type())
lgpPduRcpEntryBlinkLED.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryBlinkLED.setStatus(_A)
class _LgpPduRcpEntrySwOverTemperatureProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),(_e,1)))
_LgpPduRcpEntrySwOverTemperatureProtection_Type.__name__=_E
_LgpPduRcpEntrySwOverTemperatureProtection_Object=MibTableColumn
lgpPduRcpEntrySwOverTemperatureProtection=_LgpPduRcpEntrySwOverTemperatureProtection_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,205),_LgpPduRcpEntrySwOverTemperatureProtection_Type())
lgpPduRcpEntrySwOverTemperatureProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntrySwOverTemperatureProtection.setStatus(_A)
class _LgpPduRcpEntryOperationCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normalOperation',1),('normalWithWarning',2),('normalWithAlarm',3),('abnormal',4)))
_LgpPduRcpEntryOperationCondition_Type.__name__=_E
_LgpPduRcpEntryOperationCondition_Object=MibTableColumn
lgpPduRcpEntryOperationCondition=_LgpPduRcpEntryOperationCondition_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,210),_LgpPduRcpEntryOperationCondition_Type())
lgpPduRcpEntryOperationCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpEntryOperationCondition.setStatus(_A)
class _LgpPduRcpEntryCriticality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('critical',0),('notCritical',1)))
_LgpPduRcpEntryCriticality_Type.__name__=_E
_LgpPduRcpEntryCriticality_Object=MibTableColumn
lgpPduRcpEntryCriticality=_LgpPduRcpEntryCriticality_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,215),_LgpPduRcpEntryCriticality_Type())
lgpPduRcpEntryCriticality.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryCriticality.setStatus(_A)
_LgpPduRcpEntryPostOnDelay_Type=Unsigned32
_LgpPduRcpEntryPostOnDelay_Object=MibTableColumn
lgpPduRcpEntryPostOnDelay=_LgpPduRcpEntryPostOnDelay_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,220),_LgpPduRcpEntryPostOnDelay_Type())
lgpPduRcpEntryPostOnDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryPostOnDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryPostOnDelay.setUnits(_U)
_LgpPduRcpEntryPostOffDelay_Type=Unsigned32
_LgpPduRcpEntryPostOffDelay_Object=MibTableColumn
lgpPduRcpEntryPostOffDelay=_LgpPduRcpEntryPostOffDelay_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,225),_LgpPduRcpEntryPostOffDelay_Type())
lgpPduRcpEntryPostOffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryPostOffDelay.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpEntryPostOffDelay.setUnits(_U)
_LgpPduRcpEntryAddReceptacleToGroup_Type=ObjectIdentifier
_LgpPduRcpEntryAddReceptacleToGroup_Object=MibTableColumn
lgpPduRcpEntryAddReceptacleToGroup=_LgpPduRcpEntryAddReceptacleToGroup_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,230),_LgpPduRcpEntryAddReceptacleToGroup_Type())
lgpPduRcpEntryAddReceptacleToGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryAddReceptacleToGroup.setStatus(_A)
_LgpPduRcpEntryRemoveReceptacleFromGroup_Type=ObjectIdentifier
_LgpPduRcpEntryRemoveReceptacleFromGroup_Object=MibTableColumn
lgpPduRcpEntryRemoveReceptacleFromGroup=_LgpPduRcpEntryRemoveReceptacleFromGroup_Object((1,3,6,1,4,1,476,1,42,3,8,50,20,1,235),_LgpPduRcpEntryRemoveReceptacleFromGroup_Type())
lgpPduRcpEntryRemoveReceptacleFromGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpEntryRemoveReceptacleFromGroup.setStatus(_A)
_LgpPduRcpGroup_ObjectIdentity=ObjectIdentity
lgpPduRcpGroup=_LgpPduRcpGroup_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,50,30))
if mibBuilder.loadTexts:lgpPduRcpGroup.setStatus(_A)
_LgpPduRcpGroupTableCount_Type=Unsigned32
_LgpPduRcpGroupTableCount_Object=MibScalar
lgpPduRcpGroupTableCount=_LgpPduRcpGroupTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,9),_LgpPduRcpGroupTableCount_Type())
lgpPduRcpGroupTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpGroupTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpGroupTableCount.setUnits(_J)
_LgpPduRcpGroupTable_Object=MibTable
lgpPduRcpGroupTable=_LgpPduRcpGroupTable_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10))
if mibBuilder.loadTexts:lgpPduRcpGroupTable.setStatus(_A)
_LgpPduRcpGroupEntry_Object=MibTableRow
lgpPduRcpGroupEntry=_LgpPduRcpGroupEntry_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1))
lgpPduRcpGroupEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:lgpPduRcpGroupEntry.setStatus(_A)
_LgpPduRcpGroupIndex_Type=Unsigned32
_LgpPduRcpGroupIndex_Object=MibTableColumn
lgpPduRcpGroupIndex=_LgpPduRcpGroupIndex_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,1),_LgpPduRcpGroupIndex_Type())
lgpPduRcpGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduRcpGroupIndex.setStatus(_A)
_LgpPduRcpGroupUsrLabel_Type=DisplayString
_LgpPduRcpGroupUsrLabel_Object=MibTableColumn
lgpPduRcpGroupUsrLabel=_LgpPduRcpGroupUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,10),_LgpPduRcpGroupUsrLabel_Type())
lgpPduRcpGroupUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpGroupUsrLabel.setStatus(_A)
class _LgpPduRcpGroupDeleteGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),('delete-receptacle-group',1)))
_LgpPduRcpGroupDeleteGroup_Type.__name__=_E
_LgpPduRcpGroupDeleteGroup_Object=MibTableColumn
lgpPduRcpGroupDeleteGroup=_LgpPduRcpGroupDeleteGroup_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,20),_LgpPduRcpGroupDeleteGroup_Type())
lgpPduRcpGroupDeleteGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpGroupDeleteGroup.setStatus(_A)
class _LgpPduRcpGroupControlPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_c,0),(_a,1),(_b,2),(_A8,3)))
_LgpPduRcpGroupControlPower_Type.__name__=_E
_LgpPduRcpGroupControlPower_Object=MibTableColumn
lgpPduRcpGroupControlPower=_LgpPduRcpGroupControlPower_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,30),_LgpPduRcpGroupControlPower_Type())
lgpPduRcpGroupControlPower.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpGroupControlPower.setStatus(_A)
class _LgpPduRcpGroupControlLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),('unlock',1),('lock',2)))
_LgpPduRcpGroupControlLock_Type.__name__=_E
_LgpPduRcpGroupControlLock_Object=MibTableColumn
lgpPduRcpGroupControlLock=_LgpPduRcpGroupControlLock_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,40),_LgpPduRcpGroupControlLock_Type())
lgpPduRcpGroupControlLock.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpGroupControlLock.setStatus(_A)
class _LgpPduRcpGroupBlinkLED_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),('blinkLED',1)))
_LgpPduRcpGroupBlinkLED_Type.__name__=_E
_LgpPduRcpGroupBlinkLED_Object=MibTableColumn
lgpPduRcpGroupBlinkLED=_LgpPduRcpGroupBlinkLED_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,10,1,50),_LgpPduRcpGroupBlinkLED_Type())
lgpPduRcpGroupBlinkLED.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduRcpGroupBlinkLED.setStatus(_A)
_LgpPduRcpGroupDisplayTableCount_Type=Unsigned32
_LgpPduRcpGroupDisplayTableCount_Object=MibScalar
lgpPduRcpGroupDisplayTableCount=_LgpPduRcpGroupDisplayTableCount_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,19),_LgpPduRcpGroupDisplayTableCount_Type())
lgpPduRcpGroupDisplayTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayTableCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayTableCount.setUnits(_J)
_LgpPduRcpGroupDisplayTable_Object=MibTable
lgpPduRcpGroupDisplayTable=_LgpPduRcpGroupDisplayTable_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,20))
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayTable.setStatus(_A)
_LgpPduRcpGroupDisplayEntry_Object=MibTableRow
lgpPduRcpGroupDisplayEntry=_LgpPduRcpGroupDisplayEntry_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,20,1))
lgpPduRcpGroupDisplayEntry.setIndexNames((0,_F,_k),(0,_F,_K))
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayEntry.setStatus(_A)
_LgpPduRcpGroupDisplayIndex_Type=Unsigned32
_LgpPduRcpGroupDisplayIndex_Object=MibTableColumn
lgpPduRcpGroupDisplayIndex=_LgpPduRcpGroupDisplayIndex_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,20,1,10),_LgpPduRcpGroupDisplayIndex_Type())
lgpPduRcpGroupDisplayIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayIndex.setStatus(_A)
_LgpPduRcpGroupDisplayGroup_Type=DisplayString
_LgpPduRcpGroupDisplayGroup_Object=MibTableColumn
lgpPduRcpGroupDisplayGroup=_LgpPduRcpGroupDisplayGroup_Object((1,3,6,1,4,1,476,1,42,3,8,50,30,20,1,20),_LgpPduRcpGroupDisplayGroup_Type())
lgpPduRcpGroupDisplayGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduRcpGroupDisplayGroup.setStatus(_A)
_LgpPduAuxiliarySensors_ObjectIdentity=ObjectIdentity
lgpPduAuxiliarySensors=_LgpPduAuxiliarySensors_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,8,60))
if mibBuilder.loadTexts:lgpPduAuxiliarySensors.setStatus(_A)
_LgpPduAuxSensorCount_Type=Unsigned32
_LgpPduAuxSensorCount_Object=MibScalar
lgpPduAuxSensorCount=_LgpPduAuxSensorCount_Object((1,3,6,1,4,1,476,1,42,3,8,60,5),_LgpPduAuxSensorCount_Type())
lgpPduAuxSensorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorCount.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxSensorCount.setUnits(_J)
_LgpPduAuxSensorTable_Object=MibTable
lgpPduAuxSensorTable=_LgpPduAuxSensorTable_Object((1,3,6,1,4,1,476,1,42,3,8,60,10))
if mibBuilder.loadTexts:lgpPduAuxSensorTable.setStatus(_D)
_LgpPduAuxSensorEntry_Object=MibTableRow
lgpPduAuxSensorEntry=_LgpPduAuxSensorEntry_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1))
lgpPduAuxSensorEntry.setIndexNames((0,_F,_K),(0,_F,_A9))
if mibBuilder.loadTexts:lgpPduAuxSensorEntry.setStatus(_D)
_LgpPduAuxSensorIndex_Type=Unsigned32
_LgpPduAuxSensorIndex_Object=MibTableColumn
lgpPduAuxSensorIndex=_LgpPduAuxSensorIndex_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,1),_LgpPduAuxSensorIndex_Type())
lgpPduAuxSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduAuxSensorIndex.setStatus(_D)
class _LgpPduAuxSensorMeasType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_AA,1),('humidity',2),('temperature-and-humidity',3)))
_LgpPduAuxSensorMeasType_Type.__name__=_E
_LgpPduAuxSensorMeasType_Object=MibTableColumn
lgpPduAuxSensorMeasType=_LgpPduAuxSensorMeasType_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,5),_LgpPduAuxSensorMeasType_Type())
lgpPduAuxSensorMeasType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorMeasType.setStatus(_D)
_LgpPduAuxSensorId_Type=Unsigned32
_LgpPduAuxSensorId_Object=MibTableColumn
lgpPduAuxSensorId=_LgpPduAuxSensorId_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,10),_LgpPduAuxSensorId_Type())
lgpPduAuxSensorId.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorId.setStatus(_D)
_LgpPduAuxSensorSysAssignLabel_Type=DisplayString
_LgpPduAuxSensorSysAssignLabel_Object=MibTableColumn
lgpPduAuxSensorSysAssignLabel=_LgpPduAuxSensorSysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,15),_LgpPduAuxSensorSysAssignLabel_Type())
lgpPduAuxSensorSysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorSysAssignLabel.setStatus(_D)
_LgpPduAuxSensorPositionRelative_Type=Unsigned32
_LgpPduAuxSensorPositionRelative_Object=MibTableColumn
lgpPduAuxSensorPositionRelative=_LgpPduAuxSensorPositionRelative_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,20),_LgpPduAuxSensorPositionRelative_Type())
lgpPduAuxSensorPositionRelative.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorPositionRelative.setStatus(_D)
_LgpPduAuxSensorUsrLabel_Type=DisplayString
_LgpPduAuxSensorUsrLabel_Object=MibTableColumn
lgpPduAuxSensorUsrLabel=_LgpPduAuxSensorUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,25),_LgpPduAuxSensorUsrLabel_Type())
lgpPduAuxSensorUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorUsrLabel.setStatus(_D)
_LgpPduAuxSensorUsrTag1_Type=DisplayString
_LgpPduAuxSensorUsrTag1_Object=MibTableColumn
lgpPduAuxSensorUsrTag1=_LgpPduAuxSensorUsrTag1_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,30),_LgpPduAuxSensorUsrTag1_Type())
lgpPduAuxSensorUsrTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorUsrTag1.setStatus(_D)
_LgpPduAuxSensorUsrTag2_Type=DisplayString
_LgpPduAuxSensorUsrTag2_Object=MibTableColumn
lgpPduAuxSensorUsrTag2=_LgpPduAuxSensorUsrTag2_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,35),_LgpPduAuxSensorUsrTag2_Type())
lgpPduAuxSensorUsrTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorUsrTag2.setStatus(_D)
_LgpPduAuxSensorTempSerialNum_Type=DisplayString
_LgpPduAuxSensorTempSerialNum_Object=MibTableColumn
lgpPduAuxSensorTempSerialNum=_LgpPduAuxSensorTempSerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,40),_LgpPduAuxSensorTempSerialNum_Type())
lgpPduAuxSensorTempSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorTempSerialNum.setStatus(_D)
_LgpPduAuxSensorHumSerialNum_Type=DisplayString
_LgpPduAuxSensorHumSerialNum_Object=MibTableColumn
lgpPduAuxSensorHumSerialNum=_LgpPduAuxSensorHumSerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,45),_LgpPduAuxSensorHumSerialNum_Type())
lgpPduAuxSensorHumSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorHumSerialNum.setStatus(_D)
_LgpPduAuxSensorTempMeasurementDegF_Type=Integer32
_LgpPduAuxSensorTempMeasurementDegF_Object=MibTableColumn
lgpPduAuxSensorTempMeasurementDegF=_LgpPduAuxSensorTempMeasurementDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,50),_LgpPduAuxSensorTempMeasurementDegF_Type())
lgpPduAuxSensorTempMeasurementDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorTempMeasurementDegF.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempMeasurementDegF.setUnits(_L)
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Type=Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Object=MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegF=_LgpPduAuxSensorTempThrshldUndrAlmDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,55),_LgpPduAuxSensorTempThrshldUndrAlmDegF_Type())
lgpPduAuxSensorTempThrshldUndrAlmDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrAlmDegF.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrAlmDegF.setUnits(_L)
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Type=Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Object=MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegF=_LgpPduAuxSensorTempThrshldOvrAlmDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,60),_LgpPduAuxSensorTempThrshldOvrAlmDegF_Type())
lgpPduAuxSensorTempThrshldOvrAlmDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrAlmDegF.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrAlmDegF.setUnits(_L)
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Type=Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Object=MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegF=_LgpPduAuxSensorTempThrshldUndrWarnDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,65),_LgpPduAuxSensorTempThrshldUndrWarnDegF_Type())
lgpPduAuxSensorTempThrshldUndrWarnDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrWarnDegF.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrWarnDegF.setUnits(_L)
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Type=Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Object=MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegF=_LgpPduAuxSensorTempThrshldOvrWarnDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,70),_LgpPduAuxSensorTempThrshldOvrWarnDegF_Type())
lgpPduAuxSensorTempThrshldOvrWarnDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrWarnDegF.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrWarnDegF.setUnits(_L)
_LgpPduAuxSensorTempMeasurementDegC_Type=Integer32
_LgpPduAuxSensorTempMeasurementDegC_Object=MibTableColumn
lgpPduAuxSensorTempMeasurementDegC=_LgpPduAuxSensorTempMeasurementDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,75),_LgpPduAuxSensorTempMeasurementDegC_Type())
lgpPduAuxSensorTempMeasurementDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorTempMeasurementDegC.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempMeasurementDegC.setUnits(_M)
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Type=Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Object=MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegC=_LgpPduAuxSensorTempThrshldUndrAlmDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,80),_LgpPduAuxSensorTempThrshldUndrAlmDegC_Type())
lgpPduAuxSensorTempThrshldUndrAlmDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrAlmDegC.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrAlmDegC.setUnits(_M)
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Type=Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Object=MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegC=_LgpPduAuxSensorTempThrshldOvrAlmDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,85),_LgpPduAuxSensorTempThrshldOvrAlmDegC_Type())
lgpPduAuxSensorTempThrshldOvrAlmDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrAlmDegC.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrAlmDegC.setUnits(_M)
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Type=Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Object=MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegC=_LgpPduAuxSensorTempThrshldUndrWarnDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,90),_LgpPduAuxSensorTempThrshldUndrWarnDegC_Type())
lgpPduAuxSensorTempThrshldUndrWarnDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrWarnDegC.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldUndrWarnDegC.setUnits(_M)
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Type=Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Object=MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegC=_LgpPduAuxSensorTempThrshldOvrWarnDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,95),_LgpPduAuxSensorTempThrshldOvrWarnDegC_Type())
lgpPduAuxSensorTempThrshldOvrWarnDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrWarnDegC.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorTempThrshldOvrWarnDegC.setUnits(_M)
_LgpPduAuxSensorHumMeasurement_Type=Unsigned32
_LgpPduAuxSensorHumMeasurement_Object=MibTableColumn
lgpPduAuxSensorHumMeasurement=_LgpPduAuxSensorHumMeasurement_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,100),_LgpPduAuxSensorHumMeasurement_Type())
lgpPduAuxSensorHumMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxSensorHumMeasurement.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorHumMeasurement.setUnits(_N)
_LgpPduAuxSensorHumThrshldUndrAlm_Type=Unsigned32
_LgpPduAuxSensorHumThrshldUndrAlm_Object=MibTableColumn
lgpPduAuxSensorHumThrshldUndrAlm=_LgpPduAuxSensorHumThrshldUndrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,105),_LgpPduAuxSensorHumThrshldUndrAlm_Type())
lgpPduAuxSensorHumThrshldUndrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldUndrAlm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldUndrAlm.setUnits(_N)
_LgpPduAuxSensorHumThrshldOvrAlm_Type=Unsigned32
_LgpPduAuxSensorHumThrshldOvrAlm_Object=MibTableColumn
lgpPduAuxSensorHumThrshldOvrAlm=_LgpPduAuxSensorHumThrshldOvrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,110),_LgpPduAuxSensorHumThrshldOvrAlm_Type())
lgpPduAuxSensorHumThrshldOvrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldOvrAlm.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldOvrAlm.setUnits(_N)
_LgpPduAuxSensorHumThrshldUndrWarn_Type=Unsigned32
_LgpPduAuxSensorHumThrshldUndrWarn_Object=MibTableColumn
lgpPduAuxSensorHumThrshldUndrWarn=_LgpPduAuxSensorHumThrshldUndrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,115),_LgpPduAuxSensorHumThrshldUndrWarn_Type())
lgpPduAuxSensorHumThrshldUndrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldUndrWarn.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldUndrWarn.setUnits(_N)
_LgpPduAuxSensorHumThrshldOvrWarn_Type=Unsigned32
_LgpPduAuxSensorHumThrshldOvrWarn_Object=MibTableColumn
lgpPduAuxSensorHumThrshldOvrWarn=_LgpPduAuxSensorHumThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,10,1,120),_LgpPduAuxSensorHumThrshldOvrWarn_Type())
lgpPduAuxSensorHumThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldOvrWarn.setStatus(_D)
if mibBuilder.loadTexts:lgpPduAuxSensorHumThrshldOvrWarn.setUnits(_N)
_LgpPduAuxMeasTable_Object=MibTable
lgpPduAuxMeasTable=_LgpPduAuxMeasTable_Object((1,3,6,1,4,1,476,1,42,3,8,60,15))
if mibBuilder.loadTexts:lgpPduAuxMeasTable.setStatus(_A)
_LgpPduAuxMeasEntry_Object=MibTableRow
lgpPduAuxMeasEntry=_LgpPduAuxMeasEntry_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1))
lgpPduAuxMeasEntry.setIndexNames((0,_F,_K),(0,_F,_AB),(0,_F,_AC))
if mibBuilder.loadTexts:lgpPduAuxMeasEntry.setStatus(_A)
_LgpPduAuxMeasSensorIndex_Type=Unsigned32
_LgpPduAuxMeasSensorIndex_Object=MibTableColumn
lgpPduAuxMeasSensorIndex=_LgpPduAuxMeasSensorIndex_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,1),_LgpPduAuxMeasSensorIndex_Type())
lgpPduAuxMeasSensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduAuxMeasSensorIndex.setStatus(_A)
_LgpPduAuxMeasSensorMeasurementIndex_Type=Unsigned32
_LgpPduAuxMeasSensorMeasurementIndex_Object=MibTableColumn
lgpPduAuxMeasSensorMeasurementIndex=_LgpPduAuxMeasSensorMeasurementIndex_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,5),_LgpPduAuxMeasSensorMeasurementIndex_Type())
lgpPduAuxMeasSensorMeasurementIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduAuxMeasSensorMeasurementIndex.setStatus(_A)
class _LgpPduAuxMeasType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_AA,1),('humidity',2),('door-closure',3),('contact-closure',4),('differential-pressure',5),('leak-detection',6)))
_LgpPduAuxMeasType_Type.__name__=_E
_LgpPduAuxMeasType_Object=MibTableColumn
lgpPduAuxMeasType=_LgpPduAuxMeasType_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,10),_LgpPduAuxMeasType_Type())
lgpPduAuxMeasType.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasType.setStatus(_A)
_LgpPduAuxMeasSensorSysAssignLabel_Type=DisplayString
_LgpPduAuxMeasSensorSysAssignLabel_Object=MibTableColumn
lgpPduAuxMeasSensorSysAssignLabel=_LgpPduAuxMeasSensorSysAssignLabel_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,15),_LgpPduAuxMeasSensorSysAssignLabel_Type())
lgpPduAuxMeasSensorSysAssignLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasSensorSysAssignLabel.setStatus(_A)
_LgpPduAuxMeasUsrLabel_Type=DisplayString
_LgpPduAuxMeasUsrLabel_Object=MibTableColumn
lgpPduAuxMeasUsrLabel=_LgpPduAuxMeasUsrLabel_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,20),_LgpPduAuxMeasUsrLabel_Type())
lgpPduAuxMeasUsrLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasUsrLabel.setStatus(_A)
_LgpPduAuxMeasUsrTag1_Type=DisplayString
_LgpPduAuxMeasUsrTag1_Object=MibTableColumn
lgpPduAuxMeasUsrTag1=_LgpPduAuxMeasUsrTag1_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,25),_LgpPduAuxMeasUsrTag1_Type())
lgpPduAuxMeasUsrTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasUsrTag1.setStatus(_A)
_LgpPduAuxMeasUsrTag2_Type=DisplayString
_LgpPduAuxMeasUsrTag2_Object=MibTableColumn
lgpPduAuxMeasUsrTag2=_LgpPduAuxMeasUsrTag2_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,30),_LgpPduAuxMeasUsrTag2_Type())
lgpPduAuxMeasUsrTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasUsrTag2.setStatus(_A)
_LgpPduAuxMeasSensorSerialNum_Type=DisplayString
_LgpPduAuxMeasSensorSerialNum_Object=MibTableColumn
lgpPduAuxMeasSensorSerialNum=_LgpPduAuxMeasSensorSerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,35),_LgpPduAuxMeasSensorSerialNum_Type())
lgpPduAuxMeasSensorSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasSensorSerialNum.setStatus(_A)
_LgpPduAuxMeasTempDegF_Type=Integer32
_LgpPduAuxMeasTempDegF_Object=MibTableColumn
lgpPduAuxMeasTempDegF=_LgpPduAuxMeasTempDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,40),_LgpPduAuxMeasTempDegF_Type())
lgpPduAuxMeasTempDegF.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasTempDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempDegF.setUnits(_L)
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Type=Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Object=MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegF=_LgpPduAuxMeasTempThrshldUndrAlmDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,50),_LgpPduAuxMeasTempThrshldUndrAlmDegF_Type())
lgpPduAuxMeasTempThrshldUndrAlmDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrAlmDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrAlmDegF.setUnits(_L)
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Type=Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Object=MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegF=_LgpPduAuxMeasTempThrshldOvrAlmDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,55),_LgpPduAuxMeasTempThrshldOvrAlmDegF_Type())
lgpPduAuxMeasTempThrshldOvrAlmDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrAlmDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrAlmDegF.setUnits(_L)
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Type=Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Object=MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegF=_LgpPduAuxMeasTempThrshldUndrWarnDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,60),_LgpPduAuxMeasTempThrshldUndrWarnDegF_Type())
lgpPduAuxMeasTempThrshldUndrWarnDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrWarnDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrWarnDegF.setUnits(_L)
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Type=Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Object=MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegF=_LgpPduAuxMeasTempThrshldOvrWarnDegF_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,65),_LgpPduAuxMeasTempThrshldOvrWarnDegF_Type())
lgpPduAuxMeasTempThrshldOvrWarnDegF.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrWarnDegF.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrWarnDegF.setUnits(_L)
_LgpPduAuxMeasTempDegC_Type=Integer32
_LgpPduAuxMeasTempDegC_Object=MibTableColumn
lgpPduAuxMeasTempDegC=_LgpPduAuxMeasTempDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,70),_LgpPduAuxMeasTempDegC_Type())
lgpPduAuxMeasTempDegC.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasTempDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempDegC.setUnits(_M)
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Type=Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Object=MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegC=_LgpPduAuxMeasTempThrshldUndrAlmDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,75),_LgpPduAuxMeasTempThrshldUndrAlmDegC_Type())
lgpPduAuxMeasTempThrshldUndrAlmDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrAlmDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrAlmDegC.setUnits(_M)
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Type=Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Object=MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegC=_LgpPduAuxMeasTempThrshldOvrAlmDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,80),_LgpPduAuxMeasTempThrshldOvrAlmDegC_Type())
lgpPduAuxMeasTempThrshldOvrAlmDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrAlmDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrAlmDegC.setUnits(_M)
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Type=Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Object=MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegC=_LgpPduAuxMeasTempThrshldUndrWarnDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,85),_LgpPduAuxMeasTempThrshldUndrWarnDegC_Type())
lgpPduAuxMeasTempThrshldUndrWarnDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrWarnDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldUndrWarnDegC.setUnits(_M)
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Type=Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Object=MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegC=_LgpPduAuxMeasTempThrshldOvrWarnDegC_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,90),_LgpPduAuxMeasTempThrshldOvrWarnDegC_Type())
lgpPduAuxMeasTempThrshldOvrWarnDegC.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrWarnDegC.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasTempThrshldOvrWarnDegC.setUnits(_M)
_LgpPduAuxMeasHum_Type=Unsigned32
_LgpPduAuxMeasHum_Object=MibTableColumn
lgpPduAuxMeasHum=_LgpPduAuxMeasHum_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,95),_LgpPduAuxMeasHum_Type())
lgpPduAuxMeasHum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasHum.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasHum.setUnits(_N)
_LgpPduAuxMeasHumThrshldUndrAlm_Type=Unsigned32
_LgpPduAuxMeasHumThrshldUndrAlm_Object=MibTableColumn
lgpPduAuxMeasHumThrshldUndrAlm=_LgpPduAuxMeasHumThrshldUndrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,100),_LgpPduAuxMeasHumThrshldUndrAlm_Type())
lgpPduAuxMeasHumThrshldUndrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldUndrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldUndrAlm.setUnits(_N)
_LgpPduAuxMeasHumThrshldOvrAlm_Type=Unsigned32
_LgpPduAuxMeasHumThrshldOvrAlm_Object=MibTableColumn
lgpPduAuxMeasHumThrshldOvrAlm=_LgpPduAuxMeasHumThrshldOvrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,105),_LgpPduAuxMeasHumThrshldOvrAlm_Type())
lgpPduAuxMeasHumThrshldOvrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldOvrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldOvrAlm.setUnits(_N)
_LgpPduAuxMeasHumThrshldUndrWarn_Type=Unsigned32
_LgpPduAuxMeasHumThrshldUndrWarn_Object=MibTableColumn
lgpPduAuxMeasHumThrshldUndrWarn=_LgpPduAuxMeasHumThrshldUndrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,110),_LgpPduAuxMeasHumThrshldUndrWarn_Type())
lgpPduAuxMeasHumThrshldUndrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldUndrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldUndrWarn.setUnits(_N)
_LgpPduAuxMeasHumThrshldOvrWarn_Type=Unsigned32
_LgpPduAuxMeasHumThrshldOvrWarn_Object=MibTableColumn
lgpPduAuxMeasHumThrshldOvrWarn=_LgpPduAuxMeasHumThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,115),_LgpPduAuxMeasHumThrshldOvrWarn_Type())
lgpPduAuxMeasHumThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldOvrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasHumThrshldOvrWarn.setUnits(_N)
class _LgpPduAuxMeasDrClosureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('open',1),('closed',2)))
_LgpPduAuxMeasDrClosureState_Type.__name__=_E
_LgpPduAuxMeasDrClosureState_Object=MibTableColumn
lgpPduAuxMeasDrClosureState=_LgpPduAuxMeasDrClosureState_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,120),_LgpPduAuxMeasDrClosureState_Type())
lgpPduAuxMeasDrClosureState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasDrClosureState.setStatus(_A)
class _LgpPduAuxMeasDrClosureConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_AD,1)))
_LgpPduAuxMeasDrClosureConfig_Type.__name__=_E
_LgpPduAuxMeasDrClosureConfig_Object=MibTableColumn
lgpPduAuxMeasDrClosureConfig=_LgpPduAuxMeasDrClosureConfig_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,125),_LgpPduAuxMeasDrClosureConfig_Type())
lgpPduAuxMeasDrClosureConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasDrClosureConfig.setStatus(_A)
class _LgpPduAuxMeasCntctClosureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('open',1),('closed',2)))
_LgpPduAuxMeasCntctClosureState_Type.__name__=_E
_LgpPduAuxMeasCntctClosureState_Object=MibTableColumn
lgpPduAuxMeasCntctClosureState=_LgpPduAuxMeasCntctClosureState_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,130),_LgpPduAuxMeasCntctClosureState_Type())
lgpPduAuxMeasCntctClosureState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasCntctClosureState.setStatus(_A)
class _LgpPduAuxMeasCntctClosureConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_d,0),(_AD,1),('alarm-when-closed',2)))
_LgpPduAuxMeasCntctClosureConfig_Type.__name__=_E
_LgpPduAuxMeasCntctClosureConfig_Object=MibTableColumn
lgpPduAuxMeasCntctClosureConfig=_LgpPduAuxMeasCntctClosureConfig_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,135),_LgpPduAuxMeasCntctClosureConfig_Type())
lgpPduAuxMeasCntctClosureConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasCntctClosureConfig.setStatus(_A)
_LgpPduAuxMeasDiffPressure_Type=Integer32
_LgpPduAuxMeasDiffPressure_Object=MibTableColumn
lgpPduAuxMeasDiffPressure=_LgpPduAuxMeasDiffPressure_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,140),_LgpPduAuxMeasDiffPressure_Type())
lgpPduAuxMeasDiffPressure.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressure.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressure.setUnits(_T)
_LgpPduAuxMeasDiffPressureThrshldUndrAlm_Type=Integer32
_LgpPduAuxMeasDiffPressureThrshldUndrAlm_Object=MibTableColumn
lgpPduAuxMeasDiffPressureThrshldUndrAlm=_LgpPduAuxMeasDiffPressureThrshldUndrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,145),_LgpPduAuxMeasDiffPressureThrshldUndrAlm_Type())
lgpPduAuxMeasDiffPressureThrshldUndrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldUndrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldUndrAlm.setUnits(_T)
_LgpPduAuxMeasDiffPressureThrshldOvrAlm_Type=Integer32
_LgpPduAuxMeasDiffPressureThrshldOvrAlm_Object=MibTableColumn
lgpPduAuxMeasDiffPressureThrshldOvrAlm=_LgpPduAuxMeasDiffPressureThrshldOvrAlm_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,150),_LgpPduAuxMeasDiffPressureThrshldOvrAlm_Type())
lgpPduAuxMeasDiffPressureThrshldOvrAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldOvrAlm.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldOvrAlm.setUnits(_T)
_LgpPduAuxMeasDiffPressureThrshldUndrWarn_Type=Integer32
_LgpPduAuxMeasDiffPressureThrshldUndrWarn_Object=MibTableColumn
lgpPduAuxMeasDiffPressureThrshldUndrWarn=_LgpPduAuxMeasDiffPressureThrshldUndrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,155),_LgpPduAuxMeasDiffPressureThrshldUndrWarn_Type())
lgpPduAuxMeasDiffPressureThrshldUndrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldUndrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldUndrWarn.setUnits(_T)
_LgpPduAuxMeasDiffPressureThrshldOvrWarn_Type=Integer32
_LgpPduAuxMeasDiffPressureThrshldOvrWarn_Object=MibTableColumn
lgpPduAuxMeasDiffPressureThrshldOvrWarn=_LgpPduAuxMeasDiffPressureThrshldOvrWarn_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,160),_LgpPduAuxMeasDiffPressureThrshldOvrWarn_Type())
lgpPduAuxMeasDiffPressureThrshldOvrWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldOvrWarn.setStatus(_A)
if mibBuilder.loadTexts:lgpPduAuxMeasDiffPressureThrshldOvrWarn.setUnits(_T)
class _LgpPduAuxMeasLeakDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('no-leak-detected',1),('leak-detected',2),('leak-detection-pending',3),('cable-fault',4)))
_LgpPduAuxMeasLeakDetectState_Type.__name__=_E
_LgpPduAuxMeasLeakDetectState_Object=MibTableColumn
lgpPduAuxMeasLeakDetectState=_LgpPduAuxMeasLeakDetectState_Object((1,3,6,1,4,1,476,1,42,3,8,60,15,1,165),_LgpPduAuxMeasLeakDetectState_Type())
lgpPduAuxMeasLeakDetectState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpPduAuxMeasLeakDetectState.setStatus(_A)
_LgpPduAuxMeasOrderTable_Object=MibTable
lgpPduAuxMeasOrderTable=_LgpPduAuxMeasOrderTable_Object((1,3,6,1,4,1,476,1,42,3,8,60,20))
if mibBuilder.loadTexts:lgpPduAuxMeasOrderTable.setStatus(_A)
_LgpPduAuxMeasOrderEntry_Object=MibTableRow
lgpPduAuxMeasOrderEntry=_LgpPduAuxMeasOrderEntry_Object((1,3,6,1,4,1,476,1,42,3,8,60,20,1))
lgpPduAuxMeasOrderEntry.setIndexNames((0,_F,_K),(0,_F,_AE))
if mibBuilder.loadTexts:lgpPduAuxMeasOrderEntry.setStatus(_A)
_LgpPduAuxSensorOrderIndex_Type=Unsigned32
_LgpPduAuxSensorOrderIndex_Object=MibTableColumn
lgpPduAuxSensorOrderIndex=_LgpPduAuxSensorOrderIndex_Object((1,3,6,1,4,1,476,1,42,3,8,60,20,1,5),_LgpPduAuxSensorOrderIndex_Type())
lgpPduAuxSensorOrderIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lgpPduAuxSensorOrderIndex.setStatus(_A)
_LgpPduAuxMeasOrderSensorSerialNum_Type=DisplayString
_LgpPduAuxMeasOrderSensorSerialNum_Object=MibTableColumn
lgpPduAuxMeasOrderSensorSerialNum=_LgpPduAuxMeasOrderSensorSerialNum_Object((1,3,6,1,4,1,476,1,42,3,8,60,20,1,15),_LgpPduAuxMeasOrderSensorSerialNum_Type())
lgpPduAuxMeasOrderSensorSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpPduAuxMeasOrderSensorSerialNum.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'liebertGlobalProductsPduModule':liebertGlobalProductsPduModule,'lgpPduGlobalData':lgpPduGlobalData,'lgpPduEntrySWOverTemperatureProtectionConfig':lgpPduEntrySWOverTemperatureProtectionConfig,'lgpPduEntrySWOverTemperatureProtectionDelay':lgpPduEntrySWOverTemperatureProtectionDelay,'lgpPduCluster':lgpPduCluster,'lgpPduGrpSysStatus':lgpPduGrpSysStatus,'lgpPduTableCount':lgpPduTableCount,'lgpPduTable':lgpPduTable,'lgpPduEntry':lgpPduEntry,_K:lgpPduEntryIndex,'lgpPduEntryId':lgpPduEntryId,'lgpPduEntryUsrLabel':lgpPduEntryUsrLabel,'lgpPduEntrySysAssignLabel':lgpPduEntrySysAssignLabel,'lgpPduEntryPositionRelative':lgpPduEntryPositionRelative,'lgpPduEntrySysStatus':lgpPduEntrySysStatus,'lgpPduEntryUsrTag1':lgpPduEntryUsrTag1,'lgpPduEntryUsrTag2':lgpPduEntryUsrTag2,'lgpPduEntrySerialNumber':lgpPduEntrySerialNumber,'lgpPduEntryRbCount':lgpPduEntryRbCount,'lgpPduEntrySWOverCurrentProtection':lgpPduEntrySWOverCurrentProtection,'lgpPduPowerSource':lgpPduPowerSource,'lgpPduPsTableCount':lgpPduPsTableCount,'lgpPduPsTable':lgpPduPsTable,'lgpPduPsEntry':lgpPduPsEntry,_f:lgpPduPsEntryIndex,'lgpPduPsEntryId':lgpPduPsEntryId,'lgpPduPsEntrySysAssignLabel':lgpPduPsEntrySysAssignLabel,'lgpPduPsEntryModel':lgpPduPsEntryModel,'lgpPduPsEntryWiringType':lgpPduPsEntryWiringType,'lgpPduPsEntryEpInputRated':lgpPduPsEntryEpInputRated,'lgpPduPsEntryEcInputRated':lgpPduPsEntryEcInputRated,'lgpPduPsEntryFreqRated':lgpPduPsEntryFreqRated,'lgpPduPsEntryEnergyAccum':lgpPduPsEntryEnergyAccum,'lgpPduPsEntrySerialNum':lgpPduPsEntrySerialNum,'lgpPduPsEntryFirmwareVersion':lgpPduPsEntryFirmwareVersion,'lgpPduPsEntryPwrTotal':lgpPduPsEntryPwrTotal,'lgpPduPsEntryEcNeutral':lgpPduPsEntryEcNeutral,'lgpPduPsEntryEcNeutralThrshldOvrWarn':lgpPduPsEntryEcNeutralThrshldOvrWarn,'lgpPduPsEntryEcNeutralThrshldOvrAlarm':lgpPduPsEntryEcNeutralThrshldOvrAlarm,'lgpPduPsEntryUnbalancedLoadThrshldAlarm':lgpPduPsEntryUnbalancedLoadThrshldAlarm,'lgpPduPsEntryApTotal':lgpPduPsEntryApTotal,'lgpPduPsEntryPfTotal':lgpPduPsEntryPfTotal,'lgpPduPsEntryEcResidual':lgpPduPsEntryEcResidual,'lgpPduPsEntryEcResidualThrshldOvrAlarm':lgpPduPsEntryEcResidualThrshldOvrAlarm,'lgpPduPsLineTable':lgpPduPsLineTable,'lgpPduPsLineEntry':lgpPduPsLineEntry,_m:lgpPduPsLineEntryIndex,'lgpPduPsLineEntryId':lgpPduPsLineEntryId,'lgpPduPsLineEntryLine':lgpPduPsLineEntryLine,'lgpPduPsLineEntryEpLNTenths':lgpPduPsLineEntryEpLNTenths,'lgpPduPsLineEntryEpLN':lgpPduPsLineEntryEpLN,'lgpPduPsLineEntryEc':lgpPduPsLineEntryEc,'lgpPduPsLineEntryEcHundredths':lgpPduPsLineEntryEcHundredths,'lgpPduPsLineEntryEcThrshldUndrAlarm':lgpPduPsLineEntryEcThrshldUndrAlarm,'lgpPduPsLineEntryEcThrshldOvrWarn':lgpPduPsLineEntryEcThrshldOvrWarn,'lgpPduPsLineEntryEcThrshldOvrAlarm':lgpPduPsLineEntryEcThrshldOvrAlarm,'lgpPduPsLineEntryEcAvailBeforeAlarm':lgpPduPsLineEntryEcAvailBeforeAlarm,'lgpPduPsLineEntryEcUsedBeforeAlarm':lgpPduPsLineEntryEcUsedBeforeAlarm,'lgpPduPsLineEntryEpLL':lgpPduPsLineEntryEpLL,'lgpPduPsLineEntryEpLLTenths':lgpPduPsLineEntryEpLLTenths,'lgpPduPsLineEntryEcAvailBeforeAlarmHundredths':lgpPduPsLineEntryEcAvailBeforeAlarmHundredths,'lgpPduPsLineEntryPwrLN':lgpPduPsLineEntryPwrLN,'lgpPduPsLineEntryPwrLL':lgpPduPsLineEntryPwrLL,'lgpPduPsLineEntryApLN':lgpPduPsLineEntryApLN,'lgpPduPsLineEntryApLL':lgpPduPsLineEntryApLL,'lgpPduPsLineEntryPfLN':lgpPduPsLineEntryPfLN,'lgpPduPsLineEntryPfLL':lgpPduPsLineEntryPfLL,'lgpPduReceptacleBranch':lgpPduReceptacleBranch,'lgpPduRbTableCount':lgpPduRbTableCount,'lgpPduRbTable':lgpPduRbTable,'lgpPduRbEntry':lgpPduRbEntry,_Y:lgpPduRbEntryIndex,'lgpPduRbEntryId':lgpPduRbEntryId,'lgpPduRbEntryUsrLabel':lgpPduRbEntryUsrLabel,'lgpPduRbEntrySysAssignLabel':lgpPduRbEntrySysAssignLabel,'lgpPduRbEntryPositionRelative':lgpPduRbEntryPositionRelative,'lgpPduRbEntrySerialNum':lgpPduRbEntrySerialNum,'lgpPduRbEntryModel':lgpPduRbEntryModel,'lgpPduRbEntryFirmwareVersion':lgpPduRbEntryFirmwareVersion,'lgpPduRbEntryUsrTag1':lgpPduRbEntryUsrTag1,'lgpPduRbEntryUsrTag2':lgpPduRbEntryUsrTag2,'lgpPduRbEntryReceptacleType':lgpPduRbEntryReceptacleType,'lgpPduRbEntryCapabilities':lgpPduRbEntryCapabilities,'lgpPduRbEntryLineSource':lgpPduRbEntryLineSource,'lgpPduRbEntryRcpCount':lgpPduRbEntryRcpCount,'lgpPduRbEntryEpRated':lgpPduRbEntryEpRated,'lgpPduRbEntryEcRated':lgpPduRbEntryEcRated,'lgpPduRbEntryFreqRated':lgpPduRbEntryFreqRated,'lgpPduRbEntryEnergyAccum':lgpPduRbEntryEnergyAccum,'lgpPduRbEntryEpLNTenths':lgpPduRbEntryEpLNTenths,'lgpPduRbEntryPwr':lgpPduRbEntryPwr,'lgpPduRbEntryAp':lgpPduRbEntryAp,'lgpPduRbEntryPf':lgpPduRbEntryPf,'lgpPduRbEntryEcHundredths':lgpPduRbEntryEcHundredths,'lgpPduRbEntryEcThrshldUndrAlm':lgpPduRbEntryEcThrshldUndrAlm,'lgpPduRbEntryEcThrshldOvrWarn':lgpPduRbEntryEcThrshldOvrWarn,'lgpPduRbEntryEcThrshldOvrAlm':lgpPduRbEntryEcThrshldOvrAlm,'lgpPduRbEntryEcAvailBeforeAlarmHundredths':lgpPduRbEntryEcAvailBeforeAlarmHundredths,'lgpPduRbEntryEcUsedBeforeAlarm':lgpPduRbEntryEcUsedBeforeAlarm,'lgpPduRbEntryEpLLTenths':lgpPduRbEntryEpLLTenths,'lgpPduRbEntrySwOverCurrentProtection':lgpPduRbEntrySwOverCurrentProtection,'lgpPduRbLineTable':lgpPduRbLineTable,'lgpPduRbLineEntry':lgpPduRbLineEntry,_A6:lgpPduRbLineEntryIndex,'lgpPduRbLineEntryId':lgpPduRbLineEntryId,'lgpPduRbLineEntryLine':lgpPduRbLineEntryLine,'lgpPduRbLineEntryEpLNTenths':lgpPduRbLineEntryEpLNTenths,'lgpPduRbLineEntryEpLN':lgpPduRbLineEntryEpLN,'lgpPduRbLineEntryEc':lgpPduRbLineEntryEc,'lgpPduRbLineEntryPwr':lgpPduRbLineEntryPwr,'lgpPduRbLineEntryAp':lgpPduRbLineEntryAp,'lgpPduRbLineEntryPf':lgpPduRbLineEntryPf,'lgpPduRbLineEntryEcHundredths':lgpPduRbLineEntryEcHundredths,'lgpPduRbLineEntryEcThrshldUndrAlm':lgpPduRbLineEntryEcThrshldUndrAlm,'lgpPduRbLineEntryEcThrshldOvrWarn':lgpPduRbLineEntryEcThrshldOvrWarn,'lgpPduRbLineEntryEcThrshldOvrAlm':lgpPduRbLineEntryEcThrshldOvrAlm,'lgpPduRbLineEntryEcAvailBeforeAlarmHundredths':lgpPduRbLineEntryEcAvailBeforeAlarmHundredths,'lgpPduRbLineEntryEcAvailBeforeAlarm':lgpPduRbLineEntryEcAvailBeforeAlarm,'lgpPduRbLineEntryEcUsedBeforeAlarm':lgpPduRbLineEntryEcUsedBeforeAlarm,'lgpPduRbLineEntryEpLL':lgpPduRbLineEntryEpLL,'lgpPduRbLineEntryEpLLTenths':lgpPduRbLineEntryEpLLTenths,'lgpPduReceptacle':lgpPduReceptacle,'lgpPduRcpTableCount':lgpPduRcpTableCount,'lgpPduRcpTable':lgpPduRcpTable,'lgpPduRcpEntry':lgpPduRcpEntry,_A7:lgpPduRcpEntryIndex,'lgpPduRcpEntryId':lgpPduRcpEntryId,'lgpPduRcpEntryUsrLabel':lgpPduRcpEntryUsrLabel,'lgpPduRcpEntryUsrTag1':lgpPduRcpEntryUsrTag1,'lgpPduRcpEntryUsrTag2':lgpPduRcpEntryUsrTag2,'lgpPduRcpEntrySysAssignLabel':lgpPduRcpEntrySysAssignLabel,'lgpPduRcpEntryPosition':lgpPduRcpEntryPosition,'lgpPduRcpEntryType':lgpPduRcpEntryType,'lgpPduRcpEntryLineSource':lgpPduRcpEntryLineSource,'lgpPduRcpEntryCapabilities':lgpPduRcpEntryCapabilities,'lgpPduRcpEntryEp':lgpPduRcpEntryEp,'lgpPduRcpEntryEpTenths':lgpPduRcpEntryEpTenths,'lgpPduRcpEntryEc':lgpPduRcpEntryEc,'lgpPduRcpEntryEcHundredths':lgpPduRcpEntryEcHundredths,'lgpPduRcpEntryPwrOut':lgpPduRcpEntryPwrOut,'lgpPduRcpEntryApOut':lgpPduRcpEntryApOut,'lgpPduRcpEntryPf':lgpPduRcpEntryPf,'lgpPduRcpEntryFreq':lgpPduRcpEntryFreq,'lgpPduRcpEntryEnergyAccum':lgpPduRcpEntryEnergyAccum,'lgpPduRcpEntryPwrOnDelay':lgpPduRcpEntryPwrOnDelay,'lgpPduRcpEntryPwrState':lgpPduRcpEntryPwrState,'lgpPduRcpEntryPwrUpState':lgpPduRcpEntryPwrUpState,'lgpPduRcpEntryControl':lgpPduRcpEntryControl,'lgpPduRcpEntryControlLock':lgpPduRcpEntryControlLock,'lgpPduRcpEntryEcThrshldUnderAlarm':lgpPduRcpEntryEcThrshldUnderAlarm,'lgpPduRcpEntryEcThrshldOverWarn':lgpPduRcpEntryEcThrshldOverWarn,'lgpPduRcpEntryEcThrshldOverAlarm':lgpPduRcpEntryEcThrshldOverAlarm,'lgpPduRcpEntryEcAvailBeforeAlarmHundredths':lgpPduRcpEntryEcAvailBeforeAlarmHundredths,'lgpPduRcpEntryEcAvailBeforeAlarm':lgpPduRcpEntryEcAvailBeforeAlarm,'lgpPduRcpEntryEcUsedBeforeAlarm':lgpPduRcpEntryEcUsedBeforeAlarm,'lgpPduRcpEntryEcCrestFactor':lgpPduRcpEntryEcCrestFactor,'lgpPduRcpEntryBlinkLED':lgpPduRcpEntryBlinkLED,'lgpPduRcpEntrySwOverTemperatureProtection':lgpPduRcpEntrySwOverTemperatureProtection,'lgpPduRcpEntryOperationCondition':lgpPduRcpEntryOperationCondition,'lgpPduRcpEntryCriticality':lgpPduRcpEntryCriticality,'lgpPduRcpEntryPostOnDelay':lgpPduRcpEntryPostOnDelay,'lgpPduRcpEntryPostOffDelay':lgpPduRcpEntryPostOffDelay,'lgpPduRcpEntryAddReceptacleToGroup':lgpPduRcpEntryAddReceptacleToGroup,'lgpPduRcpEntryRemoveReceptacleFromGroup':lgpPduRcpEntryRemoveReceptacleFromGroup,'lgpPduRcpGroup':lgpPduRcpGroup,'lgpPduRcpGroupTableCount':lgpPduRcpGroupTableCount,'lgpPduRcpGroupTable':lgpPduRcpGroupTable,'lgpPduRcpGroupEntry':lgpPduRcpGroupEntry,_k:lgpPduRcpGroupIndex,'lgpPduRcpGroupUsrLabel':lgpPduRcpGroupUsrLabel,'lgpPduRcpGroupDeleteGroup':lgpPduRcpGroupDeleteGroup,'lgpPduRcpGroupControlPower':lgpPduRcpGroupControlPower,'lgpPduRcpGroupControlLock':lgpPduRcpGroupControlLock,'lgpPduRcpGroupBlinkLED':lgpPduRcpGroupBlinkLED,'lgpPduRcpGroupDisplayTableCount':lgpPduRcpGroupDisplayTableCount,'lgpPduRcpGroupDisplayTable':lgpPduRcpGroupDisplayTable,'lgpPduRcpGroupDisplayEntry':lgpPduRcpGroupDisplayEntry,'lgpPduRcpGroupDisplayIndex':lgpPduRcpGroupDisplayIndex,'lgpPduRcpGroupDisplayGroup':lgpPduRcpGroupDisplayGroup,'lgpPduAuxiliarySensors':lgpPduAuxiliarySensors,'lgpPduAuxSensorCount':lgpPduAuxSensorCount,'lgpPduAuxSensorTable':lgpPduAuxSensorTable,'lgpPduAuxSensorEntry':lgpPduAuxSensorEntry,_A9:lgpPduAuxSensorIndex,'lgpPduAuxSensorMeasType':lgpPduAuxSensorMeasType,'lgpPduAuxSensorId':lgpPduAuxSensorId,'lgpPduAuxSensorSysAssignLabel':lgpPduAuxSensorSysAssignLabel,'lgpPduAuxSensorPositionRelative':lgpPduAuxSensorPositionRelative,'lgpPduAuxSensorUsrLabel':lgpPduAuxSensorUsrLabel,'lgpPduAuxSensorUsrTag1':lgpPduAuxSensorUsrTag1,'lgpPduAuxSensorUsrTag2':lgpPduAuxSensorUsrTag2,'lgpPduAuxSensorTempSerialNum':lgpPduAuxSensorTempSerialNum,'lgpPduAuxSensorHumSerialNum':lgpPduAuxSensorHumSerialNum,'lgpPduAuxSensorTempMeasurementDegF':lgpPduAuxSensorTempMeasurementDegF,'lgpPduAuxSensorTempThrshldUndrAlmDegF':lgpPduAuxSensorTempThrshldUndrAlmDegF,'lgpPduAuxSensorTempThrshldOvrAlmDegF':lgpPduAuxSensorTempThrshldOvrAlmDegF,'lgpPduAuxSensorTempThrshldUndrWarnDegF':lgpPduAuxSensorTempThrshldUndrWarnDegF,'lgpPduAuxSensorTempThrshldOvrWarnDegF':lgpPduAuxSensorTempThrshldOvrWarnDegF,'lgpPduAuxSensorTempMeasurementDegC':lgpPduAuxSensorTempMeasurementDegC,'lgpPduAuxSensorTempThrshldUndrAlmDegC':lgpPduAuxSensorTempThrshldUndrAlmDegC,'lgpPduAuxSensorTempThrshldOvrAlmDegC':lgpPduAuxSensorTempThrshldOvrAlmDegC,'lgpPduAuxSensorTempThrshldUndrWarnDegC':lgpPduAuxSensorTempThrshldUndrWarnDegC,'lgpPduAuxSensorTempThrshldOvrWarnDegC':lgpPduAuxSensorTempThrshldOvrWarnDegC,'lgpPduAuxSensorHumMeasurement':lgpPduAuxSensorHumMeasurement,'lgpPduAuxSensorHumThrshldUndrAlm':lgpPduAuxSensorHumThrshldUndrAlm,'lgpPduAuxSensorHumThrshldOvrAlm':lgpPduAuxSensorHumThrshldOvrAlm,'lgpPduAuxSensorHumThrshldUndrWarn':lgpPduAuxSensorHumThrshldUndrWarn,'lgpPduAuxSensorHumThrshldOvrWarn':lgpPduAuxSensorHumThrshldOvrWarn,'lgpPduAuxMeasTable':lgpPduAuxMeasTable,'lgpPduAuxMeasEntry':lgpPduAuxMeasEntry,_AB:lgpPduAuxMeasSensorIndex,_AC:lgpPduAuxMeasSensorMeasurementIndex,'lgpPduAuxMeasType':lgpPduAuxMeasType,'lgpPduAuxMeasSensorSysAssignLabel':lgpPduAuxMeasSensorSysAssignLabel,'lgpPduAuxMeasUsrLabel':lgpPduAuxMeasUsrLabel,'lgpPduAuxMeasUsrTag1':lgpPduAuxMeasUsrTag1,'lgpPduAuxMeasUsrTag2':lgpPduAuxMeasUsrTag2,'lgpPduAuxMeasSensorSerialNum':lgpPduAuxMeasSensorSerialNum,'lgpPduAuxMeasTempDegF':lgpPduAuxMeasTempDegF,'lgpPduAuxMeasTempThrshldUndrAlmDegF':lgpPduAuxMeasTempThrshldUndrAlmDegF,'lgpPduAuxMeasTempThrshldOvrAlmDegF':lgpPduAuxMeasTempThrshldOvrAlmDegF,'lgpPduAuxMeasTempThrshldUndrWarnDegF':lgpPduAuxMeasTempThrshldUndrWarnDegF,'lgpPduAuxMeasTempThrshldOvrWarnDegF':lgpPduAuxMeasTempThrshldOvrWarnDegF,'lgpPduAuxMeasTempDegC':lgpPduAuxMeasTempDegC,'lgpPduAuxMeasTempThrshldUndrAlmDegC':lgpPduAuxMeasTempThrshldUndrAlmDegC,'lgpPduAuxMeasTempThrshldOvrAlmDegC':lgpPduAuxMeasTempThrshldOvrAlmDegC,'lgpPduAuxMeasTempThrshldUndrWarnDegC':lgpPduAuxMeasTempThrshldUndrWarnDegC,'lgpPduAuxMeasTempThrshldOvrWarnDegC':lgpPduAuxMeasTempThrshldOvrWarnDegC,'lgpPduAuxMeasHum':lgpPduAuxMeasHum,'lgpPduAuxMeasHumThrshldUndrAlm':lgpPduAuxMeasHumThrshldUndrAlm,'lgpPduAuxMeasHumThrshldOvrAlm':lgpPduAuxMeasHumThrshldOvrAlm,'lgpPduAuxMeasHumThrshldUndrWarn':lgpPduAuxMeasHumThrshldUndrWarn,'lgpPduAuxMeasHumThrshldOvrWarn':lgpPduAuxMeasHumThrshldOvrWarn,'lgpPduAuxMeasDrClosureState':lgpPduAuxMeasDrClosureState,'lgpPduAuxMeasDrClosureConfig':lgpPduAuxMeasDrClosureConfig,'lgpPduAuxMeasCntctClosureState':lgpPduAuxMeasCntctClosureState,'lgpPduAuxMeasCntctClosureConfig':lgpPduAuxMeasCntctClosureConfig,'lgpPduAuxMeasDiffPressure':lgpPduAuxMeasDiffPressure,'lgpPduAuxMeasDiffPressureThrshldUndrAlm':lgpPduAuxMeasDiffPressureThrshldUndrAlm,'lgpPduAuxMeasDiffPressureThrshldOvrAlm':lgpPduAuxMeasDiffPressureThrshldOvrAlm,'lgpPduAuxMeasDiffPressureThrshldUndrWarn':lgpPduAuxMeasDiffPressureThrshldUndrWarn,'lgpPduAuxMeasDiffPressureThrshldOvrWarn':lgpPduAuxMeasDiffPressureThrshldOvrWarn,'lgpPduAuxMeasLeakDetectState':lgpPduAuxMeasLeakDetectState,'lgpPduAuxMeasOrderTable':lgpPduAuxMeasOrderTable,'lgpPduAuxMeasOrderEntry':lgpPduAuxMeasOrderEntry,_AE:lgpPduAuxSensorOrderIndex,'lgpPduAuxMeasOrderSensorSerialNum':lgpPduAuxMeasOrderSensorSerialNum})