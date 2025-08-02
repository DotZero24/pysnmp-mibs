_m='cadIfDsOfdmChlDataEntry'
_l='cadDsOfdmProfExceptionLowFreq'
_k='cadDsOfdmProfExceptionProfId'
_j='cadDsOfdmProfExceptionIfIndex'
_i='cadDsOfdmProfStatProfId'
_h='cadDsOfdmProfStatIfIndex'
_g='cadDsOfdmProfileId'
_f='cadDsOfdmProfileIfIndex'
_e='samples'
_d='cadIfDsOfdmChlIfIndex'
_c='cadIfDsOfdmPowerFrequency'
_b='cadIfDsOfdmPowerIfIndex'
_a='Microseconds'
_Z='cadIfDownChannelIfIndex'
_Y='qam16384'
_X='qam8192'
_W='qam4096'
_V='qam2048'
_U='qam1024'
_T='qam512'
_S='qam128'
_R='other'
_Q='unknown'
_P='qam256'
_O='qam64'
_N='Unsigned32'
_M='CerOfdmModType'
_L='milliseconds'
_K='read-create'
_J='TenthdBmV'
_I='TruthValue'
_H='not-accessible'
_G='percent'
_F='CADANT-CMTS-DOWNCHANNEL-MIB'
_E='hertz'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadSpectrum,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSpectrum')
CardId,=mibBuilder.importSymbols('CADANT-TC','CardId')
TenthdBmV,=mibBuilder.importSymbols('DOCS-IF-MIB',_J)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval',_I)
cadDownchannelMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,15,2))
if mibBuilder.loadTexts:cadDownchannelMib.setRevisions(('2015-10-27 00:00','2015-10-07 00:00','2015-09-30 00:00','2015-09-08 00:00','2015-08-19 00:00','2015-08-12 00:00','2015-06-23 00:00','2015-05-01 00:00','2015-04-27 00:00','2015-03-04 00:00','2015-02-18 00:00','2015-02-17 00:00','2015-02-13 00:00','2015-02-06 00:00','2015-01-16 00:00','2014-11-26 00:00','2014-11-17 00:00','2014-05-20 00:00','2014-04-03 00:00','2014-01-16 00:00','2013-10-13 00:00','2013-03-15 00:00','2013-02-26 00:00','2013-01-14 00:00','2012-10-17 00:00','2012-10-15 00:00','2011-09-27 00:00','2011-08-30 00:00','2010-06-10 00:00','2010-05-03 00:00','2010-04-01 00:00','2009-12-16 00:00','2008-04-03 00:00','2007-10-09 00:00','2007-09-28 00:00','2007-02-07 00:00','2007-01-22 00:00','2006-11-01 00:00','2006-08-30 00:00','2006-08-28 00:00','2006-02-24 00:00','2005-06-21 00:00','2004-12-03 00:00','2004-03-04 00:00','2003-07-03 00:00','2002-12-03 00:00'))
class OfdmProfileId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3),ValueRangeConstraint(256,256))
class CerOfdmModType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,4,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('qam0',0),('qpsk',2),('qam16',4),(_O,6),(_S,7),(_P,8),(_T,9),(_U,10),(_V,11),(_W,12),(_X,13),(_Y,14)))
class CerOfdmModBitsType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('qam32768',0),(_Y,1),(_X,2),(_W,3),(_V,4),(_U,5),(_T,6),(_P,7),(_S,8),(_O,9),('qam32',10),('qam16',11),('qam8',12),('qpsk',13),('bpsk',14),('zeroBitload',15)))
_CadIfDownstreamChannelTable_Object=MibTable
cadIfDownstreamChannelTable=_CadIfDownstreamChannelTable_Object((1,3,6,1,4,1,4998,1,1,15,2,1))
if mibBuilder.loadTexts:cadIfDownstreamChannelTable.setStatus(_A)
_CadIfDownstreamChannelEntry_Object=MibTableRow
cadIfDownstreamChannelEntry=_CadIfDownstreamChannelEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1))
cadIfDownstreamChannelEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:cadIfDownstreamChannelEntry.setStatus(_A)
class _CadIfDownChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CadIfDownChannelId_Type.__name__=_B
_CadIfDownChannelId_Object=MibTableColumn
cadIfDownChannelId=_CadIfDownChannelId_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,1),_CadIfDownChannelId_Type())
cadIfDownChannelId.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDownChannelId.setStatus(_A)
class _CadIfDownChannelFrequency_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CadIfDownChannelFrequency_Type.__name__=_B
_CadIfDownChannelFrequency_Object=MibTableColumn
cadIfDownChannelFrequency=_CadIfDownChannelFrequency_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,2),_CadIfDownChannelFrequency_Type())
cadIfDownChannelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelFrequency.setUnits(_E)
class _CadIfDownChannelWidth_Type(Integer32):defaultValue=6000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000))
_CadIfDownChannelWidth_Type.__name__=_B
_CadIfDownChannelWidth_Object=MibTableColumn
cadIfDownChannelWidth=_CadIfDownChannelWidth_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,3),_CadIfDownChannelWidth_Type())
cadIfDownChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelWidth.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelWidth.setUnits(_E)
class _CadIfDownChannelModulation_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),(_O,3),(_P,4)))
_CadIfDownChannelModulation_Type.__name__=_B
_CadIfDownChannelModulation_Object=MibTableColumn
cadIfDownChannelModulation=_CadIfDownChannelModulation_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,4),_CadIfDownChannelModulation_Type())
cadIfDownChannelModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelModulation.setStatus(_A)
class _CadIfDownChannelInterleave_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_Q,1),(_R,2),('taps8Increment16',3),('taps16Increment8',4),('taps32Increment4',5),('taps64Increment2',6),('taps128Increment1',7),('taps12increment17',8),('taps128increment2',9),('taps128increment3',10),('taps128increment4',11),('taps128increment5',12),('taps128increment6',13),('taps128increment7',14),('taps128increment8',15)))
_CadIfDownChannelInterleave_Type.__name__=_B
_CadIfDownChannelInterleave_Object=MibTableColumn
cadIfDownChannelInterleave=_CadIfDownChannelInterleave_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,5),_CadIfDownChannelInterleave_Type())
cadIfDownChannelInterleave.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelInterleave.setStatus(_A)
class _CadIfDownChannelPower_Type(TenthdBmV):defaultValue=380;subtypeSpec=TenthdBmV.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(250,600))
_CadIfDownChannelPower_Type.__name__=_J
_CadIfDownChannelPower_Object=MibTableColumn
cadIfDownChannelPower=_CadIfDownChannelPower_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,6),_CadIfDownChannelPower_Type())
cadIfDownChannelPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPower.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPower.setUnits('dBmV')
class _CadIfDownChannelPowerFineAdj_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,0))
_CadIfDownChannelPowerFineAdj_Type.__name__=_B
_CadIfDownChannelPowerFineAdj_Object=MibTableColumn
cadIfDownChannelPowerFineAdj=_CadIfDownChannelPowerFineAdj_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,7),_CadIfDownChannelPowerFineAdj_Type())
cadIfDownChannelPowerFineAdj.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPowerFineAdj.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPowerFineAdj.setUnits('Steps')
_CadIfCmtsCardNumber_Type=CardId
_CadIfCmtsCardNumber_Object=MibTableColumn
cadIfCmtsCardNumber=_CadIfCmtsCardNumber_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,19),_CadIfCmtsCardNumber_Type())
cadIfCmtsCardNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfCmtsCardNumber.setStatus(_A)
class _CadIfDownChannelCACL1Threshold_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CadIfDownChannelCACL1Threshold_Type.__name__=_B
_CadIfDownChannelCACL1Threshold_Object=MibTableColumn
cadIfDownChannelCACL1Threshold=_CadIfDownChannelCACL1Threshold_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,21),_CadIfDownChannelCACL1Threshold_Type())
cadIfDownChannelCACL1Threshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelCACL1Threshold.setStatus(_A)
class _CadIfDownChannelCACL2Threshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CadIfDownChannelCACL2Threshold_Type.__name__=_B
_CadIfDownChannelCACL2Threshold_Object=MibTableColumn
cadIfDownChannelCACL2Threshold=_CadIfDownChannelCACL2Threshold_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,22),_CadIfDownChannelCACL2Threshold_Type())
cadIfDownChannelCACL2Threshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelCACL2Threshold.setStatus(_A)
class _CadIfDownChannelCACL3Threshold_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CadIfDownChannelCACL3Threshold_Type.__name__=_B
_CadIfDownChannelCACL3Threshold_Object=MibTableColumn
cadIfDownChannelCACL3Threshold=_CadIfDownChannelCACL3Threshold_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,23),_CadIfDownChannelCACL3Threshold_Type())
cadIfDownChannelCACL3Threshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelCACL3Threshold.setStatus(_A)
class _CadIfDownChannelMaxRoundTripDelay_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1600))
_CadIfDownChannelMaxRoundTripDelay_Type.__name__=_B
_CadIfDownChannelMaxRoundTripDelay_Object=MibTableColumn
cadIfDownChannelMaxRoundTripDelay=_CadIfDownChannelMaxRoundTripDelay_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,24),_CadIfDownChannelMaxRoundTripDelay_Type())
cadIfDownChannelMaxRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelMaxRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelMaxRoundTripDelay.setUnits(_a)
class _CadIfDownChannelAnnex_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),('annexA',3),('annexB',4),('annexC',5)))
_CadIfDownChannelAnnex_Type.__name__=_B
_CadIfDownChannelAnnex_Object=MibTableColumn
cadIfDownChannelAnnex=_CadIfDownChannelAnnex_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,26),_CadIfDownChannelAnnex_Type())
cadIfDownChannelAnnex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelAnnex.setStatus(_A)
class _CadIfDownChannelPCNormAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDownChannelPCNormAllowedUsage_Type.__name__=_B
_CadIfDownChannelPCNormAllowedUsage_Object=MibTableColumn
cadIfDownChannelPCNormAllowedUsage=_CadIfDownChannelPCNormAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,27),_CadIfDownChannelPCNormAllowedUsage_Type())
cadIfDownChannelPCNormAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCNormAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPCNormAllowedUsage.setUnits(_G)
class _CadIfDownChannelPCNormResUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDownChannelPCNormResUsage_Type.__name__=_B
_CadIfDownChannelPCNormResUsage_Object=MibTableColumn
cadIfDownChannelPCNormResUsage=_CadIfDownChannelPCNormResUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,28),_CadIfDownChannelPCNormResUsage_Type())
cadIfDownChannelPCNormResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCNormResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPCNormResUsage.setUnits(_G)
class _CadIfDownChannelPCEmerAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDownChannelPCEmerAllowedUsage_Type.__name__=_B
_CadIfDownChannelPCEmerAllowedUsage_Object=MibTableColumn
cadIfDownChannelPCEmerAllowedUsage=_CadIfDownChannelPCEmerAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,29),_CadIfDownChannelPCEmerAllowedUsage_Type())
cadIfDownChannelPCEmerAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCEmerAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPCEmerAllowedUsage.setUnits(_G)
class _CadIfDownChannelPCEmerResUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDownChannelPCEmerResUsage_Type.__name__=_B
_CadIfDownChannelPCEmerResUsage_Object=MibTableColumn
cadIfDownChannelPCEmerResUsage=_CadIfDownChannelPCEmerResUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,30),_CadIfDownChannelPCEmerResUsage_Type())
cadIfDownChannelPCEmerResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCEmerResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPCEmerResUsage.setUnits(_G)
class _CadIfDownChannelPCTotalAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDownChannelPCTotalAllowedUsage_Type.__name__=_B
_CadIfDownChannelPCTotalAllowedUsage_Object=MibTableColumn
cadIfDownChannelPCTotalAllowedUsage=_CadIfDownChannelPCTotalAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,31),_CadIfDownChannelPCTotalAllowedUsage_Type())
cadIfDownChannelPCTotalAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCTotalAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDownChannelPCTotalAllowedUsage.setUnits(_G)
_CadIfDownChannelPCPreemptionAllowed_Type=TruthValue
_CadIfDownChannelPCPreemptionAllowed_Object=MibTableColumn
cadIfDownChannelPCPreemptionAllowed=_CadIfDownChannelPCPreemptionAllowed_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,32),_CadIfDownChannelPCPreemptionAllowed_Type())
cadIfDownChannelPCPreemptionAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPCPreemptionAllowed.setStatus(_A)
_CadIfDownChannelIfIndex_Type=InterfaceIndex
_CadIfDownChannelIfIndex_Object=MibTableColumn
cadIfDownChannelIfIndex=_CadIfDownChannelIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,37),_CadIfDownChannelIfIndex_Type())
cadIfDownChannelIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDownChannelIfIndex.setStatus(_A)
class _CadIfDownChannelPrimaryCapable_Type(TruthValue):defaultValue=1
_CadIfDownChannelPrimaryCapable_Type.__name__=_I
_CadIfDownChannelPrimaryCapable_Object=MibTableColumn
cadIfDownChannelPrimaryCapable=_CadIfDownChannelPrimaryCapable_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,38),_CadIfDownChannelPrimaryCapable_Type())
cadIfDownChannelPrimaryCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownChannelPrimaryCapable.setStatus(_A)
class _CadIfDownSpectralInversion_Type(TruthValue):defaultValue=2
_CadIfDownSpectralInversion_Type.__name__=_I
_CadIfDownSpectralInversion_Object=MibTableColumn
cadIfDownSpectralInversion=_CadIfDownSpectralInversion_Object((1,3,6,1,4,1,4998,1,1,15,2,1,1,39),_CadIfDownSpectralInversion_Type())
cadIfDownSpectralInversion.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDownSpectralInversion.setStatus(_A)
_CadDownChannelParams_ObjectIdentity=ObjectIdentity
cadDownChannelParams=_CadDownChannelParams_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,2,2))
class _CadDownChannelMaxFrequency_Type(Integer32):defaultValue=867000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(858000000,858000000),ValueRangeConstraint(867000000,867000000),ValueRangeConstraint(999000000,999000000))
_CadDownChannelMaxFrequency_Type.__name__=_B
_CadDownChannelMaxFrequency_Object=MibScalar
cadDownChannelMaxFrequency=_CadDownChannelMaxFrequency_Object((1,3,6,1,4,1,4998,1,1,15,2,2,1),_CadDownChannelMaxFrequency_Type())
cadDownChannelMaxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelMaxFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadDownChannelMaxFrequency.setUnits(_E)
class _CadDownChannelMinFrequency_Type(Integer32):defaultValue=91000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(57000000,57000000),ValueRangeConstraint(85000000,85000000),ValueRangeConstraint(91000000,91000000),ValueRangeConstraint(112000000,112000000))
_CadDownChannelMinFrequency_Type.__name__=_B
_CadDownChannelMinFrequency_Object=MibScalar
cadDownChannelMinFrequency=_CadDownChannelMinFrequency_Object((1,3,6,1,4,1,4998,1,1,15,2,2,2),_CadDownChannelMinFrequency_Type())
cadDownChannelMinFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelMinFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadDownChannelMinFrequency.setUnits(_E)
class _CadDownChannelAgcEnable_Type(TruthValue):defaultValue=1
_CadDownChannelAgcEnable_Type.__name__=_I
_CadDownChannelAgcEnable_Object=MibScalar
cadDownChannelAgcEnable=_CadDownChannelAgcEnable_Object((1,3,6,1,4,1,4998,1,1,15,2,2,3),_CadDownChannelAgcEnable_Type())
cadDownChannelAgcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelAgcEnable.setStatus(_A)
class _CadDownChannelOorRecoveryEnable_Type(TruthValue):defaultValue=2
_CadDownChannelOorRecoveryEnable_Type.__name__=_I
_CadDownChannelOorRecoveryEnable_Object=MibScalar
cadDownChannelOorRecoveryEnable=_CadDownChannelOorRecoveryEnable_Object((1,3,6,1,4,1,4998,1,1,15,2,2,4),_CadDownChannelOorRecoveryEnable_Type())
cadDownChannelOorRecoveryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelOorRecoveryEnable.setStatus(_A)
class _CadDsOfdmOcdDpdPlcInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,250))
_CadDsOfdmOcdDpdPlcInterval_Type.__name__=_B
_CadDsOfdmOcdDpdPlcInterval_Object=MibScalar
cadDsOfdmOcdDpdPlcInterval=_CadDsOfdmOcdDpdPlcInterval_Object((1,3,6,1,4,1,4998,1,1,15,2,2,5),_CadDsOfdmOcdDpdPlcInterval_Type())
cadDsOfdmOcdDpdPlcInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDsOfdmOcdDpdPlcInterval.setStatus(_A)
if mibBuilder.loadTexts:cadDsOfdmOcdDpdPlcInterval.setUnits(_L)
class _CadDsOfdmDpdProfAInterval_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,600))
_CadDsOfdmDpdProfAInterval_Type.__name__=_B
_CadDsOfdmDpdProfAInterval_Object=MibScalar
cadDsOfdmDpdProfAInterval=_CadDsOfdmDpdProfAInterval_Object((1,3,6,1,4,1,4998,1,1,15,2,2,6),_CadDsOfdmDpdProfAInterval_Type())
cadDsOfdmDpdProfAInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDsOfdmDpdProfAInterval.setStatus(_A)
if mibBuilder.loadTexts:cadDsOfdmDpdProfAInterval.setUnits(_L)
class _CadDownChannelLsredMinThresh_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_CadDownChannelLsredMinThresh_Type.__name__=_B
_CadDownChannelLsredMinThresh_Object=MibScalar
cadDownChannelLsredMinThresh=_CadDownChannelLsredMinThresh_Object((1,3,6,1,4,1,4998,1,1,15,2,2,7),_CadDownChannelLsredMinThresh_Type())
cadDownChannelLsredMinThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelLsredMinThresh.setStatus(_A)
if mibBuilder.loadTexts:cadDownChannelLsredMinThresh.setUnits(_L)
class _CadDownChannelLsredMaxThresh_Type(Integer32):defaultValue=2500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2500))
_CadDownChannelLsredMaxThresh_Type.__name__=_B
_CadDownChannelLsredMaxThresh_Object=MibScalar
cadDownChannelLsredMaxThresh=_CadDownChannelLsredMaxThresh_Object((1,3,6,1,4,1,4998,1,1,15,2,2,8),_CadDownChannelLsredMaxThresh_Type())
cadDownChannelLsredMaxThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelLsredMaxThresh.setStatus(_A)
if mibBuilder.loadTexts:cadDownChannelLsredMaxThresh.setUnits(_L)
class _CadDownChannelLsredMaxProb_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CadDownChannelLsredMaxProb_Type.__name__=_B
_CadDownChannelLsredMaxProb_Object=MibScalar
cadDownChannelLsredMaxProb=_CadDownChannelLsredMaxProb_Object((1,3,6,1,4,1,4998,1,1,15,2,2,9),_CadDownChannelLsredMaxProb_Type())
cadDownChannelLsredMaxProb.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelLsredMaxProb.setStatus(_A)
if mibBuilder.loadTexts:cadDownChannelLsredMaxProb.setUnits('0.01%')
class _CadDownChannelVoiceShaping_Type(TruthValue):defaultValue=2
_CadDownChannelVoiceShaping_Type.__name__=_I
_CadDownChannelVoiceShaping_Object=MibScalar
cadDownChannelVoiceShaping=_CadDownChannelVoiceShaping_Object((1,3,6,1,4,1,4998,1,1,15,2,2,10),_CadDownChannelVoiceShaping_Type())
cadDownChannelVoiceShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:cadDownChannelVoiceShaping.setStatus(_A)
_CadIfDsOfdmPowerTable_Object=MibTable
cadIfDsOfdmPowerTable=_CadIfDsOfdmPowerTable_Object((1,3,6,1,4,1,4998,1,1,15,2,3))
if mibBuilder.loadTexts:cadIfDsOfdmPowerTable.setStatus(_A)
_CadIfDsOfdmPowerEntry_Object=MibTableRow
cadIfDsOfdmPowerEntry=_CadIfDsOfdmPowerEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1))
cadIfDsOfdmPowerEntry.setIndexNames((0,_F,_b),(0,_F,_c))
if mibBuilder.loadTexts:cadIfDsOfdmPowerEntry.setStatus(_A)
_CadIfDsOfdmPowerIfIndex_Type=InterfaceIndex
_CadIfDsOfdmPowerIfIndex_Object=MibTableColumn
cadIfDsOfdmPowerIfIndex=_CadIfDsOfdmPowerIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,1),_CadIfDsOfdmPowerIfIndex_Type())
cadIfDsOfdmPowerIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfDsOfdmPowerIfIndex.setStatus(_A)
class _CadIfDsOfdmPowerFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,192))
_CadIfDsOfdmPowerFrequency_Type.__name__=_B
_CadIfDsOfdmPowerFrequency_Object=MibTableColumn
cadIfDsOfdmPowerFrequency=_CadIfDsOfdmPowerFrequency_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,2),_CadIfDsOfdmPowerFrequency_Type())
cadIfDsOfdmPowerFrequency.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfDsOfdmPowerFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmPowerFrequency.setUnits('MHz')
class _CadIfDsOfdmPowerFineAdjustment_Type(TenthdBmV):defaultValue=0;subtypeSpec=TenthdBmV.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,0))
_CadIfDsOfdmPowerFineAdjustment_Type.__name__=_J
_CadIfDsOfdmPowerFineAdjustment_Object=MibTableColumn
cadIfDsOfdmPowerFineAdjustment=_CadIfDsOfdmPowerFineAdjustment_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,3),_CadIfDsOfdmPowerFineAdjustment_Type())
cadIfDsOfdmPowerFineAdjustment.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmPowerFineAdjustment.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmPowerFineAdjustment.setUnits('dBmVtenths')
class _CadIfDsOfdmPowerCurrLevel_Type(TenthdBmV):defaultValue=0
_CadIfDsOfdmPowerCurrLevel_Type.__name__=_J
_CadIfDsOfdmPowerCurrLevel_Object=MibTableColumn
cadIfDsOfdmPowerCurrLevel=_CadIfDsOfdmPowerCurrLevel_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,4),_CadIfDsOfdmPowerCurrLevel_Type())
cadIfDsOfdmPowerCurrLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmPowerCurrLevel.setStatus(_A)
class _CadIfDsOfdmPowerMinLevel_Type(TenthdBmV):defaultValue=0
_CadIfDsOfdmPowerMinLevel_Type.__name__=_J
_CadIfDsOfdmPowerMinLevel_Object=MibTableColumn
cadIfDsOfdmPowerMinLevel=_CadIfDsOfdmPowerMinLevel_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,5),_CadIfDsOfdmPowerMinLevel_Type())
cadIfDsOfdmPowerMinLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmPowerMinLevel.setStatus(_A)
class _CadIfDsOfdmPowerMaxLevel_Type(TenthdBmV):defaultValue=0
_CadIfDsOfdmPowerMaxLevel_Type.__name__=_J
_CadIfDsOfdmPowerMaxLevel_Object=MibTableColumn
cadIfDsOfdmPowerMaxLevel=_CadIfDsOfdmPowerMaxLevel_Object((1,3,6,1,4,1,4998,1,1,15,2,3,1,6),_CadIfDsOfdmPowerMaxLevel_Type())
cadIfDsOfdmPowerMaxLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmPowerMaxLevel.setStatus(_A)
_CadIfDsOfdmChlTable_Object=MibTable
cadIfDsOfdmChlTable=_CadIfDsOfdmChlTable_Object((1,3,6,1,4,1,4998,1,1,15,2,5))
if mibBuilder.loadTexts:cadIfDsOfdmChlTable.setStatus(_A)
_CadIfDsOfdmChlEntry_Object=MibTableRow
cadIfDsOfdmChlEntry=_CadIfDsOfdmChlEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1))
cadIfDsOfdmChlEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:cadIfDsOfdmChlEntry.setStatus(_A)
_CadIfDsOfdmChlIfIndex_Type=InterfaceIndex
_CadIfDsOfdmChlIfIndex_Object=MibTableColumn
cadIfDsOfdmChlIfIndex=_CadIfDsOfdmChlIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,1),_CadIfDsOfdmChlIfIndex_Type())
cadIfDsOfdmChlIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfDsOfdmChlIfIndex.setStatus(_A)
class _CadIfDsOfdmChlLowFreq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(108000000,1770000000))
_CadIfDsOfdmChlLowFreq_Type.__name__=_B
_CadIfDsOfdmChlLowFreq_Object=MibTableColumn
cadIfDsOfdmChlLowFreq=_CadIfDsOfdmChlLowFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,2),_CadIfDsOfdmChlLowFreq_Type())
cadIfDsOfdmChlLowFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlLowFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlLowFreq.setUnits(_E)
class _CadIfDsOfdmChlHighFreq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(132000000,1794000000))
_CadIfDsOfdmChlHighFreq_Type.__name__=_B
_CadIfDsOfdmChlHighFreq_Object=MibTableColumn
cadIfDsOfdmChlHighFreq=_CadIfDsOfdmChlHighFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,3),_CadIfDsOfdmChlHighFreq_Type())
cadIfDsOfdmChlHighFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlHighFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlHighFreq.setUnits(_E)
class _CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(108000000,1788000000))
_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type.__name__=_B
_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Object=MibTableColumn
cadIfDsOfdmChlPlcBlkLowSubcCentFreq=_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,4),_CadIfDsOfdmChlPlcBlkLowSubcCentFreq_Type())
cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setUnits(_E)
class _CadIfDsOfdmChlCyclicPrefix_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(192,192),ValueRangeConstraint(256,256),ValueRangeConstraint(512,512),ValueRangeConstraint(768,768),ValueRangeConstraint(1024,1024))
_CadIfDsOfdmChlCyclicPrefix_Type.__name__=_B
_CadIfDsOfdmChlCyclicPrefix_Object=MibTableColumn
cadIfDsOfdmChlCyclicPrefix=_CadIfDsOfdmChlCyclicPrefix_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,5),_CadIfDsOfdmChlCyclicPrefix_Type())
cadIfDsOfdmChlCyclicPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlCyclicPrefix.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlCyclicPrefix.setUnits(_e)
class _CadIfDsOfdmChlRolloffPeriod_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,64),ValueRangeConstraint(128,128),ValueRangeConstraint(192,192),ValueRangeConstraint(256,256))
_CadIfDsOfdmChlRolloffPeriod_Type.__name__=_B
_CadIfDsOfdmChlRolloffPeriod_Object=MibTableColumn
cadIfDsOfdmChlRolloffPeriod=_CadIfDsOfdmChlRolloffPeriod_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,6),_CadIfDsOfdmChlRolloffPeriod_Type())
cadIfDsOfdmChlRolloffPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlRolloffPeriod.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlRolloffPeriod.setUnits(_e)
class _CadIfDsOfdmChlTimeIntlvrDepth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CadIfDsOfdmChlTimeIntlvrDepth_Type.__name__=_B
_CadIfDsOfdmChlTimeIntlvrDepth_Object=MibTableColumn
cadIfDsOfdmChlTimeIntlvrDepth=_CadIfDsOfdmChlTimeIntlvrDepth_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,7),_CadIfDsOfdmChlTimeIntlvrDepth_Type())
cadIfDsOfdmChlTimeIntlvrDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlTimeIntlvrDepth.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlTimeIntlvrDepth.setUnits('symbols')
class _CadIfDsOfdmChlSubcSpacing_Type(Integer32):defaultValue=50000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25000,25000),ValueRangeConstraint(50000,50000))
_CadIfDsOfdmChlSubcSpacing_Type.__name__=_B
_CadIfDsOfdmChlSubcSpacing_Object=MibTableColumn
cadIfDsOfdmChlSubcSpacing=_CadIfDsOfdmChlSubcSpacing_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,8),_CadIfDsOfdmChlSubcSpacing_Type())
cadIfDsOfdmChlSubcSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlSubcSpacing.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlSubcSpacing.setUnits(_E)
class _CadIfDsOfdmChlContPilotScaleFactor_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(48,120))
_CadIfDsOfdmChlContPilotScaleFactor_Type.__name__=_B
_CadIfDsOfdmChlContPilotScaleFactor_Object=MibTableColumn
cadIfDsOfdmChlContPilotScaleFactor=_CadIfDsOfdmChlContPilotScaleFactor_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,9),_CadIfDsOfdmChlContPilotScaleFactor_Type())
cadIfDsOfdmChlContPilotScaleFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlContPilotScaleFactor.setStatus(_A)
class _CadIfDsOfdmChlMaxRoundTripDelay_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1600))
_CadIfDsOfdmChlMaxRoundTripDelay_Type.__name__=_B
_CadIfDsOfdmChlMaxRoundTripDelay_Object=MibTableColumn
cadIfDsOfdmChlMaxRoundTripDelay=_CadIfDsOfdmChlMaxRoundTripDelay_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,10),_CadIfDsOfdmChlMaxRoundTripDelay_Type())
cadIfDsOfdmChlMaxRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlMaxRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlMaxRoundTripDelay.setUnits(_a)
class _CadIfDsOfdmChlPCNormAllowedUsage_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDsOfdmChlPCNormAllowedUsage_Type.__name__=_B
_CadIfDsOfdmChlPCNormAllowedUsage_Object=MibTableColumn
cadIfDsOfdmChlPCNormAllowedUsage=_CadIfDsOfdmChlPCNormAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,11),_CadIfDsOfdmChlPCNormAllowedUsage_Type())
cadIfDsOfdmChlPCNormAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCNormAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCNormAllowedUsage.setUnits(_G)
class _CadIfDsOfdmChlPCNormResUsage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDsOfdmChlPCNormResUsage_Type.__name__=_B
_CadIfDsOfdmChlPCNormResUsage_Object=MibTableColumn
cadIfDsOfdmChlPCNormResUsage=_CadIfDsOfdmChlPCNormResUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,12),_CadIfDsOfdmChlPCNormResUsage_Type())
cadIfDsOfdmChlPCNormResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCNormResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCNormResUsage.setUnits(_G)
class _CadIfDsOfdmChlPCEmerAllowedUsage_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDsOfdmChlPCEmerAllowedUsage_Type.__name__=_B
_CadIfDsOfdmChlPCEmerAllowedUsage_Object=MibTableColumn
cadIfDsOfdmChlPCEmerAllowedUsage=_CadIfDsOfdmChlPCEmerAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,13),_CadIfDsOfdmChlPCEmerAllowedUsage_Type())
cadIfDsOfdmChlPCEmerAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCEmerAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCEmerAllowedUsage.setUnits(_G)
class _CadIfDsOfdmChlPCEmerResUsage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDsOfdmChlPCEmerResUsage_Type.__name__=_B
_CadIfDsOfdmChlPCEmerResUsage_Object=MibTableColumn
cadIfDsOfdmChlPCEmerResUsage=_CadIfDsOfdmChlPCEmerResUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,14),_CadIfDsOfdmChlPCEmerResUsage_Type())
cadIfDsOfdmChlPCEmerResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCEmerResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCEmerResUsage.setUnits(_G)
class _CadIfDsOfdmChlPCTotalAllowedUsage_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfDsOfdmChlPCTotalAllowedUsage_Type.__name__=_B
_CadIfDsOfdmChlPCTotalAllowedUsage_Object=MibTableColumn
cadIfDsOfdmChlPCTotalAllowedUsage=_CadIfDsOfdmChlPCTotalAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,15),_CadIfDsOfdmChlPCTotalAllowedUsage_Type())
cadIfDsOfdmChlPCTotalAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCTotalAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCTotalAllowedUsage.setUnits(_G)
class _CadIfDsOfdmChlPCPreemptionAllowed_Type(TruthValue):defaultValue=1
_CadIfDsOfdmChlPCPreemptionAllowed_Type.__name__=_I
_CadIfDsOfdmChlPCPreemptionAllowed_Object=MibTableColumn
cadIfDsOfdmChlPCPreemptionAllowed=_CadIfDsOfdmChlPCPreemptionAllowed_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,16),_CadIfDsOfdmChlPCPreemptionAllowed_Type())
cadIfDsOfdmChlPCPreemptionAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlPCPreemptionAllowed.setStatus(_A)
class _CadIfDsOfdmChlRfPortBasePower_Type(TenthdBmV):defaultValue=380;subtypeSpec=TenthdBmV.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,600))
_CadIfDsOfdmChlRfPortBasePower_Type.__name__=_J
_CadIfDsOfdmChlRfPortBasePower_Object=MibTableColumn
cadIfDsOfdmChlRfPortBasePower=_CadIfDsOfdmChlRfPortBasePower_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,17),_CadIfDsOfdmChlRfPortBasePower_Type())
cadIfDsOfdmChlRfPortBasePower.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfDsOfdmChlRfPortBasePower.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlRfPortBasePower.setUnits('dBmV')
class _CadIfDsOfdmChlSubcZeroCentFreq_Type(Integer32):defaultValue=0
_CadIfDsOfdmChlSubcZeroCentFreq_Type.__name__=_B
_CadIfDsOfdmChlSubcZeroCentFreq_Object=MibTableColumn
cadIfDsOfdmChlSubcZeroCentFreq=_CadIfDsOfdmChlSubcZeroCentFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,18),_CadIfDsOfdmChlSubcZeroCentFreq_Type())
cadIfDsOfdmChlSubcZeroCentFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlSubcZeroCentFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlSubcZeroCentFreq.setUnits(_E)
class _CadIfDsOfdmChlLowActSubcCentFreq_Type(Integer32):defaultValue=0
_CadIfDsOfdmChlLowActSubcCentFreq_Type.__name__=_B
_CadIfDsOfdmChlLowActSubcCentFreq_Object=MibTableColumn
cadIfDsOfdmChlLowActSubcCentFreq=_CadIfDsOfdmChlLowActSubcCentFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,19),_CadIfDsOfdmChlLowActSubcCentFreq_Type())
cadIfDsOfdmChlLowActSubcCentFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlLowActSubcCentFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlLowActSubcCentFreq.setUnits(_E)
class _CadIfDsOfdmChlHighActSubcCentFreq_Type(Integer32):defaultValue=0
_CadIfDsOfdmChlHighActSubcCentFreq_Type.__name__=_B
_CadIfDsOfdmChlHighActSubcCentFreq_Object=MibTableColumn
cadIfDsOfdmChlHighActSubcCentFreq=_CadIfDsOfdmChlHighActSubcCentFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,20),_CadIfDsOfdmChlHighActSubcCentFreq_Type())
cadIfDsOfdmChlHighActSubcCentFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlHighActSubcCentFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlHighActSubcCentFreq.setUnits(_E)
class _CadIfDsOfdmChlPlcLowSubcCentFreq_Type(Integer32):defaultValue=0
_CadIfDsOfdmChlPlcLowSubcCentFreq_Type.__name__=_B
_CadIfDsOfdmChlPlcLowSubcCentFreq_Object=MibTableColumn
cadIfDsOfdmChlPlcLowSubcCentFreq=_CadIfDsOfdmChlPlcLowSubcCentFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,21),_CadIfDsOfdmChlPlcLowSubcCentFreq_Type())
cadIfDsOfdmChlPlcLowSubcCentFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlPlcLowSubcCentFreq.setStatus(_A)
if mibBuilder.loadTexts:cadIfDsOfdmChlPlcLowSubcCentFreq.setUnits(_E)
class _CadIfDsOfdmChlNumActSubc_Type(Integer32):defaultValue=0
_CadIfDsOfdmChlNumActSubc_Type.__name__=_B
_CadIfDsOfdmChlNumActSubc_Object=MibTableColumn
cadIfDsOfdmChlNumActSubc=_CadIfDsOfdmChlNumActSubc_Object((1,3,6,1,4,1,4998,1,1,15,2,5,1,22),_CadIfDsOfdmChlNumActSubc_Type())
cadIfDsOfdmChlNumActSubc.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlNumActSubc.setStatus(_A)
_CadIfDsOfdmChlDataTable_Object=MibTable
cadIfDsOfdmChlDataTable=_CadIfDsOfdmChlDataTable_Object((1,3,6,1,4,1,4998,1,1,15,2,6))
if mibBuilder.loadTexts:cadIfDsOfdmChlDataTable.setStatus(_A)
_CadIfDsOfdmChlDataEntry_Object=MibTableRow
cadIfDsOfdmChlDataEntry=_CadIfDsOfdmChlDataEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,6,1))
if mibBuilder.loadTexts:cadIfDsOfdmChlDataEntry.setStatus(_A)
class _CadIfDsOfdmChlDataNumActSubcarriers_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(200,7600))
_CadIfDsOfdmChlDataNumActSubcarriers_Type.__name__=_B
_CadIfDsOfdmChlDataNumActSubcarriers_Object=MibTableColumn
cadIfDsOfdmChlDataNumActSubcarriers=_CadIfDsOfdmChlDataNumActSubcarriers_Object((1,3,6,1,4,1,4998,1,1,15,2,6,1,1),_CadIfDsOfdmChlDataNumActSubcarriers_Type())
cadIfDsOfdmChlDataNumActSubcarriers.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlDataNumActSubcarriers.setStatus(_A)
class _CadIfDsOfdmChlDataNumContPilots_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,128))
_CadIfDsOfdmChlDataNumContPilots_Type.__name__=_B
_CadIfDsOfdmChlDataNumContPilots_Object=MibTableColumn
cadIfDsOfdmChlDataNumContPilots=_CadIfDsOfdmChlDataNumContPilots_Object((1,3,6,1,4,1,4998,1,1,15,2,6,1,2),_CadIfDsOfdmChlDataNumContPilots_Type())
cadIfDsOfdmChlDataNumContPilots.setMaxAccess(_D)
if mibBuilder.loadTexts:cadIfDsOfdmChlDataNumContPilots.setStatus(_A)
_CadDsOfdmProfileTable_Object=MibTable
cadDsOfdmProfileTable=_CadDsOfdmProfileTable_Object((1,3,6,1,4,1,4998,1,1,15,2,8))
if mibBuilder.loadTexts:cadDsOfdmProfileTable.setStatus(_A)
_CadDsOfdmProfileEntry_Object=MibTableRow
cadDsOfdmProfileEntry=_CadDsOfdmProfileEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,8,1))
cadDsOfdmProfileEntry.setIndexNames((0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:cadDsOfdmProfileEntry.setStatus(_A)
_CadDsOfdmProfileIfIndex_Type=InterfaceIndex
_CadDsOfdmProfileIfIndex_Object=MibTableColumn
cadDsOfdmProfileIfIndex=_CadDsOfdmProfileIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,8,1,1),_CadDsOfdmProfileIfIndex_Type())
cadDsOfdmProfileIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfileIfIndex.setStatus(_A)
_CadDsOfdmProfileId_Type=OfdmProfileId
_CadDsOfdmProfileId_Object=MibTableColumn
cadDsOfdmProfileId=_CadDsOfdmProfileId_Object((1,3,6,1,4,1,4998,1,1,15,2,8,1,2),_CadDsOfdmProfileId_Type())
cadDsOfdmProfileId.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfileId.setStatus(_A)
class _CadDsOfdmProfileDefBitload_Type(CerOfdmModType):defaultValue=10
_CadDsOfdmProfileDefBitload_Type.__name__=_M
_CadDsOfdmProfileDefBitload_Object=MibTableColumn
cadDsOfdmProfileDefBitload=_CadDsOfdmProfileDefBitload_Object((1,3,6,1,4,1,4998,1,1,15,2,8,1,3),_CadDsOfdmProfileDefBitload_Type())
cadDsOfdmProfileDefBitload.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfileDefBitload.setStatus(_A)
_CadDsOfdmProfileRowStatus_Type=RowStatus
_CadDsOfdmProfileRowStatus_Object=MibTableColumn
cadDsOfdmProfileRowStatus=_CadDsOfdmProfileRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,2,8,1,4),_CadDsOfdmProfileRowStatus_Type())
cadDsOfdmProfileRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfileRowStatus.setStatus(_A)
_CadDsOfdmProfStatTable_Object=MibTable
cadDsOfdmProfStatTable=_CadDsOfdmProfStatTable_Object((1,3,6,1,4,1,4998,1,1,15,2,9))
if mibBuilder.loadTexts:cadDsOfdmProfStatTable.setStatus(_A)
_CadDsOfdmProfStatEntry_Object=MibTableRow
cadDsOfdmProfStatEntry=_CadDsOfdmProfStatEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1))
cadDsOfdmProfStatEntry.setIndexNames((0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:cadDsOfdmProfStatEntry.setStatus(_A)
_CadDsOfdmProfStatIfIndex_Type=InterfaceIndex
_CadDsOfdmProfStatIfIndex_Object=MibTableColumn
cadDsOfdmProfStatIfIndex=_CadDsOfdmProfStatIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,1),_CadDsOfdmProfStatIfIndex_Type())
cadDsOfdmProfStatIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfStatIfIndex.setStatus(_A)
_CadDsOfdmProfStatProfId_Type=OfdmProfileId
_CadDsOfdmProfStatProfId_Object=MibTableColumn
cadDsOfdmProfStatProfId=_CadDsOfdmProfStatProfId_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,2),_CadDsOfdmProfStatProfId_Type())
cadDsOfdmProfStatProfId.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfStatProfId.setStatus(_A)
_CadDsOfdmProfStatAvgBitsPerSubc_Type=Unsigned32
_CadDsOfdmProfStatAvgBitsPerSubc_Object=MibTableColumn
cadDsOfdmProfStatAvgBitsPerSubc=_CadDsOfdmProfStatAvgBitsPerSubc_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,3),_CadDsOfdmProfStatAvgBitsPerSubc_Type())
cadDsOfdmProfStatAvgBitsPerSubc.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStatAvgBitsPerSubc.setStatus(_A)
if mibBuilder.loadTexts:cadDsOfdmProfStatAvgBitsPerSubc.setUnits('HundredthBit')
_CadDsOfdmProfStatReqMods_Type=CerOfdmModBitsType
_CadDsOfdmProfStatReqMods_Object=MibTableColumn
cadDsOfdmProfStatReqMods=_CadDsOfdmProfStatReqMods_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,4),_CadDsOfdmProfStatReqMods_Type())
cadDsOfdmProfStatReqMods.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStatReqMods.setStatus(_A)
_CadDsOfdmProfStatEtherFrameBytes_Type=Counter64
_CadDsOfdmProfStatEtherFrameBytes_Object=MibTableColumn
cadDsOfdmProfStatEtherFrameBytes=_CadDsOfdmProfStatEtherFrameBytes_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,5),_CadDsOfdmProfStatEtherFrameBytes_Type())
cadDsOfdmProfStatEtherFrameBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStatEtherFrameBytes.setStatus(_A)
_CadDsOfdmProfStatTotalCodewords_Type=Counter64
_CadDsOfdmProfStatTotalCodewords_Object=MibTableColumn
cadDsOfdmProfStatTotalCodewords=_CadDsOfdmProfStatTotalCodewords_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,6),_CadDsOfdmProfStatTotalCodewords_Type())
cadDsOfdmProfStatTotalCodewords.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStatTotalCodewords.setStatus(_A)
class _CadDsOfdmProfStat30SecCwUtil_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadDsOfdmProfStat30SecCwUtil_Type.__name__=_N
_CadDsOfdmProfStat30SecCwUtil_Object=MibTableColumn
cadDsOfdmProfStat30SecCwUtil=_CadDsOfdmProfStat30SecCwUtil_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,7),_CadDsOfdmProfStat30SecCwUtil_Type())
cadDsOfdmProfStat30SecCwUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStat30SecCwUtil.setStatus(_A)
class _CadDsOfdmProfStat30SecCwEff_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadDsOfdmProfStat30SecCwEff_Type.__name__=_N
_CadDsOfdmProfStat30SecCwEff_Object=MibTableColumn
cadDsOfdmProfStat30SecCwEff=_CadDsOfdmProfStat30SecCwEff_Object((1,3,6,1,4,1,4998,1,1,15,2,9,1,8),_CadDsOfdmProfStat30SecCwEff_Type())
cadDsOfdmProfStat30SecCwEff.setMaxAccess(_D)
if mibBuilder.loadTexts:cadDsOfdmProfStat30SecCwEff.setStatus(_A)
_CadDsOfdmProfExceptionTable_Object=MibTable
cadDsOfdmProfExceptionTable=_CadDsOfdmProfExceptionTable_Object((1,3,6,1,4,1,4998,1,1,15,2,11))
if mibBuilder.loadTexts:cadDsOfdmProfExceptionTable.setStatus(_A)
_CadDsOfdmProfExceptionEntry_Object=MibTableRow
cadDsOfdmProfExceptionEntry=_CadDsOfdmProfExceptionEntry_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1))
cadDsOfdmProfExceptionEntry.setIndexNames((0,_F,_j),(0,_F,_k),(0,_F,_l))
if mibBuilder.loadTexts:cadDsOfdmProfExceptionEntry.setStatus(_A)
_CadDsOfdmProfExceptionIfIndex_Type=InterfaceIndex
_CadDsOfdmProfExceptionIfIndex_Object=MibTableColumn
cadDsOfdmProfExceptionIfIndex=_CadDsOfdmProfExceptionIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,1),_CadDsOfdmProfExceptionIfIndex_Type())
cadDsOfdmProfExceptionIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionIfIndex.setStatus(_A)
_CadDsOfdmProfExceptionProfId_Type=OfdmProfileId
_CadDsOfdmProfExceptionProfId_Object=MibTableColumn
cadDsOfdmProfExceptionProfId=_CadDsOfdmProfExceptionProfId_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,2),_CadDsOfdmProfExceptionProfId_Type())
cadDsOfdmProfExceptionProfId.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionProfId.setStatus(_A)
class _CadDsOfdmProfExceptionLowFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(108000000,1770000000))
_CadDsOfdmProfExceptionLowFreq_Type.__name__=_B
_CadDsOfdmProfExceptionLowFreq_Object=MibTableColumn
cadDsOfdmProfExceptionLowFreq=_CadDsOfdmProfExceptionLowFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,3),_CadDsOfdmProfExceptionLowFreq_Type())
cadDsOfdmProfExceptionLowFreq.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionLowFreq.setStatus(_A)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionLowFreq.setUnits(_E)
class _CadDsOfdmProfExceptionHighFreq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(108000000,1770000000))
_CadDsOfdmProfExceptionHighFreq_Type.__name__=_B
_CadDsOfdmProfExceptionHighFreq_Object=MibTableColumn
cadDsOfdmProfExceptionHighFreq=_CadDsOfdmProfExceptionHighFreq_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,4),_CadDsOfdmProfExceptionHighFreq_Type())
cadDsOfdmProfExceptionHighFreq.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionHighFreq.setStatus(_A)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionHighFreq.setUnits(_E)
class _CadDsOfdmProfExceptionSkip_Type(TruthValue):defaultValue=2
_CadDsOfdmProfExceptionSkip_Type.__name__=_I
_CadDsOfdmProfExceptionSkip_Object=MibTableColumn
cadDsOfdmProfExceptionSkip=_CadDsOfdmProfExceptionSkip_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,5),_CadDsOfdmProfExceptionSkip_Type())
cadDsOfdmProfExceptionSkip.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionSkip.setStatus(_A)
class _CadDsOfdmProfExceptionMainBitload_Type(CerOfdmModType):defaultValue=10
_CadDsOfdmProfExceptionMainBitload_Type.__name__=_M
_CadDsOfdmProfExceptionMainBitload_Object=MibTableColumn
cadDsOfdmProfExceptionMainBitload=_CadDsOfdmProfExceptionMainBitload_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,6),_CadDsOfdmProfExceptionMainBitload_Type())
cadDsOfdmProfExceptionMainBitload.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionMainBitload.setStatus(_A)
class _CadDsOfdmProfExceptionOddBitload_Type(CerOfdmModType):defaultValue=0
_CadDsOfdmProfExceptionOddBitload_Type.__name__=_M
_CadDsOfdmProfExceptionOddBitload_Object=MibTableColumn
cadDsOfdmProfExceptionOddBitload=_CadDsOfdmProfExceptionOddBitload_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,7),_CadDsOfdmProfExceptionOddBitload_Type())
cadDsOfdmProfExceptionOddBitload.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionOddBitload.setStatus(_A)
_CadDsOfdmProfExceptionRowStatus_Type=RowStatus
_CadDsOfdmProfExceptionRowStatus_Object=MibTableColumn
cadDsOfdmProfExceptionRowStatus=_CadDsOfdmProfExceptionRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,2,11,1,8),_CadDsOfdmProfExceptionRowStatus_Type())
cadDsOfdmProfExceptionRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cadDsOfdmProfExceptionRowStatus.setStatus(_A)
cadIfDsOfdmChlEntry.registerAugmentions((_F,_m))
cadIfDsOfdmChlDataEntry.setIndexNames(*cadIfDsOfdmChlEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'OfdmProfileId':OfdmProfileId,_M:CerOfdmModType,'CerOfdmModBitsType':CerOfdmModBitsType,'cadDownchannelMib':cadDownchannelMib,'cadIfDownstreamChannelTable':cadIfDownstreamChannelTable,'cadIfDownstreamChannelEntry':cadIfDownstreamChannelEntry,'cadIfDownChannelId':cadIfDownChannelId,'cadIfDownChannelFrequency':cadIfDownChannelFrequency,'cadIfDownChannelWidth':cadIfDownChannelWidth,'cadIfDownChannelModulation':cadIfDownChannelModulation,'cadIfDownChannelInterleave':cadIfDownChannelInterleave,'cadIfDownChannelPower':cadIfDownChannelPower,'cadIfDownChannelPowerFineAdj':cadIfDownChannelPowerFineAdj,'cadIfCmtsCardNumber':cadIfCmtsCardNumber,'cadIfDownChannelCACL1Threshold':cadIfDownChannelCACL1Threshold,'cadIfDownChannelCACL2Threshold':cadIfDownChannelCACL2Threshold,'cadIfDownChannelCACL3Threshold':cadIfDownChannelCACL3Threshold,'cadIfDownChannelMaxRoundTripDelay':cadIfDownChannelMaxRoundTripDelay,'cadIfDownChannelAnnex':cadIfDownChannelAnnex,'cadIfDownChannelPCNormAllowedUsage':cadIfDownChannelPCNormAllowedUsage,'cadIfDownChannelPCNormResUsage':cadIfDownChannelPCNormResUsage,'cadIfDownChannelPCEmerAllowedUsage':cadIfDownChannelPCEmerAllowedUsage,'cadIfDownChannelPCEmerResUsage':cadIfDownChannelPCEmerResUsage,'cadIfDownChannelPCTotalAllowedUsage':cadIfDownChannelPCTotalAllowedUsage,'cadIfDownChannelPCPreemptionAllowed':cadIfDownChannelPCPreemptionAllowed,_Z:cadIfDownChannelIfIndex,'cadIfDownChannelPrimaryCapable':cadIfDownChannelPrimaryCapable,'cadIfDownSpectralInversion':cadIfDownSpectralInversion,'cadDownChannelParams':cadDownChannelParams,'cadDownChannelMaxFrequency':cadDownChannelMaxFrequency,'cadDownChannelMinFrequency':cadDownChannelMinFrequency,'cadDownChannelAgcEnable':cadDownChannelAgcEnable,'cadDownChannelOorRecoveryEnable':cadDownChannelOorRecoveryEnable,'cadDsOfdmOcdDpdPlcInterval':cadDsOfdmOcdDpdPlcInterval,'cadDsOfdmDpdProfAInterval':cadDsOfdmDpdProfAInterval,'cadDownChannelLsredMinThresh':cadDownChannelLsredMinThresh,'cadDownChannelLsredMaxThresh':cadDownChannelLsredMaxThresh,'cadDownChannelLsredMaxProb':cadDownChannelLsredMaxProb,'cadDownChannelVoiceShaping':cadDownChannelVoiceShaping,'cadIfDsOfdmPowerTable':cadIfDsOfdmPowerTable,'cadIfDsOfdmPowerEntry':cadIfDsOfdmPowerEntry,_b:cadIfDsOfdmPowerIfIndex,_c:cadIfDsOfdmPowerFrequency,'cadIfDsOfdmPowerFineAdjustment':cadIfDsOfdmPowerFineAdjustment,'cadIfDsOfdmPowerCurrLevel':cadIfDsOfdmPowerCurrLevel,'cadIfDsOfdmPowerMinLevel':cadIfDsOfdmPowerMinLevel,'cadIfDsOfdmPowerMaxLevel':cadIfDsOfdmPowerMaxLevel,'cadIfDsOfdmChlTable':cadIfDsOfdmChlTable,'cadIfDsOfdmChlEntry':cadIfDsOfdmChlEntry,_d:cadIfDsOfdmChlIfIndex,'cadIfDsOfdmChlLowFreq':cadIfDsOfdmChlLowFreq,'cadIfDsOfdmChlHighFreq':cadIfDsOfdmChlHighFreq,'cadIfDsOfdmChlPlcBlkLowSubcCentFreq':cadIfDsOfdmChlPlcBlkLowSubcCentFreq,'cadIfDsOfdmChlCyclicPrefix':cadIfDsOfdmChlCyclicPrefix,'cadIfDsOfdmChlRolloffPeriod':cadIfDsOfdmChlRolloffPeriod,'cadIfDsOfdmChlTimeIntlvrDepth':cadIfDsOfdmChlTimeIntlvrDepth,'cadIfDsOfdmChlSubcSpacing':cadIfDsOfdmChlSubcSpacing,'cadIfDsOfdmChlContPilotScaleFactor':cadIfDsOfdmChlContPilotScaleFactor,'cadIfDsOfdmChlMaxRoundTripDelay':cadIfDsOfdmChlMaxRoundTripDelay,'cadIfDsOfdmChlPCNormAllowedUsage':cadIfDsOfdmChlPCNormAllowedUsage,'cadIfDsOfdmChlPCNormResUsage':cadIfDsOfdmChlPCNormResUsage,'cadIfDsOfdmChlPCEmerAllowedUsage':cadIfDsOfdmChlPCEmerAllowedUsage,'cadIfDsOfdmChlPCEmerResUsage':cadIfDsOfdmChlPCEmerResUsage,'cadIfDsOfdmChlPCTotalAllowedUsage':cadIfDsOfdmChlPCTotalAllowedUsage,'cadIfDsOfdmChlPCPreemptionAllowed':cadIfDsOfdmChlPCPreemptionAllowed,'cadIfDsOfdmChlRfPortBasePower':cadIfDsOfdmChlRfPortBasePower,'cadIfDsOfdmChlSubcZeroCentFreq':cadIfDsOfdmChlSubcZeroCentFreq,'cadIfDsOfdmChlLowActSubcCentFreq':cadIfDsOfdmChlLowActSubcCentFreq,'cadIfDsOfdmChlHighActSubcCentFreq':cadIfDsOfdmChlHighActSubcCentFreq,'cadIfDsOfdmChlPlcLowSubcCentFreq':cadIfDsOfdmChlPlcLowSubcCentFreq,'cadIfDsOfdmChlNumActSubc':cadIfDsOfdmChlNumActSubc,'cadIfDsOfdmChlDataTable':cadIfDsOfdmChlDataTable,_m:cadIfDsOfdmChlDataEntry,'cadIfDsOfdmChlDataNumActSubcarriers':cadIfDsOfdmChlDataNumActSubcarriers,'cadIfDsOfdmChlDataNumContPilots':cadIfDsOfdmChlDataNumContPilots,'cadDsOfdmProfileTable':cadDsOfdmProfileTable,'cadDsOfdmProfileEntry':cadDsOfdmProfileEntry,_f:cadDsOfdmProfileIfIndex,_g:cadDsOfdmProfileId,'cadDsOfdmProfileDefBitload':cadDsOfdmProfileDefBitload,'cadDsOfdmProfileRowStatus':cadDsOfdmProfileRowStatus,'cadDsOfdmProfStatTable':cadDsOfdmProfStatTable,'cadDsOfdmProfStatEntry':cadDsOfdmProfStatEntry,_h:cadDsOfdmProfStatIfIndex,_i:cadDsOfdmProfStatProfId,'cadDsOfdmProfStatAvgBitsPerSubc':cadDsOfdmProfStatAvgBitsPerSubc,'cadDsOfdmProfStatReqMods':cadDsOfdmProfStatReqMods,'cadDsOfdmProfStatEtherFrameBytes':cadDsOfdmProfStatEtherFrameBytes,'cadDsOfdmProfStatTotalCodewords':cadDsOfdmProfStatTotalCodewords,'cadDsOfdmProfStat30SecCwUtil':cadDsOfdmProfStat30SecCwUtil,'cadDsOfdmProfStat30SecCwEff':cadDsOfdmProfStat30SecCwEff,'cadDsOfdmProfExceptionTable':cadDsOfdmProfExceptionTable,'cadDsOfdmProfExceptionEntry':cadDsOfdmProfExceptionEntry,_j:cadDsOfdmProfExceptionIfIndex,_k:cadDsOfdmProfExceptionProfId,_l:cadDsOfdmProfExceptionLowFreq,'cadDsOfdmProfExceptionHighFreq':cadDsOfdmProfExceptionHighFreq,'cadDsOfdmProfExceptionSkip':cadDsOfdmProfExceptionSkip,'cadDsOfdmProfExceptionMainBitload':cadDsOfdmProfExceptionMainBitload,'cadDsOfdmProfExceptionOddBitload':cadDsOfdmProfExceptionOddBitload,'cadDsOfdmProfExceptionRowStatus':cadDsOfdmProfExceptionRowStatus})