_AX='tnOtsigProfileGroup'
_AW='tnOtsigGroup'
_AV='tnOtuApaGroup'
_AU='tnOtukGroup'
_AT='tnOtsigProfileExternalCardType'
_AS='tnOtsigProfileExternalCategory'
_AR='tnOtsigProfileCardType'
_AQ='tnOtsigProfile'
_AP='tnOtsigMgracd'
_AO='tnOtsigCapacity'
_AN='tnOtsigIOPMode'
_AM='tnOtsigPayloadRate'
_AL='tnOtsigDescription'
_AK='tnOtsigCdPreComp'
_AJ='tnOtsigNonLinearComp'
_AI='tnOtsigFecMode'
_AH='tnOtsigTxShape'
_AG='tnOtsigPolarizationTrack'
_AF='tnOtsigPhaseEncode'
_AE='tnOtsigEncoding'
_AD='tnOtsigBaudrate'
_AC='tnOtsigTSEB'
_AB='tnOtsigDLEB'
_AA='tnOtsigLLEB'
_A9='tnOtsigOTSilist'
_A8='tnOtsigRegenResponse'
_A7='tnOtsigTransmissionMode'
_A6='tnOtsigOtuStruct'
_A5='tnOtsigCommand'
_A4='tnOtuApaFecUncorrCnt'
_A3='tnOtuApaPreFecBer'
_A2='tnOtuFacilityDescriptorCirId'
_A1='tnOtuFacilityDescriptorDesc'
_A0='tnOtuFacilityDescriptorName'
_z='tnOtuChanPoolIfIndex'
_y='tnOtuOtsigId'
_x='tnOtukType'
_w='tnOtukMgracd'
_v='tnOtuServerPort'
_u='tnOtuAlmProfName'
_t='tnOtukOsTransmitted'
_s='tnOtukOsAccepted'
_r='tnOtukDapiTransmitted'
_q='tnOtukDapiExpected'
_p='tnOtukDapiAccepted'
_o='tnOtukDegM'
_n='tnOtukDegThr'
_m='tnOtukAsymInterworking'
_l='tnOtukPostFec'
_k='tnOtukPreFec'
_j='tnOtukAINSDebounceTimeRemaining'
_i='tnOtukUsingSysAINSDebounceTime'
_h='tnOtukAINSDebounceTime'
_g='tnOtukOperationalCapability'
_f='tnOtukStateQualifier'
_e='tnOtukOperStatus'
_d='tnOtukStateAINS'
_c='tnOtukAdminStatus'
_b='tnOtukIncRes'
_a='tnOtukRate'
_Z='tnOtukFecMode'
_Y='tnOtukTtiStatus'
_X='unknown'
_W='tnOtsigIndex'
_V='not-accessible'
_U='tnOtuApaInterval'
_T='cpmgnpln'
_S='mgnpln'
_R='unassigned'
_Q='TropicOperationalCapabilityType'
_P='AluWdmTtiStatus'
_O='AluWdmPortOchOtuRate'
_N='AluWdmFecMode'
_M='Unsigned32'
_L='tnOtsigProfileId'
_K='AluWdmOdukStatus'
_J='ifIndex'
_I='IF-MIB'
_H='TruthValue'
_G='OctetString'
_F='SnmpAdminString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='TROPIC-OTUODU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
tnOtuOduMIB,tnPortModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnOtuOduMIB','tnPortModules')
AluWdmFecMode,AluWdmOdukStatus,AluWdmPortOchOtuRate,AluWdmTtiStatus,TropicOperationalCapabilityType,TropicStateQualifierType=mibBuilder.importSymbols('TROPIC-TC',_N,_K,_O,_P,_Q,'TropicStateQualifierType')
tnOtuOduMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,5))
if mibBuilder.loadTexts:tnOtuOduMibModule.setRevisions(('2021-06-18 12:00','2021-05-14 12:00','2021-02-26 12:00','2021-01-15 12:00','2020-12-11 12:00','2020-07-10 12:00','2020-05-08 12:00','2020-03-20 12:00','2020-02-21 12:00','2019-11-01 12:00','2019-10-25 12:00','2019-08-30 12:00','2019-06-07 12:00','2019-05-31 12:00','2019-04-26 12:00','2019-04-12 12:00','2019-04-05 12:00','2019-03-08 12:00','2019-02-15 12:00','2019-02-08 12:00','2019-01-11 12:00','2018-12-28 12:00','2018-02-23 12:00','2017-07-07 12:00','2017-02-24 12:00','2017-01-20 12:00','2016-11-16 12:00','2016-03-25 12:00','2016-03-02 12:00','2015-07-17 12:00','2015-05-15 12:00','2014-11-13 12:00','2014-10-31 12:00','2014-02-26 12:00','2013-04-16 12:00','2013-03-14 12:00','2012-12-05 12:00','2012-10-22 12:00','2012-09-28 12:00','2012-09-24 12:00','2012-08-22 12:00','2012-04-10 12:00','2011-07-22 12:00','2011-04-25 12:00','2011-03-30 12:00','2011-03-04 12:00','2011-02-23 12:00','2010-11-24 12:00','2010-11-22 12:00','2010-11-14 12:00'))
_TnOtuOduConf_ObjectIdentity=ObjectIdentity
tnOtuOduConf=_TnOtuOduConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,7,1))
_TnOtuOduGroups_ObjectIdentity=ObjectIdentity
tnOtuOduGroups=_TnOtuOduGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,7,1,1))
_TnOtuOduCompliances_ObjectIdentity=ObjectIdentity
tnOtuOduCompliances=_TnOtuOduCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,7,1,2))
_TnOtuOduObjs_ObjectIdentity=ObjectIdentity
tnOtuOduObjs=_TnOtuOduObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,7,2))
_TnOtuOduBasics_ObjectIdentity=ObjectIdentity
tnOtuOduBasics=_TnOtuOduBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,7,2,1))
_TnOtukTable_Object=MibTable
tnOtukTable=_TnOtukTable_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1))
if mibBuilder.loadTexts:tnOtukTable.setStatus(_A)
_TnOtukEntry_Object=MibTableRow
tnOtukEntry=_TnOtukEntry_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1))
tnOtukEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:tnOtukEntry.setStatus(_A)
class _TnOtukTtiStatus_Type(AluWdmTtiStatus):defaultValue=4
_TnOtukTtiStatus_Type.__name__=_P
_TnOtukTtiStatus_Object=MibTableColumn
tnOtukTtiStatus=_TnOtukTtiStatus_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,1),_TnOtukTtiStatus_Type())
tnOtukTtiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukTtiStatus.setStatus(_A)
class _TnOtukFecMode_Type(AluWdmFecMode):defaultValue=3
_TnOtukFecMode_Type.__name__=_N
_TnOtukFecMode_Object=MibTableColumn
tnOtukFecMode=_TnOtukFecMode_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,2),_TnOtukFecMode_Type())
tnOtukFecMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukFecMode.setStatus(_A)
class _TnOtukRate_Type(AluWdmPortOchOtuRate):defaultValue=1
_TnOtukRate_Type.__name__=_O
_TnOtukRate_Object=MibTableColumn
tnOtukRate=_TnOtukRate_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,3),_TnOtukRate_Type())
tnOtukRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukRate.setStatus(_A)
class _TnOtukIncRes_Type(OctetString):defaultValue=OctetString('')
_TnOtukIncRes_Type.__name__=_G
_TnOtukIncRes_Object=MibTableColumn
tnOtukIncRes=_TnOtukIncRes_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,4),_TnOtukIncRes_Type())
tnOtukIncRes.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukIncRes.setStatus(_A)
class _TnOtukAdminStatus_Type(AluWdmOdukStatus):defaultValue=2
_TnOtukAdminStatus_Type.__name__=_K
_TnOtukAdminStatus_Object=MibTableColumn
tnOtukAdminStatus=_TnOtukAdminStatus_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,5),_TnOtukAdminStatus_Type())
tnOtukAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukAdminStatus.setStatus(_A)
class _TnOtukStateAINS_Type(TruthValue):defaultValue=2
_TnOtukStateAINS_Type.__name__=_H
_TnOtukStateAINS_Object=MibTableColumn
tnOtukStateAINS=_TnOtukStateAINS_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,6),_TnOtukStateAINS_Type())
tnOtukStateAINS.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukStateAINS.setStatus(_A)
class _TnOtukOperStatus_Type(AluWdmOdukStatus):defaultValue=2
_TnOtukOperStatus_Type.__name__=_K
_TnOtukOperStatus_Object=MibTableColumn
tnOtukOperStatus=_TnOtukOperStatus_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,7),_TnOtukOperStatus_Type())
tnOtukOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukOperStatus.setStatus(_A)
_TnOtukStateQualifier_Type=TropicStateQualifierType
_TnOtukStateQualifier_Object=MibTableColumn
tnOtukStateQualifier=_TnOtukStateQualifier_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,8),_TnOtukStateQualifier_Type())
tnOtukStateQualifier.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukStateQualifier.setStatus(_A)
class _TnOtukOperationalCapability_Type(TropicOperationalCapabilityType):defaultValue=1
_TnOtukOperationalCapability_Type.__name__=_Q
_TnOtukOperationalCapability_Object=MibTableColumn
tnOtukOperationalCapability=_TnOtukOperationalCapability_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,9),_TnOtukOperationalCapability_Type())
tnOtukOperationalCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukOperationalCapability.setStatus(_A)
_TnOtukAINSDebounceTime_Type=Integer32
_TnOtukAINSDebounceTime_Object=MibTableColumn
tnOtukAINSDebounceTime=_TnOtukAINSDebounceTime_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,10),_TnOtukAINSDebounceTime_Type())
tnOtukAINSDebounceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukAINSDebounceTime.setStatus(_A)
if mibBuilder.loadTexts:tnOtukAINSDebounceTime.setUnits('Seconds')
_TnOtukUsingSysAINSDebounceTime_Type=TruthValue
_TnOtukUsingSysAINSDebounceTime_Object=MibTableColumn
tnOtukUsingSysAINSDebounceTime=_TnOtukUsingSysAINSDebounceTime_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,11),_TnOtukUsingSysAINSDebounceTime_Type())
tnOtukUsingSysAINSDebounceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukUsingSysAINSDebounceTime.setStatus(_A)
class _TnOtukAINSDebounceTimeRemaining_Type(Unsigned32):defaultValue=0
_TnOtukAINSDebounceTimeRemaining_Type.__name__=_M
_TnOtukAINSDebounceTimeRemaining_Object=MibTableColumn
tnOtukAINSDebounceTimeRemaining=_TnOtukAINSDebounceTimeRemaining_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,12),_TnOtukAINSDebounceTimeRemaining_Type())
tnOtukAINSDebounceTimeRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukAINSDebounceTimeRemaining.setStatus(_A)
_TnOtukPreFec_Type=Counter64
_TnOtukPreFec_Object=MibTableColumn
tnOtukPreFec=_TnOtukPreFec_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,14),_TnOtukPreFec_Type())
tnOtukPreFec.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukPreFec.setStatus(_A)
_TnOtukPostFec_Type=Counter64
_TnOtukPostFec_Object=MibTableColumn
tnOtukPostFec=_TnOtukPostFec_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,15),_TnOtukPostFec_Type())
tnOtukPostFec.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukPostFec.setStatus(_A)
class _TnOtukAsymInterworking_Type(TruthValue):defaultValue=2
_TnOtukAsymInterworking_Type.__name__=_H
_TnOtukAsymInterworking_Object=MibTableColumn
tnOtukAsymInterworking=_TnOtukAsymInterworking_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,17),_TnOtukAsymInterworking_Type())
tnOtukAsymInterworking.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukAsymInterworking.setStatus(_A)
_TnOtukDegThr_Type=Unsigned32
_TnOtukDegThr_Object=MibTableColumn
tnOtukDegThr=_TnOtukDegThr_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,18),_TnOtukDegThr_Type())
tnOtukDegThr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukDegThr.setStatus(_A)
_TnOtukDegM_Type=Unsigned32
_TnOtukDegM_Object=MibTableColumn
tnOtukDegM=_TnOtukDegM_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,19),_TnOtukDegM_Type())
tnOtukDegM.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukDegM.setStatus(_A)
class _TnOtukDapiAccepted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TnOtukDapiAccepted_Type.__name__=_G
_TnOtukDapiAccepted_Object=MibTableColumn
tnOtukDapiAccepted=_TnOtukDapiAccepted_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,20),_TnOtukDapiAccepted_Type())
tnOtukDapiAccepted.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukDapiAccepted.setStatus(_A)
class _TnOtukDapiExpected_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TnOtukDapiExpected_Type.__name__=_G
_TnOtukDapiExpected_Object=MibTableColumn
tnOtukDapiExpected=_TnOtukDapiExpected_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,21),_TnOtukDapiExpected_Type())
tnOtukDapiExpected.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukDapiExpected.setStatus(_A)
class _TnOtukDapiTransmitted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TnOtukDapiTransmitted_Type.__name__=_G
_TnOtukDapiTransmitted_Object=MibTableColumn
tnOtukDapiTransmitted=_TnOtukDapiTransmitted_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,22),_TnOtukDapiTransmitted_Type())
tnOtukDapiTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukDapiTransmitted.setStatus(_A)
class _TnOtukOsAccepted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TnOtukOsAccepted_Type.__name__=_G
_TnOtukOsAccepted_Object=MibTableColumn
tnOtukOsAccepted=_TnOtukOsAccepted_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,23),_TnOtukOsAccepted_Type())
tnOtukOsAccepted.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtukOsAccepted.setStatus(_A)
class _TnOtukOsTransmitted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TnOtukOsTransmitted_Type.__name__=_G
_TnOtukOsTransmitted_Object=MibTableColumn
tnOtukOsTransmitted=_TnOtukOsTransmitted_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,24),_TnOtukOsTransmitted_Type())
tnOtukOsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukOsTransmitted.setStatus(_A)
_TnOtuAlmProfName_Type=OctetString
_TnOtuAlmProfName_Object=MibTableColumn
tnOtuAlmProfName=_TnOtuAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,25),_TnOtuAlmProfName_Type())
tnOtuAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtuAlmProfName.setStatus(_A)
class _TnOtuServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,11,12,13,14,21,22,31,32,33,34,35,41,42,43,44,51,52,61,62,63,64,65,71,72,81,82)));namedValues=NamedValues(*((_R,0),('spL1Ch1',11),('spL1Ch2',12),('spL1Ch3',13),('spL1Ch4',14),('spL2Ch1',21),('spL2Ch2',22),('spL1L2Ch1',31),('spL1L2Ch2',32),('spL1L2Ch3',33),('spL1L2Ch4',34),('spL1L2Ch5',35),('spL3Ch1',41),('spL3Ch2',42),('spL3Ch3',43),('spL3Ch4',44),('spL4Ch1',51),('spL4Ch2',52),('spL3L4Ch1',61),('spL3L4Ch2',62),('spL3L4Ch3',63),('spL3L4Ch4',64),('spL3L4Ch5',65),('spL5Ch1',71),('spL5Ch2',72),('spL6Ch1',81),('spL6Ch2',82)))
_TnOtuServerPort_Type.__name__=_E
_TnOtuServerPort_Object=MibTableColumn
tnOtuServerPort=_TnOtuServerPort_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,26),_TnOtuServerPort_Type())
tnOtuServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtuServerPort.setStatus(_A)
class _TnOtukMgracd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('cp',2),(_S,3),(_T,4)))
_TnOtukMgracd_Type.__name__=_E
_TnOtukMgracd_Object=MibTableColumn
tnOtukMgracd=_TnOtukMgracd_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,27),_TnOtukMgracd_Type())
tnOtukMgracd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukMgracd.setStatus(_A)
class _TnOtukType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('proprietary',2)))
_TnOtukType_Type.__name__=_E
_TnOtukType_Object=MibTableColumn
tnOtukType=_TnOtukType_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,28),_TnOtukType_Type())
tnOtukType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtukType.setStatus(_A)
class _TnOtuOtsigId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnOtuOtsigId_Type.__name__=_E
_TnOtuOtsigId_Object=MibTableColumn
tnOtuOtsigId=_TnOtuOtsigId_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,29),_TnOtuOtsigId_Type())
tnOtuOtsigId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtuOtsigId.setStatus(_A)
class _TnOtuChanPoolIfIndex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TnOtuChanPoolIfIndex_Type.__name__=_G
_TnOtuChanPoolIfIndex_Object=MibTableColumn
tnOtuChanPoolIfIndex=_TnOtuChanPoolIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,30),_TnOtuChanPoolIfIndex_Type())
tnOtuChanPoolIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtuChanPoolIfIndex.setStatus(_A)
class _TnOtuFacilityDescriptorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_TnOtuFacilityDescriptorName_Type.__name__=_F
_TnOtuFacilityDescriptorName_Object=MibTableColumn
tnOtuFacilityDescriptorName=_TnOtuFacilityDescriptorName_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,31),_TnOtuFacilityDescriptorName_Type())
tnOtuFacilityDescriptorName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtuFacilityDescriptorName.setStatus(_A)
class _TnOtuFacilityDescriptorDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnOtuFacilityDescriptorDesc_Type.__name__=_F
_TnOtuFacilityDescriptorDesc_Object=MibTableColumn
tnOtuFacilityDescriptorDesc=_TnOtuFacilityDescriptorDesc_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,32),_TnOtuFacilityDescriptorDesc_Type())
tnOtuFacilityDescriptorDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtuFacilityDescriptorDesc.setStatus(_A)
class _TnOtuFacilityDescriptorCirId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_TnOtuFacilityDescriptorCirId_Type.__name__=_F
_TnOtuFacilityDescriptorCirId_Object=MibTableColumn
tnOtuFacilityDescriptorCirId=_TnOtuFacilityDescriptorCirId_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,1,1,33),_TnOtuFacilityDescriptorCirId_Type())
tnOtuFacilityDescriptorCirId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtuFacilityDescriptorCirId.setStatus(_A)
_TnOtuApaTable_Object=MibTable
tnOtuApaTable=_TnOtuApaTable_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,11))
if mibBuilder.loadTexts:tnOtuApaTable.setStatus(_A)
_TnOtuApaEntry_Object=MibTableRow
tnOtuApaEntry=_TnOtuApaEntry_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,11,1))
tnOtuApaEntry.setIndexNames((0,_I,_J),(0,_B,_U))
if mibBuilder.loadTexts:tnOtuApaEntry.setStatus(_A)
class _TnOtuApaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TnOtuApaInterval_Type.__name__=_E
_TnOtuApaInterval_Object=MibTableColumn
tnOtuApaInterval=_TnOtuApaInterval_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,11,1,1),_TnOtuApaInterval_Type())
tnOtuApaInterval.setMaxAccess(_V)
if mibBuilder.loadTexts:tnOtuApaInterval.setStatus(_A)
_TnOtuApaPreFecBer_Type=Counter64
_TnOtuApaPreFecBer_Object=MibTableColumn
tnOtuApaPreFecBer=_TnOtuApaPreFecBer_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,11,1,2),_TnOtuApaPreFecBer_Type())
tnOtuApaPreFecBer.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtuApaPreFecBer.setStatus(_A)
_TnOtuApaFecUncorrCnt_Type=Counter64
_TnOtuApaFecUncorrCnt_Object=MibTableColumn
tnOtuApaFecUncorrCnt=_TnOtuApaFecUncorrCnt_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,11,1,3),_TnOtuApaFecUncorrCnt_Type())
tnOtuApaFecUncorrCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtuApaFecUncorrCnt.setStatus(_A)
_TnOtsigTable_Object=MibTable
tnOtsigTable=_TnOtsigTable_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12))
if mibBuilder.loadTexts:tnOtsigTable.setStatus(_A)
_TnOtsigEntry_Object=MibTableRow
tnOtsigEntry=_TnOtsigEntry_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1))
tnOtsigEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:tnOtsigEntry.setStatus(_A)
_TnOtsigIndex_Type=Integer32
_TnOtsigIndex_Object=MibTableColumn
tnOtsigIndex=_TnOtsigIndex_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,1),_TnOtsigIndex_Type())
tnOtsigIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:tnOtsigIndex.setStatus(_A)
class _TnOtsigCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noCmd',1),('create',2),('delete',3),('update',4)))
_TnOtsigCommand_Type.__name__=_E
_TnOtsigCommand_Object=MibTableColumn
tnOtsigCommand=_TnOtsigCommand_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,2),_TnOtsigCommand_Type())
tnOtsigCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigCommand.setStatus(_A)
class _TnOtsigOtuStruct_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,192))
_TnOtsigOtuStruct_Type.__name__=_F
_TnOtsigOtuStruct_Object=MibTableColumn
tnOtsigOtuStruct=_TnOtsigOtuStruct_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,3),_TnOtsigOtuStruct_Type())
tnOtsigOtuStruct.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigOtuStruct.setStatus(_A)
class _TnOtsigTransmissionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('addDrop',1),('dropOnly',2),('addOnly',3),('thru',4),('dropContinue',5),('crossRegen',6),('regenGcc0LoopThrough',7)))
_TnOtsigTransmissionMode_Type.__name__=_E
_TnOtsigTransmissionMode_Object=MibTableColumn
tnOtsigTransmissionMode=_TnOtsigTransmissionMode_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,4),_TnOtsigTransmissionMode_Type())
tnOtsigTransmissionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigTransmissionMode.setStatus(_A)
class _TnOtsigRegenResponse_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('laserOn',1),('laserOff',2)))
_TnOtsigRegenResponse_Type.__name__=_E
_TnOtsigRegenResponse_Object=MibTableColumn
tnOtsigRegenResponse=_TnOtsigRegenResponse_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,5),_TnOtsigRegenResponse_Type())
tnOtsigRegenResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigRegenResponse.setStatus(_A)
class _TnOtsigOTSilist_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TnOtsigOTSilist_Type.__name__=_F
_TnOtsigOTSilist_Object=MibTableColumn
tnOtsigOTSilist=_TnOtsigOTSilist_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,6),_TnOtsigOTSilist_Type())
tnOtsigOTSilist.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigOTSilist.setStatus(_A)
class _TnOtsigLLEB_Type(TruthValue):defaultValue=2
_TnOtsigLLEB_Type.__name__=_H
_TnOtsigLLEB_Object=MibTableColumn
tnOtsigLLEB=_TnOtsigLLEB_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,7),_TnOtsigLLEB_Type())
tnOtsigLLEB.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigLLEB.setStatus(_A)
class _TnOtsigDLEB_Type(TruthValue):defaultValue=2
_TnOtsigDLEB_Type.__name__=_H
_TnOtsigDLEB_Object=MibTableColumn
tnOtsigDLEB=_TnOtsigDLEB_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,8),_TnOtsigDLEB_Type())
tnOtsigDLEB.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigDLEB.setStatus(_A)
class _TnOtsigTSEB_Type(TruthValue):defaultValue=2
_TnOtsigTSEB_Type.__name__=_H
_TnOtsigTSEB_Object=MibTableColumn
tnOtsigTSEB=_TnOtsigTSEB_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,9),_TnOtsigTSEB_Type())
tnOtsigTSEB.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigTSEB.setStatus(_A)
_TnOtsigBaudrate_Type=Integer32
_TnOtsigBaudrate_Object=MibTableColumn
tnOtsigBaudrate=_TnOtsigBaudrate_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,10),_TnOtsigBaudrate_Type())
tnOtsigBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigBaudrate.setStatus(_A)
class _TnOtsigEncoding_Type(Integer32):defaultValue=9996;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,9996,9997,9998,9999)));namedValues=NamedValues(*(('nrz',0),('pdpsk',1),('dpsk',2),('bpsk',3),('qpsk',4),('qpskEnhOsnr',5),('nrzCFP1',6),('icohpmqpsk',7),('duobinary',8),('qpskhperf2',9),('qam16',10),('qam8',11),('spqpsk',12),('qam64',13),('cohpm16qam250G',14),('cohpmsqam16',15),('cohpmsqam64',16),('qam32',17),('optimization',9996),(_R,9997),('alien',9998),(_X,9999)))
_TnOtsigEncoding_Type.__name__=_E
_TnOtsigEncoding_Object=MibTableColumn
tnOtsigEncoding=_TnOtsigEncoding_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,11),_TnOtsigEncoding_Type())
tnOtsigEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigEncoding.setStatus(_A)
class _TnOtsigPhaseEncode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absolute',1),('differential',2)))
_TnOtsigPhaseEncode_Type.__name__=_E
_TnOtsigPhaseEncode_Object=MibTableColumn
tnOtsigPhaseEncode=_TnOtsigPhaseEncode_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,12),_TnOtsigPhaseEncode_Type())
tnOtsigPhaseEncode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigPhaseEncode.setStatus(_A)
class _TnOtsigPolarizationTrack_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fast',2),('devDefault',3)))
_TnOtsigPolarizationTrack_Type.__name__=_E
_TnOtsigPolarizationTrack_Object=MibTableColumn
tnOtsigPolarizationTrack=_TnOtsigPolarizationTrack_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,13),_TnOtsigPolarizationTrack_Type())
tnOtsigPolarizationTrack.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigPolarizationTrack.setStatus(_A)
class _TnOtsigTxShape_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('single',1),('super',2),('alien',3),('superRRC01',4)))
_TnOtsigTxShape_Type.__name__=_E
_TnOtsigTxShape_Object=MibTableColumn
tnOtsigTxShape=_TnOtsigTxShape_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,14),_TnOtsigTxShape_Type())
tnOtsigTxShape.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigTxShape.setStatus(_A)
class _TnOtsigFecMode_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('noFec',1),('g709Fec',2),('enhancedFec',3),('uFec',4),('enhancedFec2',5),('aFec',6),('eSDFec',10),('hpFec',11),('usdFec',12),('bjFec',13),('scFec',14),('sdFecAcc',15),('eSDFecG2',16),('eSDFecExt',17),('ePuncturedSDFecG2',18),('sdFecCE',19),('sdFecV',20)))
_TnOtsigFecMode_Type.__name__=_E
_TnOtsigFecMode_Object=MibTableColumn
tnOtsigFecMode=_TnOtsigFecMode_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,15),_TnOtsigFecMode_Type())
tnOtsigFecMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigFecMode.setStatus(_A)
class _TnOtsigNonLinearComp_Type(TruthValue):defaultValue=2
_TnOtsigNonLinearComp_Type.__name__=_H
_TnOtsigNonLinearComp_Object=MibTableColumn
tnOtsigNonLinearComp=_TnOtsigNonLinearComp_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,16),_TnOtsigNonLinearComp_Type())
tnOtsigNonLinearComp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigNonLinearComp.setStatus(_A)
class _TnOtsigCdPreComp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10000,10000))
_TnOtsigCdPreComp_Type.__name__=_E
_TnOtsigCdPreComp_Object=MibTableColumn
tnOtsigCdPreComp=_TnOtsigCdPreComp_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,17),_TnOtsigCdPreComp_Type())
tnOtsigCdPreComp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigCdPreComp.setStatus(_A)
class _TnOtsigDescription_Type(SnmpAdminString):defaultValue=OctetString('')
_TnOtsigDescription_Type.__name__=_F
_TnOtsigDescription_Object=MibTableColumn
tnOtsigDescription=_TnOtsigDescription_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,18),_TnOtsigDescription_Type())
tnOtsigDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigDescription.setStatus(_A)
class _TnOtsigPayloadRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_TnOtsigPayloadRate_Type.__name__=_E
_TnOtsigPayloadRate_Object=MibTableColumn
tnOtsigPayloadRate=_TnOtsigPayloadRate_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,19),_TnOtsigPayloadRate_Type())
tnOtsigPayloadRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigPayloadRate.setStatus(_A)
class _TnOtsigIOPMode_Type(Integer32):defaultValue=9999;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,9999)));namedValues=NamedValues(*(('flex',1),('legacy',2),('otucn',3),('otutcn',4),('otu4',5),(_X,9999)))
_TnOtsigIOPMode_Type.__name__=_E
_TnOtsigIOPMode_Object=MibTableColumn
tnOtsigIOPMode=_TnOtsigIOPMode_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,20),_TnOtsigIOPMode_Type())
tnOtsigIOPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigIOPMode.setStatus(_A)
class _TnOtsigCapacity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_TnOtsigCapacity_Type.__name__=_E
_TnOtsigCapacity_Object=MibTableColumn
tnOtsigCapacity=_TnOtsigCapacity_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,21),_TnOtsigCapacity_Type())
tnOtsigCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigCapacity.setStatus(_A)
class _TnOtsigProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TnOtsigProfileId_Type.__name__=_E
_TnOtsigProfileId_Object=MibTableColumn
tnOtsigProfileId=_TnOtsigProfileId_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,22),_TnOtsigProfileId_Type())
tnOtsigProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigProfileId.setStatus(_A)
class _TnOtsigMgracd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('cp',2),(_S,3),(_T,4)))
_TnOtsigMgracd_Type.__name__=_E
_TnOtsigMgracd_Object=MibTableColumn
tnOtsigMgracd=_TnOtsigMgracd_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,12,1,23),_TnOtsigMgracd_Type())
tnOtsigMgracd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOtsigMgracd.setStatus(_A)
_TnOtsigProfileTable_Object=MibTable
tnOtsigProfileTable=_TnOtsigProfileTable_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13))
if mibBuilder.loadTexts:tnOtsigProfileTable.setStatus(_A)
_TnOtsigProfileEntry_Object=MibTableRow
tnOtsigProfileEntry=_TnOtsigProfileEntry_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13,1))
tnOtsigProfileEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:tnOtsigProfileEntry.setStatus(_A)
class _TnOtsigProfile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TnOtsigProfile_Type.__name__=_F
_TnOtsigProfile_Object=MibTableColumn
tnOtsigProfile=_TnOtsigProfile_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13,1,1),_TnOtsigProfile_Type())
tnOtsigProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigProfile.setStatus(_A)
class _TnOtsigProfileCardType_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TnOtsigProfileCardType_Type.__name__=_F
_TnOtsigProfileCardType_Object=MibTableColumn
tnOtsigProfileCardType=_TnOtsigProfileCardType_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13,1,2),_TnOtsigProfileCardType_Type())
tnOtsigProfileCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigProfileCardType.setStatus(_A)
_TnOtsigProfileExternalCategory_Type=TruthValue
_TnOtsigProfileExternalCategory_Object=MibTableColumn
tnOtsigProfileExternalCategory=_TnOtsigProfileExternalCategory_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13,1,3),_TnOtsigProfileExternalCategory_Type())
tnOtsigProfileExternalCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigProfileExternalCategory.setStatus(_A)
class _TnOtsigProfileExternalCardType_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TnOtsigProfileExternalCardType_Type.__name__=_F
_TnOtsigProfileExternalCardType_Object=MibTableColumn
tnOtsigProfileExternalCardType=_TnOtsigProfileExternalCardType_Object((1,3,6,1,4,1,7483,2,2,4,7,2,1,13,1,4),_TnOtsigProfileExternalCardType_Type())
tnOtsigProfileExternalCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnOtsigProfileExternalCardType.setStatus(_A)
tnOtukGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,7,1,1,1))
tnOtukGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:tnOtukGroup.setStatus(_A)
tnOtuApaGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,7,1,1,11))
tnOtuApaGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:tnOtuApaGroup.setStatus(_A)
tnOtsigGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,7,1,1,12))
tnOtsigGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_L),(_B,_AP)))
if mibBuilder.loadTexts:tnOtsigGroup.setStatus(_A)
tnOtsigProfileGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,7,1,1,13))
tnOtsigProfileGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:tnOtsigProfileGroup.setStatus(_A)
tnOdukCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,7,1,2,1))
tnOdukCompliance.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:tnOdukCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnOtuOduMibModule':tnOtuOduMibModule,'tnOtuOduConf':tnOtuOduConf,'tnOtuOduGroups':tnOtuOduGroups,_AU:tnOtukGroup,_AV:tnOtuApaGroup,_AW:tnOtsigGroup,_AX:tnOtsigProfileGroup,'tnOtuOduCompliances':tnOtuOduCompliances,'tnOdukCompliance':tnOdukCompliance,'tnOtuOduObjs':tnOtuOduObjs,'tnOtuOduBasics':tnOtuOduBasics,'tnOtukTable':tnOtukTable,'tnOtukEntry':tnOtukEntry,_Y:tnOtukTtiStatus,_Z:tnOtukFecMode,_a:tnOtukRate,_b:tnOtukIncRes,_c:tnOtukAdminStatus,_d:tnOtukStateAINS,_e:tnOtukOperStatus,_f:tnOtukStateQualifier,_g:tnOtukOperationalCapability,_h:tnOtukAINSDebounceTime,_i:tnOtukUsingSysAINSDebounceTime,_j:tnOtukAINSDebounceTimeRemaining,_k:tnOtukPreFec,_l:tnOtukPostFec,_m:tnOtukAsymInterworking,_n:tnOtukDegThr,_o:tnOtukDegM,_p:tnOtukDapiAccepted,_q:tnOtukDapiExpected,_r:tnOtukDapiTransmitted,_s:tnOtukOsAccepted,_t:tnOtukOsTransmitted,_u:tnOtuAlmProfName,_v:tnOtuServerPort,_w:tnOtukMgracd,_x:tnOtukType,_y:tnOtuOtsigId,_z:tnOtuChanPoolIfIndex,_A0:tnOtuFacilityDescriptorName,_A1:tnOtuFacilityDescriptorDesc,_A2:tnOtuFacilityDescriptorCirId,'tnOtuApaTable':tnOtuApaTable,'tnOtuApaEntry':tnOtuApaEntry,_U:tnOtuApaInterval,_A3:tnOtuApaPreFecBer,_A4:tnOtuApaFecUncorrCnt,'tnOtsigTable':tnOtsigTable,'tnOtsigEntry':tnOtsigEntry,_W:tnOtsigIndex,_A5:tnOtsigCommand,_A6:tnOtsigOtuStruct,_A7:tnOtsigTransmissionMode,_A8:tnOtsigRegenResponse,_A9:tnOtsigOTSilist,_AA:tnOtsigLLEB,_AB:tnOtsigDLEB,_AC:tnOtsigTSEB,_AD:tnOtsigBaudrate,_AE:tnOtsigEncoding,_AF:tnOtsigPhaseEncode,_AG:tnOtsigPolarizationTrack,_AH:tnOtsigTxShape,_AI:tnOtsigFecMode,_AJ:tnOtsigNonLinearComp,_AK:tnOtsigCdPreComp,_AL:tnOtsigDescription,_AM:tnOtsigPayloadRate,_AN:tnOtsigIOPMode,_AO:tnOtsigCapacity,_L:tnOtsigProfileId,_AP:tnOtsigMgracd,'tnOtsigProfileTable':tnOtsigProfileTable,'tnOtsigProfileEntry':tnOtsigProfileEntry,_AQ:tnOtsigProfile,_AR:tnOtsigProfileCardType,_AS:tnOtsigProfileExternalCategory,_AT:tnOtsigProfileExternalCardType})