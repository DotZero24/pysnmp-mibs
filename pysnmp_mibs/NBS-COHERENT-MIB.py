_A4='nbsCohpmCurrentMaxSOP'
_A3='nbsCohpmCurrentMinSOP'
_A2='nbsCohpmCurrentAveSOP'
_A1='nbsCohpmCurrentMaxPDL'
_A0='nbsCohpmCurrentMinPDL'
_z='nbsCohpmCurrentAvePDL'
_y='nbsCohpmCurrentMaxSNRy'
_x='nbsCohpmCurrentMinSNRy'
_w='nbsCohpmCurrentAveSNRy'
_v='nbsCohpmCurrentMaxSNRx'
_u='nbsCohpmCurrentMinSNRx'
_t='nbsCohpmCurrentAveSNRx'
_s='nbsCohpmCurrentMaxOSNR'
_r='nbsCohpmCurrentMinOSNR'
_q='nbsCohpmCurrentAveOSNR'
_p='nbsCohpmCurrentMaxCFO'
_o='nbsCohpmCurrentMinCFO'
_n='nbsCohpmCurrentAveCFO'
_m='nbsCohpmCurrentMaxQ'
_l='nbsCohpmCurrentMinQ'
_k='nbsCohpmCurrentAveQ'
_j='nbsCohpmCurrentMaxDGD'
_i='nbsCohpmCurrentMinDGD'
_h='nbsCohpmCurrentAveDGD'
_g='nbsCohpmCurrentMaxCD'
_f='nbsCohpmCurrentMinCD'
_e='nbsCohpmCurrentAveCD'
_d='nbsCohpmCurrentMaxNetBERexp'
_c='nbsCohpmCurrentMaxNetBERsig'
_b='nbsCohpmCurrentMinNetBERexp'
_a='nbsCohpmCurrentMinNetBERsig'
_Z='nbsCohpmCurrentAveNetBERexp'
_Y='nbsCohpmCurrentAveNetBERsig'
_X='nbsCoherentStatsIfIndex'
_W='nbsCohpmRunningIfIndex'
_V='not-accessible'
_U='nbsCohpmHistoricSample'
_T='nbsCohpmHistoricInterval'
_S='nbsCohpmHistoricIfIndex'
_R='nbsCohpmThresholdsInterval'
_Q='nbsCohpmThresholdsIfIndex'
_P='enhanced'
_O='standard'
_N='disable'
_M='nbsCoherentCfgIfIndex'
_L='OctetString'
_K='twentyfourHour'
_J='quarterHour'
_I='notSupported'
_H='nbsCohpmCurrentInterval'
_G='nbsCohpmCurrentIfIndex'
_F='read-write'
_E='Integer32'
_D='NBS-COHERENT-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsCoherentMib=ModuleIdentity((1,3,6,1,4,1,629,242))
_NbsCoherentCfgGrp_ObjectIdentity=ObjectIdentity
nbsCoherentCfgGrp=_NbsCoherentCfgGrp_ObjectIdentity((1,3,6,1,4,1,629,242,10))
if mibBuilder.loadTexts:nbsCoherentCfgGrp.setStatus(_A)
_NbsCoherentCfgTable_Object=MibTable
nbsCoherentCfgTable=_NbsCoherentCfgTable_Object((1,3,6,1,4,1,629,242,10,2))
if mibBuilder.loadTexts:nbsCoherentCfgTable.setStatus(_A)
_NbsCoherentCfgEntry_Object=MibTableRow
nbsCoherentCfgEntry=_NbsCoherentCfgEntry_Object((1,3,6,1,4,1,629,242,10,2,1))
nbsCoherentCfgEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:nbsCoherentCfgEntry.setStatus(_A)
_NbsCoherentCfgIfIndex_Type=InterfaceIndex
_NbsCoherentCfgIfIndex_Object=MibTableColumn
nbsCoherentCfgIfIndex=_NbsCoherentCfgIfIndex_Object((1,3,6,1,4,1,629,242,10,2,1,1),_NbsCoherentCfgIfIndex_Type())
nbsCoherentCfgIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgIfIndex.setStatus(_A)
class _NbsCoherentCfgCDmodeCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NbsCoherentCfgCDmodeCaps_Type.__name__=_L
_NbsCoherentCfgCDmodeCaps_Object=MibTableColumn
nbsCoherentCfgCDmodeCaps=_NbsCoherentCfgCDmodeCaps_Object((1,3,6,1,4,1,629,242,10,2,1,3),_NbsCoherentCfgCDmodeCaps_Type())
nbsCoherentCfgCDmodeCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgCDmodeCaps.setStatus(_A)
class _NbsCoherentCfgCDmodeAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_N,2),('auto',3),('fixed',4)))
_NbsCoherentCfgCDmodeAdmin_Type.__name__=_E
_NbsCoherentCfgCDmodeAdmin_Object=MibTableColumn
nbsCoherentCfgCDmodeAdmin=_NbsCoherentCfgCDmodeAdmin_Object((1,3,6,1,4,1,629,242,10,2,1,12),_NbsCoherentCfgCDmodeAdmin_Type())
nbsCoherentCfgCDmodeAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentCfgCDmodeAdmin.setStatus(_A)
class _NbsCoherentCfgCDmodeOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_N,2),('auto',3),('fixed',4)))
_NbsCoherentCfgCDmodeOper_Type.__name__=_E
_NbsCoherentCfgCDmodeOper_Object=MibTableColumn
nbsCoherentCfgCDmodeOper=_NbsCoherentCfgCDmodeOper_Object((1,3,6,1,4,1,629,242,10,2,1,13),_NbsCoherentCfgCDmodeOper_Type())
nbsCoherentCfgCDmodeOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgCDmodeOper.setStatus(_A)
class _NbsCoherentCfgCDautolAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDautolAdmin_Type.__name__=_E
_NbsCoherentCfgCDautolAdmin_Object=MibTableColumn
nbsCoherentCfgCDautolAdmin=_NbsCoherentCfgCDautolAdmin_Object((1,3,6,1,4,1,629,242,10,2,1,14),_NbsCoherentCfgCDautolAdmin_Type())
nbsCoherentCfgCDautolAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentCfgCDautolAdmin.setStatus(_A)
class _NbsCoherentCfgCDautolOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDautolOper_Type.__name__=_E
_NbsCoherentCfgCDautolOper_Object=MibTableColumn
nbsCoherentCfgCDautolOper=_NbsCoherentCfgCDautolOper_Object((1,3,6,1,4,1,629,242,10,2,1,15),_NbsCoherentCfgCDautolOper_Type())
nbsCoherentCfgCDautolOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgCDautolOper.setStatus(_A)
class _NbsCoherentCfgCDautohAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDautohAdmin_Type.__name__=_E
_NbsCoherentCfgCDautohAdmin_Object=MibTableColumn
nbsCoherentCfgCDautohAdmin=_NbsCoherentCfgCDautohAdmin_Object((1,3,6,1,4,1,629,242,10,2,1,16),_NbsCoherentCfgCDautohAdmin_Type())
nbsCoherentCfgCDautohAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentCfgCDautohAdmin.setStatus(_A)
class _NbsCoherentCfgCDautohOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDautohOper_Type.__name__=_E
_NbsCoherentCfgCDautohOper_Object=MibTableColumn
nbsCoherentCfgCDautohOper=_NbsCoherentCfgCDautohOper_Object((1,3,6,1,4,1,629,242,10,2,1,17),_NbsCoherentCfgCDautohOper_Type())
nbsCoherentCfgCDautohOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgCDautohOper.setStatus(_A)
class _NbsCoherentCfgCDfixedAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDfixedAdmin_Type.__name__=_E
_NbsCoherentCfgCDfixedAdmin_Object=MibTableColumn
nbsCoherentCfgCDfixedAdmin=_NbsCoherentCfgCDfixedAdmin_Object((1,3,6,1,4,1,629,242,10,2,1,18),_NbsCoherentCfgCDfixedAdmin_Type())
nbsCoherentCfgCDfixedAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentCfgCDfixedAdmin.setStatus(_A)
class _NbsCoherentCfgCDfixedOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsCoherentCfgCDfixedOper_Type.__name__=_E
_NbsCoherentCfgCDfixedOper_Object=MibTableColumn
nbsCoherentCfgCDfixedOper=_NbsCoherentCfgCDfixedOper_Object((1,3,6,1,4,1,629,242,10,2,1,19),_NbsCoherentCfgCDfixedOper_Type())
nbsCoherentCfgCDfixedOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgCDfixedOper.setStatus(_A)
class _NbsCoherentCfgSOPmodeAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3)))
_NbsCoherentCfgSOPmodeAdmin_Type.__name__=_E
_NbsCoherentCfgSOPmodeAdmin_Object=MibTableColumn
nbsCoherentCfgSOPmodeAdmin=_NbsCoherentCfgSOPmodeAdmin_Object((1,3,6,1,4,1,629,242,10,2,1,22),_NbsCoherentCfgSOPmodeAdmin_Type())
nbsCoherentCfgSOPmodeAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentCfgSOPmodeAdmin.setStatus(_A)
class _NbsCoherentCfgSOPmodeOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3)))
_NbsCoherentCfgSOPmodeOper_Type.__name__=_E
_NbsCoherentCfgSOPmodeOper_Object=MibTableColumn
nbsCoherentCfgSOPmodeOper=_NbsCoherentCfgSOPmodeOper_Object((1,3,6,1,4,1,629,242,10,2,1,23),_NbsCoherentCfgSOPmodeOper_Type())
nbsCoherentCfgSOPmodeOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentCfgSOPmodeOper.setStatus(_A)
_NbsCohpmThresholdsGrp_ObjectIdentity=ObjectIdentity
nbsCohpmThresholdsGrp=_NbsCohpmThresholdsGrp_ObjectIdentity((1,3,6,1,4,1,629,242,21))
if mibBuilder.loadTexts:nbsCohpmThresholdsGrp.setStatus(_A)
_NbsCohpmThresholdsTable_Object=MibTable
nbsCohpmThresholdsTable=_NbsCohpmThresholdsTable_Object((1,3,6,1,4,1,629,242,21,1))
if mibBuilder.loadTexts:nbsCohpmThresholdsTable.setStatus(_A)
_NbsCohpmThresholdsEntry_Object=MibTableRow
nbsCohpmThresholdsEntry=_NbsCohpmThresholdsEntry_Object((1,3,6,1,4,1,629,242,21,1,1))
nbsCohpmThresholdsEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:nbsCohpmThresholdsEntry.setStatus(_A)
_NbsCohpmThresholdsIfIndex_Type=InterfaceIndex
_NbsCohpmThresholdsIfIndex_Object=MibTableColumn
nbsCohpmThresholdsIfIndex=_NbsCohpmThresholdsIfIndex_Object((1,3,6,1,4,1,629,242,21,1,1,1),_NbsCohpmThresholdsIfIndex_Type())
nbsCohpmThresholdsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmThresholdsIfIndex.setStatus(_A)
class _NbsCohpmThresholdsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsCohpmThresholdsInterval_Type.__name__=_E
_NbsCohpmThresholdsInterval_Object=MibTableColumn
nbsCohpmThresholdsInterval=_NbsCohpmThresholdsInterval_Object((1,3,6,1,4,1,629,242,21,1,1,3),_NbsCohpmThresholdsInterval_Type())
nbsCohpmThresholdsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmThresholdsInterval.setStatus(_A)
class _NbsCohpmThresholdsAveNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmThresholdsAveNetBERsig_Type.__name__=_E
_NbsCohpmThresholdsAveNetBERsig_Object=MibTableColumn
nbsCohpmThresholdsAveNetBERsig=_NbsCohpmThresholdsAveNetBERsig_Object((1,3,6,1,4,1,629,242,21,1,1,11),_NbsCohpmThresholdsAveNetBERsig_Type())
nbsCohpmThresholdsAveNetBERsig.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveNetBERsig.setStatus(_A)
class _NbsCohpmThresholdsAveNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsAveNetBERexp_Type.__name__=_E
_NbsCohpmThresholdsAveNetBERexp_Object=MibTableColumn
nbsCohpmThresholdsAveNetBERexp=_NbsCohpmThresholdsAveNetBERexp_Object((1,3,6,1,4,1,629,242,21,1,1,12),_NbsCohpmThresholdsAveNetBERexp_Type())
nbsCohpmThresholdsAveNetBERexp.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveNetBERexp.setStatus(_A)
class _NbsCohpmThresholdsMinNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmThresholdsMinNetBERsig_Type.__name__=_E
_NbsCohpmThresholdsMinNetBERsig_Object=MibTableColumn
nbsCohpmThresholdsMinNetBERsig=_NbsCohpmThresholdsMinNetBERsig_Object((1,3,6,1,4,1,629,242,21,1,1,14),_NbsCohpmThresholdsMinNetBERsig_Type())
nbsCohpmThresholdsMinNetBERsig.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinNetBERsig.setStatus(_A)
class _NbsCohpmThresholdsMinNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMinNetBERexp_Type.__name__=_E
_NbsCohpmThresholdsMinNetBERexp_Object=MibTableColumn
nbsCohpmThresholdsMinNetBERexp=_NbsCohpmThresholdsMinNetBERexp_Object((1,3,6,1,4,1,629,242,21,1,1,15),_NbsCohpmThresholdsMinNetBERexp_Type())
nbsCohpmThresholdsMinNetBERexp.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinNetBERexp.setStatus(_A)
class _NbsCohpmThresholdsMaxNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmThresholdsMaxNetBERsig_Type.__name__=_E
_NbsCohpmThresholdsMaxNetBERsig_Object=MibTableColumn
nbsCohpmThresholdsMaxNetBERsig=_NbsCohpmThresholdsMaxNetBERsig_Object((1,3,6,1,4,1,629,242,21,1,1,17),_NbsCohpmThresholdsMaxNetBERsig_Type())
nbsCohpmThresholdsMaxNetBERsig.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxNetBERsig.setStatus(_A)
class _NbsCohpmThresholdsMaxNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMaxNetBERexp_Type.__name__=_E
_NbsCohpmThresholdsMaxNetBERexp_Object=MibTableColumn
nbsCohpmThresholdsMaxNetBERexp=_NbsCohpmThresholdsMaxNetBERexp_Object((1,3,6,1,4,1,629,242,21,1,1,18),_NbsCohpmThresholdsMaxNetBERexp_Type())
nbsCohpmThresholdsMaxNetBERexp.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxNetBERexp.setStatus(_A)
class _NbsCohpmThresholdsAveCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsAveCD_Type.__name__=_E
_NbsCohpmThresholdsAveCD_Object=MibTableColumn
nbsCohpmThresholdsAveCD=_NbsCohpmThresholdsAveCD_Object((1,3,6,1,4,1,629,242,21,1,1,20),_NbsCohpmThresholdsAveCD_Type())
nbsCohpmThresholdsAveCD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveCD.setStatus(_A)
class _NbsCohpmThresholdsMinCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMinCD_Type.__name__=_E
_NbsCohpmThresholdsMinCD_Object=MibTableColumn
nbsCohpmThresholdsMinCD=_NbsCohpmThresholdsMinCD_Object((1,3,6,1,4,1,629,242,21,1,1,23),_NbsCohpmThresholdsMinCD_Type())
nbsCohpmThresholdsMinCD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinCD.setStatus(_A)
class _NbsCohpmThresholdsMaxCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMaxCD_Type.__name__=_E
_NbsCohpmThresholdsMaxCD_Object=MibTableColumn
nbsCohpmThresholdsMaxCD=_NbsCohpmThresholdsMaxCD_Object((1,3,6,1,4,1,629,242,21,1,1,26),_NbsCohpmThresholdsMaxCD_Type())
nbsCohpmThresholdsMaxCD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxCD.setStatus(_A)
class _NbsCohpmThresholdsAveDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveDGD_Type.__name__=_C
_NbsCohpmThresholdsAveDGD_Object=MibTableColumn
nbsCohpmThresholdsAveDGD=_NbsCohpmThresholdsAveDGD_Object((1,3,6,1,4,1,629,242,21,1,1,30),_NbsCohpmThresholdsAveDGD_Type())
nbsCohpmThresholdsAveDGD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveDGD.setStatus(_A)
class _NbsCohpmThresholdsMinDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinDGD_Type.__name__=_C
_NbsCohpmThresholdsMinDGD_Object=MibTableColumn
nbsCohpmThresholdsMinDGD=_NbsCohpmThresholdsMinDGD_Object((1,3,6,1,4,1,629,242,21,1,1,33),_NbsCohpmThresholdsMinDGD_Type())
nbsCohpmThresholdsMinDGD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinDGD.setStatus(_A)
class _NbsCohpmThresholdsMaxDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxDGD_Type.__name__=_C
_NbsCohpmThresholdsMaxDGD_Object=MibTableColumn
nbsCohpmThresholdsMaxDGD=_NbsCohpmThresholdsMaxDGD_Object((1,3,6,1,4,1,629,242,21,1,1,36),_NbsCohpmThresholdsMaxDGD_Type())
nbsCohpmThresholdsMaxDGD.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxDGD.setStatus(_A)
class _NbsCohpmThresholdsAveQ_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveQ_Type.__name__=_C
_NbsCohpmThresholdsAveQ_Object=MibTableColumn
nbsCohpmThresholdsAveQ=_NbsCohpmThresholdsAveQ_Object((1,3,6,1,4,1,629,242,21,1,1,40),_NbsCohpmThresholdsAveQ_Type())
nbsCohpmThresholdsAveQ.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveQ.setStatus(_A)
class _NbsCohpmThresholdsMinQ_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinQ_Type.__name__=_C
_NbsCohpmThresholdsMinQ_Object=MibTableColumn
nbsCohpmThresholdsMinQ=_NbsCohpmThresholdsMinQ_Object((1,3,6,1,4,1,629,242,21,1,1,43),_NbsCohpmThresholdsMinQ_Type())
nbsCohpmThresholdsMinQ.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinQ.setStatus(_A)
class _NbsCohpmThresholdsMaxQ_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxQ_Type.__name__=_C
_NbsCohpmThresholdsMaxQ_Object=MibTableColumn
nbsCohpmThresholdsMaxQ=_NbsCohpmThresholdsMaxQ_Object((1,3,6,1,4,1,629,242,21,1,1,46),_NbsCohpmThresholdsMaxQ_Type())
nbsCohpmThresholdsMaxQ.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxQ.setStatus(_A)
class _NbsCohpmThresholdsAveCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsAveCFO_Type.__name__=_E
_NbsCohpmThresholdsAveCFO_Object=MibTableColumn
nbsCohpmThresholdsAveCFO=_NbsCohpmThresholdsAveCFO_Object((1,3,6,1,4,1,629,242,21,1,1,50),_NbsCohpmThresholdsAveCFO_Type())
nbsCohpmThresholdsAveCFO.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveCFO.setStatus(_A)
class _NbsCohpmThresholdsMinCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMinCFO_Type.__name__=_E
_NbsCohpmThresholdsMinCFO_Object=MibTableColumn
nbsCohpmThresholdsMinCFO=_NbsCohpmThresholdsMinCFO_Object((1,3,6,1,4,1,629,242,21,1,1,53),_NbsCohpmThresholdsMinCFO_Type())
nbsCohpmThresholdsMinCFO.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinCFO.setStatus(_A)
class _NbsCohpmThresholdsMaxCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmThresholdsMaxCFO_Type.__name__=_E
_NbsCohpmThresholdsMaxCFO_Object=MibTableColumn
nbsCohpmThresholdsMaxCFO=_NbsCohpmThresholdsMaxCFO_Object((1,3,6,1,4,1,629,242,21,1,1,56),_NbsCohpmThresholdsMaxCFO_Type())
nbsCohpmThresholdsMaxCFO.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxCFO.setStatus(_A)
class _NbsCohpmThresholdsAveOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveOSNR_Type.__name__=_C
_NbsCohpmThresholdsAveOSNR_Object=MibTableColumn
nbsCohpmThresholdsAveOSNR=_NbsCohpmThresholdsAveOSNR_Object((1,3,6,1,4,1,629,242,21,1,1,60),_NbsCohpmThresholdsAveOSNR_Type())
nbsCohpmThresholdsAveOSNR.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveOSNR.setStatus(_A)
class _NbsCohpmThresholdsMinOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinOSNR_Type.__name__=_C
_NbsCohpmThresholdsMinOSNR_Object=MibTableColumn
nbsCohpmThresholdsMinOSNR=_NbsCohpmThresholdsMinOSNR_Object((1,3,6,1,4,1,629,242,21,1,1,63),_NbsCohpmThresholdsMinOSNR_Type())
nbsCohpmThresholdsMinOSNR.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinOSNR.setStatus(_A)
class _NbsCohpmThresholdsMaxOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxOSNR_Type.__name__=_C
_NbsCohpmThresholdsMaxOSNR_Object=MibTableColumn
nbsCohpmThresholdsMaxOSNR=_NbsCohpmThresholdsMaxOSNR_Object((1,3,6,1,4,1,629,242,21,1,1,66),_NbsCohpmThresholdsMaxOSNR_Type())
nbsCohpmThresholdsMaxOSNR.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxOSNR.setStatus(_A)
class _NbsCohpmThresholdsAveSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveSNRx_Type.__name__=_C
_NbsCohpmThresholdsAveSNRx_Object=MibTableColumn
nbsCohpmThresholdsAveSNRx=_NbsCohpmThresholdsAveSNRx_Object((1,3,6,1,4,1,629,242,21,1,1,70),_NbsCohpmThresholdsAveSNRx_Type())
nbsCohpmThresholdsAveSNRx.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveSNRx.setStatus(_A)
class _NbsCohpmThresholdsMinSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinSNRx_Type.__name__=_C
_NbsCohpmThresholdsMinSNRx_Object=MibTableColumn
nbsCohpmThresholdsMinSNRx=_NbsCohpmThresholdsMinSNRx_Object((1,3,6,1,4,1,629,242,21,1,1,73),_NbsCohpmThresholdsMinSNRx_Type())
nbsCohpmThresholdsMinSNRx.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinSNRx.setStatus(_A)
class _NbsCohpmThresholdsMaxSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxSNRx_Type.__name__=_C
_NbsCohpmThresholdsMaxSNRx_Object=MibTableColumn
nbsCohpmThresholdsMaxSNRx=_NbsCohpmThresholdsMaxSNRx_Object((1,3,6,1,4,1,629,242,21,1,1,76),_NbsCohpmThresholdsMaxSNRx_Type())
nbsCohpmThresholdsMaxSNRx.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxSNRx.setStatus(_A)
class _NbsCohpmThresholdsAveSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveSNRy_Type.__name__=_C
_NbsCohpmThresholdsAveSNRy_Object=MibTableColumn
nbsCohpmThresholdsAveSNRy=_NbsCohpmThresholdsAveSNRy_Object((1,3,6,1,4,1,629,242,21,1,1,80),_NbsCohpmThresholdsAveSNRy_Type())
nbsCohpmThresholdsAveSNRy.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveSNRy.setStatus(_A)
class _NbsCohpmThresholdsMinSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinSNRy_Type.__name__=_C
_NbsCohpmThresholdsMinSNRy_Object=MibTableColumn
nbsCohpmThresholdsMinSNRy=_NbsCohpmThresholdsMinSNRy_Object((1,3,6,1,4,1,629,242,21,1,1,83),_NbsCohpmThresholdsMinSNRy_Type())
nbsCohpmThresholdsMinSNRy.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinSNRy.setStatus(_A)
class _NbsCohpmThresholdsMaxSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxSNRy_Type.__name__=_C
_NbsCohpmThresholdsMaxSNRy_Object=MibTableColumn
nbsCohpmThresholdsMaxSNRy=_NbsCohpmThresholdsMaxSNRy_Object((1,3,6,1,4,1,629,242,21,1,1,86),_NbsCohpmThresholdsMaxSNRy_Type())
nbsCohpmThresholdsMaxSNRy.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxSNRy.setStatus(_A)
class _NbsCohpmThresholdsAvePDL_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAvePDL_Type.__name__=_C
_NbsCohpmThresholdsAvePDL_Object=MibTableColumn
nbsCohpmThresholdsAvePDL=_NbsCohpmThresholdsAvePDL_Object((1,3,6,1,4,1,629,242,21,1,1,90),_NbsCohpmThresholdsAvePDL_Type())
nbsCohpmThresholdsAvePDL.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAvePDL.setStatus(_A)
class _NbsCohpmThresholdsMinPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinPDL_Type.__name__=_C
_NbsCohpmThresholdsMinPDL_Object=MibTableColumn
nbsCohpmThresholdsMinPDL=_NbsCohpmThresholdsMinPDL_Object((1,3,6,1,4,1,629,242,21,1,1,93),_NbsCohpmThresholdsMinPDL_Type())
nbsCohpmThresholdsMinPDL.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinPDL.setStatus(_A)
class _NbsCohpmThresholdsMaxPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxPDL_Type.__name__=_C
_NbsCohpmThresholdsMaxPDL_Object=MibTableColumn
nbsCohpmThresholdsMaxPDL=_NbsCohpmThresholdsMaxPDL_Object((1,3,6,1,4,1,629,242,21,1,1,96),_NbsCohpmThresholdsMaxPDL_Type())
nbsCohpmThresholdsMaxPDL.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxPDL.setStatus(_A)
class _NbsCohpmThresholdsAveSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsAveSOP_Type.__name__=_C
_NbsCohpmThresholdsAveSOP_Object=MibTableColumn
nbsCohpmThresholdsAveSOP=_NbsCohpmThresholdsAveSOP_Object((1,3,6,1,4,1,629,242,21,1,1,100),_NbsCohpmThresholdsAveSOP_Type())
nbsCohpmThresholdsAveSOP.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsAveSOP.setStatus(_A)
class _NbsCohpmThresholdsMinSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMinSOP_Type.__name__=_C
_NbsCohpmThresholdsMinSOP_Object=MibTableColumn
nbsCohpmThresholdsMinSOP=_NbsCohpmThresholdsMinSOP_Object((1,3,6,1,4,1,629,242,21,1,1,103),_NbsCohpmThresholdsMinSOP_Type())
nbsCohpmThresholdsMinSOP.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMinSOP.setStatus(_A)
class _NbsCohpmThresholdsMaxSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmThresholdsMaxSOP_Type.__name__=_C
_NbsCohpmThresholdsMaxSOP_Object=MibTableColumn
nbsCohpmThresholdsMaxSOP=_NbsCohpmThresholdsMaxSOP_Object((1,3,6,1,4,1,629,242,21,1,1,106),_NbsCohpmThresholdsMaxSOP_Type())
nbsCohpmThresholdsMaxSOP.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCohpmThresholdsMaxSOP.setStatus(_A)
_NbsCohpmCurrentGrp_ObjectIdentity=ObjectIdentity
nbsCohpmCurrentGrp=_NbsCohpmCurrentGrp_ObjectIdentity((1,3,6,1,4,1,629,242,22))
if mibBuilder.loadTexts:nbsCohpmCurrentGrp.setStatus(_A)
_NbsCohpmCurrentTable_Object=MibTable
nbsCohpmCurrentTable=_NbsCohpmCurrentTable_Object((1,3,6,1,4,1,629,242,22,3))
if mibBuilder.loadTexts:nbsCohpmCurrentTable.setStatus(_A)
_NbsCohpmCurrentEntry_Object=MibTableRow
nbsCohpmCurrentEntry=_NbsCohpmCurrentEntry_Object((1,3,6,1,4,1,629,242,22,3,1))
nbsCohpmCurrentEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:nbsCohpmCurrentEntry.setStatus(_A)
_NbsCohpmCurrentIfIndex_Type=InterfaceIndex
_NbsCohpmCurrentIfIndex_Object=MibTableColumn
nbsCohpmCurrentIfIndex=_NbsCohpmCurrentIfIndex_Object((1,3,6,1,4,1,629,242,22,3,1,1),_NbsCohpmCurrentIfIndex_Type())
nbsCohpmCurrentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentIfIndex.setStatus(_A)
class _NbsCohpmCurrentInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsCohpmCurrentInterval_Type.__name__=_E
_NbsCohpmCurrentInterval_Object=MibTableColumn
nbsCohpmCurrentInterval=_NbsCohpmCurrentInterval_Object((1,3,6,1,4,1,629,242,22,3,1,3),_NbsCohpmCurrentInterval_Type())
nbsCohpmCurrentInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentInterval.setStatus(_A)
_NbsCohpmCurrentDate_Type=Integer32
_NbsCohpmCurrentDate_Object=MibTableColumn
nbsCohpmCurrentDate=_NbsCohpmCurrentDate_Object((1,3,6,1,4,1,629,242,22,3,1,5),_NbsCohpmCurrentDate_Type())
nbsCohpmCurrentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentDate.setStatus(_A)
_NbsCohpmCurrentTime_Type=Integer32
_NbsCohpmCurrentTime_Object=MibTableColumn
nbsCohpmCurrentTime=_NbsCohpmCurrentTime_Object((1,3,6,1,4,1,629,242,22,3,1,6),_NbsCohpmCurrentTime_Type())
nbsCohpmCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentTime.setStatus(_A)
class _NbsCohpmCurrentAveNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmCurrentAveNetBERsig_Type.__name__=_E
_NbsCohpmCurrentAveNetBERsig_Object=MibTableColumn
nbsCohpmCurrentAveNetBERsig=_NbsCohpmCurrentAveNetBERsig_Object((1,3,6,1,4,1,629,242,22,3,1,11),_NbsCohpmCurrentAveNetBERsig_Type())
nbsCohpmCurrentAveNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveNetBERsig.setStatus(_A)
class _NbsCohpmCurrentAveNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentAveNetBERexp_Type.__name__=_E
_NbsCohpmCurrentAveNetBERexp_Object=MibTableColumn
nbsCohpmCurrentAveNetBERexp=_NbsCohpmCurrentAveNetBERexp_Object((1,3,6,1,4,1,629,242,22,3,1,12),_NbsCohpmCurrentAveNetBERexp_Type())
nbsCohpmCurrentAveNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveNetBERexp.setStatus(_A)
class _NbsCohpmCurrentMinNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmCurrentMinNetBERsig_Type.__name__=_E
_NbsCohpmCurrentMinNetBERsig_Object=MibTableColumn
nbsCohpmCurrentMinNetBERsig=_NbsCohpmCurrentMinNetBERsig_Object((1,3,6,1,4,1,629,242,22,3,1,14),_NbsCohpmCurrentMinNetBERsig_Type())
nbsCohpmCurrentMinNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinNetBERsig.setStatus(_A)
class _NbsCohpmCurrentMinNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMinNetBERexp_Type.__name__=_E
_NbsCohpmCurrentMinNetBERexp_Object=MibTableColumn
nbsCohpmCurrentMinNetBERexp=_NbsCohpmCurrentMinNetBERexp_Object((1,3,6,1,4,1,629,242,22,3,1,15),_NbsCohpmCurrentMinNetBERexp_Type())
nbsCohpmCurrentMinNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinNetBERexp.setStatus(_A)
class _NbsCohpmCurrentMaxNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmCurrentMaxNetBERsig_Type.__name__=_E
_NbsCohpmCurrentMaxNetBERsig_Object=MibTableColumn
nbsCohpmCurrentMaxNetBERsig=_NbsCohpmCurrentMaxNetBERsig_Object((1,3,6,1,4,1,629,242,22,3,1,17),_NbsCohpmCurrentMaxNetBERsig_Type())
nbsCohpmCurrentMaxNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxNetBERsig.setStatus(_A)
class _NbsCohpmCurrentMaxNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMaxNetBERexp_Type.__name__=_E
_NbsCohpmCurrentMaxNetBERexp_Object=MibTableColumn
nbsCohpmCurrentMaxNetBERexp=_NbsCohpmCurrentMaxNetBERexp_Object((1,3,6,1,4,1,629,242,22,3,1,18),_NbsCohpmCurrentMaxNetBERexp_Type())
nbsCohpmCurrentMaxNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxNetBERexp.setStatus(_A)
class _NbsCohpmCurrentAveCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentAveCD_Type.__name__=_E
_NbsCohpmCurrentAveCD_Object=MibTableColumn
nbsCohpmCurrentAveCD=_NbsCohpmCurrentAveCD_Object((1,3,6,1,4,1,629,242,22,3,1,20),_NbsCohpmCurrentAveCD_Type())
nbsCohpmCurrentAveCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveCD.setStatus(_A)
class _NbsCohpmCurrentMinCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMinCD_Type.__name__=_E
_NbsCohpmCurrentMinCD_Object=MibTableColumn
nbsCohpmCurrentMinCD=_NbsCohpmCurrentMinCD_Object((1,3,6,1,4,1,629,242,22,3,1,23),_NbsCohpmCurrentMinCD_Type())
nbsCohpmCurrentMinCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinCD.setStatus(_A)
class _NbsCohpmCurrentMaxCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMaxCD_Type.__name__=_E
_NbsCohpmCurrentMaxCD_Object=MibTableColumn
nbsCohpmCurrentMaxCD=_NbsCohpmCurrentMaxCD_Object((1,3,6,1,4,1,629,242,22,3,1,26),_NbsCohpmCurrentMaxCD_Type())
nbsCohpmCurrentMaxCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxCD.setStatus(_A)
class _NbsCohpmCurrentAveDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveDGD_Type.__name__=_C
_NbsCohpmCurrentAveDGD_Object=MibTableColumn
nbsCohpmCurrentAveDGD=_NbsCohpmCurrentAveDGD_Object((1,3,6,1,4,1,629,242,22,3,1,30),_NbsCohpmCurrentAveDGD_Type())
nbsCohpmCurrentAveDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveDGD.setStatus(_A)
class _NbsCohpmCurrentMinDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinDGD_Type.__name__=_C
_NbsCohpmCurrentMinDGD_Object=MibTableColumn
nbsCohpmCurrentMinDGD=_NbsCohpmCurrentMinDGD_Object((1,3,6,1,4,1,629,242,22,3,1,33),_NbsCohpmCurrentMinDGD_Type())
nbsCohpmCurrentMinDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinDGD.setStatus(_A)
class _NbsCohpmCurrentMaxDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxDGD_Type.__name__=_C
_NbsCohpmCurrentMaxDGD_Object=MibTableColumn
nbsCohpmCurrentMaxDGD=_NbsCohpmCurrentMaxDGD_Object((1,3,6,1,4,1,629,242,22,3,1,36),_NbsCohpmCurrentMaxDGD_Type())
nbsCohpmCurrentMaxDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxDGD.setStatus(_A)
class _NbsCohpmCurrentAveQ_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveQ_Type.__name__=_C
_NbsCohpmCurrentAveQ_Object=MibTableColumn
nbsCohpmCurrentAveQ=_NbsCohpmCurrentAveQ_Object((1,3,6,1,4,1,629,242,22,3,1,40),_NbsCohpmCurrentAveQ_Type())
nbsCohpmCurrentAveQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveQ.setStatus(_A)
class _NbsCohpmCurrentMinQ_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinQ_Type.__name__=_C
_NbsCohpmCurrentMinQ_Object=MibTableColumn
nbsCohpmCurrentMinQ=_NbsCohpmCurrentMinQ_Object((1,3,6,1,4,1,629,242,22,3,1,43),_NbsCohpmCurrentMinQ_Type())
nbsCohpmCurrentMinQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinQ.setStatus(_A)
class _NbsCohpmCurrentMaxQ_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxQ_Type.__name__=_C
_NbsCohpmCurrentMaxQ_Object=MibTableColumn
nbsCohpmCurrentMaxQ=_NbsCohpmCurrentMaxQ_Object((1,3,6,1,4,1,629,242,22,3,1,46),_NbsCohpmCurrentMaxQ_Type())
nbsCohpmCurrentMaxQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxQ.setStatus(_A)
class _NbsCohpmCurrentAveCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentAveCFO_Type.__name__=_E
_NbsCohpmCurrentAveCFO_Object=MibTableColumn
nbsCohpmCurrentAveCFO=_NbsCohpmCurrentAveCFO_Object((1,3,6,1,4,1,629,242,22,3,1,50),_NbsCohpmCurrentAveCFO_Type())
nbsCohpmCurrentAveCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveCFO.setStatus(_A)
class _NbsCohpmCurrentMinCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMinCFO_Type.__name__=_E
_NbsCohpmCurrentMinCFO_Object=MibTableColumn
nbsCohpmCurrentMinCFO=_NbsCohpmCurrentMinCFO_Object((1,3,6,1,4,1,629,242,22,3,1,53),_NbsCohpmCurrentMinCFO_Type())
nbsCohpmCurrentMinCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinCFO.setStatus(_A)
class _NbsCohpmCurrentMaxCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmCurrentMaxCFO_Type.__name__=_E
_NbsCohpmCurrentMaxCFO_Object=MibTableColumn
nbsCohpmCurrentMaxCFO=_NbsCohpmCurrentMaxCFO_Object((1,3,6,1,4,1,629,242,22,3,1,56),_NbsCohpmCurrentMaxCFO_Type())
nbsCohpmCurrentMaxCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxCFO.setStatus(_A)
class _NbsCohpmCurrentAveOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveOSNR_Type.__name__=_C
_NbsCohpmCurrentAveOSNR_Object=MibTableColumn
nbsCohpmCurrentAveOSNR=_NbsCohpmCurrentAveOSNR_Object((1,3,6,1,4,1,629,242,22,3,1,60),_NbsCohpmCurrentAveOSNR_Type())
nbsCohpmCurrentAveOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveOSNR.setStatus(_A)
class _NbsCohpmCurrentMinOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinOSNR_Type.__name__=_C
_NbsCohpmCurrentMinOSNR_Object=MibTableColumn
nbsCohpmCurrentMinOSNR=_NbsCohpmCurrentMinOSNR_Object((1,3,6,1,4,1,629,242,22,3,1,63),_NbsCohpmCurrentMinOSNR_Type())
nbsCohpmCurrentMinOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinOSNR.setStatus(_A)
class _NbsCohpmCurrentMaxOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxOSNR_Type.__name__=_C
_NbsCohpmCurrentMaxOSNR_Object=MibTableColumn
nbsCohpmCurrentMaxOSNR=_NbsCohpmCurrentMaxOSNR_Object((1,3,6,1,4,1,629,242,22,3,1,66),_NbsCohpmCurrentMaxOSNR_Type())
nbsCohpmCurrentMaxOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxOSNR.setStatus(_A)
class _NbsCohpmCurrentAveSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveSNRx_Type.__name__=_C
_NbsCohpmCurrentAveSNRx_Object=MibTableColumn
nbsCohpmCurrentAveSNRx=_NbsCohpmCurrentAveSNRx_Object((1,3,6,1,4,1,629,242,22,3,1,70),_NbsCohpmCurrentAveSNRx_Type())
nbsCohpmCurrentAveSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveSNRx.setStatus(_A)
class _NbsCohpmCurrentMinSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinSNRx_Type.__name__=_C
_NbsCohpmCurrentMinSNRx_Object=MibTableColumn
nbsCohpmCurrentMinSNRx=_NbsCohpmCurrentMinSNRx_Object((1,3,6,1,4,1,629,242,22,3,1,73),_NbsCohpmCurrentMinSNRx_Type())
nbsCohpmCurrentMinSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinSNRx.setStatus(_A)
class _NbsCohpmCurrentMaxSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxSNRx_Type.__name__=_C
_NbsCohpmCurrentMaxSNRx_Object=MibTableColumn
nbsCohpmCurrentMaxSNRx=_NbsCohpmCurrentMaxSNRx_Object((1,3,6,1,4,1,629,242,22,3,1,76),_NbsCohpmCurrentMaxSNRx_Type())
nbsCohpmCurrentMaxSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxSNRx.setStatus(_A)
class _NbsCohpmCurrentAveSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveSNRy_Type.__name__=_C
_NbsCohpmCurrentAveSNRy_Object=MibTableColumn
nbsCohpmCurrentAveSNRy=_NbsCohpmCurrentAveSNRy_Object((1,3,6,1,4,1,629,242,22,3,1,80),_NbsCohpmCurrentAveSNRy_Type())
nbsCohpmCurrentAveSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveSNRy.setStatus(_A)
class _NbsCohpmCurrentMinSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinSNRy_Type.__name__=_C
_NbsCohpmCurrentMinSNRy_Object=MibTableColumn
nbsCohpmCurrentMinSNRy=_NbsCohpmCurrentMinSNRy_Object((1,3,6,1,4,1,629,242,22,3,1,83),_NbsCohpmCurrentMinSNRy_Type())
nbsCohpmCurrentMinSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinSNRy.setStatus(_A)
class _NbsCohpmCurrentMaxSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxSNRy_Type.__name__=_C
_NbsCohpmCurrentMaxSNRy_Object=MibTableColumn
nbsCohpmCurrentMaxSNRy=_NbsCohpmCurrentMaxSNRy_Object((1,3,6,1,4,1,629,242,22,3,1,86),_NbsCohpmCurrentMaxSNRy_Type())
nbsCohpmCurrentMaxSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxSNRy.setStatus(_A)
class _NbsCohpmCurrentAvePDL_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAvePDL_Type.__name__=_C
_NbsCohpmCurrentAvePDL_Object=MibTableColumn
nbsCohpmCurrentAvePDL=_NbsCohpmCurrentAvePDL_Object((1,3,6,1,4,1,629,242,22,3,1,90),_NbsCohpmCurrentAvePDL_Type())
nbsCohpmCurrentAvePDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAvePDL.setStatus(_A)
class _NbsCohpmCurrentMinPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinPDL_Type.__name__=_C
_NbsCohpmCurrentMinPDL_Object=MibTableColumn
nbsCohpmCurrentMinPDL=_NbsCohpmCurrentMinPDL_Object((1,3,6,1,4,1,629,242,22,3,1,93),_NbsCohpmCurrentMinPDL_Type())
nbsCohpmCurrentMinPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinPDL.setStatus(_A)
class _NbsCohpmCurrentMaxPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxPDL_Type.__name__=_C
_NbsCohpmCurrentMaxPDL_Object=MibTableColumn
nbsCohpmCurrentMaxPDL=_NbsCohpmCurrentMaxPDL_Object((1,3,6,1,4,1,629,242,22,3,1,96),_NbsCohpmCurrentMaxPDL_Type())
nbsCohpmCurrentMaxPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxPDL.setStatus(_A)
class _NbsCohpmCurrentAveSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentAveSOP_Type.__name__=_C
_NbsCohpmCurrentAveSOP_Object=MibTableColumn
nbsCohpmCurrentAveSOP=_NbsCohpmCurrentAveSOP_Object((1,3,6,1,4,1,629,242,22,3,1,100),_NbsCohpmCurrentAveSOP_Type())
nbsCohpmCurrentAveSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentAveSOP.setStatus(_A)
class _NbsCohpmCurrentMinSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMinSOP_Type.__name__=_C
_NbsCohpmCurrentMinSOP_Object=MibTableColumn
nbsCohpmCurrentMinSOP=_NbsCohpmCurrentMinSOP_Object((1,3,6,1,4,1,629,242,22,3,1,103),_NbsCohpmCurrentMinSOP_Type())
nbsCohpmCurrentMinSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMinSOP.setStatus(_A)
class _NbsCohpmCurrentMaxSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmCurrentMaxSOP_Type.__name__=_C
_NbsCohpmCurrentMaxSOP_Object=MibTableColumn
nbsCohpmCurrentMaxSOP=_NbsCohpmCurrentMaxSOP_Object((1,3,6,1,4,1,629,242,22,3,1,106),_NbsCohpmCurrentMaxSOP_Type())
nbsCohpmCurrentMaxSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmCurrentMaxSOP.setStatus(_A)
_NbsCohpmHistoricGrp_ObjectIdentity=ObjectIdentity
nbsCohpmHistoricGrp=_NbsCohpmHistoricGrp_ObjectIdentity((1,3,6,1,4,1,629,242,23))
if mibBuilder.loadTexts:nbsCohpmHistoricGrp.setStatus(_A)
_NbsCohpmHistoricTable_Object=MibTable
nbsCohpmHistoricTable=_NbsCohpmHistoricTable_Object((1,3,6,1,4,1,629,242,23,3))
if mibBuilder.loadTexts:nbsCohpmHistoricTable.setStatus(_A)
_NbsCohpmHistoricEntry_Object=MibTableRow
nbsCohpmHistoricEntry=_NbsCohpmHistoricEntry_Object((1,3,6,1,4,1,629,242,23,3,1))
nbsCohpmHistoricEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:nbsCohpmHistoricEntry.setStatus(_A)
_NbsCohpmHistoricIfIndex_Type=InterfaceIndex
_NbsCohpmHistoricIfIndex_Object=MibTableColumn
nbsCohpmHistoricIfIndex=_NbsCohpmHistoricIfIndex_Object((1,3,6,1,4,1,629,242,23,3,1,1),_NbsCohpmHistoricIfIndex_Type())
nbsCohpmHistoricIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricIfIndex.setStatus(_A)
class _NbsCohpmHistoricInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsCohpmHistoricInterval_Type.__name__=_E
_NbsCohpmHistoricInterval_Object=MibTableColumn
nbsCohpmHistoricInterval=_NbsCohpmHistoricInterval_Object((1,3,6,1,4,1,629,242,23,3,1,3),_NbsCohpmHistoricInterval_Type())
nbsCohpmHistoricInterval.setMaxAccess(_V)
if mibBuilder.loadTexts:nbsCohpmHistoricInterval.setStatus(_A)
_NbsCohpmHistoricSample_Type=Integer32
_NbsCohpmHistoricSample_Object=MibTableColumn
nbsCohpmHistoricSample=_NbsCohpmHistoricSample_Object((1,3,6,1,4,1,629,242,23,3,1,4),_NbsCohpmHistoricSample_Type())
nbsCohpmHistoricSample.setMaxAccess(_V)
if mibBuilder.loadTexts:nbsCohpmHistoricSample.setStatus(_A)
_NbsCohpmHistoricDate_Type=Integer32
_NbsCohpmHistoricDate_Object=MibTableColumn
nbsCohpmHistoricDate=_NbsCohpmHistoricDate_Object((1,3,6,1,4,1,629,242,23,3,1,5),_NbsCohpmHistoricDate_Type())
nbsCohpmHistoricDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricDate.setStatus(_A)
_NbsCohpmHistoricTime_Type=Integer32
_NbsCohpmHistoricTime_Object=MibTableColumn
nbsCohpmHistoricTime=_NbsCohpmHistoricTime_Object((1,3,6,1,4,1,629,242,23,3,1,6),_NbsCohpmHistoricTime_Type())
nbsCohpmHistoricTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricTime.setStatus(_A)
class _NbsCohpmHistoricAveNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmHistoricAveNetBERsig_Type.__name__=_E
_NbsCohpmHistoricAveNetBERsig_Object=MibTableColumn
nbsCohpmHistoricAveNetBERsig=_NbsCohpmHistoricAveNetBERsig_Object((1,3,6,1,4,1,629,242,23,3,1,11),_NbsCohpmHistoricAveNetBERsig_Type())
nbsCohpmHistoricAveNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveNetBERsig.setStatus(_A)
class _NbsCohpmHistoricAveNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricAveNetBERexp_Type.__name__=_E
_NbsCohpmHistoricAveNetBERexp_Object=MibTableColumn
nbsCohpmHistoricAveNetBERexp=_NbsCohpmHistoricAveNetBERexp_Object((1,3,6,1,4,1,629,242,23,3,1,12),_NbsCohpmHistoricAveNetBERexp_Type())
nbsCohpmHistoricAveNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveNetBERexp.setStatus(_A)
class _NbsCohpmHistoricMinNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmHistoricMinNetBERsig_Type.__name__=_E
_NbsCohpmHistoricMinNetBERsig_Object=MibTableColumn
nbsCohpmHistoricMinNetBERsig=_NbsCohpmHistoricMinNetBERsig_Object((1,3,6,1,4,1,629,242,23,3,1,14),_NbsCohpmHistoricMinNetBERsig_Type())
nbsCohpmHistoricMinNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinNetBERsig.setStatus(_A)
class _NbsCohpmHistoricMinNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMinNetBERexp_Type.__name__=_E
_NbsCohpmHistoricMinNetBERexp_Object=MibTableColumn
nbsCohpmHistoricMinNetBERexp=_NbsCohpmHistoricMinNetBERexp_Object((1,3,6,1,4,1,629,242,23,3,1,15),_NbsCohpmHistoricMinNetBERexp_Type())
nbsCohpmHistoricMinNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinNetBERexp.setStatus(_A)
class _NbsCohpmHistoricMaxNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmHistoricMaxNetBERsig_Type.__name__=_E
_NbsCohpmHistoricMaxNetBERsig_Object=MibTableColumn
nbsCohpmHistoricMaxNetBERsig=_NbsCohpmHistoricMaxNetBERsig_Object((1,3,6,1,4,1,629,242,23,3,1,17),_NbsCohpmHistoricMaxNetBERsig_Type())
nbsCohpmHistoricMaxNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxNetBERsig.setStatus(_A)
class _NbsCohpmHistoricMaxNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMaxNetBERexp_Type.__name__=_E
_NbsCohpmHistoricMaxNetBERexp_Object=MibTableColumn
nbsCohpmHistoricMaxNetBERexp=_NbsCohpmHistoricMaxNetBERexp_Object((1,3,6,1,4,1,629,242,23,3,1,18),_NbsCohpmHistoricMaxNetBERexp_Type())
nbsCohpmHistoricMaxNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxNetBERexp.setStatus(_A)
class _NbsCohpmHistoricAveCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricAveCD_Type.__name__=_E
_NbsCohpmHistoricAveCD_Object=MibTableColumn
nbsCohpmHistoricAveCD=_NbsCohpmHistoricAveCD_Object((1,3,6,1,4,1,629,242,23,3,1,20),_NbsCohpmHistoricAveCD_Type())
nbsCohpmHistoricAveCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveCD.setStatus(_A)
class _NbsCohpmHistoricMinCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMinCD_Type.__name__=_E
_NbsCohpmHistoricMinCD_Object=MibTableColumn
nbsCohpmHistoricMinCD=_NbsCohpmHistoricMinCD_Object((1,3,6,1,4,1,629,242,23,3,1,23),_NbsCohpmHistoricMinCD_Type())
nbsCohpmHistoricMinCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinCD.setStatus(_A)
class _NbsCohpmHistoricMaxCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMaxCD_Type.__name__=_E
_NbsCohpmHistoricMaxCD_Object=MibTableColumn
nbsCohpmHistoricMaxCD=_NbsCohpmHistoricMaxCD_Object((1,3,6,1,4,1,629,242,23,3,1,26),_NbsCohpmHistoricMaxCD_Type())
nbsCohpmHistoricMaxCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxCD.setStatus(_A)
class _NbsCohpmHistoricAveDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveDGD_Type.__name__=_C
_NbsCohpmHistoricAveDGD_Object=MibTableColumn
nbsCohpmHistoricAveDGD=_NbsCohpmHistoricAveDGD_Object((1,3,6,1,4,1,629,242,23,3,1,30),_NbsCohpmHistoricAveDGD_Type())
nbsCohpmHistoricAveDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveDGD.setStatus(_A)
class _NbsCohpmHistoricMinDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinDGD_Type.__name__=_C
_NbsCohpmHistoricMinDGD_Object=MibTableColumn
nbsCohpmHistoricMinDGD=_NbsCohpmHistoricMinDGD_Object((1,3,6,1,4,1,629,242,23,3,1,33),_NbsCohpmHistoricMinDGD_Type())
nbsCohpmHistoricMinDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinDGD.setStatus(_A)
class _NbsCohpmHistoricMaxDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxDGD_Type.__name__=_C
_NbsCohpmHistoricMaxDGD_Object=MibTableColumn
nbsCohpmHistoricMaxDGD=_NbsCohpmHistoricMaxDGD_Object((1,3,6,1,4,1,629,242,23,3,1,36),_NbsCohpmHistoricMaxDGD_Type())
nbsCohpmHistoricMaxDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxDGD.setStatus(_A)
class _NbsCohpmHistoricAveQ_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveQ_Type.__name__=_C
_NbsCohpmHistoricAveQ_Object=MibTableColumn
nbsCohpmHistoricAveQ=_NbsCohpmHistoricAveQ_Object((1,3,6,1,4,1,629,242,23,3,1,40),_NbsCohpmHistoricAveQ_Type())
nbsCohpmHistoricAveQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveQ.setStatus(_A)
class _NbsCohpmHistoricMinQ_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinQ_Type.__name__=_C
_NbsCohpmHistoricMinQ_Object=MibTableColumn
nbsCohpmHistoricMinQ=_NbsCohpmHistoricMinQ_Object((1,3,6,1,4,1,629,242,23,3,1,43),_NbsCohpmHistoricMinQ_Type())
nbsCohpmHistoricMinQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinQ.setStatus(_A)
class _NbsCohpmHistoricMaxQ_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxQ_Type.__name__=_C
_NbsCohpmHistoricMaxQ_Object=MibTableColumn
nbsCohpmHistoricMaxQ=_NbsCohpmHistoricMaxQ_Object((1,3,6,1,4,1,629,242,23,3,1,46),_NbsCohpmHistoricMaxQ_Type())
nbsCohpmHistoricMaxQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxQ.setStatus(_A)
class _NbsCohpmHistoricAveCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricAveCFO_Type.__name__=_E
_NbsCohpmHistoricAveCFO_Object=MibTableColumn
nbsCohpmHistoricAveCFO=_NbsCohpmHistoricAveCFO_Object((1,3,6,1,4,1,629,242,23,3,1,50),_NbsCohpmHistoricAveCFO_Type())
nbsCohpmHistoricAveCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveCFO.setStatus(_A)
class _NbsCohpmHistoricMinCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMinCFO_Type.__name__=_E
_NbsCohpmHistoricMinCFO_Object=MibTableColumn
nbsCohpmHistoricMinCFO=_NbsCohpmHistoricMinCFO_Object((1,3,6,1,4,1,629,242,23,3,1,53),_NbsCohpmHistoricMinCFO_Type())
nbsCohpmHistoricMinCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinCFO.setStatus(_A)
class _NbsCohpmHistoricMaxCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmHistoricMaxCFO_Type.__name__=_E
_NbsCohpmHistoricMaxCFO_Object=MibTableColumn
nbsCohpmHistoricMaxCFO=_NbsCohpmHistoricMaxCFO_Object((1,3,6,1,4,1,629,242,23,3,1,56),_NbsCohpmHistoricMaxCFO_Type())
nbsCohpmHistoricMaxCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxCFO.setStatus(_A)
class _NbsCohpmHistoricAveOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveOSNR_Type.__name__=_C
_NbsCohpmHistoricAveOSNR_Object=MibTableColumn
nbsCohpmHistoricAveOSNR=_NbsCohpmHistoricAveOSNR_Object((1,3,6,1,4,1,629,242,23,3,1,60),_NbsCohpmHistoricAveOSNR_Type())
nbsCohpmHistoricAveOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveOSNR.setStatus(_A)
class _NbsCohpmHistoricMinOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinOSNR_Type.__name__=_C
_NbsCohpmHistoricMinOSNR_Object=MibTableColumn
nbsCohpmHistoricMinOSNR=_NbsCohpmHistoricMinOSNR_Object((1,3,6,1,4,1,629,242,23,3,1,63),_NbsCohpmHistoricMinOSNR_Type())
nbsCohpmHistoricMinOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinOSNR.setStatus(_A)
class _NbsCohpmHistoricMaxOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxOSNR_Type.__name__=_C
_NbsCohpmHistoricMaxOSNR_Object=MibTableColumn
nbsCohpmHistoricMaxOSNR=_NbsCohpmHistoricMaxOSNR_Object((1,3,6,1,4,1,629,242,23,3,1,66),_NbsCohpmHistoricMaxOSNR_Type())
nbsCohpmHistoricMaxOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxOSNR.setStatus(_A)
class _NbsCohpmHistoricAveSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveSNRx_Type.__name__=_C
_NbsCohpmHistoricAveSNRx_Object=MibTableColumn
nbsCohpmHistoricAveSNRx=_NbsCohpmHistoricAveSNRx_Object((1,3,6,1,4,1,629,242,23,3,1,70),_NbsCohpmHistoricAveSNRx_Type())
nbsCohpmHistoricAveSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveSNRx.setStatus(_A)
class _NbsCohpmHistoricMinSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinSNRx_Type.__name__=_C
_NbsCohpmHistoricMinSNRx_Object=MibTableColumn
nbsCohpmHistoricMinSNRx=_NbsCohpmHistoricMinSNRx_Object((1,3,6,1,4,1,629,242,23,3,1,73),_NbsCohpmHistoricMinSNRx_Type())
nbsCohpmHistoricMinSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinSNRx.setStatus(_A)
class _NbsCohpmHistoricMaxSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxSNRx_Type.__name__=_C
_NbsCohpmHistoricMaxSNRx_Object=MibTableColumn
nbsCohpmHistoricMaxSNRx=_NbsCohpmHistoricMaxSNRx_Object((1,3,6,1,4,1,629,242,23,3,1,76),_NbsCohpmHistoricMaxSNRx_Type())
nbsCohpmHistoricMaxSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxSNRx.setStatus(_A)
class _NbsCohpmHistoricAveSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveSNRy_Type.__name__=_C
_NbsCohpmHistoricAveSNRy_Object=MibTableColumn
nbsCohpmHistoricAveSNRy=_NbsCohpmHistoricAveSNRy_Object((1,3,6,1,4,1,629,242,23,3,1,80),_NbsCohpmHistoricAveSNRy_Type())
nbsCohpmHistoricAveSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveSNRy.setStatus(_A)
class _NbsCohpmHistoricMinSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinSNRy_Type.__name__=_C
_NbsCohpmHistoricMinSNRy_Object=MibTableColumn
nbsCohpmHistoricMinSNRy=_NbsCohpmHistoricMinSNRy_Object((1,3,6,1,4,1,629,242,23,3,1,83),_NbsCohpmHistoricMinSNRy_Type())
nbsCohpmHistoricMinSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinSNRy.setStatus(_A)
class _NbsCohpmHistoricMaxSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxSNRy_Type.__name__=_C
_NbsCohpmHistoricMaxSNRy_Object=MibTableColumn
nbsCohpmHistoricMaxSNRy=_NbsCohpmHistoricMaxSNRy_Object((1,3,6,1,4,1,629,242,23,3,1,86),_NbsCohpmHistoricMaxSNRy_Type())
nbsCohpmHistoricMaxSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxSNRy.setStatus(_A)
class _NbsCohpmHistoricAvePDL_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAvePDL_Type.__name__=_C
_NbsCohpmHistoricAvePDL_Object=MibTableColumn
nbsCohpmHistoricAvePDL=_NbsCohpmHistoricAvePDL_Object((1,3,6,1,4,1,629,242,23,3,1,90),_NbsCohpmHistoricAvePDL_Type())
nbsCohpmHistoricAvePDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAvePDL.setStatus(_A)
class _NbsCohpmHistoricMinPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinPDL_Type.__name__=_C
_NbsCohpmHistoricMinPDL_Object=MibTableColumn
nbsCohpmHistoricMinPDL=_NbsCohpmHistoricMinPDL_Object((1,3,6,1,4,1,629,242,23,3,1,93),_NbsCohpmHistoricMinPDL_Type())
nbsCohpmHistoricMinPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinPDL.setStatus(_A)
class _NbsCohpmHistoricMaxPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxPDL_Type.__name__=_C
_NbsCohpmHistoricMaxPDL_Object=MibTableColumn
nbsCohpmHistoricMaxPDL=_NbsCohpmHistoricMaxPDL_Object((1,3,6,1,4,1,629,242,23,3,1,96),_NbsCohpmHistoricMaxPDL_Type())
nbsCohpmHistoricMaxPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxPDL.setStatus(_A)
class _NbsCohpmHistoricAveSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricAveSOP_Type.__name__=_C
_NbsCohpmHistoricAveSOP_Object=MibTableColumn
nbsCohpmHistoricAveSOP=_NbsCohpmHistoricAveSOP_Object((1,3,6,1,4,1,629,242,23,3,1,100),_NbsCohpmHistoricAveSOP_Type())
nbsCohpmHistoricAveSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricAveSOP.setStatus(_A)
class _NbsCohpmHistoricMinSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMinSOP_Type.__name__=_C
_NbsCohpmHistoricMinSOP_Object=MibTableColumn
nbsCohpmHistoricMinSOP=_NbsCohpmHistoricMinSOP_Object((1,3,6,1,4,1,629,242,23,3,1,103),_NbsCohpmHistoricMinSOP_Type())
nbsCohpmHistoricMinSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMinSOP.setStatus(_A)
class _NbsCohpmHistoricMaxSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmHistoricMaxSOP_Type.__name__=_C
_NbsCohpmHistoricMaxSOP_Object=MibTableColumn
nbsCohpmHistoricMaxSOP=_NbsCohpmHistoricMaxSOP_Object((1,3,6,1,4,1,629,242,23,3,1,106),_NbsCohpmHistoricMaxSOP_Type())
nbsCohpmHistoricMaxSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmHistoricMaxSOP.setStatus(_A)
_NbsCohpmRunningGrp_ObjectIdentity=ObjectIdentity
nbsCohpmRunningGrp=_NbsCohpmRunningGrp_ObjectIdentity((1,3,6,1,4,1,629,242,24))
if mibBuilder.loadTexts:nbsCohpmRunningGrp.setStatus(_A)
_NbsCohpmRunningTable_Object=MibTable
nbsCohpmRunningTable=_NbsCohpmRunningTable_Object((1,3,6,1,4,1,629,242,24,3))
if mibBuilder.loadTexts:nbsCohpmRunningTable.setStatus(_A)
_NbsCohpmRunningEntry_Object=MibTableRow
nbsCohpmRunningEntry=_NbsCohpmRunningEntry_Object((1,3,6,1,4,1,629,242,24,3,1))
nbsCohpmRunningEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:nbsCohpmRunningEntry.setStatus(_A)
_NbsCohpmRunningIfIndex_Type=InterfaceIndex
_NbsCohpmRunningIfIndex_Object=MibTableColumn
nbsCohpmRunningIfIndex=_NbsCohpmRunningIfIndex_Object((1,3,6,1,4,1,629,242,24,3,1,1),_NbsCohpmRunningIfIndex_Type())
nbsCohpmRunningIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningIfIndex.setStatus(_A)
_NbsCohpmRunningDate_Type=Integer32
_NbsCohpmRunningDate_Object=MibTableColumn
nbsCohpmRunningDate=_NbsCohpmRunningDate_Object((1,3,6,1,4,1,629,242,24,3,1,5),_NbsCohpmRunningDate_Type())
nbsCohpmRunningDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningDate.setStatus(_A)
_NbsCohpmRunningTime_Type=Integer32
_NbsCohpmRunningTime_Object=MibTableColumn
nbsCohpmRunningTime=_NbsCohpmRunningTime_Object((1,3,6,1,4,1,629,242,24,3,1,6),_NbsCohpmRunningTime_Type())
nbsCohpmRunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningTime.setStatus(_A)
class _NbsCohpmRunningAveNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmRunningAveNetBERsig_Type.__name__=_E
_NbsCohpmRunningAveNetBERsig_Object=MibTableColumn
nbsCohpmRunningAveNetBERsig=_NbsCohpmRunningAveNetBERsig_Object((1,3,6,1,4,1,629,242,24,3,1,11),_NbsCohpmRunningAveNetBERsig_Type())
nbsCohpmRunningAveNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveNetBERsig.setStatus(_A)
class _NbsCohpmRunningAveNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningAveNetBERexp_Type.__name__=_E
_NbsCohpmRunningAveNetBERexp_Object=MibTableColumn
nbsCohpmRunningAveNetBERexp=_NbsCohpmRunningAveNetBERexp_Object((1,3,6,1,4,1,629,242,24,3,1,12),_NbsCohpmRunningAveNetBERexp_Type())
nbsCohpmRunningAveNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveNetBERexp.setStatus(_A)
class _NbsCohpmRunningMinNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmRunningMinNetBERsig_Type.__name__=_E
_NbsCohpmRunningMinNetBERsig_Object=MibTableColumn
nbsCohpmRunningMinNetBERsig=_NbsCohpmRunningMinNetBERsig_Object((1,3,6,1,4,1,629,242,24,3,1,14),_NbsCohpmRunningMinNetBERsig_Type())
nbsCohpmRunningMinNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinNetBERsig.setStatus(_A)
class _NbsCohpmRunningMinNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMinNetBERexp_Type.__name__=_E
_NbsCohpmRunningMinNetBERexp_Object=MibTableColumn
nbsCohpmRunningMinNetBERexp=_NbsCohpmRunningMinNetBERexp_Object((1,3,6,1,4,1,629,242,24,3,1,15),_NbsCohpmRunningMinNetBERexp_Type())
nbsCohpmRunningMinNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinNetBERexp.setStatus(_A)
class _NbsCohpmRunningMaxNetBERsig_Type(Integer32):defaultValue=0
_NbsCohpmRunningMaxNetBERsig_Type.__name__=_E
_NbsCohpmRunningMaxNetBERsig_Object=MibTableColumn
nbsCohpmRunningMaxNetBERsig=_NbsCohpmRunningMaxNetBERsig_Object((1,3,6,1,4,1,629,242,24,3,1,17),_NbsCohpmRunningMaxNetBERsig_Type())
nbsCohpmRunningMaxNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxNetBERsig.setStatus(_A)
class _NbsCohpmRunningMaxNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMaxNetBERexp_Type.__name__=_E
_NbsCohpmRunningMaxNetBERexp_Object=MibTableColumn
nbsCohpmRunningMaxNetBERexp=_NbsCohpmRunningMaxNetBERexp_Object((1,3,6,1,4,1,629,242,24,3,1,18),_NbsCohpmRunningMaxNetBERexp_Type())
nbsCohpmRunningMaxNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxNetBERexp.setStatus(_A)
class _NbsCohpmRunningAveCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningAveCD_Type.__name__=_E
_NbsCohpmRunningAveCD_Object=MibTableColumn
nbsCohpmRunningAveCD=_NbsCohpmRunningAveCD_Object((1,3,6,1,4,1,629,242,24,3,1,20),_NbsCohpmRunningAveCD_Type())
nbsCohpmRunningAveCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveCD.setStatus(_A)
class _NbsCohpmRunningMinCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMinCD_Type.__name__=_E
_NbsCohpmRunningMinCD_Object=MibTableColumn
nbsCohpmRunningMinCD=_NbsCohpmRunningMinCD_Object((1,3,6,1,4,1,629,242,24,3,1,23),_NbsCohpmRunningMinCD_Type())
nbsCohpmRunningMinCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinCD.setStatus(_A)
class _NbsCohpmRunningMaxCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMaxCD_Type.__name__=_E
_NbsCohpmRunningMaxCD_Object=MibTableColumn
nbsCohpmRunningMaxCD=_NbsCohpmRunningMaxCD_Object((1,3,6,1,4,1,629,242,24,3,1,26),_NbsCohpmRunningMaxCD_Type())
nbsCohpmRunningMaxCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxCD.setStatus(_A)
class _NbsCohpmRunningAveDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveDGD_Type.__name__=_C
_NbsCohpmRunningAveDGD_Object=MibTableColumn
nbsCohpmRunningAveDGD=_NbsCohpmRunningAveDGD_Object((1,3,6,1,4,1,629,242,24,3,1,30),_NbsCohpmRunningAveDGD_Type())
nbsCohpmRunningAveDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveDGD.setStatus(_A)
class _NbsCohpmRunningMinDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinDGD_Type.__name__=_C
_NbsCohpmRunningMinDGD_Object=MibTableColumn
nbsCohpmRunningMinDGD=_NbsCohpmRunningMinDGD_Object((1,3,6,1,4,1,629,242,24,3,1,33),_NbsCohpmRunningMinDGD_Type())
nbsCohpmRunningMinDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinDGD.setStatus(_A)
class _NbsCohpmRunningMaxDGD_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxDGD_Type.__name__=_C
_NbsCohpmRunningMaxDGD_Object=MibTableColumn
nbsCohpmRunningMaxDGD=_NbsCohpmRunningMaxDGD_Object((1,3,6,1,4,1,629,242,24,3,1,36),_NbsCohpmRunningMaxDGD_Type())
nbsCohpmRunningMaxDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxDGD.setStatus(_A)
class _NbsCohpmRunningAveQ_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveQ_Type.__name__=_C
_NbsCohpmRunningAveQ_Object=MibTableColumn
nbsCohpmRunningAveQ=_NbsCohpmRunningAveQ_Object((1,3,6,1,4,1,629,242,24,3,1,40),_NbsCohpmRunningAveQ_Type())
nbsCohpmRunningAveQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveQ.setStatus(_A)
class _NbsCohpmRunningMinQ_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinQ_Type.__name__=_C
_NbsCohpmRunningMinQ_Object=MibTableColumn
nbsCohpmRunningMinQ=_NbsCohpmRunningMinQ_Object((1,3,6,1,4,1,629,242,24,3,1,43),_NbsCohpmRunningMinQ_Type())
nbsCohpmRunningMinQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinQ.setStatus(_A)
class _NbsCohpmRunningMaxQ_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxQ_Type.__name__=_C
_NbsCohpmRunningMaxQ_Object=MibTableColumn
nbsCohpmRunningMaxQ=_NbsCohpmRunningMaxQ_Object((1,3,6,1,4,1,629,242,24,3,1,46),_NbsCohpmRunningMaxQ_Type())
nbsCohpmRunningMaxQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxQ.setStatus(_A)
class _NbsCohpmRunningAveCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningAveCFO_Type.__name__=_E
_NbsCohpmRunningAveCFO_Object=MibTableColumn
nbsCohpmRunningAveCFO=_NbsCohpmRunningAveCFO_Object((1,3,6,1,4,1,629,242,24,3,1,50),_NbsCohpmRunningAveCFO_Type())
nbsCohpmRunningAveCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveCFO.setStatus(_A)
class _NbsCohpmRunningMinCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMinCFO_Type.__name__=_E
_NbsCohpmRunningMinCFO_Object=MibTableColumn
nbsCohpmRunningMinCFO=_NbsCohpmRunningMinCFO_Object((1,3,6,1,4,1,629,242,24,3,1,53),_NbsCohpmRunningMinCFO_Type())
nbsCohpmRunningMinCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinCFO.setStatus(_A)
class _NbsCohpmRunningMaxCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCohpmRunningMaxCFO_Type.__name__=_E
_NbsCohpmRunningMaxCFO_Object=MibTableColumn
nbsCohpmRunningMaxCFO=_NbsCohpmRunningMaxCFO_Object((1,3,6,1,4,1,629,242,24,3,1,56),_NbsCohpmRunningMaxCFO_Type())
nbsCohpmRunningMaxCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxCFO.setStatus(_A)
class _NbsCohpmRunningAveOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveOSNR_Type.__name__=_C
_NbsCohpmRunningAveOSNR_Object=MibTableColumn
nbsCohpmRunningAveOSNR=_NbsCohpmRunningAveOSNR_Object((1,3,6,1,4,1,629,242,24,3,1,60),_NbsCohpmRunningAveOSNR_Type())
nbsCohpmRunningAveOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveOSNR.setStatus(_A)
class _NbsCohpmRunningMinOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinOSNR_Type.__name__=_C
_NbsCohpmRunningMinOSNR_Object=MibTableColumn
nbsCohpmRunningMinOSNR=_NbsCohpmRunningMinOSNR_Object((1,3,6,1,4,1,629,242,24,3,1,63),_NbsCohpmRunningMinOSNR_Type())
nbsCohpmRunningMinOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinOSNR.setStatus(_A)
class _NbsCohpmRunningMaxOSNR_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxOSNR_Type.__name__=_C
_NbsCohpmRunningMaxOSNR_Object=MibTableColumn
nbsCohpmRunningMaxOSNR=_NbsCohpmRunningMaxOSNR_Object((1,3,6,1,4,1,629,242,24,3,1,66),_NbsCohpmRunningMaxOSNR_Type())
nbsCohpmRunningMaxOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxOSNR.setStatus(_A)
class _NbsCohpmRunningAveSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveSNRx_Type.__name__=_C
_NbsCohpmRunningAveSNRx_Object=MibTableColumn
nbsCohpmRunningAveSNRx=_NbsCohpmRunningAveSNRx_Object((1,3,6,1,4,1,629,242,24,3,1,70),_NbsCohpmRunningAveSNRx_Type())
nbsCohpmRunningAveSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveSNRx.setStatus(_A)
class _NbsCohpmRunningMinSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinSNRx_Type.__name__=_C
_NbsCohpmRunningMinSNRx_Object=MibTableColumn
nbsCohpmRunningMinSNRx=_NbsCohpmRunningMinSNRx_Object((1,3,6,1,4,1,629,242,24,3,1,73),_NbsCohpmRunningMinSNRx_Type())
nbsCohpmRunningMinSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinSNRx.setStatus(_A)
class _NbsCohpmRunningMaxSNRx_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxSNRx_Type.__name__=_C
_NbsCohpmRunningMaxSNRx_Object=MibTableColumn
nbsCohpmRunningMaxSNRx=_NbsCohpmRunningMaxSNRx_Object((1,3,6,1,4,1,629,242,24,3,1,76),_NbsCohpmRunningMaxSNRx_Type())
nbsCohpmRunningMaxSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxSNRx.setStatus(_A)
class _NbsCohpmRunningAveSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveSNRy_Type.__name__=_C
_NbsCohpmRunningAveSNRy_Object=MibTableColumn
nbsCohpmRunningAveSNRy=_NbsCohpmRunningAveSNRy_Object((1,3,6,1,4,1,629,242,24,3,1,80),_NbsCohpmRunningAveSNRy_Type())
nbsCohpmRunningAveSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveSNRy.setStatus(_A)
class _NbsCohpmRunningMinSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinSNRy_Type.__name__=_C
_NbsCohpmRunningMinSNRy_Object=MibTableColumn
nbsCohpmRunningMinSNRy=_NbsCohpmRunningMinSNRy_Object((1,3,6,1,4,1,629,242,24,3,1,83),_NbsCohpmRunningMinSNRy_Type())
nbsCohpmRunningMinSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinSNRy.setStatus(_A)
class _NbsCohpmRunningMaxSNRy_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxSNRy_Type.__name__=_C
_NbsCohpmRunningMaxSNRy_Object=MibTableColumn
nbsCohpmRunningMaxSNRy=_NbsCohpmRunningMaxSNRy_Object((1,3,6,1,4,1,629,242,24,3,1,86),_NbsCohpmRunningMaxSNRy_Type())
nbsCohpmRunningMaxSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxSNRy.setStatus(_A)
class _NbsCohpmRunningAvePDL_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAvePDL_Type.__name__=_C
_NbsCohpmRunningAvePDL_Object=MibTableColumn
nbsCohpmRunningAvePDL=_NbsCohpmRunningAvePDL_Object((1,3,6,1,4,1,629,242,24,3,1,90),_NbsCohpmRunningAvePDL_Type())
nbsCohpmRunningAvePDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAvePDL.setStatus(_A)
class _NbsCohpmRunningMinPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinPDL_Type.__name__=_C
_NbsCohpmRunningMinPDL_Object=MibTableColumn
nbsCohpmRunningMinPDL=_NbsCohpmRunningMinPDL_Object((1,3,6,1,4,1,629,242,24,3,1,93),_NbsCohpmRunningMinPDL_Type())
nbsCohpmRunningMinPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinPDL.setStatus(_A)
class _NbsCohpmRunningMaxPDL_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxPDL_Type.__name__=_C
_NbsCohpmRunningMaxPDL_Object=MibTableColumn
nbsCohpmRunningMaxPDL=_NbsCohpmRunningMaxPDL_Object((1,3,6,1,4,1,629,242,24,3,1,96),_NbsCohpmRunningMaxPDL_Type())
nbsCohpmRunningMaxPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxPDL.setStatus(_A)
class _NbsCohpmRunningAveSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningAveSOP_Type.__name__=_C
_NbsCohpmRunningAveSOP_Object=MibTableColumn
nbsCohpmRunningAveSOP=_NbsCohpmRunningAveSOP_Object((1,3,6,1,4,1,629,242,24,3,1,100),_NbsCohpmRunningAveSOP_Type())
nbsCohpmRunningAveSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningAveSOP.setStatus(_A)
class _NbsCohpmRunningMinSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMinSOP_Type.__name__=_C
_NbsCohpmRunningMinSOP_Object=MibTableColumn
nbsCohpmRunningMinSOP=_NbsCohpmRunningMinSOP_Object((1,3,6,1,4,1,629,242,24,3,1,103),_NbsCohpmRunningMinSOP_Type())
nbsCohpmRunningMinSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMinSOP.setStatus(_A)
class _NbsCohpmRunningMaxSOP_Type(Unsigned32):defaultValue=0
_NbsCohpmRunningMaxSOP_Type.__name__=_C
_NbsCohpmRunningMaxSOP_Object=MibTableColumn
nbsCohpmRunningMaxSOP=_NbsCohpmRunningMaxSOP_Object((1,3,6,1,4,1,629,242,24,3,1,106),_NbsCohpmRunningMaxSOP_Type())
nbsCohpmRunningMaxSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCohpmRunningMaxSOP.setStatus(_A)
_NbsCoherentStatsGrp_ObjectIdentity=ObjectIdentity
nbsCoherentStatsGrp=_NbsCoherentStatsGrp_ObjectIdentity((1,3,6,1,4,1,629,242,90))
if mibBuilder.loadTexts:nbsCoherentStatsGrp.setStatus(_A)
_NbsCoherentStatsTable_Object=MibTable
nbsCoherentStatsTable=_NbsCoherentStatsTable_Object((1,3,6,1,4,1,629,242,90,2))
if mibBuilder.loadTexts:nbsCoherentStatsTable.setStatus(_A)
_NbsCoherentStatsEntry_Object=MibTableRow
nbsCoherentStatsEntry=_NbsCoherentStatsEntry_Object((1,3,6,1,4,1,629,242,90,2,1))
nbsCoherentStatsEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:nbsCoherentStatsEntry.setStatus(_A)
_NbsCoherentStatsIfIndex_Type=InterfaceIndex
_NbsCoherentStatsIfIndex_Object=MibTableColumn
nbsCoherentStatsIfIndex=_NbsCoherentStatsIfIndex_Object((1,3,6,1,4,1,629,242,90,2,1,1),_NbsCoherentStatsIfIndex_Type())
nbsCoherentStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsIfIndex.setStatus(_A)
_NbsCoherentStatsDate_Type=Integer32
_NbsCoherentStatsDate_Object=MibTableColumn
nbsCoherentStatsDate=_NbsCoherentStatsDate_Object((1,3,6,1,4,1,629,242,90,2,1,5),_NbsCoherentStatsDate_Type())
nbsCoherentStatsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsDate.setStatus(_A)
_NbsCoherentStatsTime_Type=Integer32
_NbsCoherentStatsTime_Object=MibTableColumn
nbsCoherentStatsTime=_NbsCoherentStatsTime_Object((1,3,6,1,4,1,629,242,90,2,1,6),_NbsCoherentStatsTime_Type())
nbsCoherentStatsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsTime.setStatus(_A)
_NbsCoherentStatsSpan_Type=Integer32
_NbsCoherentStatsSpan_Object=MibTableColumn
nbsCoherentStatsSpan=_NbsCoherentStatsSpan_Object((1,3,6,1,4,1,629,242,90,2,1,7),_NbsCoherentStatsSpan_Type())
nbsCoherentStatsSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsSpan.setStatus(_A)
class _NbsCoherentStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('counting',2),('clearing',3),('stopped',4),('resumed',5)))
_NbsCoherentStatsState_Type.__name__=_E
_NbsCoherentStatsState_Object=MibTableColumn
nbsCoherentStatsState=_NbsCoherentStatsState_Object((1,3,6,1,4,1,629,242,90,2,1,8),_NbsCoherentStatsState_Type())
nbsCoherentStatsState.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsCoherentStatsState.setStatus(_A)
class _NbsCoherentStatsAveNetBERsig_Type(Integer32):defaultValue=0
_NbsCoherentStatsAveNetBERsig_Type.__name__=_E
_NbsCoherentStatsAveNetBERsig_Object=MibTableColumn
nbsCoherentStatsAveNetBERsig=_NbsCoherentStatsAveNetBERsig_Object((1,3,6,1,4,1,629,242,90,2,1,11),_NbsCoherentStatsAveNetBERsig_Type())
nbsCoherentStatsAveNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveNetBERsig.setStatus(_A)
class _NbsCoherentStatsAveNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsAveNetBERexp_Type.__name__=_E
_NbsCoherentStatsAveNetBERexp_Object=MibTableColumn
nbsCoherentStatsAveNetBERexp=_NbsCoherentStatsAveNetBERexp_Object((1,3,6,1,4,1,629,242,90,2,1,12),_NbsCoherentStatsAveNetBERexp_Type())
nbsCoherentStatsAveNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveNetBERexp.setStatus(_A)
class _NbsCoherentStatsMinNetBERsig_Type(Integer32):defaultValue=0
_NbsCoherentStatsMinNetBERsig_Type.__name__=_E
_NbsCoherentStatsMinNetBERsig_Object=MibTableColumn
nbsCoherentStatsMinNetBERsig=_NbsCoherentStatsMinNetBERsig_Object((1,3,6,1,4,1,629,242,90,2,1,14),_NbsCoherentStatsMinNetBERsig_Type())
nbsCoherentStatsMinNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinNetBERsig.setStatus(_A)
class _NbsCoherentStatsMinNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMinNetBERexp_Type.__name__=_E
_NbsCoherentStatsMinNetBERexp_Object=MibTableColumn
nbsCoherentStatsMinNetBERexp=_NbsCoherentStatsMinNetBERexp_Object((1,3,6,1,4,1,629,242,90,2,1,15),_NbsCoherentStatsMinNetBERexp_Type())
nbsCoherentStatsMinNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinNetBERexp.setStatus(_A)
class _NbsCoherentStatsMaxNetBERsig_Type(Integer32):defaultValue=0
_NbsCoherentStatsMaxNetBERsig_Type.__name__=_E
_NbsCoherentStatsMaxNetBERsig_Object=MibTableColumn
nbsCoherentStatsMaxNetBERsig=_NbsCoherentStatsMaxNetBERsig_Object((1,3,6,1,4,1,629,242,90,2,1,17),_NbsCoherentStatsMaxNetBERsig_Type())
nbsCoherentStatsMaxNetBERsig.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxNetBERsig.setStatus(_A)
class _NbsCoherentStatsMaxNetBERexp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMaxNetBERexp_Type.__name__=_E
_NbsCoherentStatsMaxNetBERexp_Object=MibTableColumn
nbsCoherentStatsMaxNetBERexp=_NbsCoherentStatsMaxNetBERexp_Object((1,3,6,1,4,1,629,242,90,2,1,18),_NbsCoherentStatsMaxNetBERexp_Type())
nbsCoherentStatsMaxNetBERexp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxNetBERexp.setStatus(_A)
class _NbsCoherentStatsAveCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsAveCD_Type.__name__=_E
_NbsCoherentStatsAveCD_Object=MibTableColumn
nbsCoherentStatsAveCD=_NbsCoherentStatsAveCD_Object((1,3,6,1,4,1,629,242,90,2,1,20),_NbsCoherentStatsAveCD_Type())
nbsCoherentStatsAveCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveCD.setStatus(_A)
class _NbsCoherentStatsMinCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMinCD_Type.__name__=_E
_NbsCoherentStatsMinCD_Object=MibTableColumn
nbsCoherentStatsMinCD=_NbsCoherentStatsMinCD_Object((1,3,6,1,4,1,629,242,90,2,1,23),_NbsCoherentStatsMinCD_Type())
nbsCoherentStatsMinCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinCD.setStatus(_A)
class _NbsCoherentStatsMaxCD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMaxCD_Type.__name__=_E
_NbsCoherentStatsMaxCD_Object=MibTableColumn
nbsCoherentStatsMaxCD=_NbsCoherentStatsMaxCD_Object((1,3,6,1,4,1,629,242,90,2,1,26),_NbsCoherentStatsMaxCD_Type())
nbsCoherentStatsMaxCD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxCD.setStatus(_A)
class _NbsCoherentStatsAveDGD_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveDGD_Type.__name__=_C
_NbsCoherentStatsAveDGD_Object=MibTableColumn
nbsCoherentStatsAveDGD=_NbsCoherentStatsAveDGD_Object((1,3,6,1,4,1,629,242,90,2,1,30),_NbsCoherentStatsAveDGD_Type())
nbsCoherentStatsAveDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveDGD.setStatus(_A)
class _NbsCoherentStatsMinDGD_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinDGD_Type.__name__=_C
_NbsCoherentStatsMinDGD_Object=MibTableColumn
nbsCoherentStatsMinDGD=_NbsCoherentStatsMinDGD_Object((1,3,6,1,4,1,629,242,90,2,1,33),_NbsCoherentStatsMinDGD_Type())
nbsCoherentStatsMinDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinDGD.setStatus(_A)
class _NbsCoherentStatsMaxDGD_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxDGD_Type.__name__=_C
_NbsCoherentStatsMaxDGD_Object=MibTableColumn
nbsCoherentStatsMaxDGD=_NbsCoherentStatsMaxDGD_Object((1,3,6,1,4,1,629,242,90,2,1,36),_NbsCoherentStatsMaxDGD_Type())
nbsCoherentStatsMaxDGD.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxDGD.setStatus(_A)
class _NbsCoherentStatsAveQ_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveQ_Type.__name__=_C
_NbsCoherentStatsAveQ_Object=MibTableColumn
nbsCoherentStatsAveQ=_NbsCoherentStatsAveQ_Object((1,3,6,1,4,1,629,242,90,2,1,40),_NbsCoherentStatsAveQ_Type())
nbsCoherentStatsAveQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveQ.setStatus(_A)
class _NbsCoherentStatsMinQ_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinQ_Type.__name__=_C
_NbsCoherentStatsMinQ_Object=MibTableColumn
nbsCoherentStatsMinQ=_NbsCoherentStatsMinQ_Object((1,3,6,1,4,1,629,242,90,2,1,43),_NbsCoherentStatsMinQ_Type())
nbsCoherentStatsMinQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinQ.setStatus(_A)
class _NbsCoherentStatsMaxQ_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxQ_Type.__name__=_C
_NbsCoherentStatsMaxQ_Object=MibTableColumn
nbsCoherentStatsMaxQ=_NbsCoherentStatsMaxQ_Object((1,3,6,1,4,1,629,242,90,2,1,46),_NbsCoherentStatsMaxQ_Type())
nbsCoherentStatsMaxQ.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxQ.setStatus(_A)
class _NbsCoherentStatsAveCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsAveCFO_Type.__name__=_E
_NbsCoherentStatsAveCFO_Object=MibTableColumn
nbsCoherentStatsAveCFO=_NbsCoherentStatsAveCFO_Object((1,3,6,1,4,1,629,242,90,2,1,50),_NbsCoherentStatsAveCFO_Type())
nbsCoherentStatsAveCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveCFO.setStatus(_A)
class _NbsCoherentStatsMinCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMinCFO_Type.__name__=_E
_NbsCoherentStatsMinCFO_Object=MibTableColumn
nbsCoherentStatsMinCFO=_NbsCoherentStatsMinCFO_Object((1,3,6,1,4,1,629,242,90,2,1,53),_NbsCoherentStatsMinCFO_Type())
nbsCoherentStatsMinCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinCFO.setStatus(_A)
class _NbsCoherentStatsMaxCFO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsCoherentStatsMaxCFO_Type.__name__=_E
_NbsCoherentStatsMaxCFO_Object=MibTableColumn
nbsCoherentStatsMaxCFO=_NbsCoherentStatsMaxCFO_Object((1,3,6,1,4,1,629,242,90,2,1,56),_NbsCoherentStatsMaxCFO_Type())
nbsCoherentStatsMaxCFO.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxCFO.setStatus(_A)
class _NbsCoherentStatsAveOSNR_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveOSNR_Type.__name__=_C
_NbsCoherentStatsAveOSNR_Object=MibTableColumn
nbsCoherentStatsAveOSNR=_NbsCoherentStatsAveOSNR_Object((1,3,6,1,4,1,629,242,90,2,1,60),_NbsCoherentStatsAveOSNR_Type())
nbsCoherentStatsAveOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveOSNR.setStatus(_A)
class _NbsCoherentStatsMinOSNR_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinOSNR_Type.__name__=_C
_NbsCoherentStatsMinOSNR_Object=MibTableColumn
nbsCoherentStatsMinOSNR=_NbsCoherentStatsMinOSNR_Object((1,3,6,1,4,1,629,242,90,2,1,63),_NbsCoherentStatsMinOSNR_Type())
nbsCoherentStatsMinOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinOSNR.setStatus(_A)
class _NbsCoherentStatsMaxOSNR_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxOSNR_Type.__name__=_C
_NbsCoherentStatsMaxOSNR_Object=MibTableColumn
nbsCoherentStatsMaxOSNR=_NbsCoherentStatsMaxOSNR_Object((1,3,6,1,4,1,629,242,90,2,1,66),_NbsCoherentStatsMaxOSNR_Type())
nbsCoherentStatsMaxOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxOSNR.setStatus(_A)
class _NbsCoherentStatsAveSNRx_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveSNRx_Type.__name__=_C
_NbsCoherentStatsAveSNRx_Object=MibTableColumn
nbsCoherentStatsAveSNRx=_NbsCoherentStatsAveSNRx_Object((1,3,6,1,4,1,629,242,90,2,1,70),_NbsCoherentStatsAveSNRx_Type())
nbsCoherentStatsAveSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveSNRx.setStatus(_A)
class _NbsCoherentStatsMinSNRx_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinSNRx_Type.__name__=_C
_NbsCoherentStatsMinSNRx_Object=MibTableColumn
nbsCoherentStatsMinSNRx=_NbsCoherentStatsMinSNRx_Object((1,3,6,1,4,1,629,242,90,2,1,73),_NbsCoherentStatsMinSNRx_Type())
nbsCoherentStatsMinSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinSNRx.setStatus(_A)
class _NbsCoherentStatsMaxSNRx_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxSNRx_Type.__name__=_C
_NbsCoherentStatsMaxSNRx_Object=MibTableColumn
nbsCoherentStatsMaxSNRx=_NbsCoherentStatsMaxSNRx_Object((1,3,6,1,4,1,629,242,90,2,1,76),_NbsCoherentStatsMaxSNRx_Type())
nbsCoherentStatsMaxSNRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxSNRx.setStatus(_A)
class _NbsCoherentStatsAveSNRy_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveSNRy_Type.__name__=_C
_NbsCoherentStatsAveSNRy_Object=MibTableColumn
nbsCoherentStatsAveSNRy=_NbsCoherentStatsAveSNRy_Object((1,3,6,1,4,1,629,242,90,2,1,80),_NbsCoherentStatsAveSNRy_Type())
nbsCoherentStatsAveSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveSNRy.setStatus(_A)
class _NbsCoherentStatsMinSNRy_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinSNRy_Type.__name__=_C
_NbsCoherentStatsMinSNRy_Object=MibTableColumn
nbsCoherentStatsMinSNRy=_NbsCoherentStatsMinSNRy_Object((1,3,6,1,4,1,629,242,90,2,1,83),_NbsCoherentStatsMinSNRy_Type())
nbsCoherentStatsMinSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinSNRy.setStatus(_A)
class _NbsCoherentStatsMaxSNRy_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxSNRy_Type.__name__=_C
_NbsCoherentStatsMaxSNRy_Object=MibTableColumn
nbsCoherentStatsMaxSNRy=_NbsCoherentStatsMaxSNRy_Object((1,3,6,1,4,1,629,242,90,2,1,86),_NbsCoherentStatsMaxSNRy_Type())
nbsCoherentStatsMaxSNRy.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxSNRy.setStatus(_A)
class _NbsCoherentStatsAvePDL_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAvePDL_Type.__name__=_C
_NbsCoherentStatsAvePDL_Object=MibTableColumn
nbsCoherentStatsAvePDL=_NbsCoherentStatsAvePDL_Object((1,3,6,1,4,1,629,242,90,2,1,90),_NbsCoherentStatsAvePDL_Type())
nbsCoherentStatsAvePDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAvePDL.setStatus(_A)
class _NbsCoherentStatsMinPDL_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinPDL_Type.__name__=_C
_NbsCoherentStatsMinPDL_Object=MibTableColumn
nbsCoherentStatsMinPDL=_NbsCoherentStatsMinPDL_Object((1,3,6,1,4,1,629,242,90,2,1,93),_NbsCoherentStatsMinPDL_Type())
nbsCoherentStatsMinPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinPDL.setStatus(_A)
class _NbsCoherentStatsMaxPDL_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxPDL_Type.__name__=_C
_NbsCoherentStatsMaxPDL_Object=MibTableColumn
nbsCoherentStatsMaxPDL=_NbsCoherentStatsMaxPDL_Object((1,3,6,1,4,1,629,242,90,2,1,96),_NbsCoherentStatsMaxPDL_Type())
nbsCoherentStatsMaxPDL.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxPDL.setStatus(_A)
class _NbsCoherentStatsAveSOP_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsAveSOP_Type.__name__=_C
_NbsCoherentStatsAveSOP_Object=MibTableColumn
nbsCoherentStatsAveSOP=_NbsCoherentStatsAveSOP_Object((1,3,6,1,4,1,629,242,90,2,1,100),_NbsCoherentStatsAveSOP_Type())
nbsCoherentStatsAveSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsAveSOP.setStatus(_A)
class _NbsCoherentStatsMinSOP_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMinSOP_Type.__name__=_C
_NbsCoherentStatsMinSOP_Object=MibTableColumn
nbsCoherentStatsMinSOP=_NbsCoherentStatsMinSOP_Object((1,3,6,1,4,1,629,242,90,2,1,103),_NbsCoherentStatsMinSOP_Type())
nbsCoherentStatsMinSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMinSOP.setStatus(_A)
class _NbsCoherentStatsMaxSOP_Type(Unsigned32):defaultValue=0
_NbsCoherentStatsMaxSOP_Type.__name__=_C
_NbsCoherentStatsMaxSOP_Object=MibTableColumn
nbsCoherentStatsMaxSOP=_NbsCoherentStatsMaxSOP_Object((1,3,6,1,4,1,629,242,90,2,1,106),_NbsCoherentStatsMaxSOP_Type())
nbsCoherentStatsMaxSOP.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsCoherentStatsMaxSOP.setStatus(_A)
_NbsCohpmEventsGrp_ObjectIdentity=ObjectIdentity
nbsCohpmEventsGrp=_NbsCohpmEventsGrp_ObjectIdentity((1,3,6,1,4,1,629,242,100))
if mibBuilder.loadTexts:nbsCohpmEventsGrp.setStatus(_A)
_NbsCohpmTraps_ObjectIdentity=ObjectIdentity
nbsCohpmTraps=_NbsCohpmTraps_ObjectIdentity((1,3,6,1,4,1,629,242,100,0))
if mibBuilder.loadTexts:nbsCohpmTraps.setStatus(_A)
nbsCohpmTrapsAveBER=NotificationType((1,3,6,1,4,1,629,242,100,0,11))
nbsCohpmTrapsAveBER.setObjects(*((_D,_G),(_D,_H),(_D,_Y),(_D,_Z)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveBER.setStatus(_A)
nbsCohpmTrapsMinBER=NotificationType((1,3,6,1,4,1,629,242,100,0,14))
nbsCohpmTrapsMinBER.setObjects(*((_D,_G),(_D,_H),(_D,_a),(_D,_b)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinBER.setStatus(_A)
nbsCohpmTrapsMaxBER=NotificationType((1,3,6,1,4,1,629,242,100,0,17))
nbsCohpmTrapsMaxBER.setObjects(*((_D,_G),(_D,_H),(_D,_c),(_D,_d)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxBER.setStatus(_A)
nbsCohpmTrapsAveCD=NotificationType((1,3,6,1,4,1,629,242,100,0,20))
nbsCohpmTrapsAveCD.setObjects(*((_D,_G),(_D,_H),(_D,_e)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveCD.setStatus(_A)
nbsCohpmTrapsMinCD=NotificationType((1,3,6,1,4,1,629,242,100,0,23))
nbsCohpmTrapsMinCD.setObjects(*((_D,_G),(_D,_H),(_D,_f)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinCD.setStatus(_A)
nbsCohpmTrapsMaxCD=NotificationType((1,3,6,1,4,1,629,242,100,0,26))
nbsCohpmTrapsMaxCD.setObjects(*((_D,_G),(_D,_H),(_D,_g)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxCD.setStatus(_A)
nbsCohpmTrapsAveDGD=NotificationType((1,3,6,1,4,1,629,242,100,0,30))
nbsCohpmTrapsAveDGD.setObjects(*((_D,_G),(_D,_H),(_D,_h)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveDGD.setStatus(_A)
nbsCohpmTrapsMinDGD=NotificationType((1,3,6,1,4,1,629,242,100,0,33))
nbsCohpmTrapsMinDGD.setObjects(*((_D,_G),(_D,_H),(_D,_i)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinDGD.setStatus(_A)
nbsCohpmTrapsMaxDGD=NotificationType((1,3,6,1,4,1,629,242,100,0,36))
nbsCohpmTrapsMaxDGD.setObjects(*((_D,_G),(_D,_H),(_D,_j)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxDGD.setStatus(_A)
nbsCohpmTrapsAveQ=NotificationType((1,3,6,1,4,1,629,242,100,0,40))
nbsCohpmTrapsAveQ.setObjects(*((_D,_G),(_D,_H),(_D,_k)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveQ.setStatus(_A)
nbsCohpmTrapsMinQ=NotificationType((1,3,6,1,4,1,629,242,100,0,43))
nbsCohpmTrapsMinQ.setObjects(*((_D,_G),(_D,_H),(_D,_l)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinQ.setStatus(_A)
nbsCohpmTrapsMaxQ=NotificationType((1,3,6,1,4,1,629,242,100,0,46))
nbsCohpmTrapsMaxQ.setObjects(*((_D,_G),(_D,_H),(_D,_m)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxQ.setStatus(_A)
nbsCohpmTrapsAveCFO=NotificationType((1,3,6,1,4,1,629,242,100,0,50))
nbsCohpmTrapsAveCFO.setObjects(*((_D,_G),(_D,_H),(_D,_n)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveCFO.setStatus(_A)
nbsCohpmTrapsMinCFO=NotificationType((1,3,6,1,4,1,629,242,100,0,53))
nbsCohpmTrapsMinCFO.setObjects(*((_D,_G),(_D,_H),(_D,_o)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinCFO.setStatus(_A)
nbsCohpmTrapsMaxCFO=NotificationType((1,3,6,1,4,1,629,242,100,0,56))
nbsCohpmTrapsMaxCFO.setObjects(*((_D,_G),(_D,_H),(_D,_p)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxCFO.setStatus(_A)
nbsCohpmTrapsAveOSNR=NotificationType((1,3,6,1,4,1,629,242,100,0,60))
nbsCohpmTrapsAveOSNR.setObjects(*((_D,_G),(_D,_H),(_D,_q)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveOSNR.setStatus(_A)
nbsCohpmTrapsMinOSNR=NotificationType((1,3,6,1,4,1,629,242,100,0,63))
nbsCohpmTrapsMinOSNR.setObjects(*((_D,_G),(_D,_H),(_D,_r)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinOSNR.setStatus(_A)
nbsCohpmTrapsMaxOSNR=NotificationType((1,3,6,1,4,1,629,242,100,0,66))
nbsCohpmTrapsMaxOSNR.setObjects(*((_D,_G),(_D,_H),(_D,_s)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxOSNR.setStatus(_A)
nbsCohpmTrapsAveSNRx=NotificationType((1,3,6,1,4,1,629,242,100,0,70))
nbsCohpmTrapsAveSNRx.setObjects(*((_D,_G),(_D,_H),(_D,_t)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveSNRx.setStatus(_A)
nbsCohpmTrapsMinSNRx=NotificationType((1,3,6,1,4,1,629,242,100,0,73))
nbsCohpmTrapsMinSNRx.setObjects(*((_D,_G),(_D,_H),(_D,_u)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinSNRx.setStatus(_A)
nbsCohpmTrapsMaxSNRx=NotificationType((1,3,6,1,4,1,629,242,100,0,76))
nbsCohpmTrapsMaxSNRx.setObjects(*((_D,_G),(_D,_H),(_D,_v)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxSNRx.setStatus(_A)
nbsCohpmTrapsAveSNRy=NotificationType((1,3,6,1,4,1,629,242,100,0,80))
nbsCohpmTrapsAveSNRy.setObjects(*((_D,_G),(_D,_H),(_D,_w)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveSNRy.setStatus(_A)
nbsCohpmTrapsMinSNRy=NotificationType((1,3,6,1,4,1,629,242,100,0,83))
nbsCohpmTrapsMinSNRy.setObjects(*((_D,_G),(_D,_H),(_D,_x)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinSNRy.setStatus(_A)
nbsCohpmTrapsMaxSNRy=NotificationType((1,3,6,1,4,1,629,242,100,0,86))
nbsCohpmTrapsMaxSNRy.setObjects(*((_D,_G),(_D,_H),(_D,_y)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxSNRy.setStatus(_A)
nbsCohpmTrapsAvePDL=NotificationType((1,3,6,1,4,1,629,242,100,0,90))
nbsCohpmTrapsAvePDL.setObjects(*((_D,_G),(_D,_H),(_D,_z)))
if mibBuilder.loadTexts:nbsCohpmTrapsAvePDL.setStatus(_A)
nbsCohpmTrapsMinPDL=NotificationType((1,3,6,1,4,1,629,242,100,0,93))
nbsCohpmTrapsMinPDL.setObjects(*((_D,_G),(_D,_H),(_D,_A0)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinPDL.setStatus(_A)
nbsCohpmTrapsMaxPDL=NotificationType((1,3,6,1,4,1,629,242,100,0,96))
nbsCohpmTrapsMaxPDL.setObjects(*((_D,_G),(_D,_H),(_D,_A1)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxPDL.setStatus(_A)
nbsCohpmTrapsAveSOP=NotificationType((1,3,6,1,4,1,629,242,100,0,100))
nbsCohpmTrapsAveSOP.setObjects(*((_D,_G),(_D,_H),(_D,_A2)))
if mibBuilder.loadTexts:nbsCohpmTrapsAveSOP.setStatus(_A)
nbsCohpmTrapsMinSOP=NotificationType((1,3,6,1,4,1,629,242,100,0,103))
nbsCohpmTrapsMinSOP.setObjects(*((_D,_G),(_D,_H),(_D,_A3)))
if mibBuilder.loadTexts:nbsCohpmTrapsMinSOP.setStatus(_A)
nbsCohpmTrapsMaxSOP=NotificationType((1,3,6,1,4,1,629,242,100,0,106))
nbsCohpmTrapsMaxSOP.setObjects(*((_D,_G),(_D,_H),(_D,_A4)))
if mibBuilder.loadTexts:nbsCohpmTrapsMaxSOP.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsCoherentMib':nbsCoherentMib,'nbsCoherentCfgGrp':nbsCoherentCfgGrp,'nbsCoherentCfgTable':nbsCoherentCfgTable,'nbsCoherentCfgEntry':nbsCoherentCfgEntry,_M:nbsCoherentCfgIfIndex,'nbsCoherentCfgCDmodeCaps':nbsCoherentCfgCDmodeCaps,'nbsCoherentCfgCDmodeAdmin':nbsCoherentCfgCDmodeAdmin,'nbsCoherentCfgCDmodeOper':nbsCoherentCfgCDmodeOper,'nbsCoherentCfgCDautolAdmin':nbsCoherentCfgCDautolAdmin,'nbsCoherentCfgCDautolOper':nbsCoherentCfgCDautolOper,'nbsCoherentCfgCDautohAdmin':nbsCoherentCfgCDautohAdmin,'nbsCoherentCfgCDautohOper':nbsCoherentCfgCDautohOper,'nbsCoherentCfgCDfixedAdmin':nbsCoherentCfgCDfixedAdmin,'nbsCoherentCfgCDfixedOper':nbsCoherentCfgCDfixedOper,'nbsCoherentCfgSOPmodeAdmin':nbsCoherentCfgSOPmodeAdmin,'nbsCoherentCfgSOPmodeOper':nbsCoherentCfgSOPmodeOper,'nbsCohpmThresholdsGrp':nbsCohpmThresholdsGrp,'nbsCohpmThresholdsTable':nbsCohpmThresholdsTable,'nbsCohpmThresholdsEntry':nbsCohpmThresholdsEntry,_Q:nbsCohpmThresholdsIfIndex,_R:nbsCohpmThresholdsInterval,'nbsCohpmThresholdsAveNetBERsig':nbsCohpmThresholdsAveNetBERsig,'nbsCohpmThresholdsAveNetBERexp':nbsCohpmThresholdsAveNetBERexp,'nbsCohpmThresholdsMinNetBERsig':nbsCohpmThresholdsMinNetBERsig,'nbsCohpmThresholdsMinNetBERexp':nbsCohpmThresholdsMinNetBERexp,'nbsCohpmThresholdsMaxNetBERsig':nbsCohpmThresholdsMaxNetBERsig,'nbsCohpmThresholdsMaxNetBERexp':nbsCohpmThresholdsMaxNetBERexp,'nbsCohpmThresholdsAveCD':nbsCohpmThresholdsAveCD,'nbsCohpmThresholdsMinCD':nbsCohpmThresholdsMinCD,'nbsCohpmThresholdsMaxCD':nbsCohpmThresholdsMaxCD,'nbsCohpmThresholdsAveDGD':nbsCohpmThresholdsAveDGD,'nbsCohpmThresholdsMinDGD':nbsCohpmThresholdsMinDGD,'nbsCohpmThresholdsMaxDGD':nbsCohpmThresholdsMaxDGD,'nbsCohpmThresholdsAveQ':nbsCohpmThresholdsAveQ,'nbsCohpmThresholdsMinQ':nbsCohpmThresholdsMinQ,'nbsCohpmThresholdsMaxQ':nbsCohpmThresholdsMaxQ,'nbsCohpmThresholdsAveCFO':nbsCohpmThresholdsAveCFO,'nbsCohpmThresholdsMinCFO':nbsCohpmThresholdsMinCFO,'nbsCohpmThresholdsMaxCFO':nbsCohpmThresholdsMaxCFO,'nbsCohpmThresholdsAveOSNR':nbsCohpmThresholdsAveOSNR,'nbsCohpmThresholdsMinOSNR':nbsCohpmThresholdsMinOSNR,'nbsCohpmThresholdsMaxOSNR':nbsCohpmThresholdsMaxOSNR,'nbsCohpmThresholdsAveSNRx':nbsCohpmThresholdsAveSNRx,'nbsCohpmThresholdsMinSNRx':nbsCohpmThresholdsMinSNRx,'nbsCohpmThresholdsMaxSNRx':nbsCohpmThresholdsMaxSNRx,'nbsCohpmThresholdsAveSNRy':nbsCohpmThresholdsAveSNRy,'nbsCohpmThresholdsMinSNRy':nbsCohpmThresholdsMinSNRy,'nbsCohpmThresholdsMaxSNRy':nbsCohpmThresholdsMaxSNRy,'nbsCohpmThresholdsAvePDL':nbsCohpmThresholdsAvePDL,'nbsCohpmThresholdsMinPDL':nbsCohpmThresholdsMinPDL,'nbsCohpmThresholdsMaxPDL':nbsCohpmThresholdsMaxPDL,'nbsCohpmThresholdsAveSOP':nbsCohpmThresholdsAveSOP,'nbsCohpmThresholdsMinSOP':nbsCohpmThresholdsMinSOP,'nbsCohpmThresholdsMaxSOP':nbsCohpmThresholdsMaxSOP,'nbsCohpmCurrentGrp':nbsCohpmCurrentGrp,'nbsCohpmCurrentTable':nbsCohpmCurrentTable,'nbsCohpmCurrentEntry':nbsCohpmCurrentEntry,_G:nbsCohpmCurrentIfIndex,_H:nbsCohpmCurrentInterval,'nbsCohpmCurrentDate':nbsCohpmCurrentDate,'nbsCohpmCurrentTime':nbsCohpmCurrentTime,_Y:nbsCohpmCurrentAveNetBERsig,_Z:nbsCohpmCurrentAveNetBERexp,_a:nbsCohpmCurrentMinNetBERsig,_b:nbsCohpmCurrentMinNetBERexp,_c:nbsCohpmCurrentMaxNetBERsig,_d:nbsCohpmCurrentMaxNetBERexp,_e:nbsCohpmCurrentAveCD,_f:nbsCohpmCurrentMinCD,_g:nbsCohpmCurrentMaxCD,_h:nbsCohpmCurrentAveDGD,_i:nbsCohpmCurrentMinDGD,_j:nbsCohpmCurrentMaxDGD,_k:nbsCohpmCurrentAveQ,_l:nbsCohpmCurrentMinQ,_m:nbsCohpmCurrentMaxQ,_n:nbsCohpmCurrentAveCFO,_o:nbsCohpmCurrentMinCFO,_p:nbsCohpmCurrentMaxCFO,_q:nbsCohpmCurrentAveOSNR,_r:nbsCohpmCurrentMinOSNR,_s:nbsCohpmCurrentMaxOSNR,_t:nbsCohpmCurrentAveSNRx,_u:nbsCohpmCurrentMinSNRx,_v:nbsCohpmCurrentMaxSNRx,_w:nbsCohpmCurrentAveSNRy,_x:nbsCohpmCurrentMinSNRy,_y:nbsCohpmCurrentMaxSNRy,_z:nbsCohpmCurrentAvePDL,_A0:nbsCohpmCurrentMinPDL,_A1:nbsCohpmCurrentMaxPDL,_A2:nbsCohpmCurrentAveSOP,_A3:nbsCohpmCurrentMinSOP,_A4:nbsCohpmCurrentMaxSOP,'nbsCohpmHistoricGrp':nbsCohpmHistoricGrp,'nbsCohpmHistoricTable':nbsCohpmHistoricTable,'nbsCohpmHistoricEntry':nbsCohpmHistoricEntry,_S:nbsCohpmHistoricIfIndex,_T:nbsCohpmHistoricInterval,_U:nbsCohpmHistoricSample,'nbsCohpmHistoricDate':nbsCohpmHistoricDate,'nbsCohpmHistoricTime':nbsCohpmHistoricTime,'nbsCohpmHistoricAveNetBERsig':nbsCohpmHistoricAveNetBERsig,'nbsCohpmHistoricAveNetBERexp':nbsCohpmHistoricAveNetBERexp,'nbsCohpmHistoricMinNetBERsig':nbsCohpmHistoricMinNetBERsig,'nbsCohpmHistoricMinNetBERexp':nbsCohpmHistoricMinNetBERexp,'nbsCohpmHistoricMaxNetBERsig':nbsCohpmHistoricMaxNetBERsig,'nbsCohpmHistoricMaxNetBERexp':nbsCohpmHistoricMaxNetBERexp,'nbsCohpmHistoricAveCD':nbsCohpmHistoricAveCD,'nbsCohpmHistoricMinCD':nbsCohpmHistoricMinCD,'nbsCohpmHistoricMaxCD':nbsCohpmHistoricMaxCD,'nbsCohpmHistoricAveDGD':nbsCohpmHistoricAveDGD,'nbsCohpmHistoricMinDGD':nbsCohpmHistoricMinDGD,'nbsCohpmHistoricMaxDGD':nbsCohpmHistoricMaxDGD,'nbsCohpmHistoricAveQ':nbsCohpmHistoricAveQ,'nbsCohpmHistoricMinQ':nbsCohpmHistoricMinQ,'nbsCohpmHistoricMaxQ':nbsCohpmHistoricMaxQ,'nbsCohpmHistoricAveCFO':nbsCohpmHistoricAveCFO,'nbsCohpmHistoricMinCFO':nbsCohpmHistoricMinCFO,'nbsCohpmHistoricMaxCFO':nbsCohpmHistoricMaxCFO,'nbsCohpmHistoricAveOSNR':nbsCohpmHistoricAveOSNR,'nbsCohpmHistoricMinOSNR':nbsCohpmHistoricMinOSNR,'nbsCohpmHistoricMaxOSNR':nbsCohpmHistoricMaxOSNR,'nbsCohpmHistoricAveSNRx':nbsCohpmHistoricAveSNRx,'nbsCohpmHistoricMinSNRx':nbsCohpmHistoricMinSNRx,'nbsCohpmHistoricMaxSNRx':nbsCohpmHistoricMaxSNRx,'nbsCohpmHistoricAveSNRy':nbsCohpmHistoricAveSNRy,'nbsCohpmHistoricMinSNRy':nbsCohpmHistoricMinSNRy,'nbsCohpmHistoricMaxSNRy':nbsCohpmHistoricMaxSNRy,'nbsCohpmHistoricAvePDL':nbsCohpmHistoricAvePDL,'nbsCohpmHistoricMinPDL':nbsCohpmHistoricMinPDL,'nbsCohpmHistoricMaxPDL':nbsCohpmHistoricMaxPDL,'nbsCohpmHistoricAveSOP':nbsCohpmHistoricAveSOP,'nbsCohpmHistoricMinSOP':nbsCohpmHistoricMinSOP,'nbsCohpmHistoricMaxSOP':nbsCohpmHistoricMaxSOP,'nbsCohpmRunningGrp':nbsCohpmRunningGrp,'nbsCohpmRunningTable':nbsCohpmRunningTable,'nbsCohpmRunningEntry':nbsCohpmRunningEntry,_W:nbsCohpmRunningIfIndex,'nbsCohpmRunningDate':nbsCohpmRunningDate,'nbsCohpmRunningTime':nbsCohpmRunningTime,'nbsCohpmRunningAveNetBERsig':nbsCohpmRunningAveNetBERsig,'nbsCohpmRunningAveNetBERexp':nbsCohpmRunningAveNetBERexp,'nbsCohpmRunningMinNetBERsig':nbsCohpmRunningMinNetBERsig,'nbsCohpmRunningMinNetBERexp':nbsCohpmRunningMinNetBERexp,'nbsCohpmRunningMaxNetBERsig':nbsCohpmRunningMaxNetBERsig,'nbsCohpmRunningMaxNetBERexp':nbsCohpmRunningMaxNetBERexp,'nbsCohpmRunningAveCD':nbsCohpmRunningAveCD,'nbsCohpmRunningMinCD':nbsCohpmRunningMinCD,'nbsCohpmRunningMaxCD':nbsCohpmRunningMaxCD,'nbsCohpmRunningAveDGD':nbsCohpmRunningAveDGD,'nbsCohpmRunningMinDGD':nbsCohpmRunningMinDGD,'nbsCohpmRunningMaxDGD':nbsCohpmRunningMaxDGD,'nbsCohpmRunningAveQ':nbsCohpmRunningAveQ,'nbsCohpmRunningMinQ':nbsCohpmRunningMinQ,'nbsCohpmRunningMaxQ':nbsCohpmRunningMaxQ,'nbsCohpmRunningAveCFO':nbsCohpmRunningAveCFO,'nbsCohpmRunningMinCFO':nbsCohpmRunningMinCFO,'nbsCohpmRunningMaxCFO':nbsCohpmRunningMaxCFO,'nbsCohpmRunningAveOSNR':nbsCohpmRunningAveOSNR,'nbsCohpmRunningMinOSNR':nbsCohpmRunningMinOSNR,'nbsCohpmRunningMaxOSNR':nbsCohpmRunningMaxOSNR,'nbsCohpmRunningAveSNRx':nbsCohpmRunningAveSNRx,'nbsCohpmRunningMinSNRx':nbsCohpmRunningMinSNRx,'nbsCohpmRunningMaxSNRx':nbsCohpmRunningMaxSNRx,'nbsCohpmRunningAveSNRy':nbsCohpmRunningAveSNRy,'nbsCohpmRunningMinSNRy':nbsCohpmRunningMinSNRy,'nbsCohpmRunningMaxSNRy':nbsCohpmRunningMaxSNRy,'nbsCohpmRunningAvePDL':nbsCohpmRunningAvePDL,'nbsCohpmRunningMinPDL':nbsCohpmRunningMinPDL,'nbsCohpmRunningMaxPDL':nbsCohpmRunningMaxPDL,'nbsCohpmRunningAveSOP':nbsCohpmRunningAveSOP,'nbsCohpmRunningMinSOP':nbsCohpmRunningMinSOP,'nbsCohpmRunningMaxSOP':nbsCohpmRunningMaxSOP,'nbsCoherentStatsGrp':nbsCoherentStatsGrp,'nbsCoherentStatsTable':nbsCoherentStatsTable,'nbsCoherentStatsEntry':nbsCoherentStatsEntry,_X:nbsCoherentStatsIfIndex,'nbsCoherentStatsDate':nbsCoherentStatsDate,'nbsCoherentStatsTime':nbsCoherentStatsTime,'nbsCoherentStatsSpan':nbsCoherentStatsSpan,'nbsCoherentStatsState':nbsCoherentStatsState,'nbsCoherentStatsAveNetBERsig':nbsCoherentStatsAveNetBERsig,'nbsCoherentStatsAveNetBERexp':nbsCoherentStatsAveNetBERexp,'nbsCoherentStatsMinNetBERsig':nbsCoherentStatsMinNetBERsig,'nbsCoherentStatsMinNetBERexp':nbsCoherentStatsMinNetBERexp,'nbsCoherentStatsMaxNetBERsig':nbsCoherentStatsMaxNetBERsig,'nbsCoherentStatsMaxNetBERexp':nbsCoherentStatsMaxNetBERexp,'nbsCoherentStatsAveCD':nbsCoherentStatsAveCD,'nbsCoherentStatsMinCD':nbsCoherentStatsMinCD,'nbsCoherentStatsMaxCD':nbsCoherentStatsMaxCD,'nbsCoherentStatsAveDGD':nbsCoherentStatsAveDGD,'nbsCoherentStatsMinDGD':nbsCoherentStatsMinDGD,'nbsCoherentStatsMaxDGD':nbsCoherentStatsMaxDGD,'nbsCoherentStatsAveQ':nbsCoherentStatsAveQ,'nbsCoherentStatsMinQ':nbsCoherentStatsMinQ,'nbsCoherentStatsMaxQ':nbsCoherentStatsMaxQ,'nbsCoherentStatsAveCFO':nbsCoherentStatsAveCFO,'nbsCoherentStatsMinCFO':nbsCoherentStatsMinCFO,'nbsCoherentStatsMaxCFO':nbsCoherentStatsMaxCFO,'nbsCoherentStatsAveOSNR':nbsCoherentStatsAveOSNR,'nbsCoherentStatsMinOSNR':nbsCoherentStatsMinOSNR,'nbsCoherentStatsMaxOSNR':nbsCoherentStatsMaxOSNR,'nbsCoherentStatsAveSNRx':nbsCoherentStatsAveSNRx,'nbsCoherentStatsMinSNRx':nbsCoherentStatsMinSNRx,'nbsCoherentStatsMaxSNRx':nbsCoherentStatsMaxSNRx,'nbsCoherentStatsAveSNRy':nbsCoherentStatsAveSNRy,'nbsCoherentStatsMinSNRy':nbsCoherentStatsMinSNRy,'nbsCoherentStatsMaxSNRy':nbsCoherentStatsMaxSNRy,'nbsCoherentStatsAvePDL':nbsCoherentStatsAvePDL,'nbsCoherentStatsMinPDL':nbsCoherentStatsMinPDL,'nbsCoherentStatsMaxPDL':nbsCoherentStatsMaxPDL,'nbsCoherentStatsAveSOP':nbsCoherentStatsAveSOP,'nbsCoherentStatsMinSOP':nbsCoherentStatsMinSOP,'nbsCoherentStatsMaxSOP':nbsCoherentStatsMaxSOP,'nbsCohpmEventsGrp':nbsCohpmEventsGrp,'nbsCohpmTraps':nbsCohpmTraps,'nbsCohpmTrapsAveBER':nbsCohpmTrapsAveBER,'nbsCohpmTrapsMinBER':nbsCohpmTrapsMinBER,'nbsCohpmTrapsMaxBER':nbsCohpmTrapsMaxBER,'nbsCohpmTrapsAveCD':nbsCohpmTrapsAveCD,'nbsCohpmTrapsMinCD':nbsCohpmTrapsMinCD,'nbsCohpmTrapsMaxCD':nbsCohpmTrapsMaxCD,'nbsCohpmTrapsAveDGD':nbsCohpmTrapsAveDGD,'nbsCohpmTrapsMinDGD':nbsCohpmTrapsMinDGD,'nbsCohpmTrapsMaxDGD':nbsCohpmTrapsMaxDGD,'nbsCohpmTrapsAveQ':nbsCohpmTrapsAveQ,'nbsCohpmTrapsMinQ':nbsCohpmTrapsMinQ,'nbsCohpmTrapsMaxQ':nbsCohpmTrapsMaxQ,'nbsCohpmTrapsAveCFO':nbsCohpmTrapsAveCFO,'nbsCohpmTrapsMinCFO':nbsCohpmTrapsMinCFO,'nbsCohpmTrapsMaxCFO':nbsCohpmTrapsMaxCFO,'nbsCohpmTrapsAveOSNR':nbsCohpmTrapsAveOSNR,'nbsCohpmTrapsMinOSNR':nbsCohpmTrapsMinOSNR,'nbsCohpmTrapsMaxOSNR':nbsCohpmTrapsMaxOSNR,'nbsCohpmTrapsAveSNRx':nbsCohpmTrapsAveSNRx,'nbsCohpmTrapsMinSNRx':nbsCohpmTrapsMinSNRx,'nbsCohpmTrapsMaxSNRx':nbsCohpmTrapsMaxSNRx,'nbsCohpmTrapsAveSNRy':nbsCohpmTrapsAveSNRy,'nbsCohpmTrapsMinSNRy':nbsCohpmTrapsMinSNRy,'nbsCohpmTrapsMaxSNRy':nbsCohpmTrapsMaxSNRy,'nbsCohpmTrapsAvePDL':nbsCohpmTrapsAvePDL,'nbsCohpmTrapsMinPDL':nbsCohpmTrapsMinPDL,'nbsCohpmTrapsMaxPDL':nbsCohpmTrapsMaxPDL,'nbsCohpmTrapsAveSOP':nbsCohpmTrapsAveSOP,'nbsCohpmTrapsMinSOP':nbsCohpmTrapsMinSOP,'nbsCohpmTrapsMaxSOP':nbsCohpmTrapsMaxSOP})