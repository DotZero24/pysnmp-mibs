_t='nbsOtnpmCurrentFc'
_s='nbsOtnpmCurrentUas'
_r='nbsOtnpmCurrentBberExp'
_q='nbsOtnpmCurrentBberSig'
_p='nbsOtnpmCurrentBbe'
_o='nbsOtnpmCurrentSesrExp'
_n='nbsOtnpmCurrentSesrSig'
_m='nbsOtnpmCurrentSes'
_l='nbsOtnpmCurrentEsrExp'
_k='nbsOtnpmCurrentEsrSig'
_j='nbsOtnpmCurrentEs'
_i='nbsOtnStatsIfIndex'
_h='clearing'
_g='notSupported'
_f='nbsOtnAlarmsIfIndex'
_e='nbsOtnpmRunningScope'
_d='nbsOtnpmRunningIfIndex'
_c='nbsOtnpmHistoricSample'
_b='nbsOtnpmHistoricScope'
_a='nbsOtnpmHistoricInterval'
_Z='nbsOtnpmHistoricIfIndex'
_Y='nbsOtnpmThresholdsScope'
_X='nbsOtnpmThresholdsInterval'
_W='nbsOtnpmThresholdsIfIndex'
_V='OctetString'
_U='twentyfourHour'
_T='quarterHour'
_S='not-accessible'
_R='path'
_Q='section'
_P='tcm6'
_O='tcm5'
_N='tcm4'
_M='tcm3'
_L='tcm2'
_K='tcm1'
_J='ifAlias'
_I='IF-MIB'
_H='nbsOtnpmCurrentScope'
_G='nbsOtnpmCurrentInterval'
_F='nbsOtnpmCurrentIfIndex'
_E='read-write'
_D='Integer32'
_C='NBS-OTNPM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
WritableU64,nbs=mibBuilder.importSymbols('NBS-MIB','WritableU64','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsOtnpmMib=ModuleIdentity((1,3,6,1,4,1,629,222))
class NbsOtnAlarmId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53)));namedValues=NamedValues(*(('aLOS',1),('aLOF',2),('aOOF',3),('aLOM',4),('aOOM',5),('aRxLOL',6),('aTxLOL',7),('aOtuAIS',8),('aSectBDI',9),('aSectBIAE',10),('aSectIAE',11),('aSectTIM',12),('aOduAIS',13),('aOduOCI',14),('aOduLCK',15),('aPathBDI',16),('aPathTIM',17),('aTcm1BDI',18),('aTcm2BDI',19),('aTcm3BDI',20),('aTcm4BDI',21),('aTcm5BDI',22),('aTcm6BDI',23),('aTcm1BIAE',24),('aTcm2BIAE',25),('aTcm3BIAE',26),('aTcm4BIAE',27),('aTcm5BIAE',28),('aTcm6BIAE',29),('aTcm1IAE',30),('aTcm2IAE',31),('aTcm3IAE',32),('aTcm4IAE',33),('aTcm5IAE',34),('aTcm6IAE',35),('aTcm1LTC',36),('aTcm2LTC',37),('aTcm3LTC',38),('aTcm4LTC',39),('aTcm5LTC',40),('aTcm6LTC',41),('aTcm1TIM',42),('aTcm2TIM',43),('aTcm3TIM',44),('aTcm4TIM',45),('aTcm5TIM',46),('aTcm6TIM',47),('aFwdSF',48),('aFwdSD',49),('aBwdSF',50),('aBwdSD',51),('aPTM',52),('aCSF',53)))
class NbsOtnAlarmMask(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_NbsOtnpmThresholdsGrp_ObjectIdentity=ObjectIdentity
nbsOtnpmThresholdsGrp=_NbsOtnpmThresholdsGrp_ObjectIdentity((1,3,6,1,4,1,629,222,1))
if mibBuilder.loadTexts:nbsOtnpmThresholdsGrp.setStatus(_A)
_NbsOtnpmThresholdsTable_Object=MibTable
nbsOtnpmThresholdsTable=_NbsOtnpmThresholdsTable_Object((1,3,6,1,4,1,629,222,1,1))
if mibBuilder.loadTexts:nbsOtnpmThresholdsTable.setStatus(_A)
_NbsOtnpmThresholdsEntry_Object=MibTableRow
nbsOtnpmThresholdsEntry=_NbsOtnpmThresholdsEntry_Object((1,3,6,1,4,1,629,222,1,1,1))
nbsOtnpmThresholdsEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:nbsOtnpmThresholdsEntry.setStatus(_A)
_NbsOtnpmThresholdsIfIndex_Type=InterfaceIndex
_NbsOtnpmThresholdsIfIndex_Object=MibTableColumn
nbsOtnpmThresholdsIfIndex=_NbsOtnpmThresholdsIfIndex_Object((1,3,6,1,4,1,629,222,1,1,1,1),_NbsOtnpmThresholdsIfIndex_Type())
nbsOtnpmThresholdsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmThresholdsIfIndex.setStatus(_A)
class _NbsOtnpmThresholdsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_NbsOtnpmThresholdsInterval_Type.__name__=_D
_NbsOtnpmThresholdsInterval_Object=MibTableColumn
nbsOtnpmThresholdsInterval=_NbsOtnpmThresholdsInterval_Object((1,3,6,1,4,1,629,222,1,1,1,2),_NbsOtnpmThresholdsInterval_Type())
nbsOtnpmThresholdsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmThresholdsInterval.setStatus(_A)
class _NbsOtnpmThresholdsScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8)))
_NbsOtnpmThresholdsScope_Type.__name__=_D
_NbsOtnpmThresholdsScope_Object=MibTableColumn
nbsOtnpmThresholdsScope=_NbsOtnpmThresholdsScope_Object((1,3,6,1,4,1,629,222,1,1,1,3),_NbsOtnpmThresholdsScope_Type())
nbsOtnpmThresholdsScope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmThresholdsScope.setStatus(_A)
_NbsOtnpmThresholdsEs_Type=Unsigned32
_NbsOtnpmThresholdsEs_Object=MibTableColumn
nbsOtnpmThresholdsEs=_NbsOtnpmThresholdsEs_Object((1,3,6,1,4,1,629,222,1,1,1,10),_NbsOtnpmThresholdsEs_Type())
nbsOtnpmThresholdsEs.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsEs.setStatus(_A)
class _NbsOtnpmThresholdsEsrSig_Type(Integer32):defaultValue=0
_NbsOtnpmThresholdsEsrSig_Type.__name__=_D
_NbsOtnpmThresholdsEsrSig_Object=MibTableColumn
nbsOtnpmThresholdsEsrSig=_NbsOtnpmThresholdsEsrSig_Object((1,3,6,1,4,1,629,222,1,1,1,11),_NbsOtnpmThresholdsEsrSig_Type())
nbsOtnpmThresholdsEsrSig.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsEsrSig.setStatus(_A)
class _NbsOtnpmThresholdsEsrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmThresholdsEsrExp_Type.__name__=_D
_NbsOtnpmThresholdsEsrExp_Object=MibTableColumn
nbsOtnpmThresholdsEsrExp=_NbsOtnpmThresholdsEsrExp_Object((1,3,6,1,4,1,629,222,1,1,1,12),_NbsOtnpmThresholdsEsrExp_Type())
nbsOtnpmThresholdsEsrExp.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsEsrExp.setStatus(_A)
_NbsOtnpmThresholdsSes_Type=Unsigned32
_NbsOtnpmThresholdsSes_Object=MibTableColumn
nbsOtnpmThresholdsSes=_NbsOtnpmThresholdsSes_Object((1,3,6,1,4,1,629,222,1,1,1,13),_NbsOtnpmThresholdsSes_Type())
nbsOtnpmThresholdsSes.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsSes.setStatus(_A)
class _NbsOtnpmThresholdsSesrSig_Type(Integer32):defaultValue=0
_NbsOtnpmThresholdsSesrSig_Type.__name__=_D
_NbsOtnpmThresholdsSesrSig_Object=MibTableColumn
nbsOtnpmThresholdsSesrSig=_NbsOtnpmThresholdsSesrSig_Object((1,3,6,1,4,1,629,222,1,1,1,14),_NbsOtnpmThresholdsSesrSig_Type())
nbsOtnpmThresholdsSesrSig.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsSesrSig.setStatus(_A)
class _NbsOtnpmThresholdsSesrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmThresholdsSesrExp_Type.__name__=_D
_NbsOtnpmThresholdsSesrExp_Object=MibTableColumn
nbsOtnpmThresholdsSesrExp=_NbsOtnpmThresholdsSesrExp_Object((1,3,6,1,4,1,629,222,1,1,1,15),_NbsOtnpmThresholdsSesrExp_Type())
nbsOtnpmThresholdsSesrExp.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsSesrExp.setStatus(_A)
_NbsOtnpmThresholdsBbe_Type=WritableU64
_NbsOtnpmThresholdsBbe_Object=MibTableColumn
nbsOtnpmThresholdsBbe=_NbsOtnpmThresholdsBbe_Object((1,3,6,1,4,1,629,222,1,1,1,16),_NbsOtnpmThresholdsBbe_Type())
nbsOtnpmThresholdsBbe.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsBbe.setStatus(_A)
class _NbsOtnpmThresholdsBberSig_Type(Integer32):defaultValue=0
_NbsOtnpmThresholdsBberSig_Type.__name__=_D
_NbsOtnpmThresholdsBberSig_Object=MibTableColumn
nbsOtnpmThresholdsBberSig=_NbsOtnpmThresholdsBberSig_Object((1,3,6,1,4,1,629,222,1,1,1,17),_NbsOtnpmThresholdsBberSig_Type())
nbsOtnpmThresholdsBberSig.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsBberSig.setStatus(_A)
class _NbsOtnpmThresholdsBberExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmThresholdsBberExp_Type.__name__=_D
_NbsOtnpmThresholdsBberExp_Object=MibTableColumn
nbsOtnpmThresholdsBberExp=_NbsOtnpmThresholdsBberExp_Object((1,3,6,1,4,1,629,222,1,1,1,18),_NbsOtnpmThresholdsBberExp_Type())
nbsOtnpmThresholdsBberExp.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsBberExp.setStatus(_A)
_NbsOtnpmThresholdsUas_Type=Unsigned32
_NbsOtnpmThresholdsUas_Object=MibTableColumn
nbsOtnpmThresholdsUas=_NbsOtnpmThresholdsUas_Object((1,3,6,1,4,1,629,222,1,1,1,19),_NbsOtnpmThresholdsUas_Type())
nbsOtnpmThresholdsUas.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsUas.setStatus(_A)
_NbsOtnpmThresholdsFc_Type=WritableU64
_NbsOtnpmThresholdsFc_Object=MibTableColumn
nbsOtnpmThresholdsFc=_NbsOtnpmThresholdsFc_Object((1,3,6,1,4,1,629,222,1,1,1,20),_NbsOtnpmThresholdsFc_Type())
nbsOtnpmThresholdsFc.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnpmThresholdsFc.setStatus(_A)
_NbsOtnpmCurrentGrp_ObjectIdentity=ObjectIdentity
nbsOtnpmCurrentGrp=_NbsOtnpmCurrentGrp_ObjectIdentity((1,3,6,1,4,1,629,222,2))
if mibBuilder.loadTexts:nbsOtnpmCurrentGrp.setStatus(_A)
_NbsOtnpmCurrentTable_Object=MibTable
nbsOtnpmCurrentTable=_NbsOtnpmCurrentTable_Object((1,3,6,1,4,1,629,222,2,3))
if mibBuilder.loadTexts:nbsOtnpmCurrentTable.setStatus(_A)
_NbsOtnpmCurrentEntry_Object=MibTableRow
nbsOtnpmCurrentEntry=_NbsOtnpmCurrentEntry_Object((1,3,6,1,4,1,629,222,2,3,1))
nbsOtnpmCurrentEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:nbsOtnpmCurrentEntry.setStatus(_A)
_NbsOtnpmCurrentIfIndex_Type=InterfaceIndex
_NbsOtnpmCurrentIfIndex_Object=MibTableColumn
nbsOtnpmCurrentIfIndex=_NbsOtnpmCurrentIfIndex_Object((1,3,6,1,4,1,629,222,2,3,1,1),_NbsOtnpmCurrentIfIndex_Type())
nbsOtnpmCurrentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentIfIndex.setStatus(_A)
class _NbsOtnpmCurrentInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_NbsOtnpmCurrentInterval_Type.__name__=_D
_NbsOtnpmCurrentInterval_Object=MibTableColumn
nbsOtnpmCurrentInterval=_NbsOtnpmCurrentInterval_Object((1,3,6,1,4,1,629,222,2,3,1,2),_NbsOtnpmCurrentInterval_Type())
nbsOtnpmCurrentInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentInterval.setStatus(_A)
class _NbsOtnpmCurrentScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8)))
_NbsOtnpmCurrentScope_Type.__name__=_D
_NbsOtnpmCurrentScope_Object=MibTableColumn
nbsOtnpmCurrentScope=_NbsOtnpmCurrentScope_Object((1,3,6,1,4,1,629,222,2,3,1,3),_NbsOtnpmCurrentScope_Type())
nbsOtnpmCurrentScope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentScope.setStatus(_A)
_NbsOtnpmCurrentDate_Type=Integer32
_NbsOtnpmCurrentDate_Object=MibTableColumn
nbsOtnpmCurrentDate=_NbsOtnpmCurrentDate_Object((1,3,6,1,4,1,629,222,2,3,1,5),_NbsOtnpmCurrentDate_Type())
nbsOtnpmCurrentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentDate.setStatus(_A)
_NbsOtnpmCurrentTime_Type=Integer32
_NbsOtnpmCurrentTime_Object=MibTableColumn
nbsOtnpmCurrentTime=_NbsOtnpmCurrentTime_Object((1,3,6,1,4,1,629,222,2,3,1,6),_NbsOtnpmCurrentTime_Type())
nbsOtnpmCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentTime.setStatus(_A)
_NbsOtnpmCurrentEs_Type=Unsigned32
_NbsOtnpmCurrentEs_Object=MibTableColumn
nbsOtnpmCurrentEs=_NbsOtnpmCurrentEs_Object((1,3,6,1,4,1,629,222,2,3,1,10),_NbsOtnpmCurrentEs_Type())
nbsOtnpmCurrentEs.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentEs.setStatus(_A)
class _NbsOtnpmCurrentEsrSig_Type(Integer32):defaultValue=0
_NbsOtnpmCurrentEsrSig_Type.__name__=_D
_NbsOtnpmCurrentEsrSig_Object=MibTableColumn
nbsOtnpmCurrentEsrSig=_NbsOtnpmCurrentEsrSig_Object((1,3,6,1,4,1,629,222,2,3,1,11),_NbsOtnpmCurrentEsrSig_Type())
nbsOtnpmCurrentEsrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentEsrSig.setStatus(_A)
class _NbsOtnpmCurrentEsrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmCurrentEsrExp_Type.__name__=_D
_NbsOtnpmCurrentEsrExp_Object=MibTableColumn
nbsOtnpmCurrentEsrExp=_NbsOtnpmCurrentEsrExp_Object((1,3,6,1,4,1,629,222,2,3,1,12),_NbsOtnpmCurrentEsrExp_Type())
nbsOtnpmCurrentEsrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentEsrExp.setStatus(_A)
_NbsOtnpmCurrentSes_Type=Unsigned32
_NbsOtnpmCurrentSes_Object=MibTableColumn
nbsOtnpmCurrentSes=_NbsOtnpmCurrentSes_Object((1,3,6,1,4,1,629,222,2,3,1,13),_NbsOtnpmCurrentSes_Type())
nbsOtnpmCurrentSes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentSes.setStatus(_A)
class _NbsOtnpmCurrentSesrSig_Type(Integer32):defaultValue=0
_NbsOtnpmCurrentSesrSig_Type.__name__=_D
_NbsOtnpmCurrentSesrSig_Object=MibTableColumn
nbsOtnpmCurrentSesrSig=_NbsOtnpmCurrentSesrSig_Object((1,3,6,1,4,1,629,222,2,3,1,14),_NbsOtnpmCurrentSesrSig_Type())
nbsOtnpmCurrentSesrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentSesrSig.setStatus(_A)
class _NbsOtnpmCurrentSesrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmCurrentSesrExp_Type.__name__=_D
_NbsOtnpmCurrentSesrExp_Object=MibTableColumn
nbsOtnpmCurrentSesrExp=_NbsOtnpmCurrentSesrExp_Object((1,3,6,1,4,1,629,222,2,3,1,15),_NbsOtnpmCurrentSesrExp_Type())
nbsOtnpmCurrentSesrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentSesrExp.setStatus(_A)
_NbsOtnpmCurrentBbe_Type=Counter64
_NbsOtnpmCurrentBbe_Object=MibTableColumn
nbsOtnpmCurrentBbe=_NbsOtnpmCurrentBbe_Object((1,3,6,1,4,1,629,222,2,3,1,16),_NbsOtnpmCurrentBbe_Type())
nbsOtnpmCurrentBbe.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentBbe.setStatus(_A)
class _NbsOtnpmCurrentBberSig_Type(Integer32):defaultValue=0
_NbsOtnpmCurrentBberSig_Type.__name__=_D
_NbsOtnpmCurrentBberSig_Object=MibTableColumn
nbsOtnpmCurrentBberSig=_NbsOtnpmCurrentBberSig_Object((1,3,6,1,4,1,629,222,2,3,1,17),_NbsOtnpmCurrentBberSig_Type())
nbsOtnpmCurrentBberSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentBberSig.setStatus(_A)
class _NbsOtnpmCurrentBberExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmCurrentBberExp_Type.__name__=_D
_NbsOtnpmCurrentBberExp_Object=MibTableColumn
nbsOtnpmCurrentBberExp=_NbsOtnpmCurrentBberExp_Object((1,3,6,1,4,1,629,222,2,3,1,18),_NbsOtnpmCurrentBberExp_Type())
nbsOtnpmCurrentBberExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentBberExp.setStatus(_A)
_NbsOtnpmCurrentUas_Type=Unsigned32
_NbsOtnpmCurrentUas_Object=MibTableColumn
nbsOtnpmCurrentUas=_NbsOtnpmCurrentUas_Object((1,3,6,1,4,1,629,222,2,3,1,19),_NbsOtnpmCurrentUas_Type())
nbsOtnpmCurrentUas.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentUas.setStatus(_A)
_NbsOtnpmCurrentFc_Type=Counter64
_NbsOtnpmCurrentFc_Object=MibTableColumn
nbsOtnpmCurrentFc=_NbsOtnpmCurrentFc_Object((1,3,6,1,4,1,629,222,2,3,1,20),_NbsOtnpmCurrentFc_Type())
nbsOtnpmCurrentFc.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentFc.setStatus(_A)
_NbsOtnpmCurrentAlarmsSupported_Type=NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsSupported_Object=MibTableColumn
nbsOtnpmCurrentAlarmsSupported=_NbsOtnpmCurrentAlarmsSupported_Object((1,3,6,1,4,1,629,222,2,3,1,100),_NbsOtnpmCurrentAlarmsSupported_Type())
nbsOtnpmCurrentAlarmsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentAlarmsSupported.setStatus(_A)
_NbsOtnpmCurrentAlarmsRaised_Type=NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsRaised_Object=MibTableColumn
nbsOtnpmCurrentAlarmsRaised=_NbsOtnpmCurrentAlarmsRaised_Object((1,3,6,1,4,1,629,222,2,3,1,101),_NbsOtnpmCurrentAlarmsRaised_Type())
nbsOtnpmCurrentAlarmsRaised.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentAlarmsRaised.setStatus(_A)
_NbsOtnpmCurrentAlarmsChanged_Type=NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsChanged_Object=MibTableColumn
nbsOtnpmCurrentAlarmsChanged=_NbsOtnpmCurrentAlarmsChanged_Object((1,3,6,1,4,1,629,222,2,3,1,102),_NbsOtnpmCurrentAlarmsChanged_Type())
nbsOtnpmCurrentAlarmsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmCurrentAlarmsChanged.setStatus(_A)
_NbsOtnpmHistoricGrp_ObjectIdentity=ObjectIdentity
nbsOtnpmHistoricGrp=_NbsOtnpmHistoricGrp_ObjectIdentity((1,3,6,1,4,1,629,222,3))
if mibBuilder.loadTexts:nbsOtnpmHistoricGrp.setStatus(_A)
_NbsOtnpmHistoricTable_Object=MibTable
nbsOtnpmHistoricTable=_NbsOtnpmHistoricTable_Object((1,3,6,1,4,1,629,222,3,3))
if mibBuilder.loadTexts:nbsOtnpmHistoricTable.setStatus(_A)
_NbsOtnpmHistoricEntry_Object=MibTableRow
nbsOtnpmHistoricEntry=_NbsOtnpmHistoricEntry_Object((1,3,6,1,4,1,629,222,3,3,1))
nbsOtnpmHistoricEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:nbsOtnpmHistoricEntry.setStatus(_A)
_NbsOtnpmHistoricIfIndex_Type=InterfaceIndex
_NbsOtnpmHistoricIfIndex_Object=MibTableColumn
nbsOtnpmHistoricIfIndex=_NbsOtnpmHistoricIfIndex_Object((1,3,6,1,4,1,629,222,3,3,1,1),_NbsOtnpmHistoricIfIndex_Type())
nbsOtnpmHistoricIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricIfIndex.setStatus(_A)
class _NbsOtnpmHistoricInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_NbsOtnpmHistoricInterval_Type.__name__=_D
_NbsOtnpmHistoricInterval_Object=MibTableColumn
nbsOtnpmHistoricInterval=_NbsOtnpmHistoricInterval_Object((1,3,6,1,4,1,629,222,3,3,1,2),_NbsOtnpmHistoricInterval_Type())
nbsOtnpmHistoricInterval.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsOtnpmHistoricInterval.setStatus(_A)
class _NbsOtnpmHistoricScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8)))
_NbsOtnpmHistoricScope_Type.__name__=_D
_NbsOtnpmHistoricScope_Object=MibTableColumn
nbsOtnpmHistoricScope=_NbsOtnpmHistoricScope_Object((1,3,6,1,4,1,629,222,3,3,1,3),_NbsOtnpmHistoricScope_Type())
nbsOtnpmHistoricScope.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsOtnpmHistoricScope.setStatus(_A)
_NbsOtnpmHistoricSample_Type=Integer32
_NbsOtnpmHistoricSample_Object=MibTableColumn
nbsOtnpmHistoricSample=_NbsOtnpmHistoricSample_Object((1,3,6,1,4,1,629,222,3,3,1,4),_NbsOtnpmHistoricSample_Type())
nbsOtnpmHistoricSample.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsOtnpmHistoricSample.setStatus(_A)
_NbsOtnpmHistoricDate_Type=Integer32
_NbsOtnpmHistoricDate_Object=MibTableColumn
nbsOtnpmHistoricDate=_NbsOtnpmHistoricDate_Object((1,3,6,1,4,1,629,222,3,3,1,5),_NbsOtnpmHistoricDate_Type())
nbsOtnpmHistoricDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricDate.setStatus(_A)
_NbsOtnpmHistoricTime_Type=Integer32
_NbsOtnpmHistoricTime_Object=MibTableColumn
nbsOtnpmHistoricTime=_NbsOtnpmHistoricTime_Object((1,3,6,1,4,1,629,222,3,3,1,6),_NbsOtnpmHistoricTime_Type())
nbsOtnpmHistoricTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricTime.setStatus(_A)
_NbsOtnpmHistoricEs_Type=Unsigned32
_NbsOtnpmHistoricEs_Object=MibTableColumn
nbsOtnpmHistoricEs=_NbsOtnpmHistoricEs_Object((1,3,6,1,4,1,629,222,3,3,1,10),_NbsOtnpmHistoricEs_Type())
nbsOtnpmHistoricEs.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricEs.setStatus(_A)
class _NbsOtnpmHistoricEsrSig_Type(Integer32):defaultValue=0
_NbsOtnpmHistoricEsrSig_Type.__name__=_D
_NbsOtnpmHistoricEsrSig_Object=MibTableColumn
nbsOtnpmHistoricEsrSig=_NbsOtnpmHistoricEsrSig_Object((1,3,6,1,4,1,629,222,3,3,1,11),_NbsOtnpmHistoricEsrSig_Type())
nbsOtnpmHistoricEsrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricEsrSig.setStatus(_A)
class _NbsOtnpmHistoricEsrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmHistoricEsrExp_Type.__name__=_D
_NbsOtnpmHistoricEsrExp_Object=MibTableColumn
nbsOtnpmHistoricEsrExp=_NbsOtnpmHistoricEsrExp_Object((1,3,6,1,4,1,629,222,3,3,1,12),_NbsOtnpmHistoricEsrExp_Type())
nbsOtnpmHistoricEsrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricEsrExp.setStatus(_A)
_NbsOtnpmHistoricSes_Type=Unsigned32
_NbsOtnpmHistoricSes_Object=MibTableColumn
nbsOtnpmHistoricSes=_NbsOtnpmHistoricSes_Object((1,3,6,1,4,1,629,222,3,3,1,13),_NbsOtnpmHistoricSes_Type())
nbsOtnpmHistoricSes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricSes.setStatus(_A)
class _NbsOtnpmHistoricSesrSig_Type(Integer32):defaultValue=0
_NbsOtnpmHistoricSesrSig_Type.__name__=_D
_NbsOtnpmHistoricSesrSig_Object=MibTableColumn
nbsOtnpmHistoricSesrSig=_NbsOtnpmHistoricSesrSig_Object((1,3,6,1,4,1,629,222,3,3,1,14),_NbsOtnpmHistoricSesrSig_Type())
nbsOtnpmHistoricSesrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricSesrSig.setStatus(_A)
class _NbsOtnpmHistoricSesrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmHistoricSesrExp_Type.__name__=_D
_NbsOtnpmHistoricSesrExp_Object=MibTableColumn
nbsOtnpmHistoricSesrExp=_NbsOtnpmHistoricSesrExp_Object((1,3,6,1,4,1,629,222,3,3,1,15),_NbsOtnpmHistoricSesrExp_Type())
nbsOtnpmHistoricSesrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricSesrExp.setStatus(_A)
_NbsOtnpmHistoricBbe_Type=Counter64
_NbsOtnpmHistoricBbe_Object=MibTableColumn
nbsOtnpmHistoricBbe=_NbsOtnpmHistoricBbe_Object((1,3,6,1,4,1,629,222,3,3,1,16),_NbsOtnpmHistoricBbe_Type())
nbsOtnpmHistoricBbe.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricBbe.setStatus(_A)
class _NbsOtnpmHistoricBberSig_Type(Integer32):defaultValue=0
_NbsOtnpmHistoricBberSig_Type.__name__=_D
_NbsOtnpmHistoricBberSig_Object=MibTableColumn
nbsOtnpmHistoricBberSig=_NbsOtnpmHistoricBberSig_Object((1,3,6,1,4,1,629,222,3,3,1,17),_NbsOtnpmHistoricBberSig_Type())
nbsOtnpmHistoricBberSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricBberSig.setStatus(_A)
class _NbsOtnpmHistoricBberExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmHistoricBberExp_Type.__name__=_D
_NbsOtnpmHistoricBberExp_Object=MibTableColumn
nbsOtnpmHistoricBberExp=_NbsOtnpmHistoricBberExp_Object((1,3,6,1,4,1,629,222,3,3,1,18),_NbsOtnpmHistoricBberExp_Type())
nbsOtnpmHistoricBberExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricBberExp.setStatus(_A)
_NbsOtnpmHistoricUas_Type=Unsigned32
_NbsOtnpmHistoricUas_Object=MibTableColumn
nbsOtnpmHistoricUas=_NbsOtnpmHistoricUas_Object((1,3,6,1,4,1,629,222,3,3,1,19),_NbsOtnpmHistoricUas_Type())
nbsOtnpmHistoricUas.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricUas.setStatus(_A)
_NbsOtnpmHistoricFc_Type=Counter64
_NbsOtnpmHistoricFc_Object=MibTableColumn
nbsOtnpmHistoricFc=_NbsOtnpmHistoricFc_Object((1,3,6,1,4,1,629,222,3,3,1,20),_NbsOtnpmHistoricFc_Type())
nbsOtnpmHistoricFc.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricFc.setStatus(_A)
_NbsOtnpmHistoricAlarmsSupported_Type=NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsSupported_Object=MibTableColumn
nbsOtnpmHistoricAlarmsSupported=_NbsOtnpmHistoricAlarmsSupported_Object((1,3,6,1,4,1,629,222,3,3,1,100),_NbsOtnpmHistoricAlarmsSupported_Type())
nbsOtnpmHistoricAlarmsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricAlarmsSupported.setStatus(_A)
_NbsOtnpmHistoricAlarmsRaised_Type=NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsRaised_Object=MibTableColumn
nbsOtnpmHistoricAlarmsRaised=_NbsOtnpmHistoricAlarmsRaised_Object((1,3,6,1,4,1,629,222,3,3,1,101),_NbsOtnpmHistoricAlarmsRaised_Type())
nbsOtnpmHistoricAlarmsRaised.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricAlarmsRaised.setStatus(_A)
_NbsOtnpmHistoricAlarmsChanged_Type=NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsChanged_Object=MibTableColumn
nbsOtnpmHistoricAlarmsChanged=_NbsOtnpmHistoricAlarmsChanged_Object((1,3,6,1,4,1,629,222,3,3,1,102),_NbsOtnpmHistoricAlarmsChanged_Type())
nbsOtnpmHistoricAlarmsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmHistoricAlarmsChanged.setStatus(_A)
_NbsOtnpmRunningGrp_ObjectIdentity=ObjectIdentity
nbsOtnpmRunningGrp=_NbsOtnpmRunningGrp_ObjectIdentity((1,3,6,1,4,1,629,222,4))
if mibBuilder.loadTexts:nbsOtnpmRunningGrp.setStatus(_A)
_NbsOtnpmRunningTable_Object=MibTable
nbsOtnpmRunningTable=_NbsOtnpmRunningTable_Object((1,3,6,1,4,1,629,222,4,3))
if mibBuilder.loadTexts:nbsOtnpmRunningTable.setStatus(_A)
_NbsOtnpmRunningEntry_Object=MibTableRow
nbsOtnpmRunningEntry=_NbsOtnpmRunningEntry_Object((1,3,6,1,4,1,629,222,4,3,1))
nbsOtnpmRunningEntry.setIndexNames((0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:nbsOtnpmRunningEntry.setStatus(_A)
_NbsOtnpmRunningIfIndex_Type=InterfaceIndex
_NbsOtnpmRunningIfIndex_Object=MibTableColumn
nbsOtnpmRunningIfIndex=_NbsOtnpmRunningIfIndex_Object((1,3,6,1,4,1,629,222,4,3,1,1),_NbsOtnpmRunningIfIndex_Type())
nbsOtnpmRunningIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningIfIndex.setStatus(_A)
class _NbsOtnpmRunningScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8)))
_NbsOtnpmRunningScope_Type.__name__=_D
_NbsOtnpmRunningScope_Object=MibTableColumn
nbsOtnpmRunningScope=_NbsOtnpmRunningScope_Object((1,3,6,1,4,1,629,222,4,3,1,3),_NbsOtnpmRunningScope_Type())
nbsOtnpmRunningScope.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsOtnpmRunningScope.setStatus(_A)
_NbsOtnpmRunningDate_Type=Integer32
_NbsOtnpmRunningDate_Object=MibTableColumn
nbsOtnpmRunningDate=_NbsOtnpmRunningDate_Object((1,3,6,1,4,1,629,222,4,3,1,5),_NbsOtnpmRunningDate_Type())
nbsOtnpmRunningDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningDate.setStatus(_A)
_NbsOtnpmRunningTime_Type=Integer32
_NbsOtnpmRunningTime_Object=MibTableColumn
nbsOtnpmRunningTime=_NbsOtnpmRunningTime_Object((1,3,6,1,4,1,629,222,4,3,1,6),_NbsOtnpmRunningTime_Type())
nbsOtnpmRunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningTime.setStatus(_A)
_NbsOtnpmRunningEs_Type=Counter32
_NbsOtnpmRunningEs_Object=MibTableColumn
nbsOtnpmRunningEs=_NbsOtnpmRunningEs_Object((1,3,6,1,4,1,629,222,4,3,1,10),_NbsOtnpmRunningEs_Type())
nbsOtnpmRunningEs.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningEs.setStatus(_A)
class _NbsOtnpmRunningEsrSig_Type(Integer32):defaultValue=0
_NbsOtnpmRunningEsrSig_Type.__name__=_D
_NbsOtnpmRunningEsrSig_Object=MibTableColumn
nbsOtnpmRunningEsrSig=_NbsOtnpmRunningEsrSig_Object((1,3,6,1,4,1,629,222,4,3,1,11),_NbsOtnpmRunningEsrSig_Type())
nbsOtnpmRunningEsrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningEsrSig.setStatus(_A)
class _NbsOtnpmRunningEsrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmRunningEsrExp_Type.__name__=_D
_NbsOtnpmRunningEsrExp_Object=MibTableColumn
nbsOtnpmRunningEsrExp=_NbsOtnpmRunningEsrExp_Object((1,3,6,1,4,1,629,222,4,3,1,12),_NbsOtnpmRunningEsrExp_Type())
nbsOtnpmRunningEsrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningEsrExp.setStatus(_A)
_NbsOtnpmRunningSes_Type=Counter32
_NbsOtnpmRunningSes_Object=MibTableColumn
nbsOtnpmRunningSes=_NbsOtnpmRunningSes_Object((1,3,6,1,4,1,629,222,4,3,1,13),_NbsOtnpmRunningSes_Type())
nbsOtnpmRunningSes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningSes.setStatus(_A)
class _NbsOtnpmRunningSesrSig_Type(Integer32):defaultValue=0
_NbsOtnpmRunningSesrSig_Type.__name__=_D
_NbsOtnpmRunningSesrSig_Object=MibTableColumn
nbsOtnpmRunningSesrSig=_NbsOtnpmRunningSesrSig_Object((1,3,6,1,4,1,629,222,4,3,1,14),_NbsOtnpmRunningSesrSig_Type())
nbsOtnpmRunningSesrSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningSesrSig.setStatus(_A)
class _NbsOtnpmRunningSesrExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmRunningSesrExp_Type.__name__=_D
_NbsOtnpmRunningSesrExp_Object=MibTableColumn
nbsOtnpmRunningSesrExp=_NbsOtnpmRunningSesrExp_Object((1,3,6,1,4,1,629,222,4,3,1,15),_NbsOtnpmRunningSesrExp_Type())
nbsOtnpmRunningSesrExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningSesrExp.setStatus(_A)
_NbsOtnpmRunningBbe_Type=Counter64
_NbsOtnpmRunningBbe_Object=MibTableColumn
nbsOtnpmRunningBbe=_NbsOtnpmRunningBbe_Object((1,3,6,1,4,1,629,222,4,3,1,16),_NbsOtnpmRunningBbe_Type())
nbsOtnpmRunningBbe.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningBbe.setStatus(_A)
class _NbsOtnpmRunningBberSig_Type(Integer32):defaultValue=0
_NbsOtnpmRunningBberSig_Type.__name__=_D
_NbsOtnpmRunningBberSig_Object=MibTableColumn
nbsOtnpmRunningBberSig=_NbsOtnpmRunningBberSig_Object((1,3,6,1,4,1,629,222,4,3,1,17),_NbsOtnpmRunningBberSig_Type())
nbsOtnpmRunningBberSig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningBberSig.setStatus(_A)
class _NbsOtnpmRunningBberExp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsOtnpmRunningBberExp_Type.__name__=_D
_NbsOtnpmRunningBberExp_Object=MibTableColumn
nbsOtnpmRunningBberExp=_NbsOtnpmRunningBberExp_Object((1,3,6,1,4,1,629,222,4,3,1,18),_NbsOtnpmRunningBberExp_Type())
nbsOtnpmRunningBberExp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningBberExp.setStatus(_A)
_NbsOtnpmRunningUas_Type=Counter32
_NbsOtnpmRunningUas_Object=MibTableColumn
nbsOtnpmRunningUas=_NbsOtnpmRunningUas_Object((1,3,6,1,4,1,629,222,4,3,1,19),_NbsOtnpmRunningUas_Type())
nbsOtnpmRunningUas.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningUas.setStatus(_A)
_NbsOtnpmRunningFc_Type=Counter64
_NbsOtnpmRunningFc_Object=MibTableColumn
nbsOtnpmRunningFc=_NbsOtnpmRunningFc_Object((1,3,6,1,4,1,629,222,4,3,1,20),_NbsOtnpmRunningFc_Type())
nbsOtnpmRunningFc.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningFc.setStatus(_A)
_NbsOtnpmRunningAlarmsSupported_Type=NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsSupported_Object=MibTableColumn
nbsOtnpmRunningAlarmsSupported=_NbsOtnpmRunningAlarmsSupported_Object((1,3,6,1,4,1,629,222,4,3,1,100),_NbsOtnpmRunningAlarmsSupported_Type())
nbsOtnpmRunningAlarmsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningAlarmsSupported.setStatus(_A)
_NbsOtnpmRunningAlarmsRaised_Type=NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsRaised_Object=MibTableColumn
nbsOtnpmRunningAlarmsRaised=_NbsOtnpmRunningAlarmsRaised_Object((1,3,6,1,4,1,629,222,4,3,1,101),_NbsOtnpmRunningAlarmsRaised_Type())
nbsOtnpmRunningAlarmsRaised.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningAlarmsRaised.setStatus(_A)
_NbsOtnpmRunningAlarmsChanged_Type=NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsChanged_Object=MibTableColumn
nbsOtnpmRunningAlarmsChanged=_NbsOtnpmRunningAlarmsChanged_Object((1,3,6,1,4,1,629,222,4,3,1,102),_NbsOtnpmRunningAlarmsChanged_Type())
nbsOtnpmRunningAlarmsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnpmRunningAlarmsChanged.setStatus(_A)
_NbsOtnAlarmsGrp_ObjectIdentity=ObjectIdentity
nbsOtnAlarmsGrp=_NbsOtnAlarmsGrp_ObjectIdentity((1,3,6,1,4,1,629,222,80))
if mibBuilder.loadTexts:nbsOtnAlarmsGrp.setStatus(_A)
_NbsOtnAlarmsTable_Object=MibTable
nbsOtnAlarmsTable=_NbsOtnAlarmsTable_Object((1,3,6,1,4,1,629,222,80,3))
if mibBuilder.loadTexts:nbsOtnAlarmsTable.setStatus(_A)
_NbsOtnAlarmsEntry_Object=MibTableRow
nbsOtnAlarmsEntry=_NbsOtnAlarmsEntry_Object((1,3,6,1,4,1,629,222,80,3,1))
nbsOtnAlarmsEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:nbsOtnAlarmsEntry.setStatus(_A)
_NbsOtnAlarmsIfIndex_Type=InterfaceIndex
_NbsOtnAlarmsIfIndex_Object=MibTableColumn
nbsOtnAlarmsIfIndex=_NbsOtnAlarmsIfIndex_Object((1,3,6,1,4,1,629,222,80,3,1,1),_NbsOtnAlarmsIfIndex_Type())
nbsOtnAlarmsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsIfIndex.setStatus(_A)
_NbsOtnAlarmsDate_Type=Integer32
_NbsOtnAlarmsDate_Object=MibTableColumn
nbsOtnAlarmsDate=_NbsOtnAlarmsDate_Object((1,3,6,1,4,1,629,222,80,3,1,5),_NbsOtnAlarmsDate_Type())
nbsOtnAlarmsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsDate.setStatus(_A)
_NbsOtnAlarmsTime_Type=Integer32
_NbsOtnAlarmsTime_Object=MibTableColumn
nbsOtnAlarmsTime=_NbsOtnAlarmsTime_Object((1,3,6,1,4,1,629,222,80,3,1,6),_NbsOtnAlarmsTime_Type())
nbsOtnAlarmsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsTime.setStatus(_A)
_NbsOtnAlarmsSpan_Type=Integer32
_NbsOtnAlarmsSpan_Object=MibTableColumn
nbsOtnAlarmsSpan=_NbsOtnAlarmsSpan_Object((1,3,6,1,4,1,629,222,80,3,1,7),_NbsOtnAlarmsSpan_Type())
nbsOtnAlarmsSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsSpan.setStatus(_A)
class _NbsOtnAlarmsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('monitoring',2),(_h,3)))
_NbsOtnAlarmsState_Type.__name__=_D
_NbsOtnAlarmsState_Object=MibTableColumn
nbsOtnAlarmsState=_NbsOtnAlarmsState_Object((1,3,6,1,4,1,629,222,80,3,1,8),_NbsOtnAlarmsState_Type())
nbsOtnAlarmsState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnAlarmsState.setStatus(_A)
_NbsOtnAlarmsSupported_Type=NbsOtnAlarmMask
_NbsOtnAlarmsSupported_Object=MibTableColumn
nbsOtnAlarmsSupported=_NbsOtnAlarmsSupported_Object((1,3,6,1,4,1,629,222,80,3,1,100),_NbsOtnAlarmsSupported_Type())
nbsOtnAlarmsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsSupported.setStatus(_A)
_NbsOtnAlarmsRaised_Type=NbsOtnAlarmMask
_NbsOtnAlarmsRaised_Object=MibTableColumn
nbsOtnAlarmsRaised=_NbsOtnAlarmsRaised_Object((1,3,6,1,4,1,629,222,80,3,1,101),_NbsOtnAlarmsRaised_Type())
nbsOtnAlarmsRaised.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsRaised.setStatus(_A)
_NbsOtnAlarmsChanged_Type=NbsOtnAlarmMask
_NbsOtnAlarmsChanged_Object=MibTableColumn
nbsOtnAlarmsChanged=_NbsOtnAlarmsChanged_Object((1,3,6,1,4,1,629,222,80,3,1,102),_NbsOtnAlarmsChanged_Type())
nbsOtnAlarmsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsChanged.setStatus(_A)
class _NbsOtnAlarmsRcvdFTFL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NbsOtnAlarmsRcvdFTFL_Type.__name__=_V
_NbsOtnAlarmsRcvdFTFL_Object=MibTableColumn
nbsOtnAlarmsRcvdFTFL=_NbsOtnAlarmsRcvdFTFL_Object((1,3,6,1,4,1,629,222,80,3,1,110),_NbsOtnAlarmsRcvdFTFL_Type())
nbsOtnAlarmsRcvdFTFL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnAlarmsRcvdFTFL.setStatus(_A)
_NbsOtnStatsGrp_ObjectIdentity=ObjectIdentity
nbsOtnStatsGrp=_NbsOtnStatsGrp_ObjectIdentity((1,3,6,1,4,1,629,222,90))
if mibBuilder.loadTexts:nbsOtnStatsGrp.setStatus(_A)
_NbsOtnStatsTable_Object=MibTable
nbsOtnStatsTable=_NbsOtnStatsTable_Object((1,3,6,1,4,1,629,222,90,3))
if mibBuilder.loadTexts:nbsOtnStatsTable.setStatus(_A)
_NbsOtnStatsEntry_Object=MibTableRow
nbsOtnStatsEntry=_NbsOtnStatsEntry_Object((1,3,6,1,4,1,629,222,90,3,1))
nbsOtnStatsEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:nbsOtnStatsEntry.setStatus(_A)
_NbsOtnStatsIfIndex_Type=InterfaceIndex
_NbsOtnStatsIfIndex_Object=MibTableColumn
nbsOtnStatsIfIndex=_NbsOtnStatsIfIndex_Object((1,3,6,1,4,1,629,222,90,3,1,1),_NbsOtnStatsIfIndex_Type())
nbsOtnStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsIfIndex.setStatus(_A)
_NbsOtnStatsDate_Type=Integer32
_NbsOtnStatsDate_Object=MibTableColumn
nbsOtnStatsDate=_NbsOtnStatsDate_Object((1,3,6,1,4,1,629,222,90,3,1,5),_NbsOtnStatsDate_Type())
nbsOtnStatsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsDate.setStatus(_A)
_NbsOtnStatsTime_Type=Integer32
_NbsOtnStatsTime_Object=MibTableColumn
nbsOtnStatsTime=_NbsOtnStatsTime_Object((1,3,6,1,4,1,629,222,90,3,1,6),_NbsOtnStatsTime_Type())
nbsOtnStatsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsTime.setStatus(_A)
_NbsOtnStatsSpan_Type=Integer32
_NbsOtnStatsSpan_Object=MibTableColumn
nbsOtnStatsSpan=_NbsOtnStatsSpan_Object((1,3,6,1,4,1,629,222,90,3,1,7),_NbsOtnStatsSpan_Type())
nbsOtnStatsSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsSpan.setStatus(_A)
class _NbsOtnStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_g,1),('counting',2),(_h,3),('stopped',4)))
_NbsOtnStatsState_Type.__name__=_D
_NbsOtnStatsState_Object=MibTableColumn
nbsOtnStatsState=_NbsOtnStatsState_Object((1,3,6,1,4,1,629,222,90,3,1,8),_NbsOtnStatsState_Type())
nbsOtnStatsState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsOtnStatsState.setStatus(_A)
_NbsOtnStatsErrCntSectBEI_Type=Counter64
_NbsOtnStatsErrCntSectBEI_Object=MibTableColumn
nbsOtnStatsErrCntSectBEI=_NbsOtnStatsErrCntSectBEI_Object((1,3,6,1,4,1,629,222,90,3,1,21),_NbsOtnStatsErrCntSectBEI_Type())
nbsOtnStatsErrCntSectBEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntSectBEI.setStatus(_A)
_NbsOtnStatsErrCntPathBEI_Type=Counter64
_NbsOtnStatsErrCntPathBEI_Object=MibTableColumn
nbsOtnStatsErrCntPathBEI=_NbsOtnStatsErrCntPathBEI_Object((1,3,6,1,4,1,629,222,90,3,1,22),_NbsOtnStatsErrCntPathBEI_Type())
nbsOtnStatsErrCntPathBEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntPathBEI.setStatus(_A)
_NbsOtnStatsErrCntTcm1BEI_Type=Counter64
_NbsOtnStatsErrCntTcm1BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm1BEI=_NbsOtnStatsErrCntTcm1BEI_Object((1,3,6,1,4,1,629,222,90,3,1,23),_NbsOtnStatsErrCntTcm1BEI_Type())
nbsOtnStatsErrCntTcm1BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm1BEI.setStatus(_A)
_NbsOtnStatsErrCntTcm2BEI_Type=Counter64
_NbsOtnStatsErrCntTcm2BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm2BEI=_NbsOtnStatsErrCntTcm2BEI_Object((1,3,6,1,4,1,629,222,90,3,1,24),_NbsOtnStatsErrCntTcm2BEI_Type())
nbsOtnStatsErrCntTcm2BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm2BEI.setStatus(_A)
_NbsOtnStatsErrCntTcm3BEI_Type=Counter64
_NbsOtnStatsErrCntTcm3BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm3BEI=_NbsOtnStatsErrCntTcm3BEI_Object((1,3,6,1,4,1,629,222,90,3,1,25),_NbsOtnStatsErrCntTcm3BEI_Type())
nbsOtnStatsErrCntTcm3BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm3BEI.setStatus(_A)
_NbsOtnStatsErrCntTcm4BEI_Type=Counter64
_NbsOtnStatsErrCntTcm4BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm4BEI=_NbsOtnStatsErrCntTcm4BEI_Object((1,3,6,1,4,1,629,222,90,3,1,26),_NbsOtnStatsErrCntTcm4BEI_Type())
nbsOtnStatsErrCntTcm4BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm4BEI.setStatus(_A)
_NbsOtnStatsErrCntTcm5BEI_Type=Counter64
_NbsOtnStatsErrCntTcm5BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm5BEI=_NbsOtnStatsErrCntTcm5BEI_Object((1,3,6,1,4,1,629,222,90,3,1,27),_NbsOtnStatsErrCntTcm5BEI_Type())
nbsOtnStatsErrCntTcm5BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm5BEI.setStatus(_A)
_NbsOtnStatsErrCntTcm6BEI_Type=Counter64
_NbsOtnStatsErrCntTcm6BEI_Object=MibTableColumn
nbsOtnStatsErrCntTcm6BEI=_NbsOtnStatsErrCntTcm6BEI_Object((1,3,6,1,4,1,629,222,90,3,1,28),_NbsOtnStatsErrCntTcm6BEI_Type())
nbsOtnStatsErrCntTcm6BEI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm6BEI.setStatus(_A)
_NbsOtnStatsErrCntSectBIP8_Type=Counter64
_NbsOtnStatsErrCntSectBIP8_Object=MibTableColumn
nbsOtnStatsErrCntSectBIP8=_NbsOtnStatsErrCntSectBIP8_Object((1,3,6,1,4,1,629,222,90,3,1,31),_NbsOtnStatsErrCntSectBIP8_Type())
nbsOtnStatsErrCntSectBIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntSectBIP8.setStatus(_A)
_NbsOtnStatsErrCntPathBIP8_Type=Counter64
_NbsOtnStatsErrCntPathBIP8_Object=MibTableColumn
nbsOtnStatsErrCntPathBIP8=_NbsOtnStatsErrCntPathBIP8_Object((1,3,6,1,4,1,629,222,90,3,1,32),_NbsOtnStatsErrCntPathBIP8_Type())
nbsOtnStatsErrCntPathBIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntPathBIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm1BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm1BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm1BIP8=_NbsOtnStatsErrCntTcm1BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,33),_NbsOtnStatsErrCntTcm1BIP8_Type())
nbsOtnStatsErrCntTcm1BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm1BIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm2BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm2BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm2BIP8=_NbsOtnStatsErrCntTcm2BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,34),_NbsOtnStatsErrCntTcm2BIP8_Type())
nbsOtnStatsErrCntTcm2BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm2BIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm3BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm3BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm3BIP8=_NbsOtnStatsErrCntTcm3BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,35),_NbsOtnStatsErrCntTcm3BIP8_Type())
nbsOtnStatsErrCntTcm3BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm3BIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm4BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm4BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm4BIP8=_NbsOtnStatsErrCntTcm4BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,36),_NbsOtnStatsErrCntTcm4BIP8_Type())
nbsOtnStatsErrCntTcm4BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm4BIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm5BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm5BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm5BIP8=_NbsOtnStatsErrCntTcm5BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,37),_NbsOtnStatsErrCntTcm5BIP8_Type())
nbsOtnStatsErrCntTcm5BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm5BIP8.setStatus(_A)
_NbsOtnStatsErrCntTcm6BIP8_Type=Counter64
_NbsOtnStatsErrCntTcm6BIP8_Object=MibTableColumn
nbsOtnStatsErrCntTcm6BIP8=_NbsOtnStatsErrCntTcm6BIP8_Object((1,3,6,1,4,1,629,222,90,3,1,38),_NbsOtnStatsErrCntTcm6BIP8_Type())
nbsOtnStatsErrCntTcm6BIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsErrCntTcm6BIP8.setStatus(_A)
_NbsOtnStatsAlarmsSupported_Type=NbsOtnAlarmMask
_NbsOtnStatsAlarmsSupported_Object=MibTableColumn
nbsOtnStatsAlarmsSupported=_NbsOtnStatsAlarmsSupported_Object((1,3,6,1,4,1,629,222,90,3,1,100),_NbsOtnStatsAlarmsSupported_Type())
nbsOtnStatsAlarmsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsAlarmsSupported.setStatus(_A)
_NbsOtnStatsAlarmsRaised_Type=NbsOtnAlarmMask
_NbsOtnStatsAlarmsRaised_Object=MibTableColumn
nbsOtnStatsAlarmsRaised=_NbsOtnStatsAlarmsRaised_Object((1,3,6,1,4,1,629,222,90,3,1,101),_NbsOtnStatsAlarmsRaised_Type())
nbsOtnStatsAlarmsRaised.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsAlarmsRaised.setStatus(_A)
_NbsOtnStatsAlarmsChanged_Type=NbsOtnAlarmMask
_NbsOtnStatsAlarmsChanged_Object=MibTableColumn
nbsOtnStatsAlarmsChanged=_NbsOtnStatsAlarmsChanged_Object((1,3,6,1,4,1,629,222,90,3,1,102),_NbsOtnStatsAlarmsChanged_Type())
nbsOtnStatsAlarmsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsOtnStatsAlarmsChanged.setStatus(_A)
_NbsOtnpmEventsGrp_ObjectIdentity=ObjectIdentity
nbsOtnpmEventsGrp=_NbsOtnpmEventsGrp_ObjectIdentity((1,3,6,1,4,1,629,222,100))
if mibBuilder.loadTexts:nbsOtnpmEventsGrp.setStatus(_A)
_NbsOtnpmTraps_ObjectIdentity=ObjectIdentity
nbsOtnpmTraps=_NbsOtnpmTraps_ObjectIdentity((1,3,6,1,4,1,629,222,100,0))
if mibBuilder.loadTexts:nbsOtnpmTraps.setStatus(_A)
nbsOtnpmTrapsEs=NotificationType((1,3,6,1,4,1,629,222,100,0,10))
nbsOtnpmTrapsEs.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_j)))
if mibBuilder.loadTexts:nbsOtnpmTrapsEs.setStatus(_A)
nbsOtnpmTrapsEsr=NotificationType((1,3,6,1,4,1,629,222,100,0,11))
nbsOtnpmTrapsEsr.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_k),(_C,_l)))
if mibBuilder.loadTexts:nbsOtnpmTrapsEsr.setStatus(_A)
nbsOtnpmTrapsSes=NotificationType((1,3,6,1,4,1,629,222,100,0,12))
nbsOtnpmTrapsSes.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_m)))
if mibBuilder.loadTexts:nbsOtnpmTrapsSes.setStatus(_A)
nbsOtnpmTrapsSesr=NotificationType((1,3,6,1,4,1,629,222,100,0,13))
nbsOtnpmTrapsSesr.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_n),(_C,_o)))
if mibBuilder.loadTexts:nbsOtnpmTrapsSesr.setStatus(_A)
nbsOtnpmTrapsBbe=NotificationType((1,3,6,1,4,1,629,222,100,0,14))
nbsOtnpmTrapsBbe.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_p)))
if mibBuilder.loadTexts:nbsOtnpmTrapsBbe.setStatus(_A)
nbsOtnpmTrapsBber=NotificationType((1,3,6,1,4,1,629,222,100,0,15))
nbsOtnpmTrapsBber.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_q),(_C,_r)))
if mibBuilder.loadTexts:nbsOtnpmTrapsBber.setStatus(_A)
nbsOtnpmTrapsUas=NotificationType((1,3,6,1,4,1,629,222,100,0,16))
nbsOtnpmTrapsUas.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_s)))
if mibBuilder.loadTexts:nbsOtnpmTrapsUas.setStatus(_A)
nbsOtnpmTrapsFc=NotificationType((1,3,6,1,4,1,629,222,100,0,17))
nbsOtnpmTrapsFc.setObjects(*((_C,_F),(_I,_J),(_C,_G),(_C,_H),(_C,_t)))
if mibBuilder.loadTexts:nbsOtnpmTrapsFc.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'NbsOtnAlarmId':NbsOtnAlarmId,'NbsOtnAlarmMask':NbsOtnAlarmMask,'nbsOtnpmMib':nbsOtnpmMib,'nbsOtnpmThresholdsGrp':nbsOtnpmThresholdsGrp,'nbsOtnpmThresholdsTable':nbsOtnpmThresholdsTable,'nbsOtnpmThresholdsEntry':nbsOtnpmThresholdsEntry,_W:nbsOtnpmThresholdsIfIndex,_X:nbsOtnpmThresholdsInterval,_Y:nbsOtnpmThresholdsScope,'nbsOtnpmThresholdsEs':nbsOtnpmThresholdsEs,'nbsOtnpmThresholdsEsrSig':nbsOtnpmThresholdsEsrSig,'nbsOtnpmThresholdsEsrExp':nbsOtnpmThresholdsEsrExp,'nbsOtnpmThresholdsSes':nbsOtnpmThresholdsSes,'nbsOtnpmThresholdsSesrSig':nbsOtnpmThresholdsSesrSig,'nbsOtnpmThresholdsSesrExp':nbsOtnpmThresholdsSesrExp,'nbsOtnpmThresholdsBbe':nbsOtnpmThresholdsBbe,'nbsOtnpmThresholdsBberSig':nbsOtnpmThresholdsBberSig,'nbsOtnpmThresholdsBberExp':nbsOtnpmThresholdsBberExp,'nbsOtnpmThresholdsUas':nbsOtnpmThresholdsUas,'nbsOtnpmThresholdsFc':nbsOtnpmThresholdsFc,'nbsOtnpmCurrentGrp':nbsOtnpmCurrentGrp,'nbsOtnpmCurrentTable':nbsOtnpmCurrentTable,'nbsOtnpmCurrentEntry':nbsOtnpmCurrentEntry,_F:nbsOtnpmCurrentIfIndex,_G:nbsOtnpmCurrentInterval,_H:nbsOtnpmCurrentScope,'nbsOtnpmCurrentDate':nbsOtnpmCurrentDate,'nbsOtnpmCurrentTime':nbsOtnpmCurrentTime,_j:nbsOtnpmCurrentEs,_k:nbsOtnpmCurrentEsrSig,_l:nbsOtnpmCurrentEsrExp,_m:nbsOtnpmCurrentSes,_n:nbsOtnpmCurrentSesrSig,_o:nbsOtnpmCurrentSesrExp,_p:nbsOtnpmCurrentBbe,_q:nbsOtnpmCurrentBberSig,_r:nbsOtnpmCurrentBberExp,_s:nbsOtnpmCurrentUas,_t:nbsOtnpmCurrentFc,'nbsOtnpmCurrentAlarmsSupported':nbsOtnpmCurrentAlarmsSupported,'nbsOtnpmCurrentAlarmsRaised':nbsOtnpmCurrentAlarmsRaised,'nbsOtnpmCurrentAlarmsChanged':nbsOtnpmCurrentAlarmsChanged,'nbsOtnpmHistoricGrp':nbsOtnpmHistoricGrp,'nbsOtnpmHistoricTable':nbsOtnpmHistoricTable,'nbsOtnpmHistoricEntry':nbsOtnpmHistoricEntry,_Z:nbsOtnpmHistoricIfIndex,_a:nbsOtnpmHistoricInterval,_b:nbsOtnpmHistoricScope,_c:nbsOtnpmHistoricSample,'nbsOtnpmHistoricDate':nbsOtnpmHistoricDate,'nbsOtnpmHistoricTime':nbsOtnpmHistoricTime,'nbsOtnpmHistoricEs':nbsOtnpmHistoricEs,'nbsOtnpmHistoricEsrSig':nbsOtnpmHistoricEsrSig,'nbsOtnpmHistoricEsrExp':nbsOtnpmHistoricEsrExp,'nbsOtnpmHistoricSes':nbsOtnpmHistoricSes,'nbsOtnpmHistoricSesrSig':nbsOtnpmHistoricSesrSig,'nbsOtnpmHistoricSesrExp':nbsOtnpmHistoricSesrExp,'nbsOtnpmHistoricBbe':nbsOtnpmHistoricBbe,'nbsOtnpmHistoricBberSig':nbsOtnpmHistoricBberSig,'nbsOtnpmHistoricBberExp':nbsOtnpmHistoricBberExp,'nbsOtnpmHistoricUas':nbsOtnpmHistoricUas,'nbsOtnpmHistoricFc':nbsOtnpmHistoricFc,'nbsOtnpmHistoricAlarmsSupported':nbsOtnpmHistoricAlarmsSupported,'nbsOtnpmHistoricAlarmsRaised':nbsOtnpmHistoricAlarmsRaised,'nbsOtnpmHistoricAlarmsChanged':nbsOtnpmHistoricAlarmsChanged,'nbsOtnpmRunningGrp':nbsOtnpmRunningGrp,'nbsOtnpmRunningTable':nbsOtnpmRunningTable,'nbsOtnpmRunningEntry':nbsOtnpmRunningEntry,_d:nbsOtnpmRunningIfIndex,_e:nbsOtnpmRunningScope,'nbsOtnpmRunningDate':nbsOtnpmRunningDate,'nbsOtnpmRunningTime':nbsOtnpmRunningTime,'nbsOtnpmRunningEs':nbsOtnpmRunningEs,'nbsOtnpmRunningEsrSig':nbsOtnpmRunningEsrSig,'nbsOtnpmRunningEsrExp':nbsOtnpmRunningEsrExp,'nbsOtnpmRunningSes':nbsOtnpmRunningSes,'nbsOtnpmRunningSesrSig':nbsOtnpmRunningSesrSig,'nbsOtnpmRunningSesrExp':nbsOtnpmRunningSesrExp,'nbsOtnpmRunningBbe':nbsOtnpmRunningBbe,'nbsOtnpmRunningBberSig':nbsOtnpmRunningBberSig,'nbsOtnpmRunningBberExp':nbsOtnpmRunningBberExp,'nbsOtnpmRunningUas':nbsOtnpmRunningUas,'nbsOtnpmRunningFc':nbsOtnpmRunningFc,'nbsOtnpmRunningAlarmsSupported':nbsOtnpmRunningAlarmsSupported,'nbsOtnpmRunningAlarmsRaised':nbsOtnpmRunningAlarmsRaised,'nbsOtnpmRunningAlarmsChanged':nbsOtnpmRunningAlarmsChanged,'nbsOtnAlarmsGrp':nbsOtnAlarmsGrp,'nbsOtnAlarmsTable':nbsOtnAlarmsTable,'nbsOtnAlarmsEntry':nbsOtnAlarmsEntry,_f:nbsOtnAlarmsIfIndex,'nbsOtnAlarmsDate':nbsOtnAlarmsDate,'nbsOtnAlarmsTime':nbsOtnAlarmsTime,'nbsOtnAlarmsSpan':nbsOtnAlarmsSpan,'nbsOtnAlarmsState':nbsOtnAlarmsState,'nbsOtnAlarmsSupported':nbsOtnAlarmsSupported,'nbsOtnAlarmsRaised':nbsOtnAlarmsRaised,'nbsOtnAlarmsChanged':nbsOtnAlarmsChanged,'nbsOtnAlarmsRcvdFTFL':nbsOtnAlarmsRcvdFTFL,'nbsOtnStatsGrp':nbsOtnStatsGrp,'nbsOtnStatsTable':nbsOtnStatsTable,'nbsOtnStatsEntry':nbsOtnStatsEntry,_i:nbsOtnStatsIfIndex,'nbsOtnStatsDate':nbsOtnStatsDate,'nbsOtnStatsTime':nbsOtnStatsTime,'nbsOtnStatsSpan':nbsOtnStatsSpan,'nbsOtnStatsState':nbsOtnStatsState,'nbsOtnStatsErrCntSectBEI':nbsOtnStatsErrCntSectBEI,'nbsOtnStatsErrCntPathBEI':nbsOtnStatsErrCntPathBEI,'nbsOtnStatsErrCntTcm1BEI':nbsOtnStatsErrCntTcm1BEI,'nbsOtnStatsErrCntTcm2BEI':nbsOtnStatsErrCntTcm2BEI,'nbsOtnStatsErrCntTcm3BEI':nbsOtnStatsErrCntTcm3BEI,'nbsOtnStatsErrCntTcm4BEI':nbsOtnStatsErrCntTcm4BEI,'nbsOtnStatsErrCntTcm5BEI':nbsOtnStatsErrCntTcm5BEI,'nbsOtnStatsErrCntTcm6BEI':nbsOtnStatsErrCntTcm6BEI,'nbsOtnStatsErrCntSectBIP8':nbsOtnStatsErrCntSectBIP8,'nbsOtnStatsErrCntPathBIP8':nbsOtnStatsErrCntPathBIP8,'nbsOtnStatsErrCntTcm1BIP8':nbsOtnStatsErrCntTcm1BIP8,'nbsOtnStatsErrCntTcm2BIP8':nbsOtnStatsErrCntTcm2BIP8,'nbsOtnStatsErrCntTcm3BIP8':nbsOtnStatsErrCntTcm3BIP8,'nbsOtnStatsErrCntTcm4BIP8':nbsOtnStatsErrCntTcm4BIP8,'nbsOtnStatsErrCntTcm5BIP8':nbsOtnStatsErrCntTcm5BIP8,'nbsOtnStatsErrCntTcm6BIP8':nbsOtnStatsErrCntTcm6BIP8,'nbsOtnStatsAlarmsSupported':nbsOtnStatsAlarmsSupported,'nbsOtnStatsAlarmsRaised':nbsOtnStatsAlarmsRaised,'nbsOtnStatsAlarmsChanged':nbsOtnStatsAlarmsChanged,'nbsOtnpmEventsGrp':nbsOtnpmEventsGrp,'nbsOtnpmTraps':nbsOtnpmTraps,'nbsOtnpmTrapsEs':nbsOtnpmTrapsEs,'nbsOtnpmTrapsEsr':nbsOtnpmTrapsEsr,'nbsOtnpmTrapsSes':nbsOtnpmTrapsSes,'nbsOtnpmTrapsSesr':nbsOtnpmTrapsSesr,'nbsOtnpmTrapsBbe':nbsOtnpmTrapsBbe,'nbsOtnpmTrapsBber':nbsOtnpmTrapsBber,'nbsOtnpmTrapsUas':nbsOtnpmTrapsUas,'nbsOtnpmTrapsFc':nbsOtnpmTrapsFc})