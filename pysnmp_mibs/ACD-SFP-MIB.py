_Ad='acdSfpThreshStatusGroup'
_Ac='acdSfpThreshGroup'
_Ab='acdSfpDiagGroup'
_Aa='acdSfpInfoGroup'
_AZ='acdSfpThreshStatusRxPwrLowWarn'
_AY='acdSfpThreshStatusRxPwrHighWarn'
_AX='acdSfpThreshStatusRxPwrLowAlm'
_AW='acdSfpThreshStatusRxPwrHighAlm'
_AV='acdSfpThreshStatusTxPwrLowWarn'
_AU='acdSfpThreshStatusTxPwrHighWarn'
_AT='acdSfpThreshStatusTxPwrLowAlm'
_AS='acdSfpThreshStatusTxPwrHighAlm'
_AR='acdSfpThreshStatusLbcLowWarn'
_AQ='acdSfpThreshStatusLbcHighWarn'
_AP='acdSfpThreshStatusLbcLowAlm'
_AO='acdSfpThreshStatusLbcHighAlm'
_AN='acdSfpThreshStatusVccLowWarn'
_AM='acdSfpThreshStatusVccHighWarn'
_AL='acdSfpThreshStatusVccLowAlm'
_AK='acdSfpThreshStatusVccHighAlm'
_AJ='acdSfpThreshStatusTempLowWarn'
_AI='acdSfpThreshStatusTempHighWarn'
_AH='acdSfpThreshStatusTempLowAlm'
_AG='acdSfpThreshStatusTempHighAlm'
_AF='acdSfpThreshStatusConnIdx'
_AE='acdSfpThreshRxPwrLowWarndBm'
_AD='acdSfpThreshRxPwrHighWarndBm'
_AC='acdSfpThreshRxPwrLowAlmdBm'
_AB='acdSfpThreshRxPwrHighAlmdBm'
_AA='acdSfpThreshTxPwrLowWarndBm'
_A9='acdSfpThreshTxPwrHighWarndBm'
_A8='acdSfpThreshTxPwrLowAlmdBm'
_A7='acdSfpThreshTxPwrHighAlmdBm'
_A6='acdSfpThreshRxPwrLowWarn'
_A5='acdSfpThreshRxPwrHighWarn'
_A4='acdSfpThreshRxPwrLowAlm'
_A3='acdSfpThreshRxPwrHighAlm'
_A2='acdSfpThreshTxPwrLowWarn'
_A1='acdSfpThreshTxPwrHighWarn'
_A0='acdSfpThreshTxPwrLowAlm'
_z='acdSfpThreshTxPwrHighAlm'
_y='acdSfpThreshLbcLowWarn'
_x='acdSfpThreshLbcHighWarn'
_w='acdSfpThreshLbcLowAlm'
_v='acdSfpThreshLbcHighAlm'
_u='acdSfpThreshVccLowWarn'
_t='acdSfpThreshVccHighWarn'
_s='acdSfpThreshVccLowAlm'
_r='acdSfpThreshVccHighAlm'
_q='acdSfpThreshTempLowWarn'
_p='acdSfpThreshTempHighWarn'
_o='acdSfpThreshTempLowAlm'
_n='acdSfpThreshTempHighAlm'
_m='acdSfpThreshConnIdx'
_l='acdSfpDiagRxPwrdBm'
_k='acdSfpDiagTxPwrdBm'
_j='acdSfpDiagRxPwr'
_i='acdSfpDiagTxPwr'
_h='acdSfpDiagLbc'
_g='acdSfpDiagVcc'
_f='acdSfpDiagTemp'
_e='acdSfpDiagConnIdx'
_d='acdSfpInfoTransCode'
_c='acdSfpInfoExtIdType'
_b='acdSfpInfoIdType'
_a='acdSfpInfoAlm'
_Z='acdSfpInfoInternal'
_Y='acdSfpInfoDiag'
_X='acdSfpInfoPresent'
_W='acdSfpInfoRev8472'
_V='acdSfpInfoLot'
_U='acdSfpInfoDay'
_T='acdSfpInfoMonth'
_S='acdSfpInfoYear'
_R='acdSfpInfoSerialNum'
_Q='acdSfpInfoWavelength'
_P='acdSfpInfoVendorRev'
_O='acdSfpInfoVendorPn'
_N='acdSfpInfoVendorOui'
_M='acdSfpInfoVendor'
_L='acdSfpInfoConnType'
_K='acdSfpInfoConnIdx'
_J='acdSfpThreshStatusID'
_I='acdSfpThreshID'
_H='acdSfpDiagID'
_G='acdSfpInfoID'
_F='Integer32'
_E='not-accessible'
_D='DisplayString'
_C='read-only'
_B='ACD-SFP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
acdSfp=ModuleIdentity((1,3,6,1,4,1,22420,2,4))
if mibBuilder.loadTexts:acdSfp.setRevisions(('2010-11-10 01:00','2008-04-22 01:00','2006-08-06 01:00'))
_AcdSfpInfoTable_Object=MibTable
acdSfpInfoTable=_AcdSfpInfoTable_Object((1,3,6,1,4,1,22420,2,4,1))
if mibBuilder.loadTexts:acdSfpInfoTable.setStatus(_A)
_AcdSfpInfoEntry_Object=MibTableRow
acdSfpInfoEntry=_AcdSfpInfoEntry_Object((1,3,6,1,4,1,22420,2,4,1,1))
acdSfpInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:acdSfpInfoEntry.setStatus(_A)
_AcdSfpInfoID_Type=Unsigned32
_AcdSfpInfoID_Object=MibTableColumn
acdSfpInfoID=_AcdSfpInfoID_Object((1,3,6,1,4,1,22420,2,4,1,1,1),_AcdSfpInfoID_Type())
acdSfpInfoID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSfpInfoID.setStatus(_A)
_AcdSfpInfoConnIdx_Type=Unsigned32
_AcdSfpInfoConnIdx_Object=MibTableColumn
acdSfpInfoConnIdx=_AcdSfpInfoConnIdx_Object((1,3,6,1,4,1,22420,2,4,1,1,2),_AcdSfpInfoConnIdx_Type())
acdSfpInfoConnIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoConnIdx.setStatus(_A)
class _AcdSfpInfoConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*(('sfpSC',1),('sfpFC1COPPER',2),('sfpFC2COPPER',3),('sfpBNC',4),('sfpFCCOAX',5),('sfpFIBERJACK',6),('sfpLC',7),('sfpMTRJ',8),('sfpMU',9),('sfpSG',10),('sfpPIGTAIL',11),('sfpHSSDCII',32),('sfpCOPPERPIGTAIL',33)))
_AcdSfpInfoConnType_Type.__name__=_F
_AcdSfpInfoConnType_Object=MibTableColumn
acdSfpInfoConnType=_AcdSfpInfoConnType_Object((1,3,6,1,4,1,22420,2,4,1,1,3),_AcdSfpInfoConnType_Type())
acdSfpInfoConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoConnType.setStatus(_A)
class _AcdSfpInfoVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcdSfpInfoVendor_Type.__name__=_D
_AcdSfpInfoVendor_Object=MibTableColumn
acdSfpInfoVendor=_AcdSfpInfoVendor_Object((1,3,6,1,4,1,22420,2,4,1,1,4),_AcdSfpInfoVendor_Type())
acdSfpInfoVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoVendor.setStatus(_A)
class _AcdSfpInfoVendorOui_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_AcdSfpInfoVendorOui_Type.__name__=_D
_AcdSfpInfoVendorOui_Object=MibTableColumn
acdSfpInfoVendorOui=_AcdSfpInfoVendorOui_Object((1,3,6,1,4,1,22420,2,4,1,1,5),_AcdSfpInfoVendorOui_Type())
acdSfpInfoVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoVendorOui.setStatus(_A)
class _AcdSfpInfoVendorPn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcdSfpInfoVendorPn_Type.__name__=_D
_AcdSfpInfoVendorPn_Object=MibTableColumn
acdSfpInfoVendorPn=_AcdSfpInfoVendorPn_Object((1,3,6,1,4,1,22420,2,4,1,1,6),_AcdSfpInfoVendorPn_Type())
acdSfpInfoVendorPn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoVendorPn.setStatus(_A)
class _AcdSfpInfoVendorRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcdSfpInfoVendorRev_Type.__name__=_D
_AcdSfpInfoVendorRev_Object=MibTableColumn
acdSfpInfoVendorRev=_AcdSfpInfoVendorRev_Object((1,3,6,1,4,1,22420,2,4,1,1,7),_AcdSfpInfoVendorRev_Type())
acdSfpInfoVendorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoVendorRev.setStatus(_A)
_AcdSfpInfoWavelength_Type=Unsigned32
_AcdSfpInfoWavelength_Object=MibTableColumn
acdSfpInfoWavelength=_AcdSfpInfoWavelength_Object((1,3,6,1,4,1,22420,2,4,1,1,8),_AcdSfpInfoWavelength_Type())
acdSfpInfoWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoWavelength.setStatus(_A)
class _AcdSfpInfoSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AcdSfpInfoSerialNum_Type.__name__=_D
_AcdSfpInfoSerialNum_Object=MibTableColumn
acdSfpInfoSerialNum=_AcdSfpInfoSerialNum_Object((1,3,6,1,4,1,22420,2,4,1,1,9),_AcdSfpInfoSerialNum_Type())
acdSfpInfoSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoSerialNum.setStatus(_A)
_AcdSfpInfoYear_Type=Unsigned32
_AcdSfpInfoYear_Object=MibTableColumn
acdSfpInfoYear=_AcdSfpInfoYear_Object((1,3,6,1,4,1,22420,2,4,1,1,10),_AcdSfpInfoYear_Type())
acdSfpInfoYear.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoYear.setStatus(_A)
_AcdSfpInfoMonth_Type=Unsigned32
_AcdSfpInfoMonth_Object=MibTableColumn
acdSfpInfoMonth=_AcdSfpInfoMonth_Object((1,3,6,1,4,1,22420,2,4,1,1,11),_AcdSfpInfoMonth_Type())
acdSfpInfoMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoMonth.setStatus(_A)
_AcdSfpInfoDay_Type=Unsigned32
_AcdSfpInfoDay_Object=MibTableColumn
acdSfpInfoDay=_AcdSfpInfoDay_Object((1,3,6,1,4,1,22420,2,4,1,1,12),_AcdSfpInfoDay_Type())
acdSfpInfoDay.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoDay.setStatus(_A)
_AcdSfpInfoLot_Type=Unsigned32
_AcdSfpInfoLot_Object=MibTableColumn
acdSfpInfoLot=_AcdSfpInfoLot_Object((1,3,6,1,4,1,22420,2,4,1,1,13),_AcdSfpInfoLot_Type())
acdSfpInfoLot.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoLot.setStatus(_A)
class _AcdSfpInfoRev8472_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('rev93',1),('rev94',2)))
_AcdSfpInfoRev8472_Type.__name__=_F
_AcdSfpInfoRev8472_Object=MibTableColumn
acdSfpInfoRev8472=_AcdSfpInfoRev8472_Object((1,3,6,1,4,1,22420,2,4,1,1,14),_AcdSfpInfoRev8472_Type())
acdSfpInfoRev8472.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoRev8472.setStatus(_A)
_AcdSfpInfoPresent_Type=TruthValue
_AcdSfpInfoPresent_Object=MibTableColumn
acdSfpInfoPresent=_AcdSfpInfoPresent_Object((1,3,6,1,4,1,22420,2,4,1,1,15),_AcdSfpInfoPresent_Type())
acdSfpInfoPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoPresent.setStatus(_A)
_AcdSfpInfoDiag_Type=TruthValue
_AcdSfpInfoDiag_Object=MibTableColumn
acdSfpInfoDiag=_AcdSfpInfoDiag_Object((1,3,6,1,4,1,22420,2,4,1,1,16),_AcdSfpInfoDiag_Type())
acdSfpInfoDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoDiag.setStatus(_A)
_AcdSfpInfoInternal_Type=TruthValue
_AcdSfpInfoInternal_Object=MibTableColumn
acdSfpInfoInternal=_AcdSfpInfoInternal_Object((1,3,6,1,4,1,22420,2,4,1,1,17),_AcdSfpInfoInternal_Type())
acdSfpInfoInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoInternal.setStatus(_A)
_AcdSfpInfoAlm_Type=TruthValue
_AcdSfpInfoAlm_Object=MibTableColumn
acdSfpInfoAlm=_AcdSfpInfoAlm_Object((1,3,6,1,4,1,22420,2,4,1,1,18),_AcdSfpInfoAlm_Type())
acdSfpInfoAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoAlm.setStatus(_A)
_AcdSfpInfoIdType_Type=Unsigned32
_AcdSfpInfoIdType_Object=MibTableColumn
acdSfpInfoIdType=_AcdSfpInfoIdType_Object((1,3,6,1,4,1,22420,2,4,1,1,19),_AcdSfpInfoIdType_Type())
acdSfpInfoIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoIdType.setStatus(_A)
_AcdSfpInfoExtIdType_Type=Unsigned32
_AcdSfpInfoExtIdType_Object=MibTableColumn
acdSfpInfoExtIdType=_AcdSfpInfoExtIdType_Object((1,3,6,1,4,1,22420,2,4,1,1,20),_AcdSfpInfoExtIdType_Type())
acdSfpInfoExtIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoExtIdType.setStatus(_A)
class _AcdSfpInfoTransCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_AcdSfpInfoTransCode_Type.__name__=_D
_AcdSfpInfoTransCode_Object=MibTableColumn
acdSfpInfoTransCode=_AcdSfpInfoTransCode_Object((1,3,6,1,4,1,22420,2,4,1,1,21),_AcdSfpInfoTransCode_Type())
acdSfpInfoTransCode.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpInfoTransCode.setStatus(_A)
_AcdSfpDiagTable_Object=MibTable
acdSfpDiagTable=_AcdSfpDiagTable_Object((1,3,6,1,4,1,22420,2,4,2))
if mibBuilder.loadTexts:acdSfpDiagTable.setStatus(_A)
_AcdSfpDiagEntry_Object=MibTableRow
acdSfpDiagEntry=_AcdSfpDiagEntry_Object((1,3,6,1,4,1,22420,2,4,2,1))
acdSfpDiagEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:acdSfpDiagEntry.setStatus(_A)
_AcdSfpDiagID_Type=Unsigned32
_AcdSfpDiagID_Object=MibTableColumn
acdSfpDiagID=_AcdSfpDiagID_Object((1,3,6,1,4,1,22420,2,4,2,1,1),_AcdSfpDiagID_Type())
acdSfpDiagID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSfpDiagID.setStatus(_A)
_AcdSfpDiagConnIdx_Type=Unsigned32
_AcdSfpDiagConnIdx_Object=MibTableColumn
acdSfpDiagConnIdx=_AcdSfpDiagConnIdx_Object((1,3,6,1,4,1,22420,2,4,2,1,2),_AcdSfpDiagConnIdx_Type())
acdSfpDiagConnIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagConnIdx.setStatus(_A)
_AcdSfpDiagTemp_Type=Integer32
_AcdSfpDiagTemp_Object=MibTableColumn
acdSfpDiagTemp=_AcdSfpDiagTemp_Object((1,3,6,1,4,1,22420,2,4,2,1,3),_AcdSfpDiagTemp_Type())
acdSfpDiagTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagTemp.setStatus(_A)
_AcdSfpDiagVcc_Type=Unsigned32
_AcdSfpDiagVcc_Object=MibTableColumn
acdSfpDiagVcc=_AcdSfpDiagVcc_Object((1,3,6,1,4,1,22420,2,4,2,1,4),_AcdSfpDiagVcc_Type())
acdSfpDiagVcc.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagVcc.setStatus(_A)
_AcdSfpDiagLbc_Type=Unsigned32
_AcdSfpDiagLbc_Object=MibTableColumn
acdSfpDiagLbc=_AcdSfpDiagLbc_Object((1,3,6,1,4,1,22420,2,4,2,1,5),_AcdSfpDiagLbc_Type())
acdSfpDiagLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagLbc.setStatus(_A)
_AcdSfpDiagTxPwr_Type=Unsigned32
_AcdSfpDiagTxPwr_Object=MibTableColumn
acdSfpDiagTxPwr=_AcdSfpDiagTxPwr_Object((1,3,6,1,4,1,22420,2,4,2,1,6),_AcdSfpDiagTxPwr_Type())
acdSfpDiagTxPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagTxPwr.setStatus(_A)
_AcdSfpDiagRxPwr_Type=Unsigned32
_AcdSfpDiagRxPwr_Object=MibTableColumn
acdSfpDiagRxPwr=_AcdSfpDiagRxPwr_Object((1,3,6,1,4,1,22420,2,4,2,1,7),_AcdSfpDiagRxPwr_Type())
acdSfpDiagRxPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagRxPwr.setStatus(_A)
_AcdSfpDiagTxPwrdBm_Type=DisplayString
_AcdSfpDiagTxPwrdBm_Object=MibTableColumn
acdSfpDiagTxPwrdBm=_AcdSfpDiagTxPwrdBm_Object((1,3,6,1,4,1,22420,2,4,2,1,8),_AcdSfpDiagTxPwrdBm_Type())
acdSfpDiagTxPwrdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagTxPwrdBm.setStatus(_A)
_AcdSfpDiagRxPwrdBm_Type=DisplayString
_AcdSfpDiagRxPwrdBm_Object=MibTableColumn
acdSfpDiagRxPwrdBm=_AcdSfpDiagRxPwrdBm_Object((1,3,6,1,4,1,22420,2,4,2,1,9),_AcdSfpDiagRxPwrdBm_Type())
acdSfpDiagRxPwrdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpDiagRxPwrdBm.setStatus(_A)
_AcdSfpThreshTable_Object=MibTable
acdSfpThreshTable=_AcdSfpThreshTable_Object((1,3,6,1,4,1,22420,2,4,3))
if mibBuilder.loadTexts:acdSfpThreshTable.setStatus(_A)
_AcdSfpThreshEntry_Object=MibTableRow
acdSfpThreshEntry=_AcdSfpThreshEntry_Object((1,3,6,1,4,1,22420,2,4,3,1))
acdSfpThreshEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:acdSfpThreshEntry.setStatus(_A)
_AcdSfpThreshID_Type=Unsigned32
_AcdSfpThreshID_Object=MibTableColumn
acdSfpThreshID=_AcdSfpThreshID_Object((1,3,6,1,4,1,22420,2,4,3,1,1),_AcdSfpThreshID_Type())
acdSfpThreshID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSfpThreshID.setStatus(_A)
_AcdSfpThreshConnIdx_Type=Unsigned32
_AcdSfpThreshConnIdx_Object=MibTableColumn
acdSfpThreshConnIdx=_AcdSfpThreshConnIdx_Object((1,3,6,1,4,1,22420,2,4,3,1,2),_AcdSfpThreshConnIdx_Type())
acdSfpThreshConnIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshConnIdx.setStatus(_A)
_AcdSfpThreshTempHighAlm_Type=Integer32
_AcdSfpThreshTempHighAlm_Object=MibTableColumn
acdSfpThreshTempHighAlm=_AcdSfpThreshTempHighAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,3),_AcdSfpThreshTempHighAlm_Type())
acdSfpThreshTempHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTempHighAlm.setStatus(_A)
_AcdSfpThreshTempLowAlm_Type=Integer32
_AcdSfpThreshTempLowAlm_Object=MibTableColumn
acdSfpThreshTempLowAlm=_AcdSfpThreshTempLowAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,4),_AcdSfpThreshTempLowAlm_Type())
acdSfpThreshTempLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTempLowAlm.setStatus(_A)
_AcdSfpThreshTempHighWarn_Type=Integer32
_AcdSfpThreshTempHighWarn_Object=MibTableColumn
acdSfpThreshTempHighWarn=_AcdSfpThreshTempHighWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,5),_AcdSfpThreshTempHighWarn_Type())
acdSfpThreshTempHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTempHighWarn.setStatus(_A)
_AcdSfpThreshTempLowWarn_Type=Integer32
_AcdSfpThreshTempLowWarn_Object=MibTableColumn
acdSfpThreshTempLowWarn=_AcdSfpThreshTempLowWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,6),_AcdSfpThreshTempLowWarn_Type())
acdSfpThreshTempLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTempLowWarn.setStatus(_A)
_AcdSfpThreshVccHighAlm_Type=Unsigned32
_AcdSfpThreshVccHighAlm_Object=MibTableColumn
acdSfpThreshVccHighAlm=_AcdSfpThreshVccHighAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,7),_AcdSfpThreshVccHighAlm_Type())
acdSfpThreshVccHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshVccHighAlm.setStatus(_A)
_AcdSfpThreshVccLowAlm_Type=Unsigned32
_AcdSfpThreshVccLowAlm_Object=MibTableColumn
acdSfpThreshVccLowAlm=_AcdSfpThreshVccLowAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,8),_AcdSfpThreshVccLowAlm_Type())
acdSfpThreshVccLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshVccLowAlm.setStatus(_A)
_AcdSfpThreshVccHighWarn_Type=Unsigned32
_AcdSfpThreshVccHighWarn_Object=MibTableColumn
acdSfpThreshVccHighWarn=_AcdSfpThreshVccHighWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,9),_AcdSfpThreshVccHighWarn_Type())
acdSfpThreshVccHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshVccHighWarn.setStatus(_A)
_AcdSfpThreshVccLowWarn_Type=Unsigned32
_AcdSfpThreshVccLowWarn_Object=MibTableColumn
acdSfpThreshVccLowWarn=_AcdSfpThreshVccLowWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,10),_AcdSfpThreshVccLowWarn_Type())
acdSfpThreshVccLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshVccLowWarn.setStatus(_A)
_AcdSfpThreshLbcHighAlm_Type=Unsigned32
_AcdSfpThreshLbcHighAlm_Object=MibTableColumn
acdSfpThreshLbcHighAlm=_AcdSfpThreshLbcHighAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,11),_AcdSfpThreshLbcHighAlm_Type())
acdSfpThreshLbcHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshLbcHighAlm.setStatus(_A)
_AcdSfpThreshLbcLowAlm_Type=Unsigned32
_AcdSfpThreshLbcLowAlm_Object=MibTableColumn
acdSfpThreshLbcLowAlm=_AcdSfpThreshLbcLowAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,12),_AcdSfpThreshLbcLowAlm_Type())
acdSfpThreshLbcLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshLbcLowAlm.setStatus(_A)
_AcdSfpThreshLbcHighWarn_Type=Unsigned32
_AcdSfpThreshLbcHighWarn_Object=MibTableColumn
acdSfpThreshLbcHighWarn=_AcdSfpThreshLbcHighWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,13),_AcdSfpThreshLbcHighWarn_Type())
acdSfpThreshLbcHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshLbcHighWarn.setStatus(_A)
_AcdSfpThreshLbcLowWarn_Type=Unsigned32
_AcdSfpThreshLbcLowWarn_Object=MibTableColumn
acdSfpThreshLbcLowWarn=_AcdSfpThreshLbcLowWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,14),_AcdSfpThreshLbcLowWarn_Type())
acdSfpThreshLbcLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshLbcLowWarn.setStatus(_A)
_AcdSfpThreshTxPwrHighAlm_Type=Unsigned32
_AcdSfpThreshTxPwrHighAlm_Object=MibTableColumn
acdSfpThreshTxPwrHighAlm=_AcdSfpThreshTxPwrHighAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,15),_AcdSfpThreshTxPwrHighAlm_Type())
acdSfpThreshTxPwrHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrHighAlm.setStatus(_A)
_AcdSfpThreshTxPwrLowAlm_Type=Unsigned32
_AcdSfpThreshTxPwrLowAlm_Object=MibTableColumn
acdSfpThreshTxPwrLowAlm=_AcdSfpThreshTxPwrLowAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,16),_AcdSfpThreshTxPwrLowAlm_Type())
acdSfpThreshTxPwrLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrLowAlm.setStatus(_A)
_AcdSfpThreshTxPwrHighWarn_Type=Unsigned32
_AcdSfpThreshTxPwrHighWarn_Object=MibTableColumn
acdSfpThreshTxPwrHighWarn=_AcdSfpThreshTxPwrHighWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,17),_AcdSfpThreshTxPwrHighWarn_Type())
acdSfpThreshTxPwrHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrHighWarn.setStatus(_A)
_AcdSfpThreshTxPwrLowWarn_Type=Unsigned32
_AcdSfpThreshTxPwrLowWarn_Object=MibTableColumn
acdSfpThreshTxPwrLowWarn=_AcdSfpThreshTxPwrLowWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,18),_AcdSfpThreshTxPwrLowWarn_Type())
acdSfpThreshTxPwrLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrLowWarn.setStatus(_A)
_AcdSfpThreshRxPwrHighAlm_Type=Unsigned32
_AcdSfpThreshRxPwrHighAlm_Object=MibTableColumn
acdSfpThreshRxPwrHighAlm=_AcdSfpThreshRxPwrHighAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,19),_AcdSfpThreshRxPwrHighAlm_Type())
acdSfpThreshRxPwrHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrHighAlm.setStatus(_A)
_AcdSfpThreshRxPwrLowAlm_Type=Unsigned32
_AcdSfpThreshRxPwrLowAlm_Object=MibTableColumn
acdSfpThreshRxPwrLowAlm=_AcdSfpThreshRxPwrLowAlm_Object((1,3,6,1,4,1,22420,2,4,3,1,20),_AcdSfpThreshRxPwrLowAlm_Type())
acdSfpThreshRxPwrLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrLowAlm.setStatus(_A)
_AcdSfpThreshRxPwrHighWarn_Type=Unsigned32
_AcdSfpThreshRxPwrHighWarn_Object=MibTableColumn
acdSfpThreshRxPwrHighWarn=_AcdSfpThreshRxPwrHighWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,21),_AcdSfpThreshRxPwrHighWarn_Type())
acdSfpThreshRxPwrHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrHighWarn.setStatus(_A)
_AcdSfpThreshRxPwrLowWarn_Type=Unsigned32
_AcdSfpThreshRxPwrLowWarn_Object=MibTableColumn
acdSfpThreshRxPwrLowWarn=_AcdSfpThreshRxPwrLowWarn_Object((1,3,6,1,4,1,22420,2,4,3,1,22),_AcdSfpThreshRxPwrLowWarn_Type())
acdSfpThreshRxPwrLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrLowWarn.setStatus(_A)
_AcdSfpThreshTxPwrHighAlmdBm_Type=DisplayString
_AcdSfpThreshTxPwrHighAlmdBm_Object=MibTableColumn
acdSfpThreshTxPwrHighAlmdBm=_AcdSfpThreshTxPwrHighAlmdBm_Object((1,3,6,1,4,1,22420,2,4,3,1,23),_AcdSfpThreshTxPwrHighAlmdBm_Type())
acdSfpThreshTxPwrHighAlmdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrHighAlmdBm.setStatus(_A)
_AcdSfpThreshTxPwrLowAlmdBm_Type=DisplayString
_AcdSfpThreshTxPwrLowAlmdBm_Object=MibTableColumn
acdSfpThreshTxPwrLowAlmdBm=_AcdSfpThreshTxPwrLowAlmdBm_Object((1,3,6,1,4,1,22420,2,4,3,1,24),_AcdSfpThreshTxPwrLowAlmdBm_Type())
acdSfpThreshTxPwrLowAlmdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrLowAlmdBm.setStatus(_A)
_AcdSfpThreshTxPwrHighWarndBm_Type=DisplayString
_AcdSfpThreshTxPwrHighWarndBm_Object=MibTableColumn
acdSfpThreshTxPwrHighWarndBm=_AcdSfpThreshTxPwrHighWarndBm_Object((1,3,6,1,4,1,22420,2,4,3,1,25),_AcdSfpThreshTxPwrHighWarndBm_Type())
acdSfpThreshTxPwrHighWarndBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrHighWarndBm.setStatus(_A)
_AcdSfpThreshTxPwrLowWarndBm_Type=DisplayString
_AcdSfpThreshTxPwrLowWarndBm_Object=MibTableColumn
acdSfpThreshTxPwrLowWarndBm=_AcdSfpThreshTxPwrLowWarndBm_Object((1,3,6,1,4,1,22420,2,4,3,1,26),_AcdSfpThreshTxPwrLowWarndBm_Type())
acdSfpThreshTxPwrLowWarndBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshTxPwrLowWarndBm.setStatus(_A)
_AcdSfpThreshRxPwrHighAlmdBm_Type=DisplayString
_AcdSfpThreshRxPwrHighAlmdBm_Object=MibTableColumn
acdSfpThreshRxPwrHighAlmdBm=_AcdSfpThreshRxPwrHighAlmdBm_Object((1,3,6,1,4,1,22420,2,4,3,1,27),_AcdSfpThreshRxPwrHighAlmdBm_Type())
acdSfpThreshRxPwrHighAlmdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrHighAlmdBm.setStatus(_A)
_AcdSfpThreshRxPwrLowAlmdBm_Type=DisplayString
_AcdSfpThreshRxPwrLowAlmdBm_Object=MibTableColumn
acdSfpThreshRxPwrLowAlmdBm=_AcdSfpThreshRxPwrLowAlmdBm_Object((1,3,6,1,4,1,22420,2,4,3,1,28),_AcdSfpThreshRxPwrLowAlmdBm_Type())
acdSfpThreshRxPwrLowAlmdBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrLowAlmdBm.setStatus(_A)
_AcdSfpThreshRxPwrHighWarndBm_Type=DisplayString
_AcdSfpThreshRxPwrHighWarndBm_Object=MibTableColumn
acdSfpThreshRxPwrHighWarndBm=_AcdSfpThreshRxPwrHighWarndBm_Object((1,3,6,1,4,1,22420,2,4,3,1,29),_AcdSfpThreshRxPwrHighWarndBm_Type())
acdSfpThreshRxPwrHighWarndBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrHighWarndBm.setStatus(_A)
_AcdSfpThreshRxPwrLowWarndBm_Type=DisplayString
_AcdSfpThreshRxPwrLowWarndBm_Object=MibTableColumn
acdSfpThreshRxPwrLowWarndBm=_AcdSfpThreshRxPwrLowWarndBm_Object((1,3,6,1,4,1,22420,2,4,3,1,30),_AcdSfpThreshRxPwrLowWarndBm_Type())
acdSfpThreshRxPwrLowWarndBm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshRxPwrLowWarndBm.setStatus(_A)
_AcdSfpThreshStatusTable_Object=MibTable
acdSfpThreshStatusTable=_AcdSfpThreshStatusTable_Object((1,3,6,1,4,1,22420,2,4,4))
if mibBuilder.loadTexts:acdSfpThreshStatusTable.setStatus(_A)
_AcdSfpThreshStatusEntry_Object=MibTableRow
acdSfpThreshStatusEntry=_AcdSfpThreshStatusEntry_Object((1,3,6,1,4,1,22420,2,4,4,1))
acdSfpThreshStatusEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:acdSfpThreshStatusEntry.setStatus(_A)
_AcdSfpThreshStatusID_Type=Unsigned32
_AcdSfpThreshStatusID_Object=MibTableColumn
acdSfpThreshStatusID=_AcdSfpThreshStatusID_Object((1,3,6,1,4,1,22420,2,4,4,1,1),_AcdSfpThreshStatusID_Type())
acdSfpThreshStatusID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdSfpThreshStatusID.setStatus(_A)
_AcdSfpThreshStatusConnIdx_Type=Unsigned32
_AcdSfpThreshStatusConnIdx_Object=MibTableColumn
acdSfpThreshStatusConnIdx=_AcdSfpThreshStatusConnIdx_Object((1,3,6,1,4,1,22420,2,4,4,1,2),_AcdSfpThreshStatusConnIdx_Type())
acdSfpThreshStatusConnIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusConnIdx.setStatus(_A)
_AcdSfpThreshStatusTempHighAlm_Type=TruthValue
_AcdSfpThreshStatusTempHighAlm_Object=MibTableColumn
acdSfpThreshStatusTempHighAlm=_AcdSfpThreshStatusTempHighAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,3),_AcdSfpThreshStatusTempHighAlm_Type())
acdSfpThreshStatusTempHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTempHighAlm.setStatus(_A)
_AcdSfpThreshStatusTempLowAlm_Type=TruthValue
_AcdSfpThreshStatusTempLowAlm_Object=MibTableColumn
acdSfpThreshStatusTempLowAlm=_AcdSfpThreshStatusTempLowAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,4),_AcdSfpThreshStatusTempLowAlm_Type())
acdSfpThreshStatusTempLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTempLowAlm.setStatus(_A)
_AcdSfpThreshStatusTempHighWarn_Type=TruthValue
_AcdSfpThreshStatusTempHighWarn_Object=MibTableColumn
acdSfpThreshStatusTempHighWarn=_AcdSfpThreshStatusTempHighWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,5),_AcdSfpThreshStatusTempHighWarn_Type())
acdSfpThreshStatusTempHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTempHighWarn.setStatus(_A)
_AcdSfpThreshStatusTempLowWarn_Type=TruthValue
_AcdSfpThreshStatusTempLowWarn_Object=MibTableColumn
acdSfpThreshStatusTempLowWarn=_AcdSfpThreshStatusTempLowWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,6),_AcdSfpThreshStatusTempLowWarn_Type())
acdSfpThreshStatusTempLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTempLowWarn.setStatus(_A)
_AcdSfpThreshStatusVccHighAlm_Type=TruthValue
_AcdSfpThreshStatusVccHighAlm_Object=MibTableColumn
acdSfpThreshStatusVccHighAlm=_AcdSfpThreshStatusVccHighAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,7),_AcdSfpThreshStatusVccHighAlm_Type())
acdSfpThreshStatusVccHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusVccHighAlm.setStatus(_A)
_AcdSfpThreshStatusVccLowAlm_Type=TruthValue
_AcdSfpThreshStatusVccLowAlm_Object=MibTableColumn
acdSfpThreshStatusVccLowAlm=_AcdSfpThreshStatusVccLowAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,8),_AcdSfpThreshStatusVccLowAlm_Type())
acdSfpThreshStatusVccLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusVccLowAlm.setStatus(_A)
_AcdSfpThreshStatusVccHighWarn_Type=TruthValue
_AcdSfpThreshStatusVccHighWarn_Object=MibTableColumn
acdSfpThreshStatusVccHighWarn=_AcdSfpThreshStatusVccHighWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,9),_AcdSfpThreshStatusVccHighWarn_Type())
acdSfpThreshStatusVccHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusVccHighWarn.setStatus(_A)
_AcdSfpThreshStatusVccLowWarn_Type=TruthValue
_AcdSfpThreshStatusVccLowWarn_Object=MibTableColumn
acdSfpThreshStatusVccLowWarn=_AcdSfpThreshStatusVccLowWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,10),_AcdSfpThreshStatusVccLowWarn_Type())
acdSfpThreshStatusVccLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusVccLowWarn.setStatus(_A)
_AcdSfpThreshStatusLbcHighAlm_Type=TruthValue
_AcdSfpThreshStatusLbcHighAlm_Object=MibTableColumn
acdSfpThreshStatusLbcHighAlm=_AcdSfpThreshStatusLbcHighAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,11),_AcdSfpThreshStatusLbcHighAlm_Type())
acdSfpThreshStatusLbcHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusLbcHighAlm.setStatus(_A)
_AcdSfpThreshStatusLbcLowAlm_Type=TruthValue
_AcdSfpThreshStatusLbcLowAlm_Object=MibTableColumn
acdSfpThreshStatusLbcLowAlm=_AcdSfpThreshStatusLbcLowAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,12),_AcdSfpThreshStatusLbcLowAlm_Type())
acdSfpThreshStatusLbcLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusLbcLowAlm.setStatus(_A)
_AcdSfpThreshStatusLbcHighWarn_Type=TruthValue
_AcdSfpThreshStatusLbcHighWarn_Object=MibTableColumn
acdSfpThreshStatusLbcHighWarn=_AcdSfpThreshStatusLbcHighWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,13),_AcdSfpThreshStatusLbcHighWarn_Type())
acdSfpThreshStatusLbcHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusLbcHighWarn.setStatus(_A)
_AcdSfpThreshStatusLbcLowWarn_Type=TruthValue
_AcdSfpThreshStatusLbcLowWarn_Object=MibTableColumn
acdSfpThreshStatusLbcLowWarn=_AcdSfpThreshStatusLbcLowWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,14),_AcdSfpThreshStatusLbcLowWarn_Type())
acdSfpThreshStatusLbcLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusLbcLowWarn.setStatus(_A)
_AcdSfpThreshStatusTxPwrHighAlm_Type=TruthValue
_AcdSfpThreshStatusTxPwrHighAlm_Object=MibTableColumn
acdSfpThreshStatusTxPwrHighAlm=_AcdSfpThreshStatusTxPwrHighAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,15),_AcdSfpThreshStatusTxPwrHighAlm_Type())
acdSfpThreshStatusTxPwrHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTxPwrHighAlm.setStatus(_A)
_AcdSfpThreshStatusTxPwrLowAlm_Type=TruthValue
_AcdSfpThreshStatusTxPwrLowAlm_Object=MibTableColumn
acdSfpThreshStatusTxPwrLowAlm=_AcdSfpThreshStatusTxPwrLowAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,16),_AcdSfpThreshStatusTxPwrLowAlm_Type())
acdSfpThreshStatusTxPwrLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTxPwrLowAlm.setStatus(_A)
_AcdSfpThreshStatusTxPwrHighWarn_Type=TruthValue
_AcdSfpThreshStatusTxPwrHighWarn_Object=MibTableColumn
acdSfpThreshStatusTxPwrHighWarn=_AcdSfpThreshStatusTxPwrHighWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,17),_AcdSfpThreshStatusTxPwrHighWarn_Type())
acdSfpThreshStatusTxPwrHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTxPwrHighWarn.setStatus(_A)
_AcdSfpThreshStatusTxPwrLowWarn_Type=TruthValue
_AcdSfpThreshStatusTxPwrLowWarn_Object=MibTableColumn
acdSfpThreshStatusTxPwrLowWarn=_AcdSfpThreshStatusTxPwrLowWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,18),_AcdSfpThreshStatusTxPwrLowWarn_Type())
acdSfpThreshStatusTxPwrLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusTxPwrLowWarn.setStatus(_A)
_AcdSfpThreshStatusRxPwrHighAlm_Type=TruthValue
_AcdSfpThreshStatusRxPwrHighAlm_Object=MibTableColumn
acdSfpThreshStatusRxPwrHighAlm=_AcdSfpThreshStatusRxPwrHighAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,19),_AcdSfpThreshStatusRxPwrHighAlm_Type())
acdSfpThreshStatusRxPwrHighAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusRxPwrHighAlm.setStatus(_A)
_AcdSfpThreshStatusRxPwrLowAlm_Type=TruthValue
_AcdSfpThreshStatusRxPwrLowAlm_Object=MibTableColumn
acdSfpThreshStatusRxPwrLowAlm=_AcdSfpThreshStatusRxPwrLowAlm_Object((1,3,6,1,4,1,22420,2,4,4,1,20),_AcdSfpThreshStatusRxPwrLowAlm_Type())
acdSfpThreshStatusRxPwrLowAlm.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusRxPwrLowAlm.setStatus(_A)
_AcdSfpThreshStatusRxPwrHighWarn_Type=TruthValue
_AcdSfpThreshStatusRxPwrHighWarn_Object=MibTableColumn
acdSfpThreshStatusRxPwrHighWarn=_AcdSfpThreshStatusRxPwrHighWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,21),_AcdSfpThreshStatusRxPwrHighWarn_Type())
acdSfpThreshStatusRxPwrHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusRxPwrHighWarn.setStatus(_A)
_AcdSfpThreshStatusRxPwrLowWarn_Type=TruthValue
_AcdSfpThreshStatusRxPwrLowWarn_Object=MibTableColumn
acdSfpThreshStatusRxPwrLowWarn=_AcdSfpThreshStatusRxPwrLowWarn_Object((1,3,6,1,4,1,22420,2,4,4,1,22),_AcdSfpThreshStatusRxPwrLowWarn_Type())
acdSfpThreshStatusRxPwrLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:acdSfpThreshStatusRxPwrLowWarn.setStatus(_A)
_AcdSfpNotifications_ObjectIdentity=ObjectIdentity
acdSfpNotifications=_AcdSfpNotifications_ObjectIdentity((1,3,6,1,4,1,22420,2,4,5))
_AcdSfpMIBObjects_ObjectIdentity=ObjectIdentity
acdSfpMIBObjects=_AcdSfpMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,4,6))
_AcdSfpConformance_ObjectIdentity=ObjectIdentity
acdSfpConformance=_AcdSfpConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,4,7))
_AcdSfpCompliances_ObjectIdentity=ObjectIdentity
acdSfpCompliances=_AcdSfpCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,4,7,1))
_AcdSfpGroups_ObjectIdentity=ObjectIdentity
acdSfpGroups=_AcdSfpGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,4,7,2))
acdSfpInfoGroup=ObjectGroup((1,3,6,1,4,1,22420,2,4,7,2,1))
acdSfpInfoGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:acdSfpInfoGroup.setStatus(_A)
acdSfpDiagGroup=ObjectGroup((1,3,6,1,4,1,22420,2,4,7,2,2))
acdSfpDiagGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:acdSfpDiagGroup.setStatus(_A)
acdSfpThreshGroup=ObjectGroup((1,3,6,1,4,1,22420,2,4,7,2,3))
acdSfpThreshGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:acdSfpThreshGroup.setStatus(_A)
acdSfpThreshStatusGroup=ObjectGroup((1,3,6,1,4,1,22420,2,4,7,2,4))
acdSfpThreshStatusGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:acdSfpThreshStatusGroup.setStatus(_A)
acdSfpCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,4,7,1,1))
acdSfpCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:acdSfpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'acdSfp':acdSfp,'acdSfpInfoTable':acdSfpInfoTable,'acdSfpInfoEntry':acdSfpInfoEntry,_G:acdSfpInfoID,_K:acdSfpInfoConnIdx,_L:acdSfpInfoConnType,_M:acdSfpInfoVendor,_N:acdSfpInfoVendorOui,_O:acdSfpInfoVendorPn,_P:acdSfpInfoVendorRev,_Q:acdSfpInfoWavelength,_R:acdSfpInfoSerialNum,_S:acdSfpInfoYear,_T:acdSfpInfoMonth,_U:acdSfpInfoDay,_V:acdSfpInfoLot,_W:acdSfpInfoRev8472,_X:acdSfpInfoPresent,_Y:acdSfpInfoDiag,_Z:acdSfpInfoInternal,_a:acdSfpInfoAlm,_b:acdSfpInfoIdType,_c:acdSfpInfoExtIdType,_d:acdSfpInfoTransCode,'acdSfpDiagTable':acdSfpDiagTable,'acdSfpDiagEntry':acdSfpDiagEntry,_H:acdSfpDiagID,_e:acdSfpDiagConnIdx,_f:acdSfpDiagTemp,_g:acdSfpDiagVcc,_h:acdSfpDiagLbc,_i:acdSfpDiagTxPwr,_j:acdSfpDiagRxPwr,_k:acdSfpDiagTxPwrdBm,_l:acdSfpDiagRxPwrdBm,'acdSfpThreshTable':acdSfpThreshTable,'acdSfpThreshEntry':acdSfpThreshEntry,_I:acdSfpThreshID,_m:acdSfpThreshConnIdx,_n:acdSfpThreshTempHighAlm,_o:acdSfpThreshTempLowAlm,_p:acdSfpThreshTempHighWarn,_q:acdSfpThreshTempLowWarn,_r:acdSfpThreshVccHighAlm,_s:acdSfpThreshVccLowAlm,_t:acdSfpThreshVccHighWarn,_u:acdSfpThreshVccLowWarn,_v:acdSfpThreshLbcHighAlm,_w:acdSfpThreshLbcLowAlm,_x:acdSfpThreshLbcHighWarn,_y:acdSfpThreshLbcLowWarn,_z:acdSfpThreshTxPwrHighAlm,_A0:acdSfpThreshTxPwrLowAlm,_A1:acdSfpThreshTxPwrHighWarn,_A2:acdSfpThreshTxPwrLowWarn,_A3:acdSfpThreshRxPwrHighAlm,_A4:acdSfpThreshRxPwrLowAlm,_A5:acdSfpThreshRxPwrHighWarn,_A6:acdSfpThreshRxPwrLowWarn,_A7:acdSfpThreshTxPwrHighAlmdBm,_A8:acdSfpThreshTxPwrLowAlmdBm,_A9:acdSfpThreshTxPwrHighWarndBm,_AA:acdSfpThreshTxPwrLowWarndBm,_AB:acdSfpThreshRxPwrHighAlmdBm,_AC:acdSfpThreshRxPwrLowAlmdBm,_AD:acdSfpThreshRxPwrHighWarndBm,_AE:acdSfpThreshRxPwrLowWarndBm,'acdSfpThreshStatusTable':acdSfpThreshStatusTable,'acdSfpThreshStatusEntry':acdSfpThreshStatusEntry,_J:acdSfpThreshStatusID,_AF:acdSfpThreshStatusConnIdx,_AG:acdSfpThreshStatusTempHighAlm,_AH:acdSfpThreshStatusTempLowAlm,_AI:acdSfpThreshStatusTempHighWarn,_AJ:acdSfpThreshStatusTempLowWarn,_AK:acdSfpThreshStatusVccHighAlm,_AL:acdSfpThreshStatusVccLowAlm,_AM:acdSfpThreshStatusVccHighWarn,_AN:acdSfpThreshStatusVccLowWarn,_AO:acdSfpThreshStatusLbcHighAlm,_AP:acdSfpThreshStatusLbcLowAlm,_AQ:acdSfpThreshStatusLbcHighWarn,_AR:acdSfpThreshStatusLbcLowWarn,_AS:acdSfpThreshStatusTxPwrHighAlm,_AT:acdSfpThreshStatusTxPwrLowAlm,_AU:acdSfpThreshStatusTxPwrHighWarn,_AV:acdSfpThreshStatusTxPwrLowWarn,_AW:acdSfpThreshStatusRxPwrHighAlm,_AX:acdSfpThreshStatusRxPwrLowAlm,_AY:acdSfpThreshStatusRxPwrHighWarn,_AZ:acdSfpThreshStatusRxPwrLowWarn,'acdSfpNotifications':acdSfpNotifications,'acdSfpMIBObjects':acdSfpMIBObjects,'acdSfpConformance':acdSfpConformance,'acdSfpCompliances':acdSfpCompliances,'acdSfpCompliance':acdSfpCompliance,'acdSfpGroups':acdSfpGroups,_Aa:acdSfpInfoGroup,_Ab:acdSfpDiagGroup,_Ac:acdSfpThreshGroup,_Ad:acdSfpThreshStatusGroup})