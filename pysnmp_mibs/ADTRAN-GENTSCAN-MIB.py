_AC='adGenTSCANFullRangeRate'
_AB='adGenTSCANHybridConfig'
_AA='adGenTSCANECTB2B12'
_A9='adGenTSCANECTB2B11'
_A8='adGenTSCANECTB2B10'
_A7='adGenTSCANECTB1B12'
_A6='adGenTSCANECTB1B11'
_A5='adGenTSCANECTB1B10'
_A4='adGenTSCANRepeaterIndex'
_A3='adGenTSCANLastTime'
_A2='adGenTSCANRate'
_A1='adGenTSCANLS2'
_A0='adGenTSCANLS1'
_z='adGenTSCANST2B'
_y='adGenTSCANST1B'
_x='adGenTSCANECTB2B9'
_w='adGenTSCANECTB2B8'
_v='adGenTSCANECTB2B7'
_u='adGenTSCANECTB2B6'
_t='adGenTSCANECTB2B5'
_s='adGenTSCANECTB2B4'
_r='adGenTSCANECTB2B3'
_q='adGenTSCANECTB2B2'
_p='adGenTSCANECTB2B1'
_o='adGenTSCANECTB1B9'
_n='adGenTSCANECTB1B8'
_m='adGenTSCANECTB1B7'
_l='adGenTSCANECTB1B6'
_k='adGenTSCANECTB1B5'
_j='adGenTSCANECTB1B4'
_i='adGenTSCANECTB1B3'
_h='adGenTSCANECTB1B2'
_g='adGenTSCANECTB1B1'
_f='adGenTSCANECTG2B9'
_e='adGenTSCANECTG2B8'
_d='adGenTSCANECTG2B7'
_c='adGenTSCANECTG2B6'
_b='adGenTSCANECTG2B5'
_a='adGenTSCANECTG2B4'
_Z='adGenTSCANECTG2B3'
_Y='adGenTSCANECTG2B2'
_X='adGenTSCANECTG2B1'
_W='adGenTSCANECTG1B9'
_V='adGenTSCANECTG1B8'
_U='adGenTSCANECTG1B7'
_T='adGenTSCANECTG1B6'
_S='adGenTSCANECTG1B5'
_R='adGenTSCANECTG1B4'
_Q='adGenTSCANECTG1B3'
_P='adGenTSCANECTG1B2'
_O='adGenTSCANECTG1B1'
_N='adGenTSCANTscanDataStatus'
_M='adGenTSCANAccumTscanData'
_L='complete'
_K='invalid'
_J='enable'
_I='adEShdslInvIndex'
_H='ADTRAN-SHDSL-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='ADTRAN-GENTSCAN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenHDSL,adGenHDSLID=mibBuilder.importSymbols('ADTRAN-GENHDSL-MIB','adGenHDSL','adGenHDSLID')
adEShdslInvIndex,=mibBuilder.importSymbols(_H,_I)
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenTSCANMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,51,1,1))
if mibBuilder.loadTexts:adGenTSCANMIB.setRevisions(('2012-09-05 00:00','2009-07-30 00:00'))
_AdGenTSCANmg_ObjectIdentity=ObjectIdentity
adGenTSCANmg=_AdGenTSCANmg_ObjectIdentity((1,3,6,1,4,1,664,5,51,1))
_AdGenTSCANProv_ObjectIdentity=ObjectIdentity
adGenTSCANProv=_AdGenTSCANProv_ObjectIdentity((1,3,6,1,4,1,664,5,51,1,1))
_AdGenTSCANProvTable_Object=MibTable
adGenTSCANProvTable=_AdGenTSCANProvTable_Object((1,3,6,1,4,1,664,5,51,1,1,1))
if mibBuilder.loadTexts:adGenTSCANProvTable.setStatus(_A)
_AdGenTSCANProvEntry_Object=MibTableRow
adGenTSCANProvEntry=_AdGenTSCANProvEntry_Object((1,3,6,1,4,1,664,5,51,1,1,1,1))
adGenTSCANProvEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenTSCANProvEntry.setStatus(_A)
class _AdGenTSCANAccumTscanData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_J,1))
_AdGenTSCANAccumTscanData_Type.__name__=_D
_AdGenTSCANAccumTscanData_Object=MibTableColumn
adGenTSCANAccumTscanData=_AdGenTSCANAccumTscanData_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,1),_AdGenTSCANAccumTscanData_Type())
adGenTSCANAccumTscanData.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANAccumTscanData.setStatus(_A)
class _AdGenTSCANTscanDataStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('done',1),('accumulating',2),('idle',3)))
_AdGenTSCANTscanDataStatus_Type.__name__=_D
_AdGenTSCANTscanDataStatus_Object=MibTableColumn
adGenTSCANTscanDataStatus=_AdGenTSCANTscanDataStatus_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,2),_AdGenTSCANTscanDataStatus_Type())
adGenTSCANTscanDataStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANTscanDataStatus.setStatus(_A)
_AdGenTSCANECTG1B1_Type=DisplayString
_AdGenTSCANECTG1B1_Object=MibTableColumn
adGenTSCANECTG1B1=_AdGenTSCANECTG1B1_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,3),_AdGenTSCANECTG1B1_Type())
adGenTSCANECTG1B1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B1.setStatus(_A)
_AdGenTSCANECTG1B2_Type=DisplayString
_AdGenTSCANECTG1B2_Object=MibTableColumn
adGenTSCANECTG1B2=_AdGenTSCANECTG1B2_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,4),_AdGenTSCANECTG1B2_Type())
adGenTSCANECTG1B2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B2.setStatus(_A)
_AdGenTSCANECTG1B3_Type=DisplayString
_AdGenTSCANECTG1B3_Object=MibTableColumn
adGenTSCANECTG1B3=_AdGenTSCANECTG1B3_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,5),_AdGenTSCANECTG1B3_Type())
adGenTSCANECTG1B3.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B3.setStatus(_A)
_AdGenTSCANECTG1B4_Type=DisplayString
_AdGenTSCANECTG1B4_Object=MibTableColumn
adGenTSCANECTG1B4=_AdGenTSCANECTG1B4_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,6),_AdGenTSCANECTG1B4_Type())
adGenTSCANECTG1B4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B4.setStatus(_A)
_AdGenTSCANECTG1B5_Type=DisplayString
_AdGenTSCANECTG1B5_Object=MibTableColumn
adGenTSCANECTG1B5=_AdGenTSCANECTG1B5_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,7),_AdGenTSCANECTG1B5_Type())
adGenTSCANECTG1B5.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B5.setStatus(_A)
_AdGenTSCANECTG1B6_Type=DisplayString
_AdGenTSCANECTG1B6_Object=MibTableColumn
adGenTSCANECTG1B6=_AdGenTSCANECTG1B6_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,8),_AdGenTSCANECTG1B6_Type())
adGenTSCANECTG1B6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B6.setStatus(_A)
_AdGenTSCANECTG1B7_Type=DisplayString
_AdGenTSCANECTG1B7_Object=MibTableColumn
adGenTSCANECTG1B7=_AdGenTSCANECTG1B7_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,9),_AdGenTSCANECTG1B7_Type())
adGenTSCANECTG1B7.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B7.setStatus(_A)
_AdGenTSCANECTG1B8_Type=DisplayString
_AdGenTSCANECTG1B8_Object=MibTableColumn
adGenTSCANECTG1B8=_AdGenTSCANECTG1B8_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,10),_AdGenTSCANECTG1B8_Type())
adGenTSCANECTG1B8.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B8.setStatus(_A)
_AdGenTSCANECTG1B9_Type=DisplayString
_AdGenTSCANECTG1B9_Object=MibTableColumn
adGenTSCANECTG1B9=_AdGenTSCANECTG1B9_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,11),_AdGenTSCANECTG1B9_Type())
adGenTSCANECTG1B9.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG1B9.setStatus(_A)
_AdGenTSCANECTG2B1_Type=DisplayString
_AdGenTSCANECTG2B1_Object=MibTableColumn
adGenTSCANECTG2B1=_AdGenTSCANECTG2B1_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,12),_AdGenTSCANECTG2B1_Type())
adGenTSCANECTG2B1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B1.setStatus(_A)
_AdGenTSCANECTG2B2_Type=DisplayString
_AdGenTSCANECTG2B2_Object=MibTableColumn
adGenTSCANECTG2B2=_AdGenTSCANECTG2B2_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,13),_AdGenTSCANECTG2B2_Type())
adGenTSCANECTG2B2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B2.setStatus(_A)
_AdGenTSCANECTG2B3_Type=DisplayString
_AdGenTSCANECTG2B3_Object=MibTableColumn
adGenTSCANECTG2B3=_AdGenTSCANECTG2B3_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,14),_AdGenTSCANECTG2B3_Type())
adGenTSCANECTG2B3.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B3.setStatus(_A)
_AdGenTSCANECTG2B4_Type=DisplayString
_AdGenTSCANECTG2B4_Object=MibTableColumn
adGenTSCANECTG2B4=_AdGenTSCANECTG2B4_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,15),_AdGenTSCANECTG2B4_Type())
adGenTSCANECTG2B4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B4.setStatus(_A)
_AdGenTSCANECTG2B5_Type=DisplayString
_AdGenTSCANECTG2B5_Object=MibTableColumn
adGenTSCANECTG2B5=_AdGenTSCANECTG2B5_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,16),_AdGenTSCANECTG2B5_Type())
adGenTSCANECTG2B5.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B5.setStatus(_A)
_AdGenTSCANECTG2B6_Type=DisplayString
_AdGenTSCANECTG2B6_Object=MibTableColumn
adGenTSCANECTG2B6=_AdGenTSCANECTG2B6_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,17),_AdGenTSCANECTG2B6_Type())
adGenTSCANECTG2B6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B6.setStatus(_A)
_AdGenTSCANECTG2B7_Type=DisplayString
_AdGenTSCANECTG2B7_Object=MibTableColumn
adGenTSCANECTG2B7=_AdGenTSCANECTG2B7_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,18),_AdGenTSCANECTG2B7_Type())
adGenTSCANECTG2B7.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B7.setStatus(_A)
_AdGenTSCANECTG2B8_Type=DisplayString
_AdGenTSCANECTG2B8_Object=MibTableColumn
adGenTSCANECTG2B8=_AdGenTSCANECTG2B8_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,19),_AdGenTSCANECTG2B8_Type())
adGenTSCANECTG2B8.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B8.setStatus(_A)
_AdGenTSCANECTG2B9_Type=DisplayString
_AdGenTSCANECTG2B9_Object=MibTableColumn
adGenTSCANECTG2B9=_AdGenTSCANECTG2B9_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,20),_AdGenTSCANECTG2B9_Type())
adGenTSCANECTG2B9.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTG2B9.setStatus(_A)
_AdGenTSCANECTB1B1_Type=DisplayString
_AdGenTSCANECTB1B1_Object=MibTableColumn
adGenTSCANECTB1B1=_AdGenTSCANECTB1B1_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,21),_AdGenTSCANECTB1B1_Type())
adGenTSCANECTB1B1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B1.setStatus(_A)
_AdGenTSCANECTB1B2_Type=DisplayString
_AdGenTSCANECTB1B2_Object=MibTableColumn
adGenTSCANECTB1B2=_AdGenTSCANECTB1B2_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,22),_AdGenTSCANECTB1B2_Type())
adGenTSCANECTB1B2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B2.setStatus(_A)
_AdGenTSCANECTB1B3_Type=DisplayString
_AdGenTSCANECTB1B3_Object=MibTableColumn
adGenTSCANECTB1B3=_AdGenTSCANECTB1B3_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,23),_AdGenTSCANECTB1B3_Type())
adGenTSCANECTB1B3.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B3.setStatus(_A)
_AdGenTSCANECTB1B4_Type=DisplayString
_AdGenTSCANECTB1B4_Object=MibTableColumn
adGenTSCANECTB1B4=_AdGenTSCANECTB1B4_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,24),_AdGenTSCANECTB1B4_Type())
adGenTSCANECTB1B4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B4.setStatus(_A)
_AdGenTSCANECTB1B5_Type=DisplayString
_AdGenTSCANECTB1B5_Object=MibTableColumn
adGenTSCANECTB1B5=_AdGenTSCANECTB1B5_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,25),_AdGenTSCANECTB1B5_Type())
adGenTSCANECTB1B5.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B5.setStatus(_A)
_AdGenTSCANECTB1B6_Type=DisplayString
_AdGenTSCANECTB1B6_Object=MibTableColumn
adGenTSCANECTB1B6=_AdGenTSCANECTB1B6_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,26),_AdGenTSCANECTB1B6_Type())
adGenTSCANECTB1B6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B6.setStatus(_A)
_AdGenTSCANECTB1B7_Type=DisplayString
_AdGenTSCANECTB1B7_Object=MibTableColumn
adGenTSCANECTB1B7=_AdGenTSCANECTB1B7_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,27),_AdGenTSCANECTB1B7_Type())
adGenTSCANECTB1B7.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B7.setStatus(_A)
_AdGenTSCANECTB1B8_Type=DisplayString
_AdGenTSCANECTB1B8_Object=MibTableColumn
adGenTSCANECTB1B8=_AdGenTSCANECTB1B8_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,28),_AdGenTSCANECTB1B8_Type())
adGenTSCANECTB1B8.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B8.setStatus(_A)
_AdGenTSCANECTB1B9_Type=DisplayString
_AdGenTSCANECTB1B9_Object=MibTableColumn
adGenTSCANECTB1B9=_AdGenTSCANECTB1B9_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,29),_AdGenTSCANECTB1B9_Type())
adGenTSCANECTB1B9.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B9.setStatus(_A)
_AdGenTSCANECTB2B1_Type=DisplayString
_AdGenTSCANECTB2B1_Object=MibTableColumn
adGenTSCANECTB2B1=_AdGenTSCANECTB2B1_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,30),_AdGenTSCANECTB2B1_Type())
adGenTSCANECTB2B1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B1.setStatus(_A)
_AdGenTSCANECTB2B2_Type=DisplayString
_AdGenTSCANECTB2B2_Object=MibTableColumn
adGenTSCANECTB2B2=_AdGenTSCANECTB2B2_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,31),_AdGenTSCANECTB2B2_Type())
adGenTSCANECTB2B2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B2.setStatus(_A)
_AdGenTSCANECTB2B3_Type=DisplayString
_AdGenTSCANECTB2B3_Object=MibTableColumn
adGenTSCANECTB2B3=_AdGenTSCANECTB2B3_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,32),_AdGenTSCANECTB2B3_Type())
adGenTSCANECTB2B3.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B3.setStatus(_A)
_AdGenTSCANECTB2B4_Type=DisplayString
_AdGenTSCANECTB2B4_Object=MibTableColumn
adGenTSCANECTB2B4=_AdGenTSCANECTB2B4_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,33),_AdGenTSCANECTB2B4_Type())
adGenTSCANECTB2B4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B4.setStatus(_A)
_AdGenTSCANECTB2B5_Type=DisplayString
_AdGenTSCANECTB2B5_Object=MibTableColumn
adGenTSCANECTB2B5=_AdGenTSCANECTB2B5_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,34),_AdGenTSCANECTB2B5_Type())
adGenTSCANECTB2B5.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B5.setStatus(_A)
_AdGenTSCANECTB2B6_Type=DisplayString
_AdGenTSCANECTB2B6_Object=MibTableColumn
adGenTSCANECTB2B6=_AdGenTSCANECTB2B6_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,35),_AdGenTSCANECTB2B6_Type())
adGenTSCANECTB2B6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B6.setStatus(_A)
_AdGenTSCANECTB2B7_Type=DisplayString
_AdGenTSCANECTB2B7_Object=MibTableColumn
adGenTSCANECTB2B7=_AdGenTSCANECTB2B7_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,36),_AdGenTSCANECTB2B7_Type())
adGenTSCANECTB2B7.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B7.setStatus(_A)
_AdGenTSCANECTB2B8_Type=DisplayString
_AdGenTSCANECTB2B8_Object=MibTableColumn
adGenTSCANECTB2B8=_AdGenTSCANECTB2B8_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,37),_AdGenTSCANECTB2B8_Type())
adGenTSCANECTB2B8.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B8.setStatus(_A)
_AdGenTSCANECTB2B9_Type=DisplayString
_AdGenTSCANECTB2B9_Object=MibTableColumn
adGenTSCANECTB2B9=_AdGenTSCANECTB2B9_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,38),_AdGenTSCANECTB2B9_Type())
adGenTSCANECTB2B9.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B9.setStatus(_A)
_AdGenTSCANST1B_Type=DisplayString
_AdGenTSCANST1B_Object=MibTableColumn
adGenTSCANST1B=_AdGenTSCANST1B_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,39),_AdGenTSCANST1B_Type())
adGenTSCANST1B.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANST1B.setStatus(_A)
_AdGenTSCANST2B_Type=DisplayString
_AdGenTSCANST2B_Object=MibTableColumn
adGenTSCANST2B=_AdGenTSCANST2B_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,40),_AdGenTSCANST2B_Type())
adGenTSCANST2B.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANST2B.setStatus(_A)
class _AdGenTSCANLS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AdGenTSCANLS1_Type.__name__=_D
_AdGenTSCANLS1_Object=MibTableColumn
adGenTSCANLS1=_AdGenTSCANLS1_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,41),_AdGenTSCANLS1_Type())
adGenTSCANLS1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANLS1.setStatus(_A)
class _AdGenTSCANLS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AdGenTSCANLS2_Type.__name__=_D
_AdGenTSCANLS2_Object=MibTableColumn
adGenTSCANLS2=_AdGenTSCANLS2_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,42),_AdGenTSCANLS2_Type())
adGenTSCANLS2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANLS2.setStatus(_A)
class _AdGenTSCANRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sixteenDS0s',1),('thirtytwoDS0s',2)))
_AdGenTSCANRate_Type.__name__=_D
_AdGenTSCANRate_Object=MibTableColumn
adGenTSCANRate=_AdGenTSCANRate_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,43),_AdGenTSCANRate_Type())
adGenTSCANRate.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANRate.setStatus(_A)
_AdGenTSCANLastTime_Type=TimeTicks
_AdGenTSCANLastTime_Object=MibTableColumn
adGenTSCANLastTime=_AdGenTSCANLastTime_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,44),_AdGenTSCANLastTime_Type())
adGenTSCANLastTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANLastTime.setStatus(_A)
class _AdGenTSCANRepeaterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('htuc',1),('hre1',2),('hre2',3),('hre3',4)))
_AdGenTSCANRepeaterIndex_Type.__name__=_D
_AdGenTSCANRepeaterIndex_Object=MibTableColumn
adGenTSCANRepeaterIndex=_AdGenTSCANRepeaterIndex_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,45),_AdGenTSCANRepeaterIndex_Type())
adGenTSCANRepeaterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANRepeaterIndex.setStatus(_A)
_AdGenTSCANECTB1B10_Type=DisplayString
_AdGenTSCANECTB1B10_Object=MibTableColumn
adGenTSCANECTB1B10=_AdGenTSCANECTB1B10_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,46),_AdGenTSCANECTB1B10_Type())
adGenTSCANECTB1B10.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B10.setStatus(_A)
_AdGenTSCANECTB1B11_Type=DisplayString
_AdGenTSCANECTB1B11_Object=MibTableColumn
adGenTSCANECTB1B11=_AdGenTSCANECTB1B11_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,47),_AdGenTSCANECTB1B11_Type())
adGenTSCANECTB1B11.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B11.setStatus(_A)
_AdGenTSCANECTB1B12_Type=DisplayString
_AdGenTSCANECTB1B12_Object=MibTableColumn
adGenTSCANECTB1B12=_AdGenTSCANECTB1B12_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,48),_AdGenTSCANECTB1B12_Type())
adGenTSCANECTB1B12.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB1B12.setStatus(_A)
_AdGenTSCANECTB2B10_Type=DisplayString
_AdGenTSCANECTB2B10_Object=MibTableColumn
adGenTSCANECTB2B10=_AdGenTSCANECTB2B10_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,49),_AdGenTSCANECTB2B10_Type())
adGenTSCANECTB2B10.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B10.setStatus(_A)
_AdGenTSCANECTB2B11_Type=DisplayString
_AdGenTSCANECTB2B11_Object=MibTableColumn
adGenTSCANECTB2B11=_AdGenTSCANECTB2B11_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,50),_AdGenTSCANECTB2B11_Type())
adGenTSCANECTB2B11.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B11.setStatus(_A)
_AdGenTSCANECTB2B12_Type=DisplayString
_AdGenTSCANECTB2B12_Object=MibTableColumn
adGenTSCANECTB2B12=_AdGenTSCANECTB2B12_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,51),_AdGenTSCANECTB2B12_Type())
adGenTSCANECTB2B12.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANECTB2B12.setStatus(_A)
class _AdGenTSCANHybridConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AdGenTSCANHybridConfig_Type.__name__=_D
_AdGenTSCANHybridConfig_Object=MibTableColumn
adGenTSCANHybridConfig=_AdGenTSCANHybridConfig_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,52),_AdGenTSCANHybridConfig_Type())
adGenTSCANHybridConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANHybridConfig.setStatus(_A)
_AdGenTSCANFullRangeRate_Type=Unsigned32
_AdGenTSCANFullRangeRate_Object=MibTableColumn
adGenTSCANFullRangeRate=_AdGenTSCANFullRangeRate_Object((1,3,6,1,4,1,664,5,51,1,1,1,1,53),_AdGenTSCANFullRangeRate_Type())
adGenTSCANFullRangeRate.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANFullRangeRate.setStatus(_A)
_AdGenTSCANMibConformance_ObjectIdentity=ObjectIdentity
adGenTSCANMibConformance=_AdGenTSCANMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,51,1,2))
_AdGenTSCANMibGroups_ObjectIdentity=ObjectIdentity
adGenTSCANMibGroups=_AdGenTSCANMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,51,1,2,1))
_AdGenTSCANRepeater_ObjectIdentity=ObjectIdentity
adGenTSCANRepeater=_AdGenTSCANRepeater_ObjectIdentity((1,3,6,1,4,1,664,5,51,1,3))
_AdGenTSCANRepeaterTable_Object=MibTable
adGenTSCANRepeaterTable=_AdGenTSCANRepeaterTable_Object((1,3,6,1,4,1,664,5,51,1,3,1))
if mibBuilder.loadTexts:adGenTSCANRepeaterTable.setStatus(_A)
_AdGenTSCANRepeaterEntry_Object=MibTableRow
adGenTSCANRepeaterEntry=_AdGenTSCANRepeaterEntry_Object((1,3,6,1,4,1,664,5,51,1,3,1,1))
adGenTSCANRepeaterEntry.setIndexNames((0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:adGenTSCANRepeaterEntry.setStatus(_A)
class _AdGenTSCANRepeaterStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_J,1))
_AdGenTSCANRepeaterStart_Type.__name__=_D
_AdGenTSCANRepeaterStart_Object=MibTableColumn
adGenTSCANRepeaterStart=_AdGenTSCANRepeaterStart_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,1),_AdGenTSCANRepeaterStart_Type())
adGenTSCANRepeaterStart.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANRepeaterStart.setStatus(_A)
class _AdGenTSCANRepeaterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('done',1),('accumulatingData',2),('idle',3),('error',4)))
_AdGenTSCANRepeaterStatus_Type.__name__=_D
_AdGenTSCANRepeaterStatus_Object=MibTableColumn
adGenTSCANRepeaterStatus=_AdGenTSCANRepeaterStatus_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,2),_AdGenTSCANRepeaterStatus_Type())
adGenTSCANRepeaterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterStatus.setStatus(_A)
_AdGenTSCANRepeaterLastTestCompleted_Type=DisplayString
_AdGenTSCANRepeaterLastTestCompleted_Object=MibTableColumn
adGenTSCANRepeaterLastTestCompleted=_AdGenTSCANRepeaterLastTestCompleted_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,3),_AdGenTSCANRepeaterLastTestCompleted_Type())
adGenTSCANRepeaterLastTestCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterLastTestCompleted.setStatus(_A)
class _AdGenTSCANRepeaterFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknown',0),('open',1),('short',2),('gfi',3),('singleOpen',4),('ok',5)))
_AdGenTSCANRepeaterFault_Type.__name__=_D
_AdGenTSCANRepeaterFault_Object=MibTableColumn
adGenTSCANRepeaterFault=_AdGenTSCANRepeaterFault_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,4),_AdGenTSCANRepeaterFault_Type())
adGenTSCANRepeaterFault.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterFault.setStatus(_A)
_AdGenTSCANRepeaterDistanceInFeet_Type=Integer32
_AdGenTSCANRepeaterDistanceInFeet_Object=MibTableColumn
adGenTSCANRepeaterDistanceInFeet=_AdGenTSCANRepeaterDistanceInFeet_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,5),_AdGenTSCANRepeaterDistanceInFeet_Type())
adGenTSCANRepeaterDistanceInFeet.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterDistanceInFeet.setStatus(_A)
_AdGenTSCANRepeaterDistanceInMeters_Type=Integer32
_AdGenTSCANRepeaterDistanceInMeters_Object=MibTableColumn
adGenTSCANRepeaterDistanceInMeters=_AdGenTSCANRepeaterDistanceInMeters_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,6),_AdGenTSCANRepeaterDistanceInMeters_Type())
adGenTSCANRepeaterDistanceInMeters.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterDistanceInMeters.setStatus(_A)
_AdGenTSCANRepeaterRate_Type=Integer32
_AdGenTSCANRepeaterRate_Object=MibTableColumn
adGenTSCANRepeaterRate=_AdGenTSCANRepeaterRate_Object((1,3,6,1,4,1,664,5,51,1,3,1,1,7),_AdGenTSCANRepeaterRate_Type())
adGenTSCANRepeaterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTSCANRepeaterRate.setStatus(_A)
_AdGenTSCANRepeaterPortTable_Object=MibTable
adGenTSCANRepeaterPortTable=_AdGenTSCANRepeaterPortTable_Object((1,3,6,1,4,1,664,5,51,1,3,2))
if mibBuilder.loadTexts:adGenTSCANRepeaterPortTable.setStatus(_A)
_AdGenTSCANRepeaterPortEntry_Object=MibTableRow
adGenTSCANRepeaterPortEntry=_AdGenTSCANRepeaterPortEntry_Object((1,3,6,1,4,1,664,5,51,1,3,2,1))
adGenTSCANRepeaterPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenTSCANRepeaterPortEntry.setStatus(_A)
_AdGenTSCANRepeaterPortLastErrorString_Type=DisplayString
_AdGenTSCANRepeaterPortLastErrorString_Object=MibTableColumn
adGenTSCANRepeaterPortLastErrorString=_AdGenTSCANRepeaterPortLastErrorString_Object((1,3,6,1,4,1,664,5,51,1,3,2,1,1),_AdGenTSCANRepeaterPortLastErrorString_Type())
adGenTSCANRepeaterPortLastErrorString.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenTSCANRepeaterPortLastErrorString.setStatus(_A)
adGenTSCANGroup=ObjectGroup((1,3,6,1,4,1,664,5,51,1,2,1,1))
adGenTSCANGroup.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3),(_C,_A4),(_C,_A5),(_C,_A6),(_C,_A7),(_C,_A8),(_C,_A9),(_C,_AA),(_C,_AB),(_C,_AC)))
if mibBuilder.loadTexts:adGenTSCANGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenTSCANmg':adGenTSCANmg,'adGenTSCANProv':adGenTSCANProv,'adGenTSCANProvTable':adGenTSCANProvTable,'adGenTSCANProvEntry':adGenTSCANProvEntry,_M:adGenTSCANAccumTscanData,_N:adGenTSCANTscanDataStatus,_O:adGenTSCANECTG1B1,_P:adGenTSCANECTG1B2,_Q:adGenTSCANECTG1B3,_R:adGenTSCANECTG1B4,_S:adGenTSCANECTG1B5,_T:adGenTSCANECTG1B6,_U:adGenTSCANECTG1B7,_V:adGenTSCANECTG1B8,_W:adGenTSCANECTG1B9,_X:adGenTSCANECTG2B1,_Y:adGenTSCANECTG2B2,_Z:adGenTSCANECTG2B3,_a:adGenTSCANECTG2B4,_b:adGenTSCANECTG2B5,_c:adGenTSCANECTG2B6,_d:adGenTSCANECTG2B7,_e:adGenTSCANECTG2B8,_f:adGenTSCANECTG2B9,_g:adGenTSCANECTB1B1,_h:adGenTSCANECTB1B2,_i:adGenTSCANECTB1B3,_j:adGenTSCANECTB1B4,_k:adGenTSCANECTB1B5,_l:adGenTSCANECTB1B6,_m:adGenTSCANECTB1B7,_n:adGenTSCANECTB1B8,_o:adGenTSCANECTB1B9,_p:adGenTSCANECTB2B1,_q:adGenTSCANECTB2B2,_r:adGenTSCANECTB2B3,_s:adGenTSCANECTB2B4,_t:adGenTSCANECTB2B5,_u:adGenTSCANECTB2B6,_v:adGenTSCANECTB2B7,_w:adGenTSCANECTB2B8,_x:adGenTSCANECTB2B9,_y:adGenTSCANST1B,_z:adGenTSCANST2B,_A0:adGenTSCANLS1,_A1:adGenTSCANLS2,_A2:adGenTSCANRate,_A3:adGenTSCANLastTime,_A4:adGenTSCANRepeaterIndex,_A5:adGenTSCANECTB1B10,_A6:adGenTSCANECTB1B11,_A7:adGenTSCANECTB1B12,_A8:adGenTSCANECTB2B10,_A9:adGenTSCANECTB2B11,_AA:adGenTSCANECTB2B12,_AB:adGenTSCANHybridConfig,_AC:adGenTSCANFullRangeRate,'adGenTSCANMibConformance':adGenTSCANMibConformance,'adGenTSCANMibGroups':adGenTSCANMibGroups,'adGenTSCANGroup':adGenTSCANGroup,'adGenTSCANRepeater':adGenTSCANRepeater,'adGenTSCANRepeaterTable':adGenTSCANRepeaterTable,'adGenTSCANRepeaterEntry':adGenTSCANRepeaterEntry,'adGenTSCANRepeaterStart':adGenTSCANRepeaterStart,'adGenTSCANRepeaterStatus':adGenTSCANRepeaterStatus,'adGenTSCANRepeaterLastTestCompleted':adGenTSCANRepeaterLastTestCompleted,'adGenTSCANRepeaterFault':adGenTSCANRepeaterFault,'adGenTSCANRepeaterDistanceInFeet':adGenTSCANRepeaterDistanceInFeet,'adGenTSCANRepeaterDistanceInMeters':adGenTSCANRepeaterDistanceInMeters,'adGenTSCANRepeaterRate':adGenTSCANRepeaterRate,'adGenTSCANRepeaterPortTable':adGenTSCANRepeaterPortTable,'adGenTSCANRepeaterPortEntry':adGenTSCANRepeaterPortEntry,'adGenTSCANRepeaterPortLastErrorString':adGenTSCANRepeaterPortLastErrorString,'adGenTSCANMIB':adGenTSCANMIB})