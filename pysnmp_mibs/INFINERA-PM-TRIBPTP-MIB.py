_AF='tribPtpPmRealGroup'
_AE='tribPtpPmGroup'
_AD='tribPtpPmRealTomOprTotal'
_AC='tribPtpPmRealTomOptTotal'
_AB='tribPtpPmRealTomOpr04'
_AA='tribPtpPmRealTomOpt04'
_A9='tribPtpPmRealTomTxLBC04'
_A8='tribPtpPmRealTomOpr03'
_A7='tribPtpPmRealTomOpt03'
_A6='tribPtpPmRealTomTxLBC03'
_A5='tribPtpPmRealTomOpr02'
_A4='tribPtpPmRealTomOpt02'
_A3='tribPtpPmRealTomTxLBC02'
_A2='tribPtpPmRealTomOpr'
_A1='tribPtpPmRealTomOpt'
_A0='tribPtpPmRealTomTxLBC'
_z='tribPtpPmTomOprTotalAve'
_y='tribPtpPmTomOprTotalMax'
_x='tribPtpPmTomOprTotalMin'
_w='tribPtpPmTomOptTotalAve'
_v='tribPtpPmTomOptTotalMax'
_u='tribPtpPmTomOptTotalMin'
_t='tribPtpPmTomOpr04Ave'
_s='tribPtpPmTomOpr04Max'
_r='tribPtpPmTomOpr04Min'
_q='tribPtpPmTomOpt04Ave'
_p='tribPtpPmTomOpt04Max'
_o='tribPtpPmTomOpt04Min'
_n='tribPtpPmTomTxLBC04Ave'
_m='tribPtpPmTomTxLBC04Max'
_l='tribPtpPmTomTxLBC04Min'
_k='tribPtpPmTomOpr03Ave'
_j='tribPtpPmTomOpr03Max'
_i='tribPtpPmTomOpr03Min'
_h='tribPtpPmTomOpt03Ave'
_g='tribPtpPmTomOpt03Max'
_f='tribPtpPmTomOpt03Min'
_e='tribPtpPmTomTxLBC03Ave'
_d='tribPtpPmTomTxLBC03Max'
_c='tribPtpPmTomTxLBC03Min'
_b='tribPtpPmTomOpr02Ave'
_a='tribPtpPmTomOpr02Max'
_Z='tribPtpPmTomOpr02Min'
_Y='tribPtpPmTomOpt02Ave'
_X='tribPtpPmTomOpt02Max'
_W='tribPtpPmTomOpt02Min'
_V='tribPtpPmTomTxLBC02Ave'
_U='tribPtpPmTomTxLBC02Max'
_T='tribPtpPmTomTxLBC02Min'
_S='tribPtpPmTomOprAve'
_R='tribPtpPmTomOprMax'
_Q='tribPtpPmTomOprMin'
_P='tribPtpPmTomOptAve'
_O='tribPtpPmTomOptMax'
_N='tribPtpPmTomOptMin'
_M='tribPtpPmTomTxLBCAve'
_L='tribPtpPmTomTxLBCMax'
_K='tribPtpPmTomTxLBCMin'
_J='tribPtpPmValidity'
_I='not-accessible'
_H='tribPtpPmTimestamp'
_G='tribPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-TRIBPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
commonPerfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonPerfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tribPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,11,3))
if mibBuilder.loadTexts:tribPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_TribPtpPmRealTable_Object=MibTable
tribPtpPmRealTable=_TribPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1))
if mibBuilder.loadTexts:tribPtpPmRealTable.setStatus(_A)
_TribPtpPmRealEntry_Object=MibTableRow
tribPtpPmRealEntry=_TribPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1))
tribPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tribPtpPmRealEntry.setStatus(_A)
_TribPtpPmRealTomTxLBC_Type=FloatHundredths
_TribPtpPmRealTomTxLBC_Object=MibTableColumn
tribPtpPmRealTomTxLBC=_TribPtpPmRealTomTxLBC_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,1),_TribPtpPmRealTomTxLBC_Type())
tribPtpPmRealTomTxLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomTxLBC.setStatus(_A)
_TribPtpPmRealTomOpt_Type=FloatHundredths
_TribPtpPmRealTomOpt_Object=MibTableColumn
tribPtpPmRealTomOpt=_TribPtpPmRealTomOpt_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,2),_TribPtpPmRealTomOpt_Type())
tribPtpPmRealTomOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpt.setStatus(_A)
_TribPtpPmRealTomOpr_Type=FloatHundredths
_TribPtpPmRealTomOpr_Object=MibTableColumn
tribPtpPmRealTomOpr=_TribPtpPmRealTomOpr_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,3),_TribPtpPmRealTomOpr_Type())
tribPtpPmRealTomOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpr.setStatus(_A)
_TribPtpPmRealTomTxLBC02_Type=FloatHundredths
_TribPtpPmRealTomTxLBC02_Object=MibTableColumn
tribPtpPmRealTomTxLBC02=_TribPtpPmRealTomTxLBC02_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,4),_TribPtpPmRealTomTxLBC02_Type())
tribPtpPmRealTomTxLBC02.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomTxLBC02.setStatus(_A)
_TribPtpPmRealTomOpt02_Type=FloatHundredths
_TribPtpPmRealTomOpt02_Object=MibTableColumn
tribPtpPmRealTomOpt02=_TribPtpPmRealTomOpt02_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,5),_TribPtpPmRealTomOpt02_Type())
tribPtpPmRealTomOpt02.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpt02.setStatus(_A)
_TribPtpPmRealTomOpr02_Type=FloatHundredths
_TribPtpPmRealTomOpr02_Object=MibTableColumn
tribPtpPmRealTomOpr02=_TribPtpPmRealTomOpr02_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,6),_TribPtpPmRealTomOpr02_Type())
tribPtpPmRealTomOpr02.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpr02.setStatus(_A)
_TribPtpPmRealTomTxLBC03_Type=FloatHundredths
_TribPtpPmRealTomTxLBC03_Object=MibTableColumn
tribPtpPmRealTomTxLBC03=_TribPtpPmRealTomTxLBC03_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,7),_TribPtpPmRealTomTxLBC03_Type())
tribPtpPmRealTomTxLBC03.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomTxLBC03.setStatus(_A)
_TribPtpPmRealTomOpt03_Type=FloatHundredths
_TribPtpPmRealTomOpt03_Object=MibTableColumn
tribPtpPmRealTomOpt03=_TribPtpPmRealTomOpt03_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,8),_TribPtpPmRealTomOpt03_Type())
tribPtpPmRealTomOpt03.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpt03.setStatus(_A)
_TribPtpPmRealTomOpr03_Type=FloatHundredths
_TribPtpPmRealTomOpr03_Object=MibTableColumn
tribPtpPmRealTomOpr03=_TribPtpPmRealTomOpr03_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,9),_TribPtpPmRealTomOpr03_Type())
tribPtpPmRealTomOpr03.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpr03.setStatus(_A)
_TribPtpPmRealTomTxLBC04_Type=FloatHundredths
_TribPtpPmRealTomTxLBC04_Object=MibTableColumn
tribPtpPmRealTomTxLBC04=_TribPtpPmRealTomTxLBC04_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,10),_TribPtpPmRealTomTxLBC04_Type())
tribPtpPmRealTomTxLBC04.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomTxLBC04.setStatus(_A)
_TribPtpPmRealTomOpt04_Type=FloatHundredths
_TribPtpPmRealTomOpt04_Object=MibTableColumn
tribPtpPmRealTomOpt04=_TribPtpPmRealTomOpt04_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,11),_TribPtpPmRealTomOpt04_Type())
tribPtpPmRealTomOpt04.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpt04.setStatus(_A)
_TribPtpPmRealTomOpr04_Type=FloatHundredths
_TribPtpPmRealTomOpr04_Object=MibTableColumn
tribPtpPmRealTomOpr04=_TribPtpPmRealTomOpr04_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,12),_TribPtpPmRealTomOpr04_Type())
tribPtpPmRealTomOpr04.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOpr04.setStatus(_A)
_TribPtpPmRealTomOptTotal_Type=FloatHundredths
_TribPtpPmRealTomOptTotal_Object=MibTableColumn
tribPtpPmRealTomOptTotal=_TribPtpPmRealTomOptTotal_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,13),_TribPtpPmRealTomOptTotal_Type())
tribPtpPmRealTomOptTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOptTotal.setStatus(_A)
_TribPtpPmRealTomOprTotal_Type=FloatHundredths
_TribPtpPmRealTomOprTotal_Object=MibTableColumn
tribPtpPmRealTomOprTotal=_TribPtpPmRealTomOprTotal_Object((1,3,6,1,4,1,21296,2,2,1,11,3,1,1,14),_TribPtpPmRealTomOprTotal_Type())
tribPtpPmRealTomOprTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmRealTomOprTotal.setStatus(_A)
_TribPtpPmTable_Object=MibTable
tribPtpPmTable=_TribPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2))
if mibBuilder.loadTexts:tribPtpPmTable.setStatus(_A)
_TribPtpPmEntry_Object=MibTableRow
tribPtpPmEntry=_TribPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1))
tribPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tribPtpPmEntry.setStatus(_A)
class _TribPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TribPtpPmTimestamp_Type.__name__=_F
_TribPtpPmTimestamp_Object=MibTableColumn
tribPtpPmTimestamp=_TribPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,1),_TribPtpPmTimestamp_Type())
tribPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:tribPtpPmTimestamp.setStatus(_A)
class _TribPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_TribPtpPmSampleDuration_Type.__name__=_F
_TribPtpPmSampleDuration_Object=MibTableColumn
tribPtpPmSampleDuration=_TribPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,2),_TribPtpPmSampleDuration_Type())
tribPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:tribPtpPmSampleDuration.setStatus(_A)
_TribPtpPmValidity_Type=TruthValue
_TribPtpPmValidity_Object=MibTableColumn
tribPtpPmValidity=_TribPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,3),_TribPtpPmValidity_Type())
tribPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmValidity.setStatus(_A)
_TribPtpPmTomTxLBCMin_Type=FloatHundredths
_TribPtpPmTomTxLBCMin_Object=MibTableColumn
tribPtpPmTomTxLBCMin=_TribPtpPmTomTxLBCMin_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,4),_TribPtpPmTomTxLBCMin_Type())
tribPtpPmTomTxLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBCMin.setStatus(_A)
_TribPtpPmTomTxLBCMax_Type=FloatHundredths
_TribPtpPmTomTxLBCMax_Object=MibTableColumn
tribPtpPmTomTxLBCMax=_TribPtpPmTomTxLBCMax_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,5),_TribPtpPmTomTxLBCMax_Type())
tribPtpPmTomTxLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBCMax.setStatus(_A)
_TribPtpPmTomTxLBCAve_Type=FloatHundredths
_TribPtpPmTomTxLBCAve_Object=MibTableColumn
tribPtpPmTomTxLBCAve=_TribPtpPmTomTxLBCAve_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,6),_TribPtpPmTomTxLBCAve_Type())
tribPtpPmTomTxLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBCAve.setStatus(_A)
_TribPtpPmTomOptMin_Type=FloatHundredths
_TribPtpPmTomOptMin_Object=MibTableColumn
tribPtpPmTomOptMin=_TribPtpPmTomOptMin_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,7),_TribPtpPmTomOptMin_Type())
tribPtpPmTomOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptMin.setStatus(_A)
_TribPtpPmTomOptMax_Type=FloatHundredths
_TribPtpPmTomOptMax_Object=MibTableColumn
tribPtpPmTomOptMax=_TribPtpPmTomOptMax_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,8),_TribPtpPmTomOptMax_Type())
tribPtpPmTomOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptMax.setStatus(_A)
_TribPtpPmTomOptAve_Type=FloatHundredths
_TribPtpPmTomOptAve_Object=MibTableColumn
tribPtpPmTomOptAve=_TribPtpPmTomOptAve_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,9),_TribPtpPmTomOptAve_Type())
tribPtpPmTomOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptAve.setStatus(_A)
_TribPtpPmTomOprMin_Type=FloatHundredths
_TribPtpPmTomOprMin_Object=MibTableColumn
tribPtpPmTomOprMin=_TribPtpPmTomOprMin_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,10),_TribPtpPmTomOprMin_Type())
tribPtpPmTomOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprMin.setStatus(_A)
_TribPtpPmTomOprMax_Type=FloatHundredths
_TribPtpPmTomOprMax_Object=MibTableColumn
tribPtpPmTomOprMax=_TribPtpPmTomOprMax_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,11),_TribPtpPmTomOprMax_Type())
tribPtpPmTomOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprMax.setStatus(_A)
_TribPtpPmTomOprAve_Type=FloatHundredths
_TribPtpPmTomOprAve_Object=MibTableColumn
tribPtpPmTomOprAve=_TribPtpPmTomOprAve_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,12),_TribPtpPmTomOprAve_Type())
tribPtpPmTomOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprAve.setStatus(_A)
_TribPtpPmTomTxLBC02Min_Type=FloatHundredths
_TribPtpPmTomTxLBC02Min_Object=MibTableColumn
tribPtpPmTomTxLBC02Min=_TribPtpPmTomTxLBC02Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,13),_TribPtpPmTomTxLBC02Min_Type())
tribPtpPmTomTxLBC02Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC02Min.setStatus(_A)
_TribPtpPmTomTxLBC02Max_Type=FloatHundredths
_TribPtpPmTomTxLBC02Max_Object=MibTableColumn
tribPtpPmTomTxLBC02Max=_TribPtpPmTomTxLBC02Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,14),_TribPtpPmTomTxLBC02Max_Type())
tribPtpPmTomTxLBC02Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC02Max.setStatus(_A)
_TribPtpPmTomTxLBC02Ave_Type=FloatHundredths
_TribPtpPmTomTxLBC02Ave_Object=MibTableColumn
tribPtpPmTomTxLBC02Ave=_TribPtpPmTomTxLBC02Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,15),_TribPtpPmTomTxLBC02Ave_Type())
tribPtpPmTomTxLBC02Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC02Ave.setStatus(_A)
_TribPtpPmTomOpt02Min_Type=FloatHundredths
_TribPtpPmTomOpt02Min_Object=MibTableColumn
tribPtpPmTomOpt02Min=_TribPtpPmTomOpt02Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,16),_TribPtpPmTomOpt02Min_Type())
tribPtpPmTomOpt02Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt02Min.setStatus(_A)
_TribPtpPmTomOpt02Max_Type=FloatHundredths
_TribPtpPmTomOpt02Max_Object=MibTableColumn
tribPtpPmTomOpt02Max=_TribPtpPmTomOpt02Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,17),_TribPtpPmTomOpt02Max_Type())
tribPtpPmTomOpt02Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt02Max.setStatus(_A)
_TribPtpPmTomOpt02Ave_Type=FloatHundredths
_TribPtpPmTomOpt02Ave_Object=MibTableColumn
tribPtpPmTomOpt02Ave=_TribPtpPmTomOpt02Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,18),_TribPtpPmTomOpt02Ave_Type())
tribPtpPmTomOpt02Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt02Ave.setStatus(_A)
_TribPtpPmTomOpr02Min_Type=FloatHundredths
_TribPtpPmTomOpr02Min_Object=MibTableColumn
tribPtpPmTomOpr02Min=_TribPtpPmTomOpr02Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,19),_TribPtpPmTomOpr02Min_Type())
tribPtpPmTomOpr02Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr02Min.setStatus(_A)
_TribPtpPmTomOpr02Max_Type=FloatHundredths
_TribPtpPmTomOpr02Max_Object=MibTableColumn
tribPtpPmTomOpr02Max=_TribPtpPmTomOpr02Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,20),_TribPtpPmTomOpr02Max_Type())
tribPtpPmTomOpr02Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr02Max.setStatus(_A)
_TribPtpPmTomOpr02Ave_Type=FloatHundredths
_TribPtpPmTomOpr02Ave_Object=MibTableColumn
tribPtpPmTomOpr02Ave=_TribPtpPmTomOpr02Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,21),_TribPtpPmTomOpr02Ave_Type())
tribPtpPmTomOpr02Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr02Ave.setStatus(_A)
_TribPtpPmTomTxLBC03Min_Type=FloatHundredths
_TribPtpPmTomTxLBC03Min_Object=MibTableColumn
tribPtpPmTomTxLBC03Min=_TribPtpPmTomTxLBC03Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,22),_TribPtpPmTomTxLBC03Min_Type())
tribPtpPmTomTxLBC03Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC03Min.setStatus(_A)
_TribPtpPmTomTxLBC03Max_Type=FloatHundredths
_TribPtpPmTomTxLBC03Max_Object=MibTableColumn
tribPtpPmTomTxLBC03Max=_TribPtpPmTomTxLBC03Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,23),_TribPtpPmTomTxLBC03Max_Type())
tribPtpPmTomTxLBC03Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC03Max.setStatus(_A)
_TribPtpPmTomTxLBC03Ave_Type=FloatHundredths
_TribPtpPmTomTxLBC03Ave_Object=MibTableColumn
tribPtpPmTomTxLBC03Ave=_TribPtpPmTomTxLBC03Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,24),_TribPtpPmTomTxLBC03Ave_Type())
tribPtpPmTomTxLBC03Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC03Ave.setStatus(_A)
_TribPtpPmTomOpt03Min_Type=FloatHundredths
_TribPtpPmTomOpt03Min_Object=MibTableColumn
tribPtpPmTomOpt03Min=_TribPtpPmTomOpt03Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,25),_TribPtpPmTomOpt03Min_Type())
tribPtpPmTomOpt03Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt03Min.setStatus(_A)
_TribPtpPmTomOpt03Max_Type=FloatHundredths
_TribPtpPmTomOpt03Max_Object=MibTableColumn
tribPtpPmTomOpt03Max=_TribPtpPmTomOpt03Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,26),_TribPtpPmTomOpt03Max_Type())
tribPtpPmTomOpt03Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt03Max.setStatus(_A)
_TribPtpPmTomOpt03Ave_Type=FloatHundredths
_TribPtpPmTomOpt03Ave_Object=MibTableColumn
tribPtpPmTomOpt03Ave=_TribPtpPmTomOpt03Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,27),_TribPtpPmTomOpt03Ave_Type())
tribPtpPmTomOpt03Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt03Ave.setStatus(_A)
_TribPtpPmTomOpr03Min_Type=FloatHundredths
_TribPtpPmTomOpr03Min_Object=MibTableColumn
tribPtpPmTomOpr03Min=_TribPtpPmTomOpr03Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,28),_TribPtpPmTomOpr03Min_Type())
tribPtpPmTomOpr03Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr03Min.setStatus(_A)
_TribPtpPmTomOpr03Max_Type=FloatHundredths
_TribPtpPmTomOpr03Max_Object=MibTableColumn
tribPtpPmTomOpr03Max=_TribPtpPmTomOpr03Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,29),_TribPtpPmTomOpr03Max_Type())
tribPtpPmTomOpr03Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr03Max.setStatus(_A)
_TribPtpPmTomOpr03Ave_Type=FloatHundredths
_TribPtpPmTomOpr03Ave_Object=MibTableColumn
tribPtpPmTomOpr03Ave=_TribPtpPmTomOpr03Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,30),_TribPtpPmTomOpr03Ave_Type())
tribPtpPmTomOpr03Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr03Ave.setStatus(_A)
_TribPtpPmTomTxLBC04Min_Type=FloatHundredths
_TribPtpPmTomTxLBC04Min_Object=MibTableColumn
tribPtpPmTomTxLBC04Min=_TribPtpPmTomTxLBC04Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,31),_TribPtpPmTomTxLBC04Min_Type())
tribPtpPmTomTxLBC04Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC04Min.setStatus(_A)
_TribPtpPmTomTxLBC04Max_Type=FloatHundredths
_TribPtpPmTomTxLBC04Max_Object=MibTableColumn
tribPtpPmTomTxLBC04Max=_TribPtpPmTomTxLBC04Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,32),_TribPtpPmTomTxLBC04Max_Type())
tribPtpPmTomTxLBC04Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC04Max.setStatus(_A)
_TribPtpPmTomTxLBC04Ave_Type=FloatHundredths
_TribPtpPmTomTxLBC04Ave_Object=MibTableColumn
tribPtpPmTomTxLBC04Ave=_TribPtpPmTomTxLBC04Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,33),_TribPtpPmTomTxLBC04Ave_Type())
tribPtpPmTomTxLBC04Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomTxLBC04Ave.setStatus(_A)
_TribPtpPmTomOpt04Min_Type=FloatHundredths
_TribPtpPmTomOpt04Min_Object=MibTableColumn
tribPtpPmTomOpt04Min=_TribPtpPmTomOpt04Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,34),_TribPtpPmTomOpt04Min_Type())
tribPtpPmTomOpt04Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt04Min.setStatus(_A)
_TribPtpPmTomOpt04Max_Type=FloatHundredths
_TribPtpPmTomOpt04Max_Object=MibTableColumn
tribPtpPmTomOpt04Max=_TribPtpPmTomOpt04Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,35),_TribPtpPmTomOpt04Max_Type())
tribPtpPmTomOpt04Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt04Max.setStatus(_A)
_TribPtpPmTomOpt04Ave_Type=FloatHundredths
_TribPtpPmTomOpt04Ave_Object=MibTableColumn
tribPtpPmTomOpt04Ave=_TribPtpPmTomOpt04Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,36),_TribPtpPmTomOpt04Ave_Type())
tribPtpPmTomOpt04Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpt04Ave.setStatus(_A)
_TribPtpPmTomOpr04Min_Type=FloatHundredths
_TribPtpPmTomOpr04Min_Object=MibTableColumn
tribPtpPmTomOpr04Min=_TribPtpPmTomOpr04Min_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,37),_TribPtpPmTomOpr04Min_Type())
tribPtpPmTomOpr04Min.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr04Min.setStatus(_A)
_TribPtpPmTomOpr04Max_Type=FloatHundredths
_TribPtpPmTomOpr04Max_Object=MibTableColumn
tribPtpPmTomOpr04Max=_TribPtpPmTomOpr04Max_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,38),_TribPtpPmTomOpr04Max_Type())
tribPtpPmTomOpr04Max.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr04Max.setStatus(_A)
_TribPtpPmTomOpr04Ave_Type=FloatHundredths
_TribPtpPmTomOpr04Ave_Object=MibTableColumn
tribPtpPmTomOpr04Ave=_TribPtpPmTomOpr04Ave_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,39),_TribPtpPmTomOpr04Ave_Type())
tribPtpPmTomOpr04Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOpr04Ave.setStatus(_A)
_TribPtpPmTomOptTotalMin_Type=FloatHundredths
_TribPtpPmTomOptTotalMin_Object=MibTableColumn
tribPtpPmTomOptTotalMin=_TribPtpPmTomOptTotalMin_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,40),_TribPtpPmTomOptTotalMin_Type())
tribPtpPmTomOptTotalMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptTotalMin.setStatus(_A)
_TribPtpPmTomOptTotalMax_Type=FloatHundredths
_TribPtpPmTomOptTotalMax_Object=MibTableColumn
tribPtpPmTomOptTotalMax=_TribPtpPmTomOptTotalMax_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,41),_TribPtpPmTomOptTotalMax_Type())
tribPtpPmTomOptTotalMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptTotalMax.setStatus(_A)
_TribPtpPmTomOptTotalAve_Type=FloatHundredths
_TribPtpPmTomOptTotalAve_Object=MibTableColumn
tribPtpPmTomOptTotalAve=_TribPtpPmTomOptTotalAve_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,42),_TribPtpPmTomOptTotalAve_Type())
tribPtpPmTomOptTotalAve.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOptTotalAve.setStatus(_A)
_TribPtpPmTomOprTotalMin_Type=FloatHundredths
_TribPtpPmTomOprTotalMin_Object=MibTableColumn
tribPtpPmTomOprTotalMin=_TribPtpPmTomOprTotalMin_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,43),_TribPtpPmTomOprTotalMin_Type())
tribPtpPmTomOprTotalMin.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprTotalMin.setStatus(_A)
_TribPtpPmTomOprTotalMax_Type=FloatHundredths
_TribPtpPmTomOprTotalMax_Object=MibTableColumn
tribPtpPmTomOprTotalMax=_TribPtpPmTomOprTotalMax_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,44),_TribPtpPmTomOprTotalMax_Type())
tribPtpPmTomOprTotalMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprTotalMax.setStatus(_A)
_TribPtpPmTomOprTotalAve_Type=FloatHundredths
_TribPtpPmTomOprTotalAve_Object=MibTableColumn
tribPtpPmTomOprTotalAve=_TribPtpPmTomOprTotalAve_Object((1,3,6,1,4,1,21296,2,2,1,11,3,2,1,45),_TribPtpPmTomOprTotalAve_Type())
tribPtpPmTomOprTotalAve.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPmTomOprTotalAve.setStatus(_A)
_TribPtpPmConformance_ObjectIdentity=ObjectIdentity
tribPtpPmConformance=_TribPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,3,3))
_TribPtpPmCompliances_ObjectIdentity=ObjectIdentity
tribPtpPmCompliances=_TribPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,3,3,1))
_TribPtpPmGroups_ObjectIdentity=ObjectIdentity
tribPtpPmGroups=_TribPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,11,3,3,2))
tribPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,3,3,2,1))
tribPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:tribPtpPmGroup.setStatus(_A)
tribPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,11,3,3,2,2))
tribPtpPmRealGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:tribPtpPmRealGroup.setStatus(_A)
tribPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,3,3,1,1))
tribPtpPmCompliance.setObjects((_B,_AE))
if mibBuilder.loadTexts:tribPtpPmCompliance.setStatus(_A)
tribPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,11,3,3,1,2))
tribPtpPmRealCompliance.setObjects((_B,_AF))
if mibBuilder.loadTexts:tribPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tribPtpPmMIB':tribPtpPmMIB,'tribPtpPmRealTable':tribPtpPmRealTable,'tribPtpPmRealEntry':tribPtpPmRealEntry,_A0:tribPtpPmRealTomTxLBC,_A1:tribPtpPmRealTomOpt,_A2:tribPtpPmRealTomOpr,_A3:tribPtpPmRealTomTxLBC02,_A4:tribPtpPmRealTomOpt02,_A5:tribPtpPmRealTomOpr02,_A6:tribPtpPmRealTomTxLBC03,_A7:tribPtpPmRealTomOpt03,_A8:tribPtpPmRealTomOpr03,_A9:tribPtpPmRealTomTxLBC04,_AA:tribPtpPmRealTomOpt04,_AB:tribPtpPmRealTomOpr04,_AC:tribPtpPmRealTomOptTotal,_AD:tribPtpPmRealTomOprTotal,'tribPtpPmTable':tribPtpPmTable,'tribPtpPmEntry':tribPtpPmEntry,_H:tribPtpPmTimestamp,_G:tribPtpPmSampleDuration,_J:tribPtpPmValidity,_K:tribPtpPmTomTxLBCMin,_L:tribPtpPmTomTxLBCMax,_M:tribPtpPmTomTxLBCAve,_N:tribPtpPmTomOptMin,_O:tribPtpPmTomOptMax,_P:tribPtpPmTomOptAve,_Q:tribPtpPmTomOprMin,_R:tribPtpPmTomOprMax,_S:tribPtpPmTomOprAve,_T:tribPtpPmTomTxLBC02Min,_U:tribPtpPmTomTxLBC02Max,_V:tribPtpPmTomTxLBC02Ave,_W:tribPtpPmTomOpt02Min,_X:tribPtpPmTomOpt02Max,_Y:tribPtpPmTomOpt02Ave,_Z:tribPtpPmTomOpr02Min,_a:tribPtpPmTomOpr02Max,_b:tribPtpPmTomOpr02Ave,_c:tribPtpPmTomTxLBC03Min,_d:tribPtpPmTomTxLBC03Max,_e:tribPtpPmTomTxLBC03Ave,_f:tribPtpPmTomOpt03Min,_g:tribPtpPmTomOpt03Max,_h:tribPtpPmTomOpt03Ave,_i:tribPtpPmTomOpr03Min,_j:tribPtpPmTomOpr03Max,_k:tribPtpPmTomOpr03Ave,_l:tribPtpPmTomTxLBC04Min,_m:tribPtpPmTomTxLBC04Max,_n:tribPtpPmTomTxLBC04Ave,_o:tribPtpPmTomOpt04Min,_p:tribPtpPmTomOpt04Max,_q:tribPtpPmTomOpt04Ave,_r:tribPtpPmTomOpr04Min,_s:tribPtpPmTomOpr04Max,_t:tribPtpPmTomOpr04Ave,_u:tribPtpPmTomOptTotalMin,_v:tribPtpPmTomOptTotalMax,_w:tribPtpPmTomOptTotalAve,_x:tribPtpPmTomOprTotalMin,_y:tribPtpPmTomOprTotalMax,_z:tribPtpPmTomOprTotalAve,'tribPtpPmConformance':tribPtpPmConformance,'tribPtpPmCompliances':tribPtpPmCompliances,'tribPtpPmCompliance':tribPtpPmCompliance,'tribPtpPmRealCompliance':tribPtpPmRealCompliance,'tribPtpPmGroups':tribPtpPmGroups,_AE:tribPtpPmGroup,_AF:tribPtpPmRealGroup})