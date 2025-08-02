_l='ciscoDot11HtMacOperationsGroup'
_k='ciscoDot11HtMacStationConfigGroup'
_j='cD11HtMacPCO20MinDuration'
_i='cD11HtMacPCO40MinDuration'
_h='cD11HtMacPCO20MaxDuration'
_g='cD11HtMacPCO40MaxDuration'
_f='cD11HtMacPCOActivated'
_e='cD11HtMacNonGFEntitiesPresent'
_d='cD11HtMacLSigTxOpFullProtectionEnabled'
_c='cD11HtMacDualCTSProtection'
_b='cD11HtMacServiceIntervalGranularity'
_a='cD11HtMacPSMPControlledAccess'
_Z='cD11HtMacRIFSMode'
_Y='cD11HtMacOperatingMode'
_X='cD11HtMacAMPDUEnable'
_W='cD11HtMacAMSDUEnable'
_V='cD11HtMacMCSFeedbackImplemented'
_U='cD11HtMacTransitionTime'
_T='cD11HtMacPCOImplemented'
_S='cD11HtMacMPDUDensity'
_R='cD11HtMacMaxRxAMPDUFactor'
_Q='cD11HtMacLsigTxOpProtectImplemented'
_P='cD11HtMacSTBCControlFrameImplemented'
_O='cD11HtMacPSMPImplemented'
_N='cD11HtMacMaxAMSDULength'
_M='cD11HtMacNDelayedBlockAckImplemented'
_L='cD11HtMacMIMOPowerSave'
_K='cD11HtMacOperationalMCSSet'
_J='OctetString'
_I='ifIndex'
_H='IF-MIB'
_G='TU'
_F='read-only'
_E='Integer32'
_D='TruthValue'
_C='read-write'
_B='CISCO-DOT11-HT-MAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ciscoDot11HtMacMIB=ModuleIdentity((1,3,6,1,4,1,9,9,626))
if mibBuilder.loadTexts:ciscoDot11HtMacMIB.setRevisions(('2007-05-16 00:00',))
_CiscoDot11HtMacMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11HtMacMIBNotifs=_CiscoDot11HtMacMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,626,0))
_CiscoDot11HtMacMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11HtMacMIBObjects=_CiscoDot11HtMacMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,626,1))
_CD11HtMacStationConfig_ObjectIdentity=ObjectIdentity
cD11HtMacStationConfig=_CD11HtMacStationConfig_ObjectIdentity((1,3,6,1,4,1,9,9,626,1,1))
_CD11HtMacStationConfigTable_Object=MibTable
cD11HtMacStationConfigTable=_CD11HtMacStationConfigTable_Object((1,3,6,1,4,1,9,9,626,1,1,1))
if mibBuilder.loadTexts:cD11HtMacStationConfigTable.setStatus(_A)
_CD11HtMacStationConfigEntry_Object=MibTableRow
cD11HtMacStationConfigEntry=_CD11HtMacStationConfigEntry_Object((1,3,6,1,4,1,9,9,626,1,1,1,1))
cD11HtMacStationConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cD11HtMacStationConfigEntry.setStatus(_A)
class _CD11HtMacOperationalMCSSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CD11HtMacOperationalMCSSet_Type.__name__=_J
_CD11HtMacOperationalMCSSet_Object=MibTableColumn
cD11HtMacOperationalMCSSet=_CD11HtMacOperationalMCSSet_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,1),_CD11HtMacOperationalMCSSet_Type())
cD11HtMacOperationalMCSSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacOperationalMCSSet.setStatus(_A)
class _CD11HtMacMIMOPowerSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('mimo',3)))
_CD11HtMacMIMOPowerSave_Type.__name__=_E
_CD11HtMacMIMOPowerSave_Object=MibTableColumn
cD11HtMacMIMOPowerSave=_CD11HtMacMIMOPowerSave_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,2),_CD11HtMacMIMOPowerSave_Type())
cD11HtMacMIMOPowerSave.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacMIMOPowerSave.setStatus(_A)
class _CD11HtMacNDelayedBlockAckImplemented_Type(TruthValue):defaultValue=2
_CD11HtMacNDelayedBlockAckImplemented_Type.__name__=_D
_CD11HtMacNDelayedBlockAckImplemented_Object=MibTableColumn
cD11HtMacNDelayedBlockAckImplemented=_CD11HtMacNDelayedBlockAckImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,3),_CD11HtMacNDelayedBlockAckImplemented_Type())
cD11HtMacNDelayedBlockAckImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacNDelayedBlockAckImplemented.setStatus(_A)
class _CD11HtMacMaxAMSDULength_Type(Integer32):defaultValue=3839;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3839,7935)));namedValues=NamedValues(*(('amsduSize3839',3839),('amsduSize7935',7935)))
_CD11HtMacMaxAMSDULength_Type.__name__=_E
_CD11HtMacMaxAMSDULength_Object=MibTableColumn
cD11HtMacMaxAMSDULength=_CD11HtMacMaxAMSDULength_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,4),_CD11HtMacMaxAMSDULength_Type())
cD11HtMacMaxAMSDULength.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacMaxAMSDULength.setStatus(_A)
class _CD11HtMacPSMPImplemented_Type(TruthValue):defaultValue=2
_CD11HtMacPSMPImplemented_Type.__name__=_D
_CD11HtMacPSMPImplemented_Object=MibTableColumn
cD11HtMacPSMPImplemented=_CD11HtMacPSMPImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,5),_CD11HtMacPSMPImplemented_Type())
cD11HtMacPSMPImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacPSMPImplemented.setStatus(_A)
class _CD11HtMacSTBCControlFrameImplemented_Type(TruthValue):defaultValue=2
_CD11HtMacSTBCControlFrameImplemented_Type.__name__=_D
_CD11HtMacSTBCControlFrameImplemented_Object=MibTableColumn
cD11HtMacSTBCControlFrameImplemented=_CD11HtMacSTBCControlFrameImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,6),_CD11HtMacSTBCControlFrameImplemented_Type())
cD11HtMacSTBCControlFrameImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacSTBCControlFrameImplemented.setStatus(_A)
class _CD11HtMacLsigTxOpProtectImplemented_Type(TruthValue):defaultValue=2
_CD11HtMacLsigTxOpProtectImplemented_Type.__name__=_D
_CD11HtMacLsigTxOpProtectImplemented_Object=MibTableColumn
cD11HtMacLsigTxOpProtectImplemented=_CD11HtMacLsigTxOpProtectImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,7),_CD11HtMacLsigTxOpProtectImplemented_Type())
cD11HtMacLsigTxOpProtectImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacLsigTxOpProtectImplemented.setStatus(_A)
class _CD11HtMacMaxRxAMPDUFactor_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CD11HtMacMaxRxAMPDUFactor_Type.__name__=_E
_CD11HtMacMaxRxAMPDUFactor_Object=MibTableColumn
cD11HtMacMaxRxAMPDUFactor=_CD11HtMacMaxRxAMPDUFactor_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,8),_CD11HtMacMaxRxAMPDUFactor_Type())
cD11HtMacMaxRxAMPDUFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacMaxRxAMPDUFactor.setStatus(_A)
class _CD11HtMacMPDUDensity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noTimeRestriction',1),('oneEighth',2),('oneFourth',3),('half',4),('one',5),('two',6),('four',7),('eight',8)))
_CD11HtMacMPDUDensity_Type.__name__=_E
_CD11HtMacMPDUDensity_Object=MibTableColumn
cD11HtMacMPDUDensity=_CD11HtMacMPDUDensity_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,9),_CD11HtMacMPDUDensity_Type())
cD11HtMacMPDUDensity.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacMPDUDensity.setStatus(_A)
class _CD11HtMacPCOImplemented_Type(TruthValue):defaultValue=2
_CD11HtMacPCOImplemented_Type.__name__=_D
_CD11HtMacPCOImplemented_Object=MibTableColumn
cD11HtMacPCOImplemented=_CD11HtMacPCOImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,10),_CD11HtMacPCOImplemented_Type())
cD11HtMacPCOImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacPCOImplemented.setStatus(_A)
class _CD11HtMacTransitionTime_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(400,1500,5000)));namedValues=NamedValues(*(('fourHundred',400),('oneThousandFiveHundred',1500),('fiveThousand',5000)))
_CD11HtMacTransitionTime_Type.__name__=_E
_CD11HtMacTransitionTime_Object=MibTableColumn
cD11HtMacTransitionTime=_CD11HtMacTransitionTime_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,11),_CD11HtMacTransitionTime_Type())
cD11HtMacTransitionTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacTransitionTime.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacTransitionTime.setUnits('microseconds')
class _CD11HtMacMCSFeedbackImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('unsolicited',2),('both',3)))
_CD11HtMacMCSFeedbackImplemented_Type.__name__=_E
_CD11HtMacMCSFeedbackImplemented_Object=MibTableColumn
cD11HtMacMCSFeedbackImplemented=_CD11HtMacMCSFeedbackImplemented_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,12),_CD11HtMacMCSFeedbackImplemented_Type())
cD11HtMacMCSFeedbackImplemented.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtMacMCSFeedbackImplemented.setStatus(_A)
class _CD11HtMacAMSDUEnable_Type(TruthValue):defaultValue=2
_CD11HtMacAMSDUEnable_Type.__name__=_D
_CD11HtMacAMSDUEnable_Object=MibTableColumn
cD11HtMacAMSDUEnable=_CD11HtMacAMSDUEnable_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,13),_CD11HtMacAMSDUEnable_Type())
cD11HtMacAMSDUEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacAMSDUEnable.setStatus(_A)
class _CD11HtMacAMPDUEnable_Type(TruthValue):defaultValue=2
_CD11HtMacAMPDUEnable_Type.__name__=_D
_CD11HtMacAMPDUEnable_Object=MibTableColumn
cD11HtMacAMPDUEnable=_CD11HtMacAMPDUEnable_Object((1,3,6,1,4,1,9,9,626,1,1,1,1,14),_CD11HtMacAMPDUEnable_Type())
cD11HtMacAMPDUEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacAMPDUEnable.setStatus(_A)
_CD11HtMacOperations_ObjectIdentity=ObjectIdentity
cD11HtMacOperations=_CD11HtMacOperations_ObjectIdentity((1,3,6,1,4,1,9,9,626,1,2))
_CD11HtMacOperationTable_Object=MibTable
cD11HtMacOperationTable=_CD11HtMacOperationTable_Object((1,3,6,1,4,1,9,9,626,1,2,1))
if mibBuilder.loadTexts:cD11HtMacOperationTable.setStatus(_A)
_CD11HtMacOperationEntry_Object=MibTableRow
cD11HtMacOperationEntry=_CD11HtMacOperationEntry_Object((1,3,6,1,4,1,9,9,626,1,2,1,1))
cD11HtMacOperationEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cD11HtMacOperationEntry.setStatus(_A)
class _CD11HtMacOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pureHt',1),('optionalProtection',2),('mandatoryFortyProtection',3),('mandatoryAllProtection',4)))
_CD11HtMacOperatingMode_Type.__name__=_E
_CD11HtMacOperatingMode_Object=MibTableColumn
cD11HtMacOperatingMode=_CD11HtMacOperatingMode_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,1),_CD11HtMacOperatingMode_Type())
cD11HtMacOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacOperatingMode.setStatus(_A)
class _CD11HtMacRIFSMode_Type(TruthValue):defaultValue=2
_CD11HtMacRIFSMode_Type.__name__=_D
_CD11HtMacRIFSMode_Object=MibTableColumn
cD11HtMacRIFSMode=_CD11HtMacRIFSMode_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,2),_CD11HtMacRIFSMode_Type())
cD11HtMacRIFSMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacRIFSMode.setStatus(_A)
class _CD11HtMacPSMPControlledAccess_Type(TruthValue):defaultValue=2
_CD11HtMacPSMPControlledAccess_Type.__name__=_D
_CD11HtMacPSMPControlledAccess_Object=MibTableColumn
cD11HtMacPSMPControlledAccess=_CD11HtMacPSMPControlledAccess_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,3),_CD11HtMacPSMPControlledAccess_Type())
cD11HtMacPSMPControlledAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPSMPControlledAccess.setStatus(_A)
class _CD11HtMacServiceIntervalGranularity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CD11HtMacServiceIntervalGranularity_Type.__name__=_E
_CD11HtMacServiceIntervalGranularity_Object=MibTableColumn
cD11HtMacServiceIntervalGranularity=_CD11HtMacServiceIntervalGranularity_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,4),_CD11HtMacServiceIntervalGranularity_Type())
cD11HtMacServiceIntervalGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacServiceIntervalGranularity.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacServiceIntervalGranularity.setUnits('milliseconds')
class _CD11HtMacDualCTSProtection_Type(TruthValue):defaultValue=2
_CD11HtMacDualCTSProtection_Type.__name__=_D
_CD11HtMacDualCTSProtection_Object=MibTableColumn
cD11HtMacDualCTSProtection=_CD11HtMacDualCTSProtection_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,5),_CD11HtMacDualCTSProtection_Type())
cD11HtMacDualCTSProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacDualCTSProtection.setStatus(_A)
class _CD11HtMacLSigTxOpFullProtectionEnabled_Type(TruthValue):defaultValue=2
_CD11HtMacLSigTxOpFullProtectionEnabled_Type.__name__=_D
_CD11HtMacLSigTxOpFullProtectionEnabled_Object=MibTableColumn
cD11HtMacLSigTxOpFullProtectionEnabled=_CD11HtMacLSigTxOpFullProtectionEnabled_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,6),_CD11HtMacLSigTxOpFullProtectionEnabled_Type())
cD11HtMacLSigTxOpFullProtectionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacLSigTxOpFullProtectionEnabled.setStatus(_A)
class _CD11HtMacNonGFEntitiesPresent_Type(TruthValue):defaultValue=2
_CD11HtMacNonGFEntitiesPresent_Type.__name__=_D
_CD11HtMacNonGFEntitiesPresent_Object=MibTableColumn
cD11HtMacNonGFEntitiesPresent=_CD11HtMacNonGFEntitiesPresent_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,7),_CD11HtMacNonGFEntitiesPresent_Type())
cD11HtMacNonGFEntitiesPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacNonGFEntitiesPresent.setStatus(_A)
class _CD11HtMacPCOActivated_Type(TruthValue):defaultValue=2
_CD11HtMacPCOActivated_Type.__name__=_D
_CD11HtMacPCOActivated_Object=MibTableColumn
cD11HtMacPCOActivated=_CD11HtMacPCOActivated_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,8),_CD11HtMacPCOActivated_Type())
cD11HtMacPCOActivated.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPCOActivated.setStatus(_A)
class _CD11HtMacPCO20MaxDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CD11HtMacPCO20MaxDuration_Type.__name__=_E
_CD11HtMacPCO20MaxDuration_Object=MibTableColumn
cD11HtMacPCO20MaxDuration=_CD11HtMacPCO20MaxDuration_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,9),_CD11HtMacPCO20MaxDuration_Type())
cD11HtMacPCO20MaxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPCO20MaxDuration.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacPCO20MaxDuration.setUnits(_G)
class _CD11HtMacPCO40MaxDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CD11HtMacPCO40MaxDuration_Type.__name__=_E
_CD11HtMacPCO40MaxDuration_Object=MibTableColumn
cD11HtMacPCO40MaxDuration=_CD11HtMacPCO40MaxDuration_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,10),_CD11HtMacPCO40MaxDuration_Type())
cD11HtMacPCO40MaxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPCO40MaxDuration.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacPCO40MaxDuration.setUnits(_G)
class _CD11HtMacPCO20MinDuration_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CD11HtMacPCO20MinDuration_Type.__name__=_E
_CD11HtMacPCO20MinDuration_Object=MibTableColumn
cD11HtMacPCO20MinDuration=_CD11HtMacPCO20MinDuration_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,11),_CD11HtMacPCO20MinDuration_Type())
cD11HtMacPCO20MinDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPCO20MinDuration.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacPCO20MinDuration.setUnits(_G)
class _CD11HtMacPCO40MinDuration_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CD11HtMacPCO40MinDuration_Type.__name__=_E
_CD11HtMacPCO40MinDuration_Object=MibTableColumn
cD11HtMacPCO40MinDuration=_CD11HtMacPCO40MinDuration_Object((1,3,6,1,4,1,9,9,626,1,2,1,1,12),_CD11HtMacPCO40MinDuration_Type())
cD11HtMacPCO40MinDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtMacPCO40MinDuration.setStatus(_A)
if mibBuilder.loadTexts:cD11HtMacPCO40MinDuration.setUnits(_G)
_CiscoDot11HtMacMIBConform_ObjectIdentity=ObjectIdentity
ciscoDot11HtMacMIBConform=_CiscoDot11HtMacMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,626,2))
_CiscoDot11HtMacMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11HtMacMIBCompliances=_CiscoDot11HtMacMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,626,2,1))
_CiscoDot11HtMacMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11HtMacMIBGroups=_CiscoDot11HtMacMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,626,2,2))
ciscoDot11HtMacStationConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,626,2,2,1))
ciscoDot11HtMacStationConfigGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoDot11HtMacStationConfigGroup.setStatus(_A)
ciscoDot11HtMacOperationsGroup=ObjectGroup((1,3,6,1,4,1,9,9,626,2,2,2))
ciscoDot11HtMacOperationsGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoDot11HtMacOperationsGroup.setStatus(_A)
cD11HtMacCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,626,2,1,1))
cD11HtMacCompliance.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cD11HtMacCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDot11HtMacMIB':ciscoDot11HtMacMIB,'ciscoDot11HtMacMIBNotifs':ciscoDot11HtMacMIBNotifs,'ciscoDot11HtMacMIBObjects':ciscoDot11HtMacMIBObjects,'cD11HtMacStationConfig':cD11HtMacStationConfig,'cD11HtMacStationConfigTable':cD11HtMacStationConfigTable,'cD11HtMacStationConfigEntry':cD11HtMacStationConfigEntry,_K:cD11HtMacOperationalMCSSet,_L:cD11HtMacMIMOPowerSave,_M:cD11HtMacNDelayedBlockAckImplemented,_N:cD11HtMacMaxAMSDULength,_O:cD11HtMacPSMPImplemented,_P:cD11HtMacSTBCControlFrameImplemented,_Q:cD11HtMacLsigTxOpProtectImplemented,_R:cD11HtMacMaxRxAMPDUFactor,_S:cD11HtMacMPDUDensity,_T:cD11HtMacPCOImplemented,_U:cD11HtMacTransitionTime,_V:cD11HtMacMCSFeedbackImplemented,_W:cD11HtMacAMSDUEnable,_X:cD11HtMacAMPDUEnable,'cD11HtMacOperations':cD11HtMacOperations,'cD11HtMacOperationTable':cD11HtMacOperationTable,'cD11HtMacOperationEntry':cD11HtMacOperationEntry,_Y:cD11HtMacOperatingMode,_Z:cD11HtMacRIFSMode,_a:cD11HtMacPSMPControlledAccess,_b:cD11HtMacServiceIntervalGranularity,_c:cD11HtMacDualCTSProtection,_d:cD11HtMacLSigTxOpFullProtectionEnabled,_e:cD11HtMacNonGFEntitiesPresent,_f:cD11HtMacPCOActivated,_h:cD11HtMacPCO20MaxDuration,_g:cD11HtMacPCO40MaxDuration,_j:cD11HtMacPCO20MinDuration,_i:cD11HtMacPCO40MinDuration,'ciscoDot11HtMacMIBConform':ciscoDot11HtMacMIBConform,'ciscoDot11HtMacMIBCompliances':ciscoDot11HtMacMIBCompliances,'cD11HtMacCompliance':cD11HtMacCompliance,'ciscoDot11HtMacMIBGroups':ciscoDot11HtMacMIBGroups,_k:ciscoDot11HtMacStationConfigGroup,_l:ciscoDot11HtMacOperationsGroup})