_N='eltCascadeEntry'
_M='eltPhdUnitGenParamEntry'
_L='read-write'
_K='hybrid'
_J='eltPhdTransceiverThresholdType'
_I='vendorspec'
_H='TruthValue'
_G='ifIndex'
_F='IF-MIB'
_E='ELTEX-MES-PHYSICAL-DESCRIPTION-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex','InterfaceIndexOrZero',_G)
JackType,=mibBuilder.importSymbols('MAU-MIB','JackType')
rlCascadeEntry,rlPhdUnitGenParamEntry=mibBuilder.importSymbols('RADLAN-Physicaldescription-MIB','rlCascadeEntry','rlPhdUnitGenParamEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
eltMesPhysicalDescription=ModuleIdentity((1,3,6,1,4,1,35265,1,23,53))
if mibBuilder.loadTexts:eltMesPhysicalDescription.setRevisions(('2018-04-24 00:00','2017-11-11 00:00','2015-09-14 00:00','2013-03-21 00:00'))
_EltMesPhdTransceiver_ObjectIdentity=ObjectIdentity
eltMesPhdTransceiver=_EltMesPhdTransceiver_ObjectIdentity((1,3,6,1,4,1,35265,1,23,53,1))
_EltPhdTransceiverInfoTable_Object=MibTable
eltPhdTransceiverInfoTable=_EltPhdTransceiverInfoTable_Object((1,3,6,1,4,1,35265,1,23,53,1,1))
if mibBuilder.loadTexts:eltPhdTransceiverInfoTable.setStatus(_A)
_EltPhdTransceiverInfoEntry_Object=MibTableRow
eltPhdTransceiverInfoEntry=_EltPhdTransceiverInfoEntry_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1))
eltPhdTransceiverInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:eltPhdTransceiverInfoEntry.setStatus(_A)
class _EltPhdTransceiverInfoConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,32,33,34,35,127,255)));namedValues=NamedValues(*((_D,0),('sc',1),('fibre-ch-st1',2),('fibre-ch-st2',3),('bnc-tnc',4),('fibre-ch-coaxial-headers',5),('fibrejack',6),('lc',7),('mt-rj',8),('mu',9),('sg',10),('optical-pigtail',11),('mpo-parallel-optic',12),('hssdc-ii',32),('copper-pigtail',33),('rj45',34),('no-separable-connector',35),('unallocated',127),(_I,255)))
_EltPhdTransceiverInfoConnectorType_Type.__name__=_C
_EltPhdTransceiverInfoConnectorType_Object=MibTableColumn
eltPhdTransceiverInfoConnectorType=_EltPhdTransceiverInfoConnectorType_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,1),_EltPhdTransceiverInfoConnectorType_Type())
eltPhdTransceiverInfoConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoConnectorType.setStatus(_A)
class _EltPhdTransceiverInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,127,255)));namedValues=NamedValues(*((_D,0),('gbic',1),('sff',2),('sfp-sfpplus',3),('xbi-300-pin',4),('xenpak',5),('xfp',6),('xff',7),('xfp-e',8),('xpak',9),('x2',10),('dwdm-sfp',11),('qsfp',12),('qsfpplus',13),('reserved',127),(_I,255)))
_EltPhdTransceiverInfoType_Type.__name__=_C
_EltPhdTransceiverInfoType_Object=MibTableColumn
eltPhdTransceiverInfoType=_EltPhdTransceiverInfoType_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,2),_EltPhdTransceiverInfoType_Type())
eltPhdTransceiverInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoType.setStatus(_A)
_EltPhdTransceiverInfoComplianceCode_Type=OctetString
_EltPhdTransceiverInfoComplianceCode_Object=MibTableColumn
eltPhdTransceiverInfoComplianceCode=_EltPhdTransceiverInfoComplianceCode_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,3),_EltPhdTransceiverInfoComplianceCode_Type())
eltPhdTransceiverInfoComplianceCode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoComplianceCode.setStatus(_A)
_EltPhdTransceiverInfoWaveLength_Type=Integer32
_EltPhdTransceiverInfoWaveLength_Object=MibTableColumn
eltPhdTransceiverInfoWaveLength=_EltPhdTransceiverInfoWaveLength_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,4),_EltPhdTransceiverInfoWaveLength_Type())
eltPhdTransceiverInfoWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoWaveLength.setStatus(_A)
_EltPhdTransceiverInfoVendorName_Type=OctetString
_EltPhdTransceiverInfoVendorName_Object=MibTableColumn
eltPhdTransceiverInfoVendorName=_EltPhdTransceiverInfoVendorName_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,5),_EltPhdTransceiverInfoVendorName_Type())
eltPhdTransceiverInfoVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoVendorName.setStatus(_A)
_EltPhdTransceiverInfoSerialNumber_Type=OctetString
_EltPhdTransceiverInfoSerialNumber_Object=MibTableColumn
eltPhdTransceiverInfoSerialNumber=_EltPhdTransceiverInfoSerialNumber_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,6),_EltPhdTransceiverInfoSerialNumber_Type())
eltPhdTransceiverInfoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoSerialNumber.setStatus(_A)
class _EltPhdTransceiverInfoFiberDiameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,65535)));namedValues=NamedValues(*(('fiber9',1),('fiber50',2),('fiber625',3),('copper',4),(_D,65535)))
_EltPhdTransceiverInfoFiberDiameterType_Type.__name__=_C
_EltPhdTransceiverInfoFiberDiameterType_Object=MibTableColumn
eltPhdTransceiverInfoFiberDiameterType=_EltPhdTransceiverInfoFiberDiameterType_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,7),_EltPhdTransceiverInfoFiberDiameterType_Type())
eltPhdTransceiverInfoFiberDiameterType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoFiberDiameterType.setStatus(_A)
_EltPhdTransceiverInfoTransferDistance_Type=Integer32
_EltPhdTransceiverInfoTransferDistance_Object=MibTableColumn
eltPhdTransceiverInfoTransferDistance=_EltPhdTransceiverInfoTransferDistance_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,8),_EltPhdTransceiverInfoTransferDistance_Type())
eltPhdTransceiverInfoTransferDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoTransferDistance.setStatus(_A)
_EltPhdTransceiverInfoDiagnostic_Type=TruthValue
_EltPhdTransceiverInfoDiagnostic_Object=MibTableColumn
eltPhdTransceiverInfoDiagnostic=_EltPhdTransceiverInfoDiagnostic_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,9),_EltPhdTransceiverInfoDiagnostic_Type())
eltPhdTransceiverInfoDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoDiagnostic.setStatus(_A)
_EltPhdTransceiverInfoPartNumber_Type=OctetString
_EltPhdTransceiverInfoPartNumber_Object=MibTableColumn
eltPhdTransceiverInfoPartNumber=_EltPhdTransceiverInfoPartNumber_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,10),_EltPhdTransceiverInfoPartNumber_Type())
eltPhdTransceiverInfoPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoPartNumber.setStatus(_A)
_EltPhdTransceiverInfoVendorRev_Type=OctetString
_EltPhdTransceiverInfoVendorRev_Object=MibTableColumn
eltPhdTransceiverInfoVendorRev=_EltPhdTransceiverInfoVendorRev_Object((1,3,6,1,4,1,35265,1,23,53,1,1,1,11),_EltPhdTransceiverInfoVendorRev_Type())
eltPhdTransceiverInfoVendorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverInfoVendorRev.setStatus(_A)
_EltPhdTransceiverThresholdTable_Object=MibTable
eltPhdTransceiverThresholdTable=_EltPhdTransceiverThresholdTable_Object((1,3,6,1,4,1,35265,1,23,53,1,2))
if mibBuilder.loadTexts:eltPhdTransceiverThresholdTable.setStatus(_A)
_EltPhdTransceiverThresholdEntry_Object=MibTableRow
eltPhdTransceiverThresholdEntry=_EltPhdTransceiverThresholdEntry_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1))
eltPhdTransceiverThresholdEntry.setIndexNames((0,_F,_G),(0,_E,_J))
if mibBuilder.loadTexts:eltPhdTransceiverThresholdEntry.setStatus(_A)
class _EltPhdTransceiverThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('temperature',0),('supply',1),('txBias',2),('txOutput',3),('rxOpticalPower',4)))
_EltPhdTransceiverThresholdType_Type.__name__=_C
_EltPhdTransceiverThresholdType_Object=MibTableColumn
eltPhdTransceiverThresholdType=_EltPhdTransceiverThresholdType_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,1),_EltPhdTransceiverThresholdType_Type())
eltPhdTransceiverThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdType.setStatus(_A)
class _EltPhdTransceiverThresholdAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('log',1),('send-trap',2)))
_EltPhdTransceiverThresholdAction_Type.__name__=_C
_EltPhdTransceiverThresholdAction_Object=MibTableColumn
eltPhdTransceiverThresholdAction=_EltPhdTransceiverThresholdAction_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,2),_EltPhdTransceiverThresholdAction_Type())
eltPhdTransceiverThresholdAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdAction.setStatus(_A)
_EltPhdTransceiverThresholdHighAlarm_Type=Integer32
_EltPhdTransceiverThresholdHighAlarm_Object=MibTableColumn
eltPhdTransceiverThresholdHighAlarm=_EltPhdTransceiverThresholdHighAlarm_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,3),_EltPhdTransceiverThresholdHighAlarm_Type())
eltPhdTransceiverThresholdHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdHighAlarm.setStatus(_A)
_EltPhdTransceiverThresholdHighWarning_Type=Integer32
_EltPhdTransceiverThresholdHighWarning_Object=MibTableColumn
eltPhdTransceiverThresholdHighWarning=_EltPhdTransceiverThresholdHighWarning_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,4),_EltPhdTransceiverThresholdHighWarning_Type())
eltPhdTransceiverThresholdHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdHighWarning.setStatus(_A)
_EltPhdTransceiverThresholdLowWarning_Type=Integer32
_EltPhdTransceiverThresholdLowWarning_Object=MibTableColumn
eltPhdTransceiverThresholdLowWarning=_EltPhdTransceiverThresholdLowWarning_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,5),_EltPhdTransceiverThresholdLowWarning_Type())
eltPhdTransceiverThresholdLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdLowWarning.setStatus(_A)
_EltPhdTransceiverThresholdLowAlarm_Type=Integer32
_EltPhdTransceiverThresholdLowAlarm_Object=MibTableColumn
eltPhdTransceiverThresholdLowAlarm=_EltPhdTransceiverThresholdLowAlarm_Object((1,3,6,1,4,1,35265,1,23,53,1,2,1,6),_EltPhdTransceiverThresholdLowAlarm_Type())
eltPhdTransceiverThresholdLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdTransceiverThresholdLowAlarm.setStatus(_A)
_EltPhdUnitGenParamTable_Object=MibTable
eltPhdUnitGenParamTable=_EltPhdUnitGenParamTable_Object((1,3,6,1,4,1,35265,1,23,53,2))
if mibBuilder.loadTexts:eltPhdUnitGenParamTable.setStatus(_A)
_EltPhdUnitGenParamEntry_Object=MibTableRow
eltPhdUnitGenParamEntry=_EltPhdUnitGenParamEntry_Object((1,3,6,1,4,1,35265,1,23,53,2,1))
if mibBuilder.loadTexts:eltPhdUnitGenParamEntry.setStatus(_A)
_EltPhdUnitGenParamCommitHash_Type=DisplayString
_EltPhdUnitGenParamCommitHash_Object=MibTableColumn
eltPhdUnitGenParamCommitHash=_EltPhdUnitGenParamCommitHash_Object((1,3,6,1,4,1,35265,1,23,53,2,1,1),_EltPhdUnitGenParamCommitHash_Type())
eltPhdUnitGenParamCommitHash.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdUnitGenParamCommitHash.setStatus(_A)
_EltPhdUnitGenParamBuildTag_Type=DisplayString
_EltPhdUnitGenParamBuildTag_Object=MibTableColumn
eltPhdUnitGenParamBuildTag=_EltPhdUnitGenParamBuildTag_Object((1,3,6,1,4,1,35265,1,23,53,2,1,2),_EltPhdUnitGenParamBuildTag_Type())
eltPhdUnitGenParamBuildTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdUnitGenParamBuildTag.setStatus(_A)
_EltPhdUnitGenParamBuildNumber_Type=DisplayString
_EltPhdUnitGenParamBuildNumber_Object=MibTableColumn
eltPhdUnitGenParamBuildNumber=_EltPhdUnitGenParamBuildNumber_Object((1,3,6,1,4,1,35265,1,23,53,2,1,3),_EltPhdUnitGenParamBuildNumber_Type())
eltPhdUnitGenParamBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPhdUnitGenParamBuildNumber.setStatus(_A)
_EltCascadeTable_Object=MibTable
eltCascadeTable=_EltCascadeTable_Object((1,3,6,1,4,1,35265,1,23,53,3))
if mibBuilder.loadTexts:eltCascadeTable.setStatus(_A)
_EltCascadeEntry_Object=MibTableRow
eltCascadeEntry=_EltCascadeEntry_Object((1,3,6,1,4,1,35265,1,23,53,3,1))
if mibBuilder.loadTexts:eltCascadeEntry.setStatus(_A)
_EltCascadeLastChange_Type=TimeTicks
_EltCascadeLastChange_Object=MibTableColumn
eltCascadeLastChange=_EltCascadeLastChange_Object((1,3,6,1,4,1,35265,1,23,53,3,1,1),_EltCascadeLastChange_Type())
eltCascadeLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeLastChange.setStatus(_A)
class _EltCascadeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_EltCascadeOperStatus_Type.__name__=_C
_EltCascadeOperStatus_Object=MibTableColumn
eltCascadeOperStatus=_EltCascadeOperStatus_Object((1,3,6,1,4,1,35265,1,23,53,3,1,2),_EltCascadeOperStatus_Type())
eltCascadeOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeOperStatus.setStatus(_A)
class _EltCascadeDuplexOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('half',1),('full',2),(_K,3),(_D,4)))
_EltCascadeDuplexOperMode_Type.__name__=_C
_EltCascadeDuplexOperMode_Object=MibTableColumn
eltCascadeDuplexOperMode=_EltCascadeDuplexOperMode_Object((1,3,6,1,4,1,35265,1,23,53,3,1,3),_EltCascadeDuplexOperMode_Type())
eltCascadeDuplexOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeDuplexOperMode.setStatus(_A)
class _EltCascadeOperSpeedDuplexAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_K,3),(_D,4)))
_EltCascadeOperSpeedDuplexAutoNegotiation_Type.__name__=_C
_EltCascadeOperSpeedDuplexAutoNegotiation_Object=MibTableColumn
eltCascadeOperSpeedDuplexAutoNegotiation=_EltCascadeOperSpeedDuplexAutoNegotiation_Object((1,3,6,1,4,1,35265,1,23,53,3,1,4),_EltCascadeOperSpeedDuplexAutoNegotiation_Type())
eltCascadeOperSpeedDuplexAutoNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeOperSpeedDuplexAutoNegotiation.setStatus(_A)
class _EltCascadeOperMdix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('cross',2),('auto',3),(_D,4)))
_EltCascadeOperMdix_Type.__name__=_C
_EltCascadeOperMdix_Object=MibTableColumn
eltCascadeOperMdix=_EltCascadeOperMdix_Object((1,3,6,1,4,1,35265,1,23,53,3,1,5),_EltCascadeOperMdix_Type())
eltCascadeOperMdix.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeOperMdix.setStatus(_A)
class _EltCascadeTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('regular',1),('fiberOptics',2),('comboRegular',3),('comboFiberOptics',4)))
_EltCascadeTransceiverType_Type.__name__=_C
_EltCascadeTransceiverType_Object=MibTableColumn
eltCascadeTransceiverType=_EltCascadeTransceiverType_Object((1,3,6,1,4,1,35265,1,23,53,3,1,6),_EltCascadeTransceiverType_Type())
eltCascadeTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeTransceiverType.setStatus(_A)
class _EltCascadeIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('eth10M',1),('eth100M',2),('eth1000M',3),('eth10G',4),('eth20G',5),('eth40G',6),('eth100G',7),(_D,8)))
_EltCascadeIfType_Type.__name__=_C
_EltCascadeIfType_Object=MibTableColumn
eltCascadeIfType=_EltCascadeIfType_Object((1,3,6,1,4,1,35265,1,23,53,3,1,7),_EltCascadeIfType_Type())
eltCascadeIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCascadeIfType.setStatus(_A)
_EltMesPhdNsf_ObjectIdentity=ObjectIdentity
eltMesPhdNsf=_EltMesPhdNsf_ObjectIdentity((1,3,6,1,4,1,35265,1,23,53,4))
class _EltPhdNsfEnable_Type(TruthValue):defaultValue=2
_EltPhdNsfEnable_Type.__name__=_H
_EltPhdNsfEnable_Object=MibScalar
eltPhdNsfEnable=_EltPhdNsfEnable_Object((1,3,6,1,4,1,35265,1,23,53,4,1),_EltPhdNsfEnable_Type())
eltPhdNsfEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:eltPhdNsfEnable.setStatus(_A)
class _EltPhdNsfTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_EltPhdNsfTime_Type.__name__=_C
_EltPhdNsfTime_Object=MibScalar
eltPhdNsfTime=_EltPhdNsfTime_Object((1,3,6,1,4,1,35265,1,23,53,4,2),_EltPhdNsfTime_Type())
eltPhdNsfTime.setMaxAccess(_L)
if mibBuilder.loadTexts:eltPhdNsfTime.setStatus(_A)
rlPhdUnitGenParamEntry.registerAugmentions((_E,_M))
eltPhdUnitGenParamEntry.setIndexNames(*rlPhdUnitGenParamEntry.getIndexNames())
rlCascadeEntry.registerAugmentions((_E,_N))
eltCascadeEntry.setIndexNames(*rlCascadeEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'eltMesPhysicalDescription':eltMesPhysicalDescription,'eltMesPhdTransceiver':eltMesPhdTransceiver,'eltPhdTransceiverInfoTable':eltPhdTransceiverInfoTable,'eltPhdTransceiverInfoEntry':eltPhdTransceiverInfoEntry,'eltPhdTransceiverInfoConnectorType':eltPhdTransceiverInfoConnectorType,'eltPhdTransceiverInfoType':eltPhdTransceiverInfoType,'eltPhdTransceiverInfoComplianceCode':eltPhdTransceiverInfoComplianceCode,'eltPhdTransceiverInfoWaveLength':eltPhdTransceiverInfoWaveLength,'eltPhdTransceiverInfoVendorName':eltPhdTransceiverInfoVendorName,'eltPhdTransceiverInfoSerialNumber':eltPhdTransceiverInfoSerialNumber,'eltPhdTransceiverInfoFiberDiameterType':eltPhdTransceiverInfoFiberDiameterType,'eltPhdTransceiverInfoTransferDistance':eltPhdTransceiverInfoTransferDistance,'eltPhdTransceiverInfoDiagnostic':eltPhdTransceiverInfoDiagnostic,'eltPhdTransceiverInfoPartNumber':eltPhdTransceiverInfoPartNumber,'eltPhdTransceiverInfoVendorRev':eltPhdTransceiverInfoVendorRev,'eltPhdTransceiverThresholdTable':eltPhdTransceiverThresholdTable,'eltPhdTransceiverThresholdEntry':eltPhdTransceiverThresholdEntry,_J:eltPhdTransceiverThresholdType,'eltPhdTransceiverThresholdAction':eltPhdTransceiverThresholdAction,'eltPhdTransceiverThresholdHighAlarm':eltPhdTransceiverThresholdHighAlarm,'eltPhdTransceiverThresholdHighWarning':eltPhdTransceiverThresholdHighWarning,'eltPhdTransceiverThresholdLowWarning':eltPhdTransceiverThresholdLowWarning,'eltPhdTransceiverThresholdLowAlarm':eltPhdTransceiverThresholdLowAlarm,'eltPhdUnitGenParamTable':eltPhdUnitGenParamTable,_M:eltPhdUnitGenParamEntry,'eltPhdUnitGenParamCommitHash':eltPhdUnitGenParamCommitHash,'eltPhdUnitGenParamBuildTag':eltPhdUnitGenParamBuildTag,'eltPhdUnitGenParamBuildNumber':eltPhdUnitGenParamBuildNumber,'eltCascadeTable':eltCascadeTable,_N:eltCascadeEntry,'eltCascadeLastChange':eltCascadeLastChange,'eltCascadeOperStatus':eltCascadeOperStatus,'eltCascadeDuplexOperMode':eltCascadeDuplexOperMode,'eltCascadeOperSpeedDuplexAutoNegotiation':eltCascadeOperSpeedDuplexAutoNegotiation,'eltCascadeOperMdix':eltCascadeOperMdix,'eltCascadeTransceiverType':eltCascadeTransceiverType,'eltCascadeIfType':eltCascadeIfType,'eltMesPhdNsf':eltMesPhdNsf,'eltPhdNsfEnable':eltPhdNsfEnable,'eltPhdNsfTime':eltPhdNsfTime})