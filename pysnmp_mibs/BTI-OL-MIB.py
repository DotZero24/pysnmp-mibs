_BJ='olPortActCnxDegree'
_BI='olPortExpCnxDegree'
_BH='wchOperStatQlfr'
_BG='wchOperStatus'
_BF='wdmOperStatQlfr'
_BE='wdmOperStatus'
_BD='olPortOperStatQlfr'
_BC='olPortOperStatus'
_BB='olOSCOperStatQlfr'
_BA='olOSCOperStatus'
_B9='wchHistPMIntervalIdx'
_B8='wchHistPMIntervalTypeIdx'
_B7='wchHistPMIdx'
_B6='wchHistPMPortIdx'
_B5='wchHistPMPortTypeIdx'
_B4='wchHistPMSlotIdx'
_B3='wchHistPMShelfIdx'
_B2='wchHistPMCpTypeIdx'
_B1='wchCrntPMIntervalTypeIdx'
_B0='wchCrntPMIdx'
_A_='wchCrntPMPortIdx'
_Az='wchCrntPMPortTypeIdx'
_Ay='wchCrntPMSlotIdx'
_Ax='wchCrntPMShelfIdx'
_Aw='wchCrntPMCpTypeIdx'
_Av='olPortHistPMIntervalIdx'
_Au='olPortHistPMIntervalTypeIdx'
_At='olPortHistPMIdx'
_As='olPortHistPMTypeIdx'
_Ar='olPortHistPMSlotIdx'
_Aq='olPortHistPMShelfIdx'
_Ap='olPortHistPMCpTypeIdx'
_Ao='olPortCrntPMIntervalTypeIdx'
_An='olPortCrntPMIdx'
_Am='olPortCrntPMTypeIdx'
_Al='olPortCrntPMSlotIdx'
_Ak='olPortCrntPMShelfIdx'
_Aj='olPortCrntPMCpTypeIdx'
_Ai='olOSCPMThresholdIntervalTypeIdx'
_Ah='olOSCPMThresholdLineIdx'
_Ag='olOSCPMThresholdSlotIdx'
_Af='olOSCPMThresholdShelfIdx'
_Ae='olOSCPMThresholdCpTypeIdx'
_Ad='olOSCHistPMIntervalIdx'
_Ac='olOSCHistPMIntervalTypeIdx'
_Ab='olOSCHistPMLineIdx'
_Aa='olOSCHistPMSlotIdx'
_AZ='olOSCHistPMShelfIdx'
_AY='olOSCHistPMCpTypeIdx'
_AX='olOSCCrntPMIntervalTypeIdx'
_AW='olOSCCrntPMLineIdx'
_AV='olOSCCrntPMSlotIdx'
_AU='olOSCCrntPMShelfIdx'
_AT='olOSCCrntPMCpTypeIdx'
_AS='wchXCDstChannelIdx'
_AR='wchXCDstPortIdx'
_AQ='wchXCDstPortTypeIdx'
_AP='wchXCDstSlotIdx'
_AO='wchXCDstShelfIdx'
_AN='wchXCDstCpTypeIdx'
_AM='wchXCSrcChannelIdx'
_AL='wchXCSrcPortIdx'
_AK='wchXCSrcPortTypeIdx'
_AJ='wchXCSrcSlotIdx'
_AI='wchXCSrcShelfIdx'
_AH='wchXCSrcCpTypeIdx'
_AG='odccLineIdx'
_AF='odccSlotIdx'
_AE='odccShelfIdx'
_AD='odccCpTypeIdx'
_AC='eqptConnDstIdx'
_AB='eqptConnDstPortTypeIdx'
_AA='eqptConnDstSlotIdx'
_A9='eqptConnDstShelfIdx'
_A8='eqptConnDstCpTypeIdx'
_A7='eqptConnSrcIdx'
_A6='eqptConnSrcPortTypeIdx'
_A5='eqptConnSrcSlotIdx'
_A4='eqptConnSrcShelfIdx'
_A3='eqptConnSrcCpTypeIdx'
_A2='terahertz/100'
_A1='nanometers/100'
_A0='olEqptSlotIdx'
_z='olEqptShelfIdx'
_y='olEqptCpTypeIdx'
_x='olGroupIdx'
_w='tcaValue'
_v='tcaThreshold'
_u='tcaMontype'
_t='tcaIntervalType'
_s='tcaDateAndTime'
_r='accessible-for-notify'
_q='evtObjectType'
_p='evtDescription'
_o='evtDateAndTime'
_n='evtCodeType'
_m='deprecated'
_l='wdmLineIdx'
_k='wdmSlotIdx'
_j='wdmShelfIdx'
_i='wdmCpTypeIdx'
_h='dB/10'
_g='read-create'
_f='wchIdx'
_e='wchPortIdx'
_d='wchPortTypeIdx'
_c='wchSlotIdx'
_b='wchShelfIdx'
_a='wchCpTypeIdx'
_Z='olOSCLineIdx'
_Y='olOSCSlotIdx'
_X='olOSCShelfIdx'
_W='olOSCCpTypeIdx'
_V='olPortTypeIdx'
_U='olPortSlotIdx'
_T='olPortShelfIdx'
_S='olPortCpTypeIdx'
_R='olPortIdx'
_Q='DisplayString'
_P='dBm/10'
_O='condSeverity'
_N='condServiceAffecting'
_M='condReportType'
_L='condObjectType'
_K='condDescription'
_J='condDateAndTime'
_I='condCodeType'
_H='trapSeqNum'
_G='read-write'
_F='Integer32'
_E='not-accessible'
_D='read-only'
_C='BTI-OL-MIB'
_B='current'
_A='BTI-7000-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
condCodeType,condDateAndTime,condDescription,condObjectType,condReportType,condServiceAffecting,condSeverity,evtCodeType,evtDateAndTime,evtDescription,evtObjectType,olCondNotifications,olEvtNotifications,opticalLayer,tcaDateAndTime,tcaIntervalType,tcaMontype,tcaThreshold,tcaValue,trapSeqNum=mibBuilder.importSymbols(_A,_I,_J,_K,_L,_M,_N,_O,_n,_o,_p,_q,'olCondNotifications','olEvtNotifications','opticalLayer',_s,_t,_u,_v,_w,_H)
btiModules,=mibBuilder.importSymbols('BTI-MIB','btiModules')
AdminStatus,BERType,CpType,FiberType,FixedX10,FixedX100,HoursAndMinutes,InitializeCmd,OperStatQlfr,OperStatus,PMIntervalType,PMValidity=mibBuilder.importSymbols('BTI-TC-MIB','AdminStatus','BERType','CpType','FiberType','FixedX10','FixedX100','HoursAndMinutes','InitializeCmd','OperStatQlfr','OperStatus','PMIntervalType','PMValidity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_Q,'PhysAddress','RowStatus','TextualConvention')
olMib=ModuleIdentity((1,3,6,1,4,1,18070,1,6))
if mibBuilder.loadTexts:olMib.setRevisions(('2012-08-17 12:00','2012-02-10 12:00','2011-09-26 12:00'))
class OlGroupType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('noEqlzTerm',2),('eqlzTerm',3),('noEqlzLine',4),('eqlzLine',5),('roadm',6)))
class OlPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('line',1),('client',2),('dcm',3),('channel',4),('expansion',5)))
_OlGroupTable_Object=MibTable
olGroupTable=_OlGroupTable_Object((1,3,6,1,4,1,18070,2,2,1,16,1))
if mibBuilder.loadTexts:olGroupTable.setStatus(_B)
_OlGroupEntry_Object=MibTableRow
olGroupEntry=_OlGroupEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1))
olGroupEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:olGroupEntry.setStatus(_B)
class _OlGroupIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlGroupIdx_Type.__name__=_F
_OlGroupIdx_Object=MibTableColumn
olGroupIdx=_OlGroupIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,1),_OlGroupIdx_Type())
olGroupIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olGroupIdx.setStatus(_B)
_OlGroupType_Type=OlGroupType
_OlGroupType_Object=MibTableColumn
olGroupType=_OlGroupType_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,2),_OlGroupType_Type())
olGroupType.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupType.setStatus(_B)
class _OlGroupId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OlGroupId_Type.__name__=_Q
_OlGroupId_Object=MibTableColumn
olGroupId=_OlGroupId_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,3),_OlGroupId_Type())
olGroupId.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupId.setStatus(_B)
class _OlGroupCustom1_Type(DisplayString):defaultValue=OctetString('')
_OlGroupCustom1_Type.__name__=_Q
_OlGroupCustom1_Object=MibTableColumn
olGroupCustom1=_OlGroupCustom1_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,4),_OlGroupCustom1_Type())
olGroupCustom1.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupCustom1.setStatus(_B)
class _OlGroupCustom2_Type(DisplayString):defaultValue=OctetString('')
_OlGroupCustom2_Type.__name__=_Q
_OlGroupCustom2_Object=MibTableColumn
olGroupCustom2=_OlGroupCustom2_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,5),_OlGroupCustom2_Type())
olGroupCustom2.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupCustom2.setStatus(_B)
class _OlGroupCustom3_Type(DisplayString):defaultValue=OctetString('')
_OlGroupCustom3_Type.__name__=_Q
_OlGroupCustom3_Object=MibTableColumn
olGroupCustom3=_OlGroupCustom3_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,6),_OlGroupCustom3_Type())
olGroupCustom3.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupCustom3.setStatus(_B)
_OlGroupRowStatus_Type=RowStatus
_OlGroupRowStatus_Object=MibTableColumn
olGroupRowStatus=_OlGroupRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,1,1,100),_OlGroupRowStatus_Type())
olGroupRowStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:olGroupRowStatus.setStatus(_B)
_OlEqptTable_Object=MibTable
olEqptTable=_OlEqptTable_Object((1,3,6,1,4,1,18070,2,2,1,16,3))
if mibBuilder.loadTexts:olEqptTable.setStatus(_B)
_OlEqptEntry_Object=MibTableRow
olEqptEntry=_OlEqptEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1))
olEqptEntry.setIndexNames((0,_C,_y),(0,_C,_z),(0,_C,_A0))
if mibBuilder.loadTexts:olEqptEntry.setStatus(_B)
_OlEqptCpTypeIdx_Type=CpType
_OlEqptCpTypeIdx_Object=MibTableColumn
olEqptCpTypeIdx=_OlEqptCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,1),_OlEqptCpTypeIdx_Type())
olEqptCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olEqptCpTypeIdx.setStatus(_B)
class _OlEqptShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlEqptShelfIdx_Type.__name__=_F
_OlEqptShelfIdx_Object=MibTableColumn
olEqptShelfIdx=_OlEqptShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,2),_OlEqptShelfIdx_Type())
olEqptShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olEqptShelfIdx.setStatus(_B)
class _OlEqptSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlEqptSlotIdx_Type.__name__=_F
_OlEqptSlotIdx_Object=MibTableColumn
olEqptSlotIdx=_OlEqptSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,3),_OlEqptSlotIdx_Type())
olEqptSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olEqptSlotIdx.setStatus(_B)
class _OlEqptGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlEqptGroupNum_Type.__name__=_F
_OlEqptGroupNum_Object=MibTableColumn
olEqptGroupNum=_OlEqptGroupNum_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,4),_OlEqptGroupNum_Type())
olEqptGroupNum.setMaxAccess(_g)
if mibBuilder.loadTexts:olEqptGroupNum.setStatus(_B)
class _OlEqptDegreeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OlEqptDegreeNum_Type.__name__=_F
_OlEqptDegreeNum_Object=MibTableColumn
olEqptDegreeNum=_OlEqptDegreeNum_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,5),_OlEqptDegreeNum_Type())
olEqptDegreeNum.setMaxAccess(_g)
if mibBuilder.loadTexts:olEqptDegreeNum.setStatus(_B)
_OlEqptRowStatus_Type=RowStatus
_OlEqptRowStatus_Object=MibTableColumn
olEqptRowStatus=_OlEqptRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,3,1,100),_OlEqptRowStatus_Type())
olEqptRowStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:olEqptRowStatus.setStatus(_B)
_OlPortTable_Object=MibTable
olPortTable=_OlPortTable_Object((1,3,6,1,4,1,18070,2,2,1,16,4))
if mibBuilder.loadTexts:olPortTable.setStatus(_B)
_OlPortEntry_Object=MibTableRow
olPortEntry=_OlPortEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1))
olPortEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_U),(0,_C,_V),(0,_C,_R))
if mibBuilder.loadTexts:olPortEntry.setStatus(_B)
_OlPortCpTypeIdx_Type=CpType
_OlPortCpTypeIdx_Object=MibTableColumn
olPortCpTypeIdx=_OlPortCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,1),_OlPortCpTypeIdx_Type())
olPortCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCpTypeIdx.setStatus(_B)
class _OlPortShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlPortShelfIdx_Type.__name__=_F
_OlPortShelfIdx_Object=MibTableColumn
olPortShelfIdx=_OlPortShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,2),_OlPortShelfIdx_Type())
olPortShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortShelfIdx.setStatus(_B)
class _OlPortSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlPortSlotIdx_Type.__name__=_F
_OlPortSlotIdx_Object=MibTableColumn
olPortSlotIdx=_OlPortSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,3),_OlPortSlotIdx_Type())
olPortSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortSlotIdx.setStatus(_B)
_OlPortTypeIdx_Type=OlPortType
_OlPortTypeIdx_Object=MibTableColumn
olPortTypeIdx=_OlPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,4),_OlPortTypeIdx_Type())
olPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortTypeIdx.setStatus(_B)
class _OlPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_OlPortIdx_Type.__name__=_F
_OlPortIdx_Object=MibTableColumn
olPortIdx=_OlPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,5),_OlPortIdx_Type())
olPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortIdx.setStatus(_B)
class _OlPortId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OlPortId_Type.__name__=_Q
_OlPortId_Object=MibTableColumn
olPortId=_OlPortId_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,6),_OlPortId_Type())
olPortId.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortId.setStatus(_B)
class _OlPortCustom1_Type(DisplayString):defaultValue=OctetString('')
_OlPortCustom1_Type.__name__=_Q
_OlPortCustom1_Object=MibTableColumn
olPortCustom1=_OlPortCustom1_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,7),_OlPortCustom1_Type())
olPortCustom1.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortCustom1.setStatus(_B)
class _OlPortCustom2_Type(DisplayString):defaultValue=OctetString('')
_OlPortCustom2_Type.__name__=_Q
_OlPortCustom2_Object=MibTableColumn
olPortCustom2=_OlPortCustom2_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,8),_OlPortCustom2_Type())
olPortCustom2.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortCustom2.setStatus(_B)
class _OlPortCustom3_Type(DisplayString):defaultValue=OctetString('')
_OlPortCustom3_Type.__name__=_Q
_OlPortCustom3_Object=MibTableColumn
olPortCustom3=_OlPortCustom3_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,9),_OlPortCustom3_Type())
olPortCustom3.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortCustom3.setStatus(_B)
class _OlPortDWDMType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('native',1),('alien',2)))
_OlPortDWDMType_Type.__name__=_F
_OlPortDWDMType_Object=MibTableColumn
olPortDWDMType=_OlPortDWDMType_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,10),_OlPortDWDMType_Type())
olPortDWDMType.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortDWDMType.setStatus(_B)
class _OlPortGrid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ghz100',1),('ghz50',2)))
_OlPortGrid_Type.__name__=_F
_OlPortGrid_Object=MibTableColumn
olPortGrid=_OlPortGrid_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,11),_OlPortGrid_Type())
olPortGrid.setMaxAccess(_G)
if mibBuilder.loadTexts:olPortGrid.setStatus(_B)
_OlPortWavelength_Type=FixedX100
_OlPortWavelength_Object=MibTableColumn
olPortWavelength=_OlPortWavelength_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,12),_OlPortWavelength_Type())
olPortWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortWavelength.setStatus(_B)
if mibBuilder.loadTexts:olPortWavelength.setUnits(_A1)
_OlPortFrequency_Type=FixedX100
_OlPortFrequency_Object=MibTableColumn
olPortFrequency=_OlPortFrequency_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,13),_OlPortFrequency_Type())
olPortFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortFrequency.setStatus(_B)
if mibBuilder.loadTexts:olPortFrequency.setUnits(_A2)
_OlPortOperStatus_Type=OperStatus
_OlPortOperStatus_Object=MibTableColumn
olPortOperStatus=_OlPortOperStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,14),_OlPortOperStatus_Type())
olPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortOperStatus.setStatus(_B)
_OlPortOperStatQlfr_Type=OperStatQlfr
_OlPortOperStatQlfr_Object=MibTableColumn
olPortOperStatQlfr=_OlPortOperStatQlfr_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,15),_OlPortOperStatQlfr_Type())
olPortOperStatQlfr.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortOperStatQlfr.setStatus(_B)
class _OlPortRemoteId_Type(DisplayString):defaultValue=OctetString('')
_OlPortRemoteId_Type.__name__=_Q
_OlPortRemoteId_Object=MibTableColumn
olPortRemoteId=_OlPortRemoteId_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,16),_OlPortRemoteId_Type())
olPortRemoteId.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortRemoteId.setStatus(_B)
class _OlPortExpCnxDegree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_OlPortExpCnxDegree_Type.__name__=_F
_OlPortExpCnxDegree_Object=MibTableColumn
olPortExpCnxDegree=_OlPortExpCnxDegree_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,17),_OlPortExpCnxDegree_Type())
olPortExpCnxDegree.setMaxAccess(_r)
if mibBuilder.loadTexts:olPortExpCnxDegree.setStatus(_B)
class _OlPortActCnxDegree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_OlPortActCnxDegree_Type.__name__=_F
_OlPortActCnxDegree_Object=MibTableColumn
olPortActCnxDegree=_OlPortActCnxDegree_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,18),_OlPortActCnxDegree_Type())
olPortActCnxDegree.setMaxAccess(_r)
if mibBuilder.loadTexts:olPortActCnxDegree.setStatus(_B)
_OlPortRowStatus_Type=RowStatus
_OlPortRowStatus_Object=MibTableColumn
olPortRowStatus=_OlPortRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,4,1,100),_OlPortRowStatus_Type())
olPortRowStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:olPortRowStatus.setStatus(_B)
_EqptConnTable_Object=MibTable
eqptConnTable=_EqptConnTable_Object((1,3,6,1,4,1,18070,2,2,1,16,5))
if mibBuilder.loadTexts:eqptConnTable.setStatus(_B)
_EqptConnEntry_Object=MibTableRow
eqptConnEntry=_EqptConnEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1))
eqptConnEntry.setIndexNames((0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6),(0,_C,_A7),(0,_C,_A8),(0,_C,_A9),(0,_C,_AA),(0,_C,_AB),(0,_C,_AC))
if mibBuilder.loadTexts:eqptConnEntry.setStatus(_B)
_EqptConnSrcCpTypeIdx_Type=CpType
_EqptConnSrcCpTypeIdx_Object=MibTableColumn
eqptConnSrcCpTypeIdx=_EqptConnSrcCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,1),_EqptConnSrcCpTypeIdx_Type())
eqptConnSrcCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnSrcCpTypeIdx.setStatus(_B)
class _EqptConnSrcShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_EqptConnSrcShelfIdx_Type.__name__=_F
_EqptConnSrcShelfIdx_Object=MibTableColumn
eqptConnSrcShelfIdx=_EqptConnSrcShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,2),_EqptConnSrcShelfIdx_Type())
eqptConnSrcShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnSrcShelfIdx.setStatus(_B)
class _EqptConnSrcSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EqptConnSrcSlotIdx_Type.__name__=_F
_EqptConnSrcSlotIdx_Object=MibTableColumn
eqptConnSrcSlotIdx=_EqptConnSrcSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,3),_EqptConnSrcSlotIdx_Type())
eqptConnSrcSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnSrcSlotIdx.setStatus(_B)
_EqptConnSrcPortTypeIdx_Type=OlPortType
_EqptConnSrcPortTypeIdx_Object=MibTableColumn
eqptConnSrcPortTypeIdx=_EqptConnSrcPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,4),_EqptConnSrcPortTypeIdx_Type())
eqptConnSrcPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnSrcPortTypeIdx.setStatus(_B)
class _EqptConnSrcIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_EqptConnSrcIdx_Type.__name__=_F
_EqptConnSrcIdx_Object=MibTableColumn
eqptConnSrcIdx=_EqptConnSrcIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,5),_EqptConnSrcIdx_Type())
eqptConnSrcIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnSrcIdx.setStatus(_B)
_EqptConnDstCpTypeIdx_Type=CpType
_EqptConnDstCpTypeIdx_Object=MibTableColumn
eqptConnDstCpTypeIdx=_EqptConnDstCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,6),_EqptConnDstCpTypeIdx_Type())
eqptConnDstCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnDstCpTypeIdx.setStatus(_B)
class _EqptConnDstShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_EqptConnDstShelfIdx_Type.__name__=_F
_EqptConnDstShelfIdx_Object=MibTableColumn
eqptConnDstShelfIdx=_EqptConnDstShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,7),_EqptConnDstShelfIdx_Type())
eqptConnDstShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnDstShelfIdx.setStatus(_B)
class _EqptConnDstSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EqptConnDstSlotIdx_Type.__name__=_F
_EqptConnDstSlotIdx_Object=MibTableColumn
eqptConnDstSlotIdx=_EqptConnDstSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,8),_EqptConnDstSlotIdx_Type())
eqptConnDstSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnDstSlotIdx.setStatus(_B)
_EqptConnDstPortTypeIdx_Type=OlPortType
_EqptConnDstPortTypeIdx_Object=MibTableColumn
eqptConnDstPortTypeIdx=_EqptConnDstPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,9),_EqptConnDstPortTypeIdx_Type())
eqptConnDstPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnDstPortTypeIdx.setStatus(_B)
class _EqptConnDstIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_EqptConnDstIdx_Type.__name__=_F
_EqptConnDstIdx_Object=MibTableColumn
eqptConnDstIdx=_EqptConnDstIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,10),_EqptConnDstIdx_Type())
eqptConnDstIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptConnDstIdx.setStatus(_B)
class _EqptConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('duplex',1),('loopback',2)))
_EqptConnType_Type.__name__=_F
_EqptConnType_Object=MibTableColumn
eqptConnType=_EqptConnType_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,11),_EqptConnType_Type())
eqptConnType.setMaxAccess(_D)
if mibBuilder.loadTexts:eqptConnType.setStatus(_B)
_EqptConnRowStatus_Type=RowStatus
_EqptConnRowStatus_Object=MibTableColumn
eqptConnRowStatus=_EqptConnRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,5,1,100),_EqptConnRowStatus_Type())
eqptConnRowStatus.setMaxAccess(_r)
if mibBuilder.loadTexts:eqptConnRowStatus.setStatus(_B)
_OlOSCTable_Object=MibTable
olOSCTable=_OlOSCTable_Object((1,3,6,1,4,1,18070,2,2,1,16,6))
if mibBuilder.loadTexts:olOSCTable.setStatus(_B)
_OlOSCEntry_Object=MibTableRow
olOSCEntry=_OlOSCEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1))
olOSCEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:olOSCEntry.setStatus(_B)
_OlOSCCpTypeIdx_Type=CpType
_OlOSCCpTypeIdx_Object=MibTableColumn
olOSCCpTypeIdx=_OlOSCCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,1),_OlOSCCpTypeIdx_Type())
olOSCCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCpTypeIdx.setStatus(_B)
class _OlOSCShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlOSCShelfIdx_Type.__name__=_F
_OlOSCShelfIdx_Object=MibTableColumn
olOSCShelfIdx=_OlOSCShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,2),_OlOSCShelfIdx_Type())
olOSCShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCShelfIdx.setStatus(_B)
class _OlOSCSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlOSCSlotIdx_Type.__name__=_F
_OlOSCSlotIdx_Object=MibTableColumn
olOSCSlotIdx=_OlOSCSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,3),_OlOSCSlotIdx_Type())
olOSCSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCSlotIdx.setStatus(_B)
class _OlOSCLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OlOSCLineIdx_Type.__name__=_F
_OlOSCLineIdx_Object=MibTableColumn
olOSCLineIdx=_OlOSCLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,4),_OlOSCLineIdx_Type())
olOSCLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCLineIdx.setStatus(_B)
_OlOSCAdminStatus_Type=AdminStatus
_OlOSCAdminStatus_Object=MibTableColumn
olOSCAdminStatus=_OlOSCAdminStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,5),_OlOSCAdminStatus_Type())
olOSCAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCAdminStatus.setStatus(_B)
_OlOSCOperStatus_Type=OperStatus
_OlOSCOperStatus_Object=MibTableColumn
olOSCOperStatus=_OlOSCOperStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,6),_OlOSCOperStatus_Type())
olOSCOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCOperStatus.setStatus(_B)
_OlOSCOperStatQlfr_Type=OperStatQlfr
_OlOSCOperStatQlfr_Object=MibTableColumn
olOSCOperStatQlfr=_OlOSCOperStatQlfr_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,7),_OlOSCOperStatQlfr_Type())
olOSCOperStatQlfr.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCOperStatQlfr.setStatus(_B)
_OlOSCAutoEnableTimer_Type=HoursAndMinutes
_OlOSCAutoEnableTimer_Object=MibTableColumn
olOSCAutoEnableTimer=_OlOSCAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,8),_OlOSCAutoEnableTimer_Type())
olOSCAutoEnableTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCAutoEnableTimer.setStatus(_B)
_OlOSCActAutoEnableTimer_Type=HoursAndMinutes
_OlOSCActAutoEnableTimer_Object=MibTableColumn
olOSCActAutoEnableTimer=_OlOSCActAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,9),_OlOSCActAutoEnableTimer_Type())
olOSCActAutoEnableTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCActAutoEnableTimer.setStatus(_B)
class _OlOSCId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OlOSCId_Type.__name__=_Q
_OlOSCId_Object=MibTableColumn
olOSCId=_OlOSCId_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,10),_OlOSCId_Type())
olOSCId.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCId.setStatus(_B)
class _OlOSCCustom1_Type(DisplayString):defaultValue=OctetString('')
_OlOSCCustom1_Type.__name__=_Q
_OlOSCCustom1_Object=MibTableColumn
olOSCCustom1=_OlOSCCustom1_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,11),_OlOSCCustom1_Type())
olOSCCustom1.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCustom1.setStatus(_B)
class _OlOSCCustom2_Type(DisplayString):defaultValue=OctetString('')
_OlOSCCustom2_Type.__name__=_Q
_OlOSCCustom2_Object=MibTableColumn
olOSCCustom2=_OlOSCCustom2_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,12),_OlOSCCustom2_Type())
olOSCCustom2.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCustom2.setStatus(_B)
class _OlOSCCustom3_Type(DisplayString):defaultValue=OctetString('')
_OlOSCCustom3_Type.__name__=_Q
_OlOSCCustom3_Object=MibTableColumn
olOSCCustom3=_OlOSCCustom3_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,13),_OlOSCCustom3_Type())
olOSCCustom3.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCustom3.setStatus(_B)
class _OlOSCFEIMMon_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OlOSCFEIMMon_Type.__name__=_F
_OlOSCFEIMMon_Object=MibTableColumn
olOSCFEIMMon=_OlOSCFEIMMon_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,14),_OlOSCFEIMMon_Type())
olOSCFEIMMon.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCFEIMMon.setStatus(_B)
class _OlOSCExpFESysName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_OlOSCExpFESysName_Type.__name__=_Q
_OlOSCExpFESysName_Object=MibTableColumn
olOSCExpFESysName=_OlOSCExpFESysName_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,15),_OlOSCExpFESysName_Type())
olOSCExpFESysName.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCExpFESysName.setStatus(_B)
_OlOSCExpFEIPAddr_Type=IpAddress
_OlOSCExpFEIPAddr_Object=MibTableColumn
olOSCExpFEIPAddr=_OlOSCExpFEIPAddr_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,16),_OlOSCExpFEIPAddr_Type())
olOSCExpFEIPAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCExpFEIPAddr.setStatus(_B)
class _OlOSCExpFEGrp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OlOSCExpFEGrp_Type.__name__=_F
_OlOSCExpFEGrp_Object=MibTableColumn
olOSCExpFEGrp=_OlOSCExpFEGrp_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,17),_OlOSCExpFEGrp_Type())
olOSCExpFEGrp.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCExpFEGrp.setStatus(_B)
class _OlOSCExpFEDegr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OlOSCExpFEDegr_Type.__name__=_F
_OlOSCExpFEDegr_Object=MibTableColumn
olOSCExpFEDegr=_OlOSCExpFEDegr_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,18),_OlOSCExpFEDegr_Type())
olOSCExpFEDegr.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCExpFEDegr.setStatus(_B)
class _OlOSCFESysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_OlOSCFESysName_Type.__name__=_Q
_OlOSCFESysName_Object=MibTableColumn
olOSCFESysName=_OlOSCFESysName_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,19),_OlOSCFESysName_Type())
olOSCFESysName.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCFESysName.setStatus(_B)
_OlOSCFEIPAddr_Type=IpAddress
_OlOSCFEIPAddr_Object=MibTableColumn
olOSCFEIPAddr=_OlOSCFEIPAddr_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,20),_OlOSCFEIPAddr_Type())
olOSCFEIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCFEIPAddr.setStatus(_B)
class _OlOSCFEGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OlOSCFEGrp_Type.__name__=_F
_OlOSCFEGrp_Object=MibTableColumn
olOSCFEGrp=_OlOSCFEGrp_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,21),_OlOSCFEGrp_Type())
olOSCFEGrp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCFEGrp.setStatus(_B)
class _OlOSCFEDegr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OlOSCFEDegr_Type.__name__=_F
_OlOSCFEDegr_Object=MibTableColumn
olOSCFEDegr=_OlOSCFEDegr_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,22),_OlOSCFEDegr_Type())
olOSCFEDegr.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCFEDegr.setStatus(_B)
_OlOSCFEGrpType_Type=OlGroupType
_OlOSCFEGrpType_Object=MibTableColumn
olOSCFEGrpType=_OlOSCFEGrpType_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,23),_OlOSCFEGrpType_Type())
olOSCFEGrpType.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCFEGrpType.setStatus(_B)
_OlOSCRowStatus_Type=RowStatus
_OlOSCRowStatus_Object=MibTableColumn
olOSCRowStatus=_OlOSCRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,6,1,100),_OlOSCRowStatus_Type())
olOSCRowStatus.setMaxAccess(_r)
if mibBuilder.loadTexts:olOSCRowStatus.setStatus(_B)
_OdccTable_Object=MibTable
odccTable=_OdccTable_Object((1,3,6,1,4,1,18070,2,2,1,16,7))
if mibBuilder.loadTexts:odccTable.setStatus(_B)
_OdccEntry_Object=MibTableRow
odccEntry=_OdccEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1))
odccEntry.setIndexNames((0,_C,_AD),(0,_C,_AE),(0,_C,_AF),(0,_C,_AG))
if mibBuilder.loadTexts:odccEntry.setStatus(_B)
_OdccCpTypeIdx_Type=CpType
_OdccCpTypeIdx_Object=MibTableColumn
odccCpTypeIdx=_OdccCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,1),_OdccCpTypeIdx_Type())
odccCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:odccCpTypeIdx.setStatus(_B)
class _OdccShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OdccShelfIdx_Type.__name__=_F
_OdccShelfIdx_Object=MibTableColumn
odccShelfIdx=_OdccShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,2),_OdccShelfIdx_Type())
odccShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:odccShelfIdx.setStatus(_B)
class _OdccSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OdccSlotIdx_Type.__name__=_F
_OdccSlotIdx_Object=MibTableColumn
odccSlotIdx=_OdccSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,3),_OdccSlotIdx_Type())
odccSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:odccSlotIdx.setStatus(_B)
class _OdccLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OdccLineIdx_Type.__name__=_F
_OdccLineIdx_Object=MibTableColumn
odccLineIdx=_OdccLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,4),_OdccLineIdx_Type())
odccLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:odccLineIdx.setStatus(_B)
_OdccAdminStatus_Type=AdminStatus
_OdccAdminStatus_Object=MibTableColumn
odccAdminStatus=_OdccAdminStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,5),_OdccAdminStatus_Type())
odccAdminStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:odccAdminStatus.setStatus(_B)
_OdccRowStatus_Type=RowStatus
_OdccRowStatus_Object=MibTableColumn
odccRowStatus=_OdccRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,7,1,100),_OdccRowStatus_Type())
odccRowStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:odccRowStatus.setStatus(_B)
_WdmTable_Object=MibTable
wdmTable=_WdmTable_Object((1,3,6,1,4,1,18070,2,2,1,16,8))
if mibBuilder.loadTexts:wdmTable.setStatus(_B)
_WdmEntry_Object=MibTableRow
wdmEntry=_WdmEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1))
wdmEntry.setIndexNames((0,_C,_i),(0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:wdmEntry.setStatus(_B)
_WdmCpTypeIdx_Type=CpType
_WdmCpTypeIdx_Object=MibTableColumn
wdmCpTypeIdx=_WdmCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,1),_WdmCpTypeIdx_Type())
wdmCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wdmCpTypeIdx.setStatus(_B)
class _WdmShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WdmShelfIdx_Type.__name__=_F
_WdmShelfIdx_Object=MibTableColumn
wdmShelfIdx=_WdmShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,2),_WdmShelfIdx_Type())
wdmShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wdmShelfIdx.setStatus(_B)
class _WdmSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WdmSlotIdx_Type.__name__=_F
_WdmSlotIdx_Object=MibTableColumn
wdmSlotIdx=_WdmSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,3),_WdmSlotIdx_Type())
wdmSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wdmSlotIdx.setStatus(_B)
class _WdmLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_WdmLineIdx_Type.__name__=_F
_WdmLineIdx_Object=MibTableColumn
wdmLineIdx=_WdmLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,4),_WdmLineIdx_Type())
wdmLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wdmLineIdx.setStatus(_B)
_WdmAdminStatus_Type=AdminStatus
_WdmAdminStatus_Object=MibTableColumn
wdmAdminStatus=_WdmAdminStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,5),_WdmAdminStatus_Type())
wdmAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmAdminStatus.setStatus(_B)
_WdmOperStatus_Type=OperStatus
_WdmOperStatus_Object=MibTableColumn
wdmOperStatus=_WdmOperStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,6),_WdmOperStatus_Type())
wdmOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmOperStatus.setStatus(_B)
_WdmOperStatQlfr_Type=OperStatQlfr
_WdmOperStatQlfr_Object=MibTableColumn
wdmOperStatQlfr=_WdmOperStatQlfr_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,7),_WdmOperStatQlfr_Type())
wdmOperStatQlfr.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmOperStatQlfr.setStatus(_B)
_WdmAutoEnableTimer_Type=HoursAndMinutes
_WdmAutoEnableTimer_Object=MibTableColumn
wdmAutoEnableTimer=_WdmAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,8),_WdmAutoEnableTimer_Type())
wdmAutoEnableTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmAutoEnableTimer.setStatus(_B)
_WdmActAutoEnableTimer_Type=HoursAndMinutes
_WdmActAutoEnableTimer_Object=MibTableColumn
wdmActAutoEnableTimer=_WdmActAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,9),_WdmActAutoEnableTimer_Type())
wdmActAutoEnableTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmActAutoEnableTimer.setStatus(_B)
class _WdmId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WdmId_Type.__name__=_Q
_WdmId_Object=MibTableColumn
wdmId=_WdmId_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,10),_WdmId_Type())
wdmId.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmId.setStatus(_B)
class _WdmCustom1_Type(DisplayString):defaultValue=OctetString('')
_WdmCustom1_Type.__name__=_Q
_WdmCustom1_Object=MibTableColumn
wdmCustom1=_WdmCustom1_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,11),_WdmCustom1_Type())
wdmCustom1.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmCustom1.setStatus(_B)
class _WdmCustom2_Type(DisplayString):defaultValue=OctetString('')
_WdmCustom2_Type.__name__=_Q
_WdmCustom2_Object=MibTableColumn
wdmCustom2=_WdmCustom2_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,12),_WdmCustom2_Type())
wdmCustom2.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmCustom2.setStatus(_B)
class _WdmCustom3_Type(DisplayString):defaultValue=OctetString('')
_WdmCustom3_Type.__name__=_Q
_WdmCustom3_Object=MibTableColumn
wdmCustom3=_WdmCustom3_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,13),_WdmCustom3_Type())
wdmCustom3.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmCustom3.setStatus(_B)
class _WdmFiberType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('smf',1))
_WdmFiberType_Type.__name__=_F
_WdmFiberType_Object=MibTableColumn
wdmFiberType=_WdmFiberType_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,14),_WdmFiberType_Type())
wdmFiberType.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmFiberType.setStatus(_B)
_WdmSpanLength_Type=Unsigned32
_WdmSpanLength_Object=MibTableColumn
wdmSpanLength=_WdmSpanLength_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,15),_WdmSpanLength_Type())
wdmSpanLength.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmSpanLength.setStatus(_B)
if mibBuilder.loadTexts:wdmSpanLength.setUnits('kilometers')
_WdmSpanLossRxHighTh_Type=FixedX10
_WdmSpanLossRxHighTh_Object=MibTableColumn
wdmSpanLossRxHighTh=_WdmSpanLossRxHighTh_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,16),_WdmSpanLossRxHighTh_Type())
wdmSpanLossRxHighTh.setMaxAccess(_G)
if mibBuilder.loadTexts:wdmSpanLossRxHighTh.setStatus(_B)
if mibBuilder.loadTexts:wdmSpanLossRxHighTh.setUnits(_h)
_WdmSpanLossSpecMax_Type=FixedX10
_WdmSpanLossSpecMax_Object=MibTableColumn
wdmSpanLossSpecMax=_WdmSpanLossSpecMax_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,17),_WdmSpanLossSpecMax_Type())
wdmSpanLossSpecMax.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmSpanLossSpecMax.setStatus(_B)
if mibBuilder.loadTexts:wdmSpanLossSpecMax.setUnits(_h)
class _WdmNumChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,44))
_WdmNumChannels_Type.__name__=_F
_WdmNumChannels_Object=MibTableColumn
wdmNumChannels=_WdmNumChannels_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,18),_WdmNumChannels_Type())
wdmNumChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:wdmNumChannels.setStatus(_B)
_WdmRowStatus_Type=RowStatus
_WdmRowStatus_Object=MibTableColumn
wdmRowStatus=_WdmRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,8,1,100),_WdmRowStatus_Type())
wdmRowStatus.setMaxAccess(_r)
if mibBuilder.loadTexts:wdmRowStatus.setStatus(_B)
_WchXCTable_Object=MibTable
wchXCTable=_WchXCTable_Object((1,3,6,1,4,1,18070,2,2,1,16,9))
if mibBuilder.loadTexts:wchXCTable.setStatus(_B)
_WchXCEntry_Object=MibTableRow
wchXCEntry=_WchXCEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1))
wchXCEntry.setIndexNames((0,_C,_AH),(0,_C,_AI),(0,_C,_AJ),(0,_C,_AK),(0,_C,_AL),(0,_C,_AM),(0,_C,_AN),(0,_C,_AO),(0,_C,_AP),(0,_C,_AQ),(0,_C,_AR),(0,_C,_AS))
if mibBuilder.loadTexts:wchXCEntry.setStatus(_B)
_WchXCSrcCpTypeIdx_Type=CpType
_WchXCSrcCpTypeIdx_Object=MibTableColumn
wchXCSrcCpTypeIdx=_WchXCSrcCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,1),_WchXCSrcCpTypeIdx_Type())
wchXCSrcCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcCpTypeIdx.setStatus(_B)
class _WchXCSrcShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WchXCSrcShelfIdx_Type.__name__=_F
_WchXCSrcShelfIdx_Object=MibTableColumn
wchXCSrcShelfIdx=_WchXCSrcShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,2),_WchXCSrcShelfIdx_Type())
wchXCSrcShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcShelfIdx.setStatus(_B)
class _WchXCSrcSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WchXCSrcSlotIdx_Type.__name__=_F
_WchXCSrcSlotIdx_Object=MibTableColumn
wchXCSrcSlotIdx=_WchXCSrcSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,3),_WchXCSrcSlotIdx_Type())
wchXCSrcSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcSlotIdx.setStatus(_B)
_WchXCSrcPortTypeIdx_Type=OlPortType
_WchXCSrcPortTypeIdx_Object=MibTableColumn
wchXCSrcPortTypeIdx=_WchXCSrcPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,4),_WchXCSrcPortTypeIdx_Type())
wchXCSrcPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcPortTypeIdx.setStatus(_B)
class _WchXCSrcPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_WchXCSrcPortIdx_Type.__name__=_F
_WchXCSrcPortIdx_Object=MibTableColumn
wchXCSrcPortIdx=_WchXCSrcPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,5),_WchXCSrcPortIdx_Type())
wchXCSrcPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcPortIdx.setStatus(_B)
class _WchXCSrcChannelIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(135,610))
_WchXCSrcChannelIdx_Type.__name__=_F
_WchXCSrcChannelIdx_Object=MibTableColumn
wchXCSrcChannelIdx=_WchXCSrcChannelIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,6),_WchXCSrcChannelIdx_Type())
wchXCSrcChannelIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCSrcChannelIdx.setStatus(_B)
_WchXCDstCpTypeIdx_Type=CpType
_WchXCDstCpTypeIdx_Object=MibTableColumn
wchXCDstCpTypeIdx=_WchXCDstCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,7),_WchXCDstCpTypeIdx_Type())
wchXCDstCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstCpTypeIdx.setStatus(_B)
class _WchXCDstShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WchXCDstShelfIdx_Type.__name__=_F
_WchXCDstShelfIdx_Object=MibTableColumn
wchXCDstShelfIdx=_WchXCDstShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,8),_WchXCDstShelfIdx_Type())
wchXCDstShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstShelfIdx.setStatus(_B)
class _WchXCDstSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WchXCDstSlotIdx_Type.__name__=_F
_WchXCDstSlotIdx_Object=MibTableColumn
wchXCDstSlotIdx=_WchXCDstSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,9),_WchXCDstSlotIdx_Type())
wchXCDstSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstSlotIdx.setStatus(_B)
_WchXCDstPortTypeIdx_Type=OlPortType
_WchXCDstPortTypeIdx_Object=MibTableColumn
wchXCDstPortTypeIdx=_WchXCDstPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,10),_WchXCDstPortTypeIdx_Type())
wchXCDstPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstPortTypeIdx.setStatus(_B)
class _WchXCDstPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_WchXCDstPortIdx_Type.__name__=_F
_WchXCDstPortIdx_Object=MibTableColumn
wchXCDstPortIdx=_WchXCDstPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,11),_WchXCDstPortIdx_Type())
wchXCDstPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstPortIdx.setStatus(_B)
class _WchXCDstChannelIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(135,610))
_WchXCDstChannelIdx_Type.__name__=_F
_WchXCDstChannelIdx_Object=MibTableColumn
wchXCDstChannelIdx=_WchXCDstChannelIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,12),_WchXCDstChannelIdx_Type())
wchXCDstChannelIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchXCDstChannelIdx.setStatus(_B)
class _WchXCServiceName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WchXCServiceName_Type.__name__=_Q
_WchXCServiceName_Object=MibTableColumn
wchXCServiceName=_WchXCServiceName_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,13),_WchXCServiceName_Type())
wchXCServiceName.setMaxAccess(_g)
if mibBuilder.loadTexts:wchXCServiceName.setStatus(_B)
_WchXCRowStatus_Type=RowStatus
_WchXCRowStatus_Object=MibTableColumn
wchXCRowStatus=_WchXCRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,9,1,100),_WchXCRowStatus_Type())
wchXCRowStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:wchXCRowStatus.setStatus(_B)
_WchTable_Object=MibTable
wchTable=_WchTable_Object((1,3,6,1,4,1,18070,2,2,1,16,10))
if mibBuilder.loadTexts:wchTable.setStatus(_B)
_WchEntry_Object=MibTableRow
wchEntry=_WchEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1))
wchEntry.setIndexNames((0,_C,_a),(0,_C,_b),(0,_C,_c),(0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:wchEntry.setStatus(_B)
_WchCpTypeIdx_Type=CpType
_WchCpTypeIdx_Object=MibTableColumn
wchCpTypeIdx=_WchCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,1),_WchCpTypeIdx_Type())
wchCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCpTypeIdx.setStatus(_B)
class _WchShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WchShelfIdx_Type.__name__=_F
_WchShelfIdx_Object=MibTableColumn
wchShelfIdx=_WchShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,2),_WchShelfIdx_Type())
wchShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchShelfIdx.setStatus(_B)
class _WchSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WchSlotIdx_Type.__name__=_F
_WchSlotIdx_Object=MibTableColumn
wchSlotIdx=_WchSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,3),_WchSlotIdx_Type())
wchSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchSlotIdx.setStatus(_B)
_WchPortTypeIdx_Type=OlPortType
_WchPortTypeIdx_Object=MibTableColumn
wchPortTypeIdx=_WchPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,4),_WchPortTypeIdx_Type())
wchPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchPortTypeIdx.setStatus(_B)
class _WchPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WchPortIdx_Type.__name__=_F
_WchPortIdx_Object=MibTableColumn
wchPortIdx=_WchPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,5),_WchPortIdx_Type())
wchPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchPortIdx.setStatus(_B)
class _WchIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(135,610))
_WchIdx_Type.__name__=_F
_WchIdx_Object=MibTableColumn
wchIdx=_WchIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,6),_WchIdx_Type())
wchIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchIdx.setStatus(_B)
_WchAdminStatus_Type=AdminStatus
_WchAdminStatus_Object=MibTableColumn
wchAdminStatus=_WchAdminStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,7),_WchAdminStatus_Type())
wchAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wchAdminStatus.setStatus(_B)
_WchOperStatus_Type=OperStatus
_WchOperStatus_Object=MibTableColumn
wchOperStatus=_WchOperStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,8),_WchOperStatus_Type())
wchOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wchOperStatus.setStatus(_B)
_WchOperStatQlfr_Type=OperStatQlfr
_WchOperStatQlfr_Object=MibTableColumn
wchOperStatQlfr=_WchOperStatQlfr_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,9),_WchOperStatQlfr_Type())
wchOperStatQlfr.setMaxAccess(_D)
if mibBuilder.loadTexts:wchOperStatQlfr.setStatus(_B)
_WchAutoEnableTimer_Type=HoursAndMinutes
_WchAutoEnableTimer_Object=MibTableColumn
wchAutoEnableTimer=_WchAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,10),_WchAutoEnableTimer_Type())
wchAutoEnableTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:wchAutoEnableTimer.setStatus(_B)
_WchActAutoEnableTimer_Type=HoursAndMinutes
_WchActAutoEnableTimer_Object=MibTableColumn
wchActAutoEnableTimer=_WchActAutoEnableTimer_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,11),_WchActAutoEnableTimer_Type())
wchActAutoEnableTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:wchActAutoEnableTimer.setStatus(_B)
class _WchId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WchId_Type.__name__=_Q
_WchId_Object=MibTableColumn
wchId=_WchId_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,12),_WchId_Type())
wchId.setMaxAccess(_G)
if mibBuilder.loadTexts:wchId.setStatus(_B)
class _WchCustom1_Type(DisplayString):defaultValue=OctetString('')
_WchCustom1_Type.__name__=_Q
_WchCustom1_Object=MibTableColumn
wchCustom1=_WchCustom1_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,13),_WchCustom1_Type())
wchCustom1.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCustom1.setStatus(_B)
class _WchCustom2_Type(DisplayString):defaultValue=OctetString('')
_WchCustom2_Type.__name__=_Q
_WchCustom2_Object=MibTableColumn
wchCustom2=_WchCustom2_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,14),_WchCustom2_Type())
wchCustom2.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCustom2.setStatus(_B)
class _WchCustom3_Type(DisplayString):defaultValue=OctetString('')
_WchCustom3_Type.__name__=_Q
_WchCustom3_Object=MibTableColumn
wchCustom3=_WchCustom3_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,15),_WchCustom3_Type())
wchCustom3.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCustom3.setStatus(_B)
class _WchBitrate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('tenGig',1))
_WchBitrate_Type.__name__=_F
_WchBitrate_Object=MibTableColumn
wchBitrate=_WchBitrate_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,16),_WchBitrate_Type())
wchBitrate.setMaxAccess(_G)
if mibBuilder.loadTexts:wchBitrate.setStatus(_B)
class _WchGrid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ghz100',1),('ghz50',2)))
_WchGrid_Type.__name__=_F
_WchGrid_Object=MibTableColumn
wchGrid=_WchGrid_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,17),_WchGrid_Type())
wchGrid.setMaxAccess(_G)
if mibBuilder.loadTexts:wchGrid.setStatus(_B)
_WchWavelength_Type=FixedX100
_WchWavelength_Object=MibTableColumn
wchWavelength=_WchWavelength_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,18),_WchWavelength_Type())
wchWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:wchWavelength.setStatus(_B)
if mibBuilder.loadTexts:wchWavelength.setUnits(_A1)
_WchFrequency_Type=FixedX100
_WchFrequency_Object=MibTableColumn
wchFrequency=_WchFrequency_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,19),_WchFrequency_Type())
wchFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:wchFrequency.setStatus(_B)
if mibBuilder.loadTexts:wchFrequency.setUnits(_A2)
_WchRowStatus_Type=RowStatus
_WchRowStatus_Object=MibTableColumn
wchRowStatus=_WchRowStatus_Object((1,3,6,1,4,1,18070,2,2,1,16,10,1,100),_WchRowStatus_Type())
wchRowStatus.setMaxAccess(_r)
if mibBuilder.loadTexts:wchRowStatus.setStatus(_B)
_OlGroupMerge_ObjectIdentity=ObjectIdentity
olGroupMerge=_OlGroupMerge_ObjectIdentity((1,3,6,1,4,1,18070,2,2,1,16,11))
class _OlGroupMergeCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('invoke',2)))
_OlGroupMergeCmd_Type.__name__=_F
_OlGroupMergeCmd_Object=MibScalar
olGroupMergeCmd=_OlGroupMergeCmd_Object((1,3,6,1,4,1,18070,2,2,1,16,11,1),_OlGroupMergeCmd_Type())
olGroupMergeCmd.setMaxAccess(_G)
if mibBuilder.loadTexts:olGroupMergeCmd.setStatus(_B)
class _OlGroupMergePrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlGroupMergePrimary_Type.__name__=_F
_OlGroupMergePrimary_Object=MibScalar
olGroupMergePrimary=_OlGroupMergePrimary_Object((1,3,6,1,4,1,18070,2,2,1,16,11,2),_OlGroupMergePrimary_Type())
olGroupMergePrimary.setMaxAccess(_G)
if mibBuilder.loadTexts:olGroupMergePrimary.setStatus(_B)
class _OlGroupMergeSecondary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OlGroupMergeSecondary_Type.__name__=_F
_OlGroupMergeSecondary_Object=MibScalar
olGroupMergeSecondary=_OlGroupMergeSecondary_Object((1,3,6,1,4,1,18070,2,2,1,16,11,3),_OlGroupMergeSecondary_Type())
olGroupMergeSecondary.setMaxAccess(_G)
if mibBuilder.loadTexts:olGroupMergeSecondary.setStatus(_B)
_OlPerformance_ObjectIdentity=ObjectIdentity
olPerformance=_OlPerformance_ObjectIdentity((1,3,6,1,4,1,18070,2,2,1,16,12))
_OlOSCCrntPMTable_Object=MibTable
olOSCCrntPMTable=_OlOSCCrntPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1))
if mibBuilder.loadTexts:olOSCCrntPMTable.setStatus(_B)
_OlOSCCrntPMEntry_Object=MibTableRow
olOSCCrntPMEntry=_OlOSCCrntPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1))
olOSCCrntPMEntry.setIndexNames((0,_C,_AT),(0,_C,_AU),(0,_C,_AV),(0,_C,_AW),(0,_C,_AX))
if mibBuilder.loadTexts:olOSCCrntPMEntry.setStatus(_B)
_OlOSCCrntPMCpTypeIdx_Type=CpType
_OlOSCCrntPMCpTypeIdx_Object=MibTableColumn
olOSCCrntPMCpTypeIdx=_OlOSCCrntPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,1),_OlOSCCrntPMCpTypeIdx_Type())
olOSCCrntPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCrntPMCpTypeIdx.setStatus(_B)
class _OlOSCCrntPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlOSCCrntPMShelfIdx_Type.__name__=_F
_OlOSCCrntPMShelfIdx_Object=MibTableColumn
olOSCCrntPMShelfIdx=_OlOSCCrntPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,2),_OlOSCCrntPMShelfIdx_Type())
olOSCCrntPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCrntPMShelfIdx.setStatus(_B)
class _OlOSCCrntPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlOSCCrntPMSlotIdx_Type.__name__=_F
_OlOSCCrntPMSlotIdx_Object=MibTableColumn
olOSCCrntPMSlotIdx=_OlOSCCrntPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,3),_OlOSCCrntPMSlotIdx_Type())
olOSCCrntPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCrntPMSlotIdx.setStatus(_B)
class _OlOSCCrntPMLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OlOSCCrntPMLineIdx_Type.__name__=_F
_OlOSCCrntPMLineIdx_Object=MibTableColumn
olOSCCrntPMLineIdx=_OlOSCCrntPMLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,4),_OlOSCCrntPMLineIdx_Type())
olOSCCrntPMLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCrntPMLineIdx.setStatus(_B)
_OlOSCCrntPMIntervalTypeIdx_Type=PMIntervalType
_OlOSCCrntPMIntervalTypeIdx_Object=MibTableColumn
olOSCCrntPMIntervalTypeIdx=_OlOSCCrntPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,5),_OlOSCCrntPMIntervalTypeIdx_Type())
olOSCCrntPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCCrntPMIntervalTypeIdx.setStatus(_B)
_OlOSCCrntPMOPRValue_Type=FixedX10
_OlOSCCrntPMOPRValue_Object=MibTableColumn
olOSCCrntPMOPRValue=_OlOSCCrntPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,6),_OlOSCCrntPMOPRValue_Type())
olOSCCrntPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCCrntPMOPRValue.setUnits(_P)
_OlOSCCrntPMOPRTimeStamp_Type=DateAndTime
_OlOSCCrntPMOPRTimeStamp_Object=MibTableColumn
olOSCCrntPMOPRTimeStamp=_OlOSCCrntPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,7),_OlOSCCrntPMOPRTimeStamp_Type())
olOSCCrntPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPRTimeStamp.setStatus(_B)
_OlOSCCrntPMOPRValidity_Type=PMValidity
_OlOSCCrntPMOPRValidity_Object=MibTableColumn
olOSCCrntPMOPRValidity=_OlOSCCrntPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,8),_OlOSCCrntPMOPRValidity_Type())
olOSCCrntPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPRValidity.setStatus(_B)
_OlOSCCrntPMOPTValue_Type=FixedX10
_OlOSCCrntPMOPTValue_Object=MibTableColumn
olOSCCrntPMOPTValue=_OlOSCCrntPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,9),_OlOSCCrntPMOPTValue_Type())
olOSCCrntPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCCrntPMOPTValue.setUnits(_P)
_OlOSCCrntPMOPTTimeStamp_Type=DateAndTime
_OlOSCCrntPMOPTTimeStamp_Object=MibTableColumn
olOSCCrntPMOPTTimeStamp=_OlOSCCrntPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,10),_OlOSCCrntPMOPTTimeStamp_Type())
olOSCCrntPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPTTimeStamp.setStatus(_B)
_OlOSCCrntPMOPTValidity_Type=PMValidity
_OlOSCCrntPMOPTValidity_Object=MibTableColumn
olOSCCrntPMOPTValidity=_OlOSCCrntPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,11),_OlOSCCrntPMOPTValidity_Type())
olOSCCrntPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOPTValidity.setStatus(_B)
_OlOSCCrntPMOBRValue_Type=FixedX10
_OlOSCCrntPMOBRValue_Object=MibTableColumn
olOSCCrntPMOBRValue=_OlOSCCrntPMOBRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,12),_OlOSCCrntPMOBRValue_Type())
olOSCCrntPMOBRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOBRValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCCrntPMOBRValue.setUnits(_h)
_OlOSCCrntPMOBRTimeStamp_Type=DateAndTime
_OlOSCCrntPMOBRTimeStamp_Object=MibTableColumn
olOSCCrntPMOBRTimeStamp=_OlOSCCrntPMOBRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,13),_OlOSCCrntPMOBRTimeStamp_Type())
olOSCCrntPMOBRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOBRTimeStamp.setStatus(_B)
_OlOSCCrntPMOBRValidity_Type=PMValidity
_OlOSCCrntPMOBRValidity_Object=MibTableColumn
olOSCCrntPMOBRValidity=_OlOSCCrntPMOBRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,14),_OlOSCCrntPMOBRValidity_Type())
olOSCCrntPMOBRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMOBRValidity.setStatus(_B)
_OlOSCCrntPMCVSValue_Type=Unsigned32
_OlOSCCrntPMCVSValue_Object=MibTableColumn
olOSCCrntPMCVSValue=_OlOSCCrntPMCVSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,15),_OlOSCCrntPMCVSValue_Type())
olOSCCrntPMCVSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMCVSValue.setStatus(_B)
_OlOSCCrntPMCVSTimeStamp_Type=DateAndTime
_OlOSCCrntPMCVSTimeStamp_Object=MibTableColumn
olOSCCrntPMCVSTimeStamp=_OlOSCCrntPMCVSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,16),_OlOSCCrntPMCVSTimeStamp_Type())
olOSCCrntPMCVSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMCVSTimeStamp.setStatus(_B)
_OlOSCCrntPMCVSValidity_Type=PMValidity
_OlOSCCrntPMCVSValidity_Object=MibTableColumn
olOSCCrntPMCVSValidity=_OlOSCCrntPMCVSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,17),_OlOSCCrntPMCVSValidity_Type())
olOSCCrntPMCVSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMCVSValidity.setStatus(_B)
_OlOSCCrntPMCVSInitialize_Type=InitializeCmd
_OlOSCCrntPMCVSInitialize_Object=MibTableColumn
olOSCCrntPMCVSInitialize=_OlOSCCrntPMCVSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,18),_OlOSCCrntPMCVSInitialize_Type())
olOSCCrntPMCVSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMCVSInitialize.setStatus(_B)
_OlOSCCrntPMESSValue_Type=Unsigned32
_OlOSCCrntPMESSValue_Object=MibTableColumn
olOSCCrntPMESSValue=_OlOSCCrntPMESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,19),_OlOSCCrntPMESSValue_Type())
olOSCCrntPMESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMESSValue.setStatus(_B)
_OlOSCCrntPMESSTimeStamp_Type=DateAndTime
_OlOSCCrntPMESSTimeStamp_Object=MibTableColumn
olOSCCrntPMESSTimeStamp=_OlOSCCrntPMESSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,20),_OlOSCCrntPMESSTimeStamp_Type())
olOSCCrntPMESSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMESSTimeStamp.setStatus(_B)
_OlOSCCrntPMESSValidity_Type=PMValidity
_OlOSCCrntPMESSValidity_Object=MibTableColumn
olOSCCrntPMESSValidity=_OlOSCCrntPMESSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,21),_OlOSCCrntPMESSValidity_Type())
olOSCCrntPMESSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMESSValidity.setStatus(_B)
_OlOSCCrntPMESSInitialize_Type=InitializeCmd
_OlOSCCrntPMESSInitialize_Object=MibTableColumn
olOSCCrntPMESSInitialize=_OlOSCCrntPMESSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,22),_OlOSCCrntPMESSInitialize_Type())
olOSCCrntPMESSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMESSInitialize.setStatus(_B)
_OlOSCCrntPMSESSValue_Type=Unsigned32
_OlOSCCrntPMSESSValue_Object=MibTableColumn
olOSCCrntPMSESSValue=_OlOSCCrntPMSESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,23),_OlOSCCrntPMSESSValue_Type())
olOSCCrntPMSESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMSESSValue.setStatus(_B)
_OlOSCCrntPMSESSTimeStamp_Type=DateAndTime
_OlOSCCrntPMSESSTimeStamp_Object=MibTableColumn
olOSCCrntPMSESSTimeStamp=_OlOSCCrntPMSESSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,24),_OlOSCCrntPMSESSTimeStamp_Type())
olOSCCrntPMSESSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMSESSTimeStamp.setStatus(_B)
_OlOSCCrntPMSESSValidity_Type=PMValidity
_OlOSCCrntPMSESSValidity_Object=MibTableColumn
olOSCCrntPMSESSValidity=_OlOSCCrntPMSESSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,25),_OlOSCCrntPMSESSValidity_Type())
olOSCCrntPMSESSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMSESSValidity.setStatus(_B)
_OlOSCCrntPMSESSInitialize_Type=InitializeCmd
_OlOSCCrntPMSESSInitialize_Object=MibTableColumn
olOSCCrntPMSESSInitialize=_OlOSCCrntPMSESSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,26),_OlOSCCrntPMSESSInitialize_Type())
olOSCCrntPMSESSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMSESSInitialize.setStatus(_B)
_OlOSCCrntPMSEFSSValue_Type=Unsigned32
_OlOSCCrntPMSEFSSValue_Object=MibTableColumn
olOSCCrntPMSEFSSValue=_OlOSCCrntPMSEFSSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,27),_OlOSCCrntPMSEFSSValue_Type())
olOSCCrntPMSEFSSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMSEFSSValue.setStatus(_B)
_OlOSCCrntPMSEFSSTimeStamp_Type=DateAndTime
_OlOSCCrntPMSEFSSTimeStamp_Object=MibTableColumn
olOSCCrntPMSEFSSTimeStamp=_OlOSCCrntPMSEFSSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,28),_OlOSCCrntPMSEFSSTimeStamp_Type())
olOSCCrntPMSEFSSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMSEFSSTimeStamp.setStatus(_B)
_OlOSCCrntPMSEFSSValidity_Type=PMValidity
_OlOSCCrntPMSEFSSValidity_Object=MibTableColumn
olOSCCrntPMSEFSSValidity=_OlOSCCrntPMSEFSSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,29),_OlOSCCrntPMSEFSSValidity_Type())
olOSCCrntPMSEFSSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMSEFSSValidity.setStatus(_B)
_OlOSCCrntPMSEFSSInitialize_Type=InitializeCmd
_OlOSCCrntPMSEFSSInitialize_Object=MibTableColumn
olOSCCrntPMSEFSSInitialize=_OlOSCCrntPMSEFSSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,30),_OlOSCCrntPMSEFSSInitialize_Type())
olOSCCrntPMSEFSSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMSEFSSInitialize.setStatus(_B)
_OlOSCCrntPMUASSValue_Type=Unsigned32
_OlOSCCrntPMUASSValue_Object=MibTableColumn
olOSCCrntPMUASSValue=_OlOSCCrntPMUASSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,31),_OlOSCCrntPMUASSValue_Type())
olOSCCrntPMUASSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMUASSValue.setStatus(_B)
_OlOSCCrntPMUASSTimeStamp_Type=DateAndTime
_OlOSCCrntPMUASSTimeStamp_Object=MibTableColumn
olOSCCrntPMUASSTimeStamp=_OlOSCCrntPMUASSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,32),_OlOSCCrntPMUASSTimeStamp_Type())
olOSCCrntPMUASSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMUASSTimeStamp.setStatus(_B)
_OlOSCCrntPMUASSValidity_Type=PMValidity
_OlOSCCrntPMUASSValidity_Object=MibTableColumn
olOSCCrntPMUASSValidity=_OlOSCCrntPMUASSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,33),_OlOSCCrntPMUASSValidity_Type())
olOSCCrntPMUASSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCCrntPMUASSValidity.setStatus(_B)
_OlOSCCrntPMUASSInitialize_Type=InitializeCmd
_OlOSCCrntPMUASSInitialize_Object=MibTableColumn
olOSCCrntPMUASSInitialize=_OlOSCCrntPMUASSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,1,1,34),_OlOSCCrntPMUASSInitialize_Type())
olOSCCrntPMUASSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCCrntPMUASSInitialize.setStatus(_B)
_OlOSCHistPMTable_Object=MibTable
olOSCHistPMTable=_OlOSCHistPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2))
if mibBuilder.loadTexts:olOSCHistPMTable.setStatus(_B)
_OlOSCHistPMEntry_Object=MibTableRow
olOSCHistPMEntry=_OlOSCHistPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1))
olOSCHistPMEntry.setIndexNames((0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa),(0,_C,_Ab),(0,_C,_Ac),(0,_C,_Ad))
if mibBuilder.loadTexts:olOSCHistPMEntry.setStatus(_B)
_OlOSCHistPMCpTypeIdx_Type=CpType
_OlOSCHistPMCpTypeIdx_Object=MibTableColumn
olOSCHistPMCpTypeIdx=_OlOSCHistPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,1),_OlOSCHistPMCpTypeIdx_Type())
olOSCHistPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMCpTypeIdx.setStatus(_B)
class _OlOSCHistPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlOSCHistPMShelfIdx_Type.__name__=_F
_OlOSCHistPMShelfIdx_Object=MibTableColumn
olOSCHistPMShelfIdx=_OlOSCHistPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,2),_OlOSCHistPMShelfIdx_Type())
olOSCHistPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMShelfIdx.setStatus(_B)
class _OlOSCHistPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlOSCHistPMSlotIdx_Type.__name__=_F
_OlOSCHistPMSlotIdx_Object=MibTableColumn
olOSCHistPMSlotIdx=_OlOSCHistPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,3),_OlOSCHistPMSlotIdx_Type())
olOSCHistPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMSlotIdx.setStatus(_B)
class _OlOSCHistPMLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OlOSCHistPMLineIdx_Type.__name__=_F
_OlOSCHistPMLineIdx_Object=MibTableColumn
olOSCHistPMLineIdx=_OlOSCHistPMLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,4),_OlOSCHistPMLineIdx_Type())
olOSCHistPMLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMLineIdx.setStatus(_B)
_OlOSCHistPMIntervalTypeIdx_Type=PMIntervalType
_OlOSCHistPMIntervalTypeIdx_Object=MibTableColumn
olOSCHistPMIntervalTypeIdx=_OlOSCHistPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,5),_OlOSCHistPMIntervalTypeIdx_Type())
olOSCHistPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMIntervalTypeIdx.setStatus(_B)
class _OlOSCHistPMIntervalIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_OlOSCHistPMIntervalIdx_Type.__name__=_F
_OlOSCHistPMIntervalIdx_Object=MibTableColumn
olOSCHistPMIntervalIdx=_OlOSCHistPMIntervalIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,6),_OlOSCHistPMIntervalIdx_Type())
olOSCHistPMIntervalIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCHistPMIntervalIdx.setStatus(_B)
_OlOSCHistPMOPRValue_Type=FixedX10
_OlOSCHistPMOPRValue_Object=MibTableColumn
olOSCHistPMOPRValue=_OlOSCHistPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,7),_OlOSCHistPMOPRValue_Type())
olOSCHistPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCHistPMOPRValue.setUnits(_P)
_OlOSCHistPMOPRTimeStamp_Type=DateAndTime
_OlOSCHistPMOPRTimeStamp_Object=MibTableColumn
olOSCHistPMOPRTimeStamp=_OlOSCHistPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,8),_OlOSCHistPMOPRTimeStamp_Type())
olOSCHistPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPRTimeStamp.setStatus(_B)
_OlOSCHistPMOPRValidity_Type=PMValidity
_OlOSCHistPMOPRValidity_Object=MibTableColumn
olOSCHistPMOPRValidity=_OlOSCHistPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,9),_OlOSCHistPMOPRValidity_Type())
olOSCHistPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPRValidity.setStatus(_B)
_OlOSCHistPMOPTValue_Type=FixedX10
_OlOSCHistPMOPTValue_Object=MibTableColumn
olOSCHistPMOPTValue=_OlOSCHistPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,10),_OlOSCHistPMOPTValue_Type())
olOSCHistPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCHistPMOPTValue.setUnits(_P)
_OlOSCHistPMOPTTimeStamp_Type=DateAndTime
_OlOSCHistPMOPTTimeStamp_Object=MibTableColumn
olOSCHistPMOPTTimeStamp=_OlOSCHistPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,11),_OlOSCHistPMOPTTimeStamp_Type())
olOSCHistPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPTTimeStamp.setStatus(_B)
_OlOSCHistPMOPTValidity_Type=PMValidity
_OlOSCHistPMOPTValidity_Object=MibTableColumn
olOSCHistPMOPTValidity=_OlOSCHistPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,12),_OlOSCHistPMOPTValidity_Type())
olOSCHistPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOPTValidity.setStatus(_B)
_OlOSCHistPMOBRValue_Type=FixedX10
_OlOSCHistPMOBRValue_Object=MibTableColumn
olOSCHistPMOBRValue=_OlOSCHistPMOBRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,13),_OlOSCHistPMOBRValue_Type())
olOSCHistPMOBRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOBRValue.setStatus(_B)
if mibBuilder.loadTexts:olOSCHistPMOBRValue.setUnits(_P)
_OlOSCHistPMOBRTimeStamp_Type=DateAndTime
_OlOSCHistPMOBRTimeStamp_Object=MibTableColumn
olOSCHistPMOBRTimeStamp=_OlOSCHistPMOBRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,14),_OlOSCHistPMOBRTimeStamp_Type())
olOSCHistPMOBRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOBRTimeStamp.setStatus(_B)
_OlOSCHistPMOBRValidity_Type=PMValidity
_OlOSCHistPMOBRValidity_Object=MibTableColumn
olOSCHistPMOBRValidity=_OlOSCHistPMOBRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,15),_OlOSCHistPMOBRValidity_Type())
olOSCHistPMOBRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMOBRValidity.setStatus(_B)
_OlOSCHistPMCVSValue_Type=Unsigned32
_OlOSCHistPMCVSValue_Object=MibTableColumn
olOSCHistPMCVSValue=_OlOSCHistPMCVSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,16),_OlOSCHistPMCVSValue_Type())
olOSCHistPMCVSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMCVSValue.setStatus(_B)
_OlOSCHistPMCVSTimeStamp_Type=DateAndTime
_OlOSCHistPMCVSTimeStamp_Object=MibTableColumn
olOSCHistPMCVSTimeStamp=_OlOSCHistPMCVSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,17),_OlOSCHistPMCVSTimeStamp_Type())
olOSCHistPMCVSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMCVSTimeStamp.setStatus(_B)
_OlOSCHistPMCVSValidity_Type=PMValidity
_OlOSCHistPMCVSValidity_Object=MibTableColumn
olOSCHistPMCVSValidity=_OlOSCHistPMCVSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,18),_OlOSCHistPMCVSValidity_Type())
olOSCHistPMCVSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMCVSValidity.setStatus(_B)
_OlOSCHistPMCVSInitialize_Type=InitializeCmd
_OlOSCHistPMCVSInitialize_Object=MibTableColumn
olOSCHistPMCVSInitialize=_OlOSCHistPMCVSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,19),_OlOSCHistPMCVSInitialize_Type())
olOSCHistPMCVSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMCVSInitialize.setStatus(_B)
_OlOSCHistPMESSValue_Type=Unsigned32
_OlOSCHistPMESSValue_Object=MibTableColumn
olOSCHistPMESSValue=_OlOSCHistPMESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,20),_OlOSCHistPMESSValue_Type())
olOSCHistPMESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMESSValue.setStatus(_B)
_OlOSCHistPMESSTimeStamp_Type=DateAndTime
_OlOSCHistPMESSTimeStamp_Object=MibTableColumn
olOSCHistPMESSTimeStamp=_OlOSCHistPMESSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,21),_OlOSCHistPMESSTimeStamp_Type())
olOSCHistPMESSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMESSTimeStamp.setStatus(_B)
_OlOSCHistPMESSValidity_Type=PMValidity
_OlOSCHistPMESSValidity_Object=MibTableColumn
olOSCHistPMESSValidity=_OlOSCHistPMESSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,22),_OlOSCHistPMESSValidity_Type())
olOSCHistPMESSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMESSValidity.setStatus(_B)
_OlOSCHistPMESSInitialize_Type=InitializeCmd
_OlOSCHistPMESSInitialize_Object=MibTableColumn
olOSCHistPMESSInitialize=_OlOSCHistPMESSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,23),_OlOSCHistPMESSInitialize_Type())
olOSCHistPMESSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMESSInitialize.setStatus(_B)
_OlOSCHistPMSESSValue_Type=Unsigned32
_OlOSCHistPMSESSValue_Object=MibTableColumn
olOSCHistPMSESSValue=_OlOSCHistPMSESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,24),_OlOSCHistPMSESSValue_Type())
olOSCHistPMSESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMSESSValue.setStatus(_B)
_OlOSCHistPMSESSTimeStamp_Type=DateAndTime
_OlOSCHistPMSESSTimeStamp_Object=MibTableColumn
olOSCHistPMSESSTimeStamp=_OlOSCHistPMSESSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,25),_OlOSCHistPMSESSTimeStamp_Type())
olOSCHistPMSESSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMSESSTimeStamp.setStatus(_B)
_OlOSCHistPMSESSValidity_Type=PMValidity
_OlOSCHistPMSESSValidity_Object=MibTableColumn
olOSCHistPMSESSValidity=_OlOSCHistPMSESSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,26),_OlOSCHistPMSESSValidity_Type())
olOSCHistPMSESSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMSESSValidity.setStatus(_B)
_OlOSCHistPMSESSInitialize_Type=InitializeCmd
_OlOSCHistPMSESSInitialize_Object=MibTableColumn
olOSCHistPMSESSInitialize=_OlOSCHistPMSESSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,27),_OlOSCHistPMSESSInitialize_Type())
olOSCHistPMSESSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMSESSInitialize.setStatus(_B)
_OlOSCHistPMSEFSSValue_Type=Unsigned32
_OlOSCHistPMSEFSSValue_Object=MibTableColumn
olOSCHistPMSEFSSValue=_OlOSCHistPMSEFSSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,28),_OlOSCHistPMSEFSSValue_Type())
olOSCHistPMSEFSSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMSEFSSValue.setStatus(_B)
_OlOSCHistPMSEFSSTimeStamp_Type=DateAndTime
_OlOSCHistPMSEFSSTimeStamp_Object=MibTableColumn
olOSCHistPMSEFSSTimeStamp=_OlOSCHistPMSEFSSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,29),_OlOSCHistPMSEFSSTimeStamp_Type())
olOSCHistPMSEFSSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMSEFSSTimeStamp.setStatus(_B)
_OlOSCHistPMSEFSSValidity_Type=PMValidity
_OlOSCHistPMSEFSSValidity_Object=MibTableColumn
olOSCHistPMSEFSSValidity=_OlOSCHistPMSEFSSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,30),_OlOSCHistPMSEFSSValidity_Type())
olOSCHistPMSEFSSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMSEFSSValidity.setStatus(_B)
_OlOSCHistPMSEFSSInitialize_Type=InitializeCmd
_OlOSCHistPMSEFSSInitialize_Object=MibTableColumn
olOSCHistPMSEFSSInitialize=_OlOSCHistPMSEFSSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,31),_OlOSCHistPMSEFSSInitialize_Type())
olOSCHistPMSEFSSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMSEFSSInitialize.setStatus(_B)
_OlOSCHistPMUASSValue_Type=Unsigned32
_OlOSCHistPMUASSValue_Object=MibTableColumn
olOSCHistPMUASSValue=_OlOSCHistPMUASSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,32),_OlOSCHistPMUASSValue_Type())
olOSCHistPMUASSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMUASSValue.setStatus(_B)
_OlOSCHistPMUASSTimeStamp_Type=DateAndTime
_OlOSCHistPMUASSTimeStamp_Object=MibTableColumn
olOSCHistPMUASSTimeStamp=_OlOSCHistPMUASSTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,33),_OlOSCHistPMUASSTimeStamp_Type())
olOSCHistPMUASSTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMUASSTimeStamp.setStatus(_B)
_OlOSCHistPMUASSValidity_Type=PMValidity
_OlOSCHistPMUASSValidity_Object=MibTableColumn
olOSCHistPMUASSValidity=_OlOSCHistPMUASSValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,34),_OlOSCHistPMUASSValidity_Type())
olOSCHistPMUASSValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olOSCHistPMUASSValidity.setStatus(_B)
_OlOSCHistPMUASSInitialize_Type=InitializeCmd
_OlOSCHistPMUASSInitialize_Object=MibTableColumn
olOSCHistPMUASSInitialize=_OlOSCHistPMUASSInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,2,1,35),_OlOSCHistPMUASSInitialize_Type())
olOSCHistPMUASSInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCHistPMUASSInitialize.setStatus(_B)
_OlOSCPMThresholdTable_Object=MibTable
olOSCPMThresholdTable=_OlOSCPMThresholdTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3))
if mibBuilder.loadTexts:olOSCPMThresholdTable.setStatus(_B)
_OlOSCPMThresholdEntry_Object=MibTableRow
olOSCPMThresholdEntry=_OlOSCPMThresholdEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1))
olOSCPMThresholdEntry.setIndexNames((0,_C,_Ae),(0,_C,_Af),(0,_C,_Ag),(0,_C,_Ah),(0,_C,_Ai))
if mibBuilder.loadTexts:olOSCPMThresholdEntry.setStatus(_B)
_OlOSCPMThresholdCpTypeIdx_Type=CpType
_OlOSCPMThresholdCpTypeIdx_Object=MibTableColumn
olOSCPMThresholdCpTypeIdx=_OlOSCPMThresholdCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,1),_OlOSCPMThresholdCpTypeIdx_Type())
olOSCPMThresholdCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCPMThresholdCpTypeIdx.setStatus(_B)
class _OlOSCPMThresholdShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlOSCPMThresholdShelfIdx_Type.__name__=_F
_OlOSCPMThresholdShelfIdx_Object=MibTableColumn
olOSCPMThresholdShelfIdx=_OlOSCPMThresholdShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,2),_OlOSCPMThresholdShelfIdx_Type())
olOSCPMThresholdShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCPMThresholdShelfIdx.setStatus(_B)
class _OlOSCPMThresholdSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlOSCPMThresholdSlotIdx_Type.__name__=_F
_OlOSCPMThresholdSlotIdx_Object=MibTableColumn
olOSCPMThresholdSlotIdx=_OlOSCPMThresholdSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,3),_OlOSCPMThresholdSlotIdx_Type())
olOSCPMThresholdSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCPMThresholdSlotIdx.setStatus(_B)
class _OlOSCPMThresholdLineIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OlOSCPMThresholdLineIdx_Type.__name__=_F
_OlOSCPMThresholdLineIdx_Object=MibTableColumn
olOSCPMThresholdLineIdx=_OlOSCPMThresholdLineIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,4),_OlOSCPMThresholdLineIdx_Type())
olOSCPMThresholdLineIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCPMThresholdLineIdx.setStatus(_B)
_OlOSCPMThresholdIntervalTypeIdx_Type=PMIntervalType
_OlOSCPMThresholdIntervalTypeIdx_Object=MibTableColumn
olOSCPMThresholdIntervalTypeIdx=_OlOSCPMThresholdIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,5),_OlOSCPMThresholdIntervalTypeIdx_Type())
olOSCPMThresholdIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olOSCPMThresholdIntervalTypeIdx.setStatus(_B)
_OlOSCPMThresholdCVSValue_Type=Unsigned32
_OlOSCPMThresholdCVSValue_Object=MibTableColumn
olOSCPMThresholdCVSValue=_OlOSCPMThresholdCVSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,6),_OlOSCPMThresholdCVSValue_Type())
olOSCPMThresholdCVSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCPMThresholdCVSValue.setStatus(_B)
_OlOSCPMThresholdESSValue_Type=Unsigned32
_OlOSCPMThresholdESSValue_Object=MibTableColumn
olOSCPMThresholdESSValue=_OlOSCPMThresholdESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,7),_OlOSCPMThresholdESSValue_Type())
olOSCPMThresholdESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCPMThresholdESSValue.setStatus(_B)
_OlOSCPMThresholdSESSValue_Type=Unsigned32
_OlOSCPMThresholdSESSValue_Object=MibTableColumn
olOSCPMThresholdSESSValue=_OlOSCPMThresholdSESSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,8),_OlOSCPMThresholdSESSValue_Type())
olOSCPMThresholdSESSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCPMThresholdSESSValue.setStatus(_B)
_OlOSCPMThresholdSEFSSValue_Type=Unsigned32
_OlOSCPMThresholdSEFSSValue_Object=MibTableColumn
olOSCPMThresholdSEFSSValue=_OlOSCPMThresholdSEFSSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,9),_OlOSCPMThresholdSEFSSValue_Type())
olOSCPMThresholdSEFSSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCPMThresholdSEFSSValue.setStatus(_B)
_OlOSCPMThresholdUASSValue_Type=Unsigned32
_OlOSCPMThresholdUASSValue_Object=MibTableColumn
olOSCPMThresholdUASSValue=_OlOSCPMThresholdUASSValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,3,1,10),_OlOSCPMThresholdUASSValue_Type())
olOSCPMThresholdUASSValue.setMaxAccess(_G)
if mibBuilder.loadTexts:olOSCPMThresholdUASSValue.setStatus(_B)
_OlPortCrntPMTable_Object=MibTable
olPortCrntPMTable=_OlPortCrntPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4))
if mibBuilder.loadTexts:olPortCrntPMTable.setStatus(_B)
_OlPortCrntPMEntry_Object=MibTableRow
olPortCrntPMEntry=_OlPortCrntPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1))
olPortCrntPMEntry.setIndexNames((0,_C,_Aj),(0,_C,_Ak),(0,_C,_Al),(0,_C,_Am),(0,_C,_An),(0,_C,_Ao))
if mibBuilder.loadTexts:olPortCrntPMEntry.setStatus(_B)
_OlPortCrntPMCpTypeIdx_Type=CpType
_OlPortCrntPMCpTypeIdx_Object=MibTableColumn
olPortCrntPMCpTypeIdx=_OlPortCrntPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,1),_OlPortCrntPMCpTypeIdx_Type())
olPortCrntPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMCpTypeIdx.setStatus(_B)
class _OlPortCrntPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlPortCrntPMShelfIdx_Type.__name__=_F
_OlPortCrntPMShelfIdx_Object=MibTableColumn
olPortCrntPMShelfIdx=_OlPortCrntPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,2),_OlPortCrntPMShelfIdx_Type())
olPortCrntPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMShelfIdx.setStatus(_B)
class _OlPortCrntPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlPortCrntPMSlotIdx_Type.__name__=_F
_OlPortCrntPMSlotIdx_Object=MibTableColumn
olPortCrntPMSlotIdx=_OlPortCrntPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,3),_OlPortCrntPMSlotIdx_Type())
olPortCrntPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMSlotIdx.setStatus(_B)
_OlPortCrntPMTypeIdx_Type=OlPortType
_OlPortCrntPMTypeIdx_Object=MibTableColumn
olPortCrntPMTypeIdx=_OlPortCrntPMTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,4),_OlPortCrntPMTypeIdx_Type())
olPortCrntPMTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMTypeIdx.setStatus(_B)
class _OlPortCrntPMIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OlPortCrntPMIdx_Type.__name__=_F
_OlPortCrntPMIdx_Object=MibTableColumn
olPortCrntPMIdx=_OlPortCrntPMIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,5),_OlPortCrntPMIdx_Type())
olPortCrntPMIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMIdx.setStatus(_B)
_OlPortCrntPMIntervalTypeIdx_Type=PMIntervalType
_OlPortCrntPMIntervalTypeIdx_Object=MibTableColumn
olPortCrntPMIntervalTypeIdx=_OlPortCrntPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,6),_OlPortCrntPMIntervalTypeIdx_Type())
olPortCrntPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortCrntPMIntervalTypeIdx.setStatus(_B)
_OlPortCrntPMOPRValue_Type=FixedX10
_OlPortCrntPMOPRValue_Object=MibTableColumn
olPortCrntPMOPRValue=_OlPortCrntPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,7),_OlPortCrntPMOPRValue_Type())
olPortCrntPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPRValue.setUnits(_P)
_OlPortCrntPMOPRTimeStamp_Type=DateAndTime
_OlPortCrntPMOPRTimeStamp_Object=MibTableColumn
olPortCrntPMOPRTimeStamp=_OlPortCrntPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,8),_OlPortCrntPMOPRTimeStamp_Type())
olPortCrntPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRTimeStamp.setStatus(_B)
_OlPortCrntPMOPRValidity_Type=PMValidity
_OlPortCrntPMOPRValidity_Object=MibTableColumn
olPortCrntPMOPRValidity=_OlPortCrntPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,9),_OlPortCrntPMOPRValidity_Type())
olPortCrntPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRValidity.setStatus(_B)
_OlPortCrntPMOPRMinValue_Type=FixedX10
_OlPortCrntPMOPRMinValue_Object=MibTableColumn
olPortCrntPMOPRMinValue=_OlPortCrntPMOPRMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,10),_OlPortCrntPMOPRMinValue_Type())
olPortCrntPMOPRMinValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMinValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPRMinValue.setUnits(_P)
_OlPortCrntPMOPRMinTimeStamp_Type=DateAndTime
_OlPortCrntPMOPRMinTimeStamp_Object=MibTableColumn
olPortCrntPMOPRMinTimeStamp=_OlPortCrntPMOPRMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,11),_OlPortCrntPMOPRMinTimeStamp_Type())
olPortCrntPMOPRMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMinTimeStamp.setStatus(_B)
_OlPortCrntPMOPRMinValidity_Type=PMValidity
_OlPortCrntPMOPRMinValidity_Object=MibTableColumn
olPortCrntPMOPRMinValidity=_OlPortCrntPMOPRMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,12),_OlPortCrntPMOPRMinValidity_Type())
olPortCrntPMOPRMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMinValidity.setStatus(_B)
_OlPortCrntPMOPRMaxValue_Type=FixedX10
_OlPortCrntPMOPRMaxValue_Object=MibTableColumn
olPortCrntPMOPRMaxValue=_OlPortCrntPMOPRMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,13),_OlPortCrntPMOPRMaxValue_Type())
olPortCrntPMOPRMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMaxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPRMaxValue.setUnits(_P)
_OlPortCrntPMOPRMaxTimeStamp_Type=DateAndTime
_OlPortCrntPMOPRMaxTimeStamp_Object=MibTableColumn
olPortCrntPMOPRMaxTimeStamp=_OlPortCrntPMOPRMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,14),_OlPortCrntPMOPRMaxTimeStamp_Type())
olPortCrntPMOPRMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMaxTimeStamp.setStatus(_B)
_OlPortCrntPMOPRMaxValidity_Type=PMValidity
_OlPortCrntPMOPRMaxValidity_Object=MibTableColumn
olPortCrntPMOPRMaxValidity=_OlPortCrntPMOPRMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,15),_OlPortCrntPMOPRMaxValidity_Type())
olPortCrntPMOPRMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRMaxValidity.setStatus(_B)
_OlPortCrntPMOPRAvgValue_Type=FixedX10
_OlPortCrntPMOPRAvgValue_Object=MibTableColumn
olPortCrntPMOPRAvgValue=_OlPortCrntPMOPRAvgValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,16),_OlPortCrntPMOPRAvgValue_Type())
olPortCrntPMOPRAvgValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRAvgValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPRAvgValue.setUnits(_P)
_OlPortCrntPMOPRAvgTimeStamp_Type=DateAndTime
_OlPortCrntPMOPRAvgTimeStamp_Object=MibTableColumn
olPortCrntPMOPRAvgTimeStamp=_OlPortCrntPMOPRAvgTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,17),_OlPortCrntPMOPRAvgTimeStamp_Type())
olPortCrntPMOPRAvgTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRAvgTimeStamp.setStatus(_B)
_OlPortCrntPMOPRAvgValidity_Type=PMValidity
_OlPortCrntPMOPRAvgValidity_Object=MibTableColumn
olPortCrntPMOPRAvgValidity=_OlPortCrntPMOPRAvgValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,18),_OlPortCrntPMOPRAvgValidity_Type())
olPortCrntPMOPRAvgValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRAvgValidity.setStatus(_B)
_OlPortCrntPMOPRStdDevValue_Type=FixedX10
_OlPortCrntPMOPRStdDevValue_Object=MibTableColumn
olPortCrntPMOPRStdDevValue=_OlPortCrntPMOPRStdDevValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,19),_OlPortCrntPMOPRStdDevValue_Type())
olPortCrntPMOPRStdDevValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRStdDevValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPRStdDevValue.setUnits(_h)
_OlPortCrntPMOPRStdDevTimeStamp_Type=DateAndTime
_OlPortCrntPMOPRStdDevTimeStamp_Object=MibTableColumn
olPortCrntPMOPRStdDevTimeStamp=_OlPortCrntPMOPRStdDevTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,20),_OlPortCrntPMOPRStdDevTimeStamp_Type())
olPortCrntPMOPRStdDevTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRStdDevTimeStamp.setStatus(_B)
_OlPortCrntPMOPRStdDevValidity_Type=PMValidity
_OlPortCrntPMOPRStdDevValidity_Object=MibTableColumn
olPortCrntPMOPRStdDevValidity=_OlPortCrntPMOPRStdDevValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,21),_OlPortCrntPMOPRStdDevValidity_Type())
olPortCrntPMOPRStdDevValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPRStdDevValidity.setStatus(_B)
_OlPortCrntPMOPTValue_Type=FixedX10
_OlPortCrntPMOPTValue_Object=MibTableColumn
olPortCrntPMOPTValue=_OlPortCrntPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,22),_OlPortCrntPMOPTValue_Type())
olPortCrntPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPTValue.setUnits(_P)
_OlPortCrntPMOPTTimeStamp_Type=DateAndTime
_OlPortCrntPMOPTTimeStamp_Object=MibTableColumn
olPortCrntPMOPTTimeStamp=_OlPortCrntPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,23),_OlPortCrntPMOPTTimeStamp_Type())
olPortCrntPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTTimeStamp.setStatus(_B)
_OlPortCrntPMOPTValidity_Type=PMValidity
_OlPortCrntPMOPTValidity_Object=MibTableColumn
olPortCrntPMOPTValidity=_OlPortCrntPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,24),_OlPortCrntPMOPTValidity_Type())
olPortCrntPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTValidity.setStatus(_B)
_OlPortCrntPMOPTMinValue_Type=FixedX10
_OlPortCrntPMOPTMinValue_Object=MibTableColumn
olPortCrntPMOPTMinValue=_OlPortCrntPMOPTMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,25),_OlPortCrntPMOPTMinValue_Type())
olPortCrntPMOPTMinValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMinValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPTMinValue.setUnits(_P)
_OlPortCrntPMOPTMinTimeStamp_Type=DateAndTime
_OlPortCrntPMOPTMinTimeStamp_Object=MibTableColumn
olPortCrntPMOPTMinTimeStamp=_OlPortCrntPMOPTMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,26),_OlPortCrntPMOPTMinTimeStamp_Type())
olPortCrntPMOPTMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMinTimeStamp.setStatus(_B)
_OlPortCrntPMOPTMinValidity_Type=PMValidity
_OlPortCrntPMOPTMinValidity_Object=MibTableColumn
olPortCrntPMOPTMinValidity=_OlPortCrntPMOPTMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,27),_OlPortCrntPMOPTMinValidity_Type())
olPortCrntPMOPTMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMinValidity.setStatus(_B)
_OlPortCrntPMOPTMaxValue_Type=FixedX10
_OlPortCrntPMOPTMaxValue_Object=MibTableColumn
olPortCrntPMOPTMaxValue=_OlPortCrntPMOPTMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,28),_OlPortCrntPMOPTMaxValue_Type())
olPortCrntPMOPTMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMaxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPTMaxValue.setUnits(_P)
_OlPortCrntPMOPTMaxTimeStamp_Type=DateAndTime
_OlPortCrntPMOPTMaxTimeStamp_Object=MibTableColumn
olPortCrntPMOPTMaxTimeStamp=_OlPortCrntPMOPTMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,29),_OlPortCrntPMOPTMaxTimeStamp_Type())
olPortCrntPMOPTMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMaxTimeStamp.setStatus(_B)
_OlPortCrntPMOPTMaxValidity_Type=PMValidity
_OlPortCrntPMOPTMaxValidity_Object=MibTableColumn
olPortCrntPMOPTMaxValidity=_OlPortCrntPMOPTMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,30),_OlPortCrntPMOPTMaxValidity_Type())
olPortCrntPMOPTMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTMaxValidity.setStatus(_B)
_OlPortCrntPMOPTAvgValue_Type=FixedX10
_OlPortCrntPMOPTAvgValue_Object=MibTableColumn
olPortCrntPMOPTAvgValue=_OlPortCrntPMOPTAvgValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,31),_OlPortCrntPMOPTAvgValue_Type())
olPortCrntPMOPTAvgValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTAvgValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPTAvgValue.setUnits(_P)
_OlPortCrntPMOPTAvgTimeStamp_Type=DateAndTime
_OlPortCrntPMOPTAvgTimeStamp_Object=MibTableColumn
olPortCrntPMOPTAvgTimeStamp=_OlPortCrntPMOPTAvgTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,32),_OlPortCrntPMOPTAvgTimeStamp_Type())
olPortCrntPMOPTAvgTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTAvgTimeStamp.setStatus(_B)
_OlPortCrntPMOPTAvgValidity_Type=PMValidity
_OlPortCrntPMOPTAvgValidity_Object=MibTableColumn
olPortCrntPMOPTAvgValidity=_OlPortCrntPMOPTAvgValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,33),_OlPortCrntPMOPTAvgValidity_Type())
olPortCrntPMOPTAvgValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTAvgValidity.setStatus(_B)
_OlPortCrntPMOPTStdDevValue_Type=FixedX10
_OlPortCrntPMOPTStdDevValue_Object=MibTableColumn
olPortCrntPMOPTStdDevValue=_OlPortCrntPMOPTStdDevValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,34),_OlPortCrntPMOPTStdDevValue_Type())
olPortCrntPMOPTStdDevValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTStdDevValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMOPTStdDevValue.setUnits(_h)
_OlPortCrntPMOPTStdDevTimeStamp_Type=DateAndTime
_OlPortCrntPMOPTStdDevTimeStamp_Object=MibTableColumn
olPortCrntPMOPTStdDevTimeStamp=_OlPortCrntPMOPTStdDevTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,35),_OlPortCrntPMOPTStdDevTimeStamp_Type())
olPortCrntPMOPTStdDevTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTStdDevTimeStamp.setStatus(_B)
_OlPortCrntPMOPTStdDevValidity_Type=PMValidity
_OlPortCrntPMOPTStdDevValidity_Object=MibTableColumn
olPortCrntPMOPTStdDevValidity=_OlPortCrntPMOPTStdDevValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,36),_OlPortCrntPMOPTStdDevValidity_Type())
olPortCrntPMOPTStdDevValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMOPTStdDevValidity.setStatus(_B)
_OlPortCrntPMLossRxValue_Type=FixedX10
_OlPortCrntPMLossRxValue_Object=MibTableColumn
olPortCrntPMLossRxValue=_OlPortCrntPMLossRxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,37),_OlPortCrntPMLossRxValue_Type())
olPortCrntPMLossRxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossRxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMLossRxValue.setUnits(_h)
_OlPortCrntPMLossRxTimeStamp_Type=DateAndTime
_OlPortCrntPMLossRxTimeStamp_Object=MibTableColumn
olPortCrntPMLossRxTimeStamp=_OlPortCrntPMLossRxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,38),_OlPortCrntPMLossRxTimeStamp_Type())
olPortCrntPMLossRxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossRxTimeStamp.setStatus(_B)
_OlPortCrntPMLossRxValidity_Type=PMValidity
_OlPortCrntPMLossRxValidity_Object=MibTableColumn
olPortCrntPMLossRxValidity=_OlPortCrntPMLossRxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,39),_OlPortCrntPMLossRxValidity_Type())
olPortCrntPMLossRxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossRxValidity.setStatus(_B)
_OlPortCrntPMLossTxValue_Type=FixedX10
_OlPortCrntPMLossTxValue_Object=MibTableColumn
olPortCrntPMLossTxValue=_OlPortCrntPMLossTxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,40),_OlPortCrntPMLossTxValue_Type())
olPortCrntPMLossTxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossTxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortCrntPMLossTxValue.setUnits(_h)
_OlPortCrntPMLossTxTimeStamp_Type=DateAndTime
_OlPortCrntPMLossTxTimeStamp_Object=MibTableColumn
olPortCrntPMLossTxTimeStamp=_OlPortCrntPMLossTxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,41),_OlPortCrntPMLossTxTimeStamp_Type())
olPortCrntPMLossTxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossTxTimeStamp.setStatus(_B)
_OlPortCrntPMLossTxValidity_Type=PMValidity
_OlPortCrntPMLossTxValidity_Object=MibTableColumn
olPortCrntPMLossTxValidity=_OlPortCrntPMLossTxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,42),_OlPortCrntPMLossTxValidity_Type())
olPortCrntPMLossTxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortCrntPMLossTxValidity.setStatus(_B)
_OlPortCrntPMInitializeAll_Type=InitializeCmd
_OlPortCrntPMInitializeAll_Object=MibTableColumn
olPortCrntPMInitializeAll=_OlPortCrntPMInitializeAll_Object((1,3,6,1,4,1,18070,2,2,1,16,12,4,1,43),_OlPortCrntPMInitializeAll_Type())
olPortCrntPMInitializeAll.setMaxAccess(_G)
if mibBuilder.loadTexts:olPortCrntPMInitializeAll.setStatus(_B)
_OlPortHistPMTable_Object=MibTable
olPortHistPMTable=_OlPortHistPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5))
if mibBuilder.loadTexts:olPortHistPMTable.setStatus(_B)
_OlPortHistPMEntry_Object=MibTableRow
olPortHistPMEntry=_OlPortHistPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1))
olPortHistPMEntry.setIndexNames((0,_C,_Ap),(0,_C,_Aq),(0,_C,_Ar),(0,_C,_As),(0,_C,_At),(0,_C,_Au),(0,_C,_Av))
if mibBuilder.loadTexts:olPortHistPMEntry.setStatus(_B)
_OlPortHistPMCpTypeIdx_Type=CpType
_OlPortHistPMCpTypeIdx_Object=MibTableColumn
olPortHistPMCpTypeIdx=_OlPortHistPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,1),_OlPortHistPMCpTypeIdx_Type())
olPortHistPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMCpTypeIdx.setStatus(_B)
class _OlPortHistPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_OlPortHistPMShelfIdx_Type.__name__=_F
_OlPortHistPMShelfIdx_Object=MibTableColumn
olPortHistPMShelfIdx=_OlPortHistPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,2),_OlPortHistPMShelfIdx_Type())
olPortHistPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMShelfIdx.setStatus(_B)
class _OlPortHistPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OlPortHistPMSlotIdx_Type.__name__=_F
_OlPortHistPMSlotIdx_Object=MibTableColumn
olPortHistPMSlotIdx=_OlPortHistPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,3),_OlPortHistPMSlotIdx_Type())
olPortHistPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMSlotIdx.setStatus(_B)
_OlPortHistPMTypeIdx_Type=OlPortType
_OlPortHistPMTypeIdx_Object=MibTableColumn
olPortHistPMTypeIdx=_OlPortHistPMTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,4),_OlPortHistPMTypeIdx_Type())
olPortHistPMTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMTypeIdx.setStatus(_B)
class _OlPortHistPMIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OlPortHistPMIdx_Type.__name__=_F
_OlPortHistPMIdx_Object=MibTableColumn
olPortHistPMIdx=_OlPortHistPMIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,5),_OlPortHistPMIdx_Type())
olPortHistPMIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMIdx.setStatus(_B)
_OlPortHistPMIntervalTypeIdx_Type=PMIntervalType
_OlPortHistPMIntervalTypeIdx_Object=MibTableColumn
olPortHistPMIntervalTypeIdx=_OlPortHistPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,6),_OlPortHistPMIntervalTypeIdx_Type())
olPortHistPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMIntervalTypeIdx.setStatus(_B)
class _OlPortHistPMIntervalIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_OlPortHistPMIntervalIdx_Type.__name__=_F
_OlPortHistPMIntervalIdx_Object=MibTableColumn
olPortHistPMIntervalIdx=_OlPortHistPMIntervalIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,7),_OlPortHistPMIntervalIdx_Type())
olPortHistPMIntervalIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:olPortHistPMIntervalIdx.setStatus(_B)
_OlPortHistPMOPRValue_Type=FixedX10
_OlPortHistPMOPRValue_Object=MibTableColumn
olPortHistPMOPRValue=_OlPortHistPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,8),_OlPortHistPMOPRValue_Type())
olPortHistPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPRValue.setUnits(_P)
_OlPortHistPMOPRTimeStamp_Type=DateAndTime
_OlPortHistPMOPRTimeStamp_Object=MibTableColumn
olPortHistPMOPRTimeStamp=_OlPortHistPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,9),_OlPortHistPMOPRTimeStamp_Type())
olPortHistPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRTimeStamp.setStatus(_B)
_OlPortHistPMOPRValidity_Type=PMValidity
_OlPortHistPMOPRValidity_Object=MibTableColumn
olPortHistPMOPRValidity=_OlPortHistPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,10),_OlPortHistPMOPRValidity_Type())
olPortHistPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRValidity.setStatus(_B)
_OlPortHistPMOPRMinValue_Type=FixedX10
_OlPortHistPMOPRMinValue_Object=MibTableColumn
olPortHistPMOPRMinValue=_OlPortHistPMOPRMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,11),_OlPortHistPMOPRMinValue_Type())
olPortHistPMOPRMinValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMinValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPRMinValue.setUnits(_P)
_OlPortHistPMOPRMinTimeStamp_Type=DateAndTime
_OlPortHistPMOPRMinTimeStamp_Object=MibTableColumn
olPortHistPMOPRMinTimeStamp=_OlPortHistPMOPRMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,12),_OlPortHistPMOPRMinTimeStamp_Type())
olPortHistPMOPRMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMinTimeStamp.setStatus(_B)
_OlPortHistPMOPRMinValidity_Type=PMValidity
_OlPortHistPMOPRMinValidity_Object=MibTableColumn
olPortHistPMOPRMinValidity=_OlPortHistPMOPRMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,13),_OlPortHistPMOPRMinValidity_Type())
olPortHistPMOPRMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMinValidity.setStatus(_B)
_OlPortHistPMOPRMaxValue_Type=FixedX10
_OlPortHistPMOPRMaxValue_Object=MibTableColumn
olPortHistPMOPRMaxValue=_OlPortHistPMOPRMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,14),_OlPortHistPMOPRMaxValue_Type())
olPortHistPMOPRMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMaxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPRMaxValue.setUnits(_P)
_OlPortHistPMOPRMaxTimeStamp_Type=DateAndTime
_OlPortHistPMOPRMaxTimeStamp_Object=MibTableColumn
olPortHistPMOPRMaxTimeStamp=_OlPortHistPMOPRMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,15),_OlPortHistPMOPRMaxTimeStamp_Type())
olPortHistPMOPRMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMaxTimeStamp.setStatus(_B)
_OlPortHistPMOPRMaxValidity_Type=PMValidity
_OlPortHistPMOPRMaxValidity_Object=MibTableColumn
olPortHistPMOPRMaxValidity=_OlPortHistPMOPRMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,16),_OlPortHistPMOPRMaxValidity_Type())
olPortHistPMOPRMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRMaxValidity.setStatus(_B)
_OlPortHistPMOPRAvgValue_Type=FixedX10
_OlPortHistPMOPRAvgValue_Object=MibTableColumn
olPortHistPMOPRAvgValue=_OlPortHistPMOPRAvgValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,17),_OlPortHistPMOPRAvgValue_Type())
olPortHistPMOPRAvgValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRAvgValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPRAvgValue.setUnits(_P)
_OlPortHistPMOPRAvgTimeStamp_Type=DateAndTime
_OlPortHistPMOPRAvgTimeStamp_Object=MibTableColumn
olPortHistPMOPRAvgTimeStamp=_OlPortHistPMOPRAvgTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,18),_OlPortHistPMOPRAvgTimeStamp_Type())
olPortHistPMOPRAvgTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRAvgTimeStamp.setStatus(_B)
_OlPortHistPMOPRAvgValidity_Type=PMValidity
_OlPortHistPMOPRAvgValidity_Object=MibTableColumn
olPortHistPMOPRAvgValidity=_OlPortHistPMOPRAvgValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,19),_OlPortHistPMOPRAvgValidity_Type())
olPortHistPMOPRAvgValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRAvgValidity.setStatus(_B)
_OlPortHistPMOPRStdDevValue_Type=FixedX10
_OlPortHistPMOPRStdDevValue_Object=MibTableColumn
olPortHistPMOPRStdDevValue=_OlPortHistPMOPRStdDevValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,20),_OlPortHistPMOPRStdDevValue_Type())
olPortHistPMOPRStdDevValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRStdDevValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPRStdDevValue.setUnits(_h)
_OlPortHistPMOPRStdDevTimeStamp_Type=DateAndTime
_OlPortHistPMOPRStdDevTimeStamp_Object=MibTableColumn
olPortHistPMOPRStdDevTimeStamp=_OlPortHistPMOPRStdDevTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,21),_OlPortHistPMOPRStdDevTimeStamp_Type())
olPortHistPMOPRStdDevTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRStdDevTimeStamp.setStatus(_B)
_OlPortHistPMOPRStdDevValidity_Type=PMValidity
_OlPortHistPMOPRStdDevValidity_Object=MibTableColumn
olPortHistPMOPRStdDevValidity=_OlPortHistPMOPRStdDevValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,22),_OlPortHistPMOPRStdDevValidity_Type())
olPortHistPMOPRStdDevValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPRStdDevValidity.setStatus(_B)
_OlPortHistPMOPTValue_Type=FixedX10
_OlPortHistPMOPTValue_Object=MibTableColumn
olPortHistPMOPTValue=_OlPortHistPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,23),_OlPortHistPMOPTValue_Type())
olPortHistPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPTValue.setUnits(_P)
_OlPortHistPMOPTTimeStamp_Type=DateAndTime
_OlPortHistPMOPTTimeStamp_Object=MibTableColumn
olPortHistPMOPTTimeStamp=_OlPortHistPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,24),_OlPortHistPMOPTTimeStamp_Type())
olPortHistPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTTimeStamp.setStatus(_B)
_OlPortHistPMOPTValidity_Type=PMValidity
_OlPortHistPMOPTValidity_Object=MibTableColumn
olPortHistPMOPTValidity=_OlPortHistPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,25),_OlPortHistPMOPTValidity_Type())
olPortHistPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTValidity.setStatus(_B)
_OlPortHistPMOPTMinValue_Type=FixedX10
_OlPortHistPMOPTMinValue_Object=MibTableColumn
olPortHistPMOPTMinValue=_OlPortHistPMOPTMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,26),_OlPortHistPMOPTMinValue_Type())
olPortHistPMOPTMinValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMinValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPTMinValue.setUnits(_P)
_OlPortHistPMOPTMinTimeStamp_Type=DateAndTime
_OlPortHistPMOPTMinTimeStamp_Object=MibTableColumn
olPortHistPMOPTMinTimeStamp=_OlPortHistPMOPTMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,27),_OlPortHistPMOPTMinTimeStamp_Type())
olPortHistPMOPTMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMinTimeStamp.setStatus(_B)
_OlPortHistPMOPTMinValidity_Type=PMValidity
_OlPortHistPMOPTMinValidity_Object=MibTableColumn
olPortHistPMOPTMinValidity=_OlPortHistPMOPTMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,28),_OlPortHistPMOPTMinValidity_Type())
olPortHistPMOPTMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMinValidity.setStatus(_B)
_OlPortHistPMOPTMaxValue_Type=FixedX10
_OlPortHistPMOPTMaxValue_Object=MibTableColumn
olPortHistPMOPTMaxValue=_OlPortHistPMOPTMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,29),_OlPortHistPMOPTMaxValue_Type())
olPortHistPMOPTMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMaxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPTMaxValue.setUnits(_P)
_OlPortHistPMOPTMaxTimeStamp_Type=DateAndTime
_OlPortHistPMOPTMaxTimeStamp_Object=MibTableColumn
olPortHistPMOPTMaxTimeStamp=_OlPortHistPMOPTMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,30),_OlPortHistPMOPTMaxTimeStamp_Type())
olPortHistPMOPTMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMaxTimeStamp.setStatus(_B)
_OlPortHistPMOPTMaxValidity_Type=PMValidity
_OlPortHistPMOPTMaxValidity_Object=MibTableColumn
olPortHistPMOPTMaxValidity=_OlPortHistPMOPTMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,31),_OlPortHistPMOPTMaxValidity_Type())
olPortHistPMOPTMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTMaxValidity.setStatus(_B)
_OlPortHistPMOPTAvgValue_Type=FixedX10
_OlPortHistPMOPTAvgValue_Object=MibTableColumn
olPortHistPMOPTAvgValue=_OlPortHistPMOPTAvgValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,32),_OlPortHistPMOPTAvgValue_Type())
olPortHistPMOPTAvgValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTAvgValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPTAvgValue.setUnits(_P)
_OlPortHistPMOPTAvgTimeStamp_Type=DateAndTime
_OlPortHistPMOPTAvgTimeStamp_Object=MibTableColumn
olPortHistPMOPTAvgTimeStamp=_OlPortHistPMOPTAvgTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,33),_OlPortHistPMOPTAvgTimeStamp_Type())
olPortHistPMOPTAvgTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTAvgTimeStamp.setStatus(_B)
_OlPortHistPMOPTAvgValidity_Type=PMValidity
_OlPortHistPMOPTAvgValidity_Object=MibTableColumn
olPortHistPMOPTAvgValidity=_OlPortHistPMOPTAvgValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,34),_OlPortHistPMOPTAvgValidity_Type())
olPortHistPMOPTAvgValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTAvgValidity.setStatus(_B)
_OlPortHistPMOPTStdDevValue_Type=FixedX10
_OlPortHistPMOPTStdDevValue_Object=MibTableColumn
olPortHistPMOPTStdDevValue=_OlPortHistPMOPTStdDevValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,35),_OlPortHistPMOPTStdDevValue_Type())
olPortHistPMOPTStdDevValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTStdDevValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMOPTStdDevValue.setUnits(_h)
_OlPortHistPMOPTStdDevTimeStamp_Type=DateAndTime
_OlPortHistPMOPTStdDevTimeStamp_Object=MibTableColumn
olPortHistPMOPTStdDevTimeStamp=_OlPortHistPMOPTStdDevTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,36),_OlPortHistPMOPTStdDevTimeStamp_Type())
olPortHistPMOPTStdDevTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTStdDevTimeStamp.setStatus(_B)
_OlPortHistPMOPTStdDevValidity_Type=PMValidity
_OlPortHistPMOPTStdDevValidity_Object=MibTableColumn
olPortHistPMOPTStdDevValidity=_OlPortHistPMOPTStdDevValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,37),_OlPortHistPMOPTStdDevValidity_Type())
olPortHistPMOPTStdDevValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMOPTStdDevValidity.setStatus(_B)
_OlPortHistPMLossRxValue_Type=FixedX10
_OlPortHistPMLossRxValue_Object=MibTableColumn
olPortHistPMLossRxValue=_OlPortHistPMLossRxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,38),_OlPortHistPMLossRxValue_Type())
olPortHistPMLossRxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossRxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMLossRxValue.setUnits(_h)
_OlPortHistPMLossRxTimeStamp_Type=DateAndTime
_OlPortHistPMLossRxTimeStamp_Object=MibTableColumn
olPortHistPMLossRxTimeStamp=_OlPortHistPMLossRxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,39),_OlPortHistPMLossRxTimeStamp_Type())
olPortHistPMLossRxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossRxTimeStamp.setStatus(_B)
_OlPortHistPMLossRxValidity_Type=PMValidity
_OlPortHistPMLossRxValidity_Object=MibTableColumn
olPortHistPMLossRxValidity=_OlPortHistPMLossRxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,40),_OlPortHistPMLossRxValidity_Type())
olPortHistPMLossRxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossRxValidity.setStatus(_B)
_OlPortHistPMLossTxValue_Type=FixedX10
_OlPortHistPMLossTxValue_Object=MibTableColumn
olPortHistPMLossTxValue=_OlPortHistPMLossTxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,41),_OlPortHistPMLossTxValue_Type())
olPortHistPMLossTxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossTxValue.setStatus(_B)
if mibBuilder.loadTexts:olPortHistPMLossTxValue.setUnits(_h)
_OlPortHistPMLossTxTimeStamp_Type=DateAndTime
_OlPortHistPMLossTxTimeStamp_Object=MibTableColumn
olPortHistPMLossTxTimeStamp=_OlPortHistPMLossTxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,42),_OlPortHistPMLossTxTimeStamp_Type())
olPortHistPMLossTxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossTxTimeStamp.setStatus(_B)
_OlPortHistPMLossTxValidity_Type=PMValidity
_OlPortHistPMLossTxValidity_Object=MibTableColumn
olPortHistPMLossTxValidity=_OlPortHistPMLossTxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,43),_OlPortHistPMLossTxValidity_Type())
olPortHistPMLossTxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:olPortHistPMLossTxValidity.setStatus(_B)
_OlPortHistPMInitializeAll_Type=InitializeCmd
_OlPortHistPMInitializeAll_Object=MibTableColumn
olPortHistPMInitializeAll=_OlPortHistPMInitializeAll_Object((1,3,6,1,4,1,18070,2,2,1,16,12,5,1,44),_OlPortHistPMInitializeAll_Type())
olPortHistPMInitializeAll.setMaxAccess(_G)
if mibBuilder.loadTexts:olPortHistPMInitializeAll.setStatus(_B)
_WchCrntPMTable_Object=MibTable
wchCrntPMTable=_WchCrntPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6))
if mibBuilder.loadTexts:wchCrntPMTable.setStatus(_B)
_WchCrntPMEntry_Object=MibTableRow
wchCrntPMEntry=_WchCrntPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1))
wchCrntPMEntry.setIndexNames((0,_C,_Aw),(0,_C,_Ax),(0,_C,_Ay),(0,_C,_Az),(0,_C,_A_),(0,_C,_B0),(0,_C,_B1))
if mibBuilder.loadTexts:wchCrntPMEntry.setStatus(_B)
_WchCrntPMCpTypeIdx_Type=CpType
_WchCrntPMCpTypeIdx_Object=MibTableColumn
wchCrntPMCpTypeIdx=_WchCrntPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,1),_WchCrntPMCpTypeIdx_Type())
wchCrntPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMCpTypeIdx.setStatus(_B)
class _WchCrntPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WchCrntPMShelfIdx_Type.__name__=_F
_WchCrntPMShelfIdx_Object=MibTableColumn
wchCrntPMShelfIdx=_WchCrntPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,2),_WchCrntPMShelfIdx_Type())
wchCrntPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMShelfIdx.setStatus(_B)
class _WchCrntPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WchCrntPMSlotIdx_Type.__name__=_F
_WchCrntPMSlotIdx_Object=MibTableColumn
wchCrntPMSlotIdx=_WchCrntPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,3),_WchCrntPMSlotIdx_Type())
wchCrntPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMSlotIdx.setStatus(_B)
_WchCrntPMPortTypeIdx_Type=OlPortType
_WchCrntPMPortTypeIdx_Object=MibTableColumn
wchCrntPMPortTypeIdx=_WchCrntPMPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,4),_WchCrntPMPortTypeIdx_Type())
wchCrntPMPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMPortTypeIdx.setStatus(_B)
class _WchCrntPMPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WchCrntPMPortIdx_Type.__name__=_F
_WchCrntPMPortIdx_Object=MibTableColumn
wchCrntPMPortIdx=_WchCrntPMPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,5),_WchCrntPMPortIdx_Type())
wchCrntPMPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMPortIdx.setStatus(_B)
class _WchCrntPMIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(135,610))
_WchCrntPMIdx_Type.__name__=_F
_WchCrntPMIdx_Object=MibTableColumn
wchCrntPMIdx=_WchCrntPMIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,6),_WchCrntPMIdx_Type())
wchCrntPMIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMIdx.setStatus(_B)
_WchCrntPMIntervalTypeIdx_Type=PMIntervalType
_WchCrntPMIntervalTypeIdx_Object=MibTableColumn
wchCrntPMIntervalTypeIdx=_WchCrntPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,7),_WchCrntPMIntervalTypeIdx_Type())
wchCrntPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchCrntPMIntervalTypeIdx.setStatus(_B)
_WchCrntPMOPRValue_Type=FixedX10
_WchCrntPMOPRValue_Object=MibTableColumn
wchCrntPMOPRValue=_WchCrntPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,8),_WchCrntPMOPRValue_Type())
wchCrntPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPRValue.setUnits(_P)
_WchCrntPMOPRTimeStamp_Type=DateAndTime
_WchCrntPMOPRTimeStamp_Object=MibTableColumn
wchCrntPMOPRTimeStamp=_WchCrntPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,9),_WchCrntPMOPRTimeStamp_Type())
wchCrntPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRTimeStamp.setStatus(_B)
_WchCrntPMOPRValidity_Type=PMValidity
_WchCrntPMOPRValidity_Object=MibTableColumn
wchCrntPMOPRValidity=_WchCrntPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,10),_WchCrntPMOPRValidity_Type())
wchCrntPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRValidity.setStatus(_B)
_WchCrntPMOPRMinValue_Type=FixedX10
_WchCrntPMOPRMinValue_Object=MibTableColumn
wchCrntPMOPRMinValue=_WchCrntPMOPRMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,11),_WchCrntPMOPRMinValue_Type())
wchCrntPMOPRMinValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPRMinValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPRMinValue.setUnits(_P)
_WchCrntPMOPRMinTimeStamp_Type=DateAndTime
_WchCrntPMOPRMinTimeStamp_Object=MibTableColumn
wchCrntPMOPRMinTimeStamp=_WchCrntPMOPRMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,12),_WchCrntPMOPRMinTimeStamp_Type())
wchCrntPMOPRMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRMinTimeStamp.setStatus(_B)
_WchCrntPMOPRMinValidity_Type=PMValidity
_WchCrntPMOPRMinValidity_Object=MibTableColumn
wchCrntPMOPRMinValidity=_WchCrntPMOPRMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,13),_WchCrntPMOPRMinValidity_Type())
wchCrntPMOPRMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRMinValidity.setStatus(_B)
_WchCrntPMOPRMinInitialize_Type=InitializeCmd
_WchCrntPMOPRMinInitialize_Object=MibTableColumn
wchCrntPMOPRMinInitialize=_WchCrntPMOPRMinInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,14),_WchCrntPMOPRMinInitialize_Type())
wchCrntPMOPRMinInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPRMinInitialize.setStatus(_B)
_WchCrntPMOPRMaxValue_Type=FixedX10
_WchCrntPMOPRMaxValue_Object=MibTableColumn
wchCrntPMOPRMaxValue=_WchCrntPMOPRMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,15),_WchCrntPMOPRMaxValue_Type())
wchCrntPMOPRMaxValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPRMaxValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPRMaxValue.setUnits(_P)
_WchCrntPMOPRMaxTimeStamp_Type=DateAndTime
_WchCrntPMOPRMaxTimeStamp_Object=MibTableColumn
wchCrntPMOPRMaxTimeStamp=_WchCrntPMOPRMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,16),_WchCrntPMOPRMaxTimeStamp_Type())
wchCrntPMOPRMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPRMaxTimeStamp.setStatus(_B)
_WchCrntPMOPRMaxValidity_Type=PMValidity
_WchCrntPMOPRMaxValidity_Object=MibTableColumn
wchCrntPMOPRMaxValidity=_WchCrntPMOPRMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,17),_WchCrntPMOPRMaxValidity_Type())
wchCrntPMOPRMaxValidity.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPRMaxValidity.setStatus(_B)
_WchCrntPMOPRMaxInitialize_Type=InitializeCmd
_WchCrntPMOPRMaxInitialize_Object=MibTableColumn
wchCrntPMOPRMaxInitialize=_WchCrntPMOPRMaxInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,18),_WchCrntPMOPRMaxInitialize_Type())
wchCrntPMOPRMaxInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPRMaxInitialize.setStatus(_B)
_WchCrntPMOPTValue_Type=FixedX10
_WchCrntPMOPTValue_Object=MibTableColumn
wchCrntPMOPTValue=_WchCrntPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,19),_WchCrntPMOPTValue_Type())
wchCrntPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPTValue.setUnits(_P)
_WchCrntPMOPTTimeStamp_Type=DateAndTime
_WchCrntPMOPTTimeStamp_Object=MibTableColumn
wchCrntPMOPTTimeStamp=_WchCrntPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,20),_WchCrntPMOPTTimeStamp_Type())
wchCrntPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTTimeStamp.setStatus(_B)
_WchCrntPMOPTValidity_Type=PMValidity
_WchCrntPMOPTValidity_Object=MibTableColumn
wchCrntPMOPTValidity=_WchCrntPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,21),_WchCrntPMOPTValidity_Type())
wchCrntPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTValidity.setStatus(_B)
_WchCrntPMOPTMinValue_Type=FixedX10
_WchCrntPMOPTMinValue_Object=MibTableColumn
wchCrntPMOPTMinValue=_WchCrntPMOPTMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,22),_WchCrntPMOPTMinValue_Type())
wchCrntPMOPTMinValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPTMinValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPTMinValue.setUnits(_P)
_WchCrntPMOPTMinTimeStamp_Type=DateAndTime
_WchCrntPMOPTMinTimeStamp_Object=MibTableColumn
wchCrntPMOPTMinTimeStamp=_WchCrntPMOPTMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,23),_WchCrntPMOPTMinTimeStamp_Type())
wchCrntPMOPTMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTMinTimeStamp.setStatus(_B)
_WchCrntPMOPTMinValidity_Type=PMValidity
_WchCrntPMOPTMinValidity_Object=MibTableColumn
wchCrntPMOPTMinValidity=_WchCrntPMOPTMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,24),_WchCrntPMOPTMinValidity_Type())
wchCrntPMOPTMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTMinValidity.setStatus(_B)
_WchCrntPMOPTMinInitialize_Type=InitializeCmd
_WchCrntPMOPTMinInitialize_Object=MibTableColumn
wchCrntPMOPTMinInitialize=_WchCrntPMOPTMinInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,25),_WchCrntPMOPTMinInitialize_Type())
wchCrntPMOPTMinInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPTMinInitialize.setStatus(_B)
_WchCrntPMOPTMaxValue_Type=FixedX10
_WchCrntPMOPTMaxValue_Object=MibTableColumn
wchCrntPMOPTMaxValue=_WchCrntPMOPTMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,26),_WchCrntPMOPTMaxValue_Type())
wchCrntPMOPTMaxValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPTMaxValue.setStatus(_B)
if mibBuilder.loadTexts:wchCrntPMOPTMaxValue.setUnits(_P)
_WchCrntPMOPTMaxTimeStamp_Type=DateAndTime
_WchCrntPMOPTMaxTimeStamp_Object=MibTableColumn
wchCrntPMOPTMaxTimeStamp=_WchCrntPMOPTMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,27),_WchCrntPMOPTMaxTimeStamp_Type())
wchCrntPMOPTMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTMaxTimeStamp.setStatus(_B)
_WchCrntPMOPTMaxValidity_Type=PMValidity
_WchCrntPMOPTMaxValidity_Object=MibTableColumn
wchCrntPMOPTMaxValidity=_WchCrntPMOPTMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,28),_WchCrntPMOPTMaxValidity_Type())
wchCrntPMOPTMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchCrntPMOPTMaxValidity.setStatus(_B)
_WchCrntPMOPTMaxInitialize_Type=InitializeCmd
_WchCrntPMOPTMaxInitialize_Object=MibTableColumn
wchCrntPMOPTMaxInitialize=_WchCrntPMOPTMaxInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,6,1,29),_WchCrntPMOPTMaxInitialize_Type())
wchCrntPMOPTMaxInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchCrntPMOPTMaxInitialize.setStatus(_B)
_WchHistPMTable_Object=MibTable
wchHistPMTable=_WchHistPMTable_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7))
if mibBuilder.loadTexts:wchHistPMTable.setStatus(_B)
_WchHistPMEntry_Object=MibTableRow
wchHistPMEntry=_WchHistPMEntry_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1))
wchHistPMEntry.setIndexNames((0,_C,_B2),(0,_C,_B3),(0,_C,_B4),(0,_C,_B5),(0,_C,_B6),(0,_C,_B7),(0,_C,_B8),(0,_C,_B9))
if mibBuilder.loadTexts:wchHistPMEntry.setStatus(_B)
_WchHistPMCpTypeIdx_Type=CpType
_WchHistPMCpTypeIdx_Object=MibTableColumn
wchHistPMCpTypeIdx=_WchHistPMCpTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,1),_WchHistPMCpTypeIdx_Type())
wchHistPMCpTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMCpTypeIdx.setStatus(_B)
class _WchHistPMShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(11,11),ValueRangeConstraint(21,21),ValueRangeConstraint(31,31))
_WchHistPMShelfIdx_Type.__name__=_F
_WchHistPMShelfIdx_Object=MibTableColumn
wchHistPMShelfIdx=_WchHistPMShelfIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,2),_WchHistPMShelfIdx_Type())
wchHistPMShelfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMShelfIdx.setStatus(_B)
class _WchHistPMSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WchHistPMSlotIdx_Type.__name__=_F
_WchHistPMSlotIdx_Object=MibTableColumn
wchHistPMSlotIdx=_WchHistPMSlotIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,3),_WchHistPMSlotIdx_Type())
wchHistPMSlotIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMSlotIdx.setStatus(_B)
_WchHistPMPortTypeIdx_Type=OlPortType
_WchHistPMPortTypeIdx_Object=MibTableColumn
wchHistPMPortTypeIdx=_WchHistPMPortTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,4),_WchHistPMPortTypeIdx_Type())
wchHistPMPortTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMPortTypeIdx.setStatus(_B)
class _WchHistPMPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WchHistPMPortIdx_Type.__name__=_F
_WchHistPMPortIdx_Object=MibTableColumn
wchHistPMPortIdx=_WchHistPMPortIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,5),_WchHistPMPortIdx_Type())
wchHistPMPortIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMPortIdx.setStatus(_B)
class _WchHistPMIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(135,610))
_WchHistPMIdx_Type.__name__=_F
_WchHistPMIdx_Object=MibTableColumn
wchHistPMIdx=_WchHistPMIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,6),_WchHistPMIdx_Type())
wchHistPMIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMIdx.setStatus(_B)
_WchHistPMIntervalTypeIdx_Type=PMIntervalType
_WchHistPMIntervalTypeIdx_Object=MibTableColumn
wchHistPMIntervalTypeIdx=_WchHistPMIntervalTypeIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,7),_WchHistPMIntervalTypeIdx_Type())
wchHistPMIntervalTypeIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMIntervalTypeIdx.setStatus(_B)
class _WchHistPMIntervalIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_WchHistPMIntervalIdx_Type.__name__=_F
_WchHistPMIntervalIdx_Object=MibTableColumn
wchHistPMIntervalIdx=_WchHistPMIntervalIdx_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,8),_WchHistPMIntervalIdx_Type())
wchHistPMIntervalIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:wchHistPMIntervalIdx.setStatus(_B)
_WchHistPMOPRValue_Type=FixedX10
_WchHistPMOPRValue_Object=MibTableColumn
wchHistPMOPRValue=_WchHistPMOPRValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,9),_WchHistPMOPRValue_Type())
wchHistPMOPRValue.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPRValue.setUnits(_P)
_WchHistPMOPRTimeStamp_Type=DateAndTime
_WchHistPMOPRTimeStamp_Object=MibTableColumn
wchHistPMOPRTimeStamp=_WchHistPMOPRTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,10),_WchHistPMOPRTimeStamp_Type())
wchHistPMOPRTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRTimeStamp.setStatus(_B)
_WchHistPMOPRValidity_Type=PMValidity
_WchHistPMOPRValidity_Object=MibTableColumn
wchHistPMOPRValidity=_WchHistPMOPRValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,11),_WchHistPMOPRValidity_Type())
wchHistPMOPRValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRValidity.setStatus(_B)
_WchHistPMOPRMinValue_Type=FixedX10
_WchHistPMOPRMinValue_Object=MibTableColumn
wchHistPMOPRMinValue=_WchHistPMOPRMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,12),_WchHistPMOPRMinValue_Type())
wchHistPMOPRMinValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPRMinValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPRMinValue.setUnits(_P)
_WchHistPMOPRMinTimeStamp_Type=DateAndTime
_WchHistPMOPRMinTimeStamp_Object=MibTableColumn
wchHistPMOPRMinTimeStamp=_WchHistPMOPRMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,13),_WchHistPMOPRMinTimeStamp_Type())
wchHistPMOPRMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRMinTimeStamp.setStatus(_B)
_WchHistPMOPRMinValidity_Type=PMValidity
_WchHistPMOPRMinValidity_Object=MibTableColumn
wchHistPMOPRMinValidity=_WchHistPMOPRMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,14),_WchHistPMOPRMinValidity_Type())
wchHistPMOPRMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRMinValidity.setStatus(_B)
_WchHistPMOPRMinInitialize_Type=InitializeCmd
_WchHistPMOPRMinInitialize_Object=MibTableColumn
wchHistPMOPRMinInitialize=_WchHistPMOPRMinInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,15),_WchHistPMOPRMinInitialize_Type())
wchHistPMOPRMinInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPRMinInitialize.setStatus(_B)
_WchHistPMOPRMaxValue_Type=FixedX10
_WchHistPMOPRMaxValue_Object=MibTableColumn
wchHistPMOPRMaxValue=_WchHistPMOPRMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,16),_WchHistPMOPRMaxValue_Type())
wchHistPMOPRMaxValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPRMaxValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPRMaxValue.setUnits(_P)
_WchHistPMOPRMaxTimeStamp_Type=DateAndTime
_WchHistPMOPRMaxTimeStamp_Object=MibTableColumn
wchHistPMOPRMaxTimeStamp=_WchHistPMOPRMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,17),_WchHistPMOPRMaxTimeStamp_Type())
wchHistPMOPRMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRMaxTimeStamp.setStatus(_B)
_WchHistPMOPRMaxValidity_Type=PMValidity
_WchHistPMOPRMaxValidity_Object=MibTableColumn
wchHistPMOPRMaxValidity=_WchHistPMOPRMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,18),_WchHistPMOPRMaxValidity_Type())
wchHistPMOPRMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPRMaxValidity.setStatus(_B)
_WchHistPMOPRMaxInitialize_Type=InitializeCmd
_WchHistPMOPRMaxInitialize_Object=MibTableColumn
wchHistPMOPRMaxInitialize=_WchHistPMOPRMaxInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,19),_WchHistPMOPRMaxInitialize_Type())
wchHistPMOPRMaxInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPRMaxInitialize.setStatus(_B)
_WchHistPMOPTValue_Type=FixedX10
_WchHistPMOPTValue_Object=MibTableColumn
wchHistPMOPTValue=_WchHistPMOPTValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,20),_WchHistPMOPTValue_Type())
wchHistPMOPTValue.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPTValue.setUnits(_P)
_WchHistPMOPTTimeStamp_Type=DateAndTime
_WchHistPMOPTTimeStamp_Object=MibTableColumn
wchHistPMOPTTimeStamp=_WchHistPMOPTTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,21),_WchHistPMOPTTimeStamp_Type())
wchHistPMOPTTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTTimeStamp.setStatus(_B)
_WchHistPMOPTValidity_Type=PMValidity
_WchHistPMOPTValidity_Object=MibTableColumn
wchHistPMOPTValidity=_WchHistPMOPTValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,22),_WchHistPMOPTValidity_Type())
wchHistPMOPTValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTValidity.setStatus(_B)
_WchHistPMOPTMinValue_Type=FixedX10
_WchHistPMOPTMinValue_Object=MibTableColumn
wchHistPMOPTMinValue=_WchHistPMOPTMinValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,23),_WchHistPMOPTMinValue_Type())
wchHistPMOPTMinValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPTMinValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPTMinValue.setUnits(_P)
_WchHistPMOPTMinTimeStamp_Type=DateAndTime
_WchHistPMOPTMinTimeStamp_Object=MibTableColumn
wchHistPMOPTMinTimeStamp=_WchHistPMOPTMinTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,24),_WchHistPMOPTMinTimeStamp_Type())
wchHistPMOPTMinTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTMinTimeStamp.setStatus(_B)
_WchHistPMOPTMinValidity_Type=PMValidity
_WchHistPMOPTMinValidity_Object=MibTableColumn
wchHistPMOPTMinValidity=_WchHistPMOPTMinValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,25),_WchHistPMOPTMinValidity_Type())
wchHistPMOPTMinValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTMinValidity.setStatus(_B)
_WchHistPMOPTMinInitialize_Type=InitializeCmd
_WchHistPMOPTMinInitialize_Object=MibTableColumn
wchHistPMOPTMinInitialize=_WchHistPMOPTMinInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,26),_WchHistPMOPTMinInitialize_Type())
wchHistPMOPTMinInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPTMinInitialize.setStatus(_B)
_WchHistPMOPTMaxValue_Type=FixedX10
_WchHistPMOPTMaxValue_Object=MibTableColumn
wchHistPMOPTMaxValue=_WchHistPMOPTMaxValue_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,27),_WchHistPMOPTMaxValue_Type())
wchHistPMOPTMaxValue.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPTMaxValue.setStatus(_B)
if mibBuilder.loadTexts:wchHistPMOPTMaxValue.setUnits(_P)
_WchHistPMOPTMaxTimeStamp_Type=DateAndTime
_WchHistPMOPTMaxTimeStamp_Object=MibTableColumn
wchHistPMOPTMaxTimeStamp=_WchHistPMOPTMaxTimeStamp_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,28),_WchHistPMOPTMaxTimeStamp_Type())
wchHistPMOPTMaxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTMaxTimeStamp.setStatus(_B)
_WchHistPMOPTMaxValidity_Type=PMValidity
_WchHistPMOPTMaxValidity_Object=MibTableColumn
wchHistPMOPTMaxValidity=_WchHistPMOPTMaxValidity_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,29),_WchHistPMOPTMaxValidity_Type())
wchHistPMOPTMaxValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:wchHistPMOPTMaxValidity.setStatus(_B)
_WchHistPMOPTMaxInitialize_Type=InitializeCmd
_WchHistPMOPTMaxInitialize_Object=MibTableColumn
wchHistPMOPTMaxInitialize=_WchHistPMOPTMaxInitialize_Object((1,3,6,1,4,1,18070,2,2,1,16,12,7,1,30),_WchHistPMOPTMaxInitialize_Type())
wchHistPMOPTMaxInitialize.setMaxAccess(_G)
if mibBuilder.loadTexts:wchHistPMOPTMaxInitialize.setStatus(_B)
_OlOSCEvtNotifications_ObjectIdentity=ObjectIdentity
olOSCEvtNotifications=_OlOSCEvtNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,1,33,1))
_OlPortEvtNotifications_ObjectIdentity=ObjectIdentity
olPortEvtNotifications=_OlPortEvtNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,1,33,2))
_WdmEvtNotifications_ObjectIdentity=ObjectIdentity
wdmEvtNotifications=_WdmEvtNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,1,33,3))
_WchEvtNotifications_ObjectIdentity=ObjectIdentity
wchEvtNotifications=_WchEvtNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,1,33,4))
_OlOSCCondNotifications_ObjectIdentity=ObjectIdentity
olOSCCondNotifications=_OlOSCCondNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,2,28,1))
_OlPortCondNotifications_ObjectIdentity=ObjectIdentity
olPortCondNotifications=_OlPortCondNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,2,28,2))
_WdmCondNotifications_ObjectIdentity=ObjectIdentity
wdmCondNotifications=_WdmCondNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,2,28,3))
_WchCondNotifications_ObjectIdentity=ObjectIdentity
wchCondNotifications=_WchCondNotifications_ObjectIdentity((1,3,6,1,4,1,18070,2,2,2,2,28,4))
olOSCStatusChangeEvt=NotificationType((1,3,6,1,4,1,18070,2,2,2,1,33,1,0,1))
olOSCStatusChangeEvt.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_BA),(_C,_BB),(_A,_o),(_A,_H),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:olOSCStatusChangeEvt.setStatus(_B)
olOSCTcaEvt=NotificationType((1,3,6,1,4,1,18070,2,2,2,1,33,1,0,2))
olOSCTcaEvt.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_t),(_A,_s),(_A,_u),(_A,_w),(_A,_v),(_A,_o),(_A,_H),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:olOSCTcaEvt.setStatus(_B)
olPortStatusChangeEvt=NotificationType((1,3,6,1,4,1,18070,2,2,2,1,33,2,0,1))
olPortStatusChangeEvt.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_C,_BC),(_C,_BD),(_A,_o),(_A,_H),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:olPortStatusChangeEvt.setStatus(_B)
wdmStatusChangeEvt=NotificationType((1,3,6,1,4,1,18070,2,2,2,1,33,3,0,1))
wdmStatusChangeEvt.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_R),(_C,_BE),(_C,_BF),(_A,_o),(_A,_H),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:wdmStatusChangeEvt.setStatus(_B)
wchStatusChangeEvt=NotificationType((1,3,6,1,4,1,18070,2,2,2,1,33,4,0,1))
wchStatusChangeEvt.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_BG),(_C,_BH),(_A,_o),(_A,_H),(_A,_p),(_A,_q),(_A,_n)))
if mibBuilder.loadTexts:wchStatusChangeEvt.setStatus(_B)
olOSCLossOfLightRxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,1))
olOSCLossOfLightRxCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfLightRxCond.setStatus(_B)
olOSCLossOfLightRxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,2))
olOSCLossOfLightRxClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfLightRxClear.setStatus(_B)
olOSCLossOfFrameCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,3))
olOSCLossOfFrameCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfFrameCond.setStatus(_B)
olOSCLossOfFrameClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,4))
olOSCLossOfFrameClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfFrameClear.setStatus(_B)
olOSCLossOfLightTxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,5))
olOSCLossOfLightTxCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfLightTxCond.setStatus(_B)
olOSCLossOfLightTxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,6))
olOSCLossOfLightTxClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCLossOfLightTxClear.setStatus(_B)
olOSCFarEndIdMismatchCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,7))
olOSCFarEndIdMismatchCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCFarEndIdMismatchCond.setStatus(_B)
olOSCFarEndIdMismatchClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,8))
olOSCFarEndIdMismatchClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCFarEndIdMismatchClear.setStatus(_B)
olOSCFarEndNodeCnfgInconsistentCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,9))
olOSCFarEndNodeCnfgInconsistentCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCFarEndNodeCnfgInconsistentCond.setStatus(_B)
olOSCFarEndNodeCnfgInconsistentClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,10))
olOSCFarEndNodeCnfgInconsistentClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCFarEndNodeCnfgInconsistentClear.setStatus(_B)
olOSCSpanContCommCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,11))
olOSCSpanContCommCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCSpanContCommCond.setStatus(_B)
olOSCSpanContCommClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,12))
olOSCSpanContCommClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCSpanContCommClear.setStatus(_B)
olOSCEqlzContCommCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,13))
olOSCEqlzContCommCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCEqlzContCommCond.setStatus(_B)
olOSCEqlzContCommClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,14))
olOSCEqlzContCommClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCEqlzContCommClear.setStatus(_B)
olOSCOpticalBackReflOutOfSpecCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,15))
olOSCOpticalBackReflOutOfSpecCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCOpticalBackReflOutOfSpecCond.setStatus(_B)
olOSCOpticalBackReflOutOfSpecClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,16))
olOSCOpticalBackReflOutOfSpecClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCOpticalBackReflOutOfSpecClear.setStatus(_B)
olOSCOpticalBackReflHighThCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,17))
olOSCOpticalBackReflHighThCond.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCOpticalBackReflHighThCond.setStatus(_B)
olOSCOpticalBackReflHighThClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,1,0,18))
olOSCOpticalBackReflHighThClear.setObjects(*((_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olOSCOpticalBackReflHighThClear.setStatus(_B)
olPortPowerOutOfSpecRxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,1))
olPortPowerOutOfSpecRxCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortPowerOutOfSpecRxCond.setStatus(_B)
olPortPowerOutOfSpecRxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,2))
olPortPowerOutOfSpecRxClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortPowerOutOfSpecRxClear.setStatus(_B)
olPortLossOfLightRxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,3))
olPortLossOfLightRxCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossOfLightRxCond.setStatus(_B)
olPortLossOfLightRxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,4))
olPortLossOfLightRxClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossOfLightRxClear.setStatus(_B)
olPortLossRxOutOfSpecCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,5))
olPortLossRxOutOfSpecCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossRxOutOfSpecCond.setStatus(_B)
olPortLossRxOutOfSpecClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,6))
olPortLossRxOutOfSpecClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossRxOutOfSpecClear.setStatus(_B)
olPortLossRxHighThCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,7))
olPortLossRxHighThCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossRxHighThCond.setStatus(_B)
olPortLossRxHighThClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,8))
olPortLossRxHighThClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortLossRxHighThClear.setStatus(_B)
olPortAPSDCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,9))
olPortAPSDCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortAPSDCond.setStatus(_B)
olPortAPSDClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,10))
olPortAPSDClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortAPSDClear.setStatus(_B)
olPortPayloadMissingIndCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,11))
olPortPayloadMissingIndCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortPayloadMissingIndCond.setStatus(_B)
olPortPayloadMissingIndClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,12))
olPortPayloadMissingIndClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortPayloadMissingIndClear.setStatus(_B)
olPortBackwardDefectIndCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,13))
olPortBackwardDefectIndCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortBackwardDefectIndCond.setStatus(_B)
olPortBackwardDefectIndClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,14))
olPortBackwardDefectIndClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortBackwardDefectIndClear.setStatus(_B)
olPortChannelCountDeficiencyCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,15))
olPortChannelCountDeficiencyCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortChannelCountDeficiencyCond.setStatus(_B)
olPortChannelCountDeficiencyClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,16))
olPortChannelCountDeficiencyClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortChannelCountDeficiencyClear.setStatus(_B)
olPortConnectionMismatchCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,17))
olPortConnectionMismatchCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_C,_BI),(_C,_BJ),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortConnectionMismatchCond.setStatus(_B)
olPortConnectionMismatchClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,18))
olPortConnectionMismatchClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortConnectionMismatchClear.setStatus(_B)
olPortConnectionValidationTimeoutCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,19))
olPortConnectionValidationTimeoutCond.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortConnectionValidationTimeoutCond.setStatus(_B)
olPortConnectionValidationTimeoutClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,2,0,20))
olPortConnectionValidationTimeoutClear.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_R),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:olPortConnectionValidationTimeoutClear.setStatus(_B)
wdmInvalidPreAmpOperCnfgCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,1))
wdmInvalidPreAmpOperCnfgCond.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidPreAmpOperCnfgCond.setStatus(_B)
wdmInvalidPreAmpOperCnfgClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,2))
wdmInvalidPreAmpOperCnfgClear.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidPreAmpOperCnfgClear.setStatus(_B)
wdmInvalidMidAmpOperCnfgCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,3))
wdmInvalidMidAmpOperCnfgCond.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidMidAmpOperCnfgCond.setStatus(_B)
wdmInvalidMidAmpOperCnfgClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,4))
wdmInvalidMidAmpOperCnfgClear.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidMidAmpOperCnfgClear.setStatus(_B)
wdmInvalidBoostAmpOperCnfgCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,5))
wdmInvalidBoostAmpOperCnfgCond.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidBoostAmpOperCnfgCond.setStatus(_B)
wdmInvalidBoostAmpOperCnfgClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,3,0,6))
wdmInvalidBoostAmpOperCnfgClear.setObjects(*((_C,_i),(_C,_j),(_C,_k),(_C,_l),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wdmInvalidBoostAmpOperCnfgClear.setStatus(_B)
wchPowerOutOfSpecRxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,1))
wchPowerOutOfSpecRxCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxCond.setStatus(_m)
wchPowerOutOfSpecRxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,2))
wchPowerOutOfSpecRxClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxClear.setStatus(_m)
wchLossOfLightRxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,3))
wchLossOfLightRxCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchLossOfLightRxCond.setStatus(_B)
wchLossOfLightRxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,4))
wchLossOfLightRxClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchLossOfLightRxClear.setStatus(_B)
wchPowerOutOfSpecTxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,5))
wchPowerOutOfSpecTxCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecTxCond.setStatus(_B)
wchPowerOutOfSpecTxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,6))
wchPowerOutOfSpecTxClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecTxClear.setStatus(_B)
wchLossOfLightTxCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,7))
wchLossOfLightTxCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchLossOfLightTxCond.setStatus(_B)
wchLossOfLightTxClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,8))
wchLossOfLightTxClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchLossOfLightTxClear.setStatus(_B)
wchUnequippedCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,9))
wchUnequippedCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchUnequippedCond.setStatus(_B)
wchUnequippedClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,10))
wchUnequippedClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchUnequippedClear.setStatus(_B)
wchAISCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,11))
wchAISCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchAISCond.setStatus(_B)
wchAISClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,12))
wchAISClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchAISClear.setStatus(_B)
wchPowerOutOfSpecRxHighCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,13))
wchPowerOutOfSpecRxHighCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxHighCond.setStatus(_m)
wchPowerOutOfSpecRxHighClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,14))
wchPowerOutOfSpecRxHighClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxHighClear.setStatus(_m)
wchPowerOutOfSpecRxLowCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,15))
wchPowerOutOfSpecRxLowCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxLowCond.setStatus(_m)
wchPowerOutOfSpecRxLowClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,16))
wchPowerOutOfSpecRxLowClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerOutOfSpecRxLowClear.setStatus(_m)
wchPowerRxHighFailCond=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,17))
wchPowerRxHighFailCond.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerRxHighFailCond.setStatus(_m)
wchPowerRxHighFailClear=NotificationType((1,3,6,1,4,1,18070,2,2,2,2,28,4,0,18))
wchPowerRxHighFailClear.setObjects(*((_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_A,_M),(_A,_J),(_A,_O),(_A,_N),(_A,_H),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:wchPowerRxHighFailClear.setStatus(_m)
mibBuilder.exportSymbols(_C,**{'OlGroupType':OlGroupType,'OlPortType':OlPortType,'olMib':olMib,'olGroupTable':olGroupTable,'olGroupEntry':olGroupEntry,_x:olGroupIdx,'olGroupType':olGroupType,'olGroupId':olGroupId,'olGroupCustom1':olGroupCustom1,'olGroupCustom2':olGroupCustom2,'olGroupCustom3':olGroupCustom3,'olGroupRowStatus':olGroupRowStatus,'olEqptTable':olEqptTable,'olEqptEntry':olEqptEntry,_y:olEqptCpTypeIdx,_z:olEqptShelfIdx,_A0:olEqptSlotIdx,'olEqptGroupNum':olEqptGroupNum,'olEqptDegreeNum':olEqptDegreeNum,'olEqptRowStatus':olEqptRowStatus,'olPortTable':olPortTable,'olPortEntry':olPortEntry,_S:olPortCpTypeIdx,_T:olPortShelfIdx,_U:olPortSlotIdx,_V:olPortTypeIdx,_R:olPortIdx,'olPortId':olPortId,'olPortCustom1':olPortCustom1,'olPortCustom2':olPortCustom2,'olPortCustom3':olPortCustom3,'olPortDWDMType':olPortDWDMType,'olPortGrid':olPortGrid,'olPortWavelength':olPortWavelength,'olPortFrequency':olPortFrequency,_BC:olPortOperStatus,_BD:olPortOperStatQlfr,'olPortRemoteId':olPortRemoteId,_BI:olPortExpCnxDegree,_BJ:olPortActCnxDegree,'olPortRowStatus':olPortRowStatus,'eqptConnTable':eqptConnTable,'eqptConnEntry':eqptConnEntry,_A3:eqptConnSrcCpTypeIdx,_A4:eqptConnSrcShelfIdx,_A5:eqptConnSrcSlotIdx,_A6:eqptConnSrcPortTypeIdx,_A7:eqptConnSrcIdx,_A8:eqptConnDstCpTypeIdx,_A9:eqptConnDstShelfIdx,_AA:eqptConnDstSlotIdx,_AB:eqptConnDstPortTypeIdx,_AC:eqptConnDstIdx,'eqptConnType':eqptConnType,'eqptConnRowStatus':eqptConnRowStatus,'olOSCTable':olOSCTable,'olOSCEntry':olOSCEntry,_W:olOSCCpTypeIdx,_X:olOSCShelfIdx,_Y:olOSCSlotIdx,_Z:olOSCLineIdx,'olOSCAdminStatus':olOSCAdminStatus,_BA:olOSCOperStatus,_BB:olOSCOperStatQlfr,'olOSCAutoEnableTimer':olOSCAutoEnableTimer,'olOSCActAutoEnableTimer':olOSCActAutoEnableTimer,'olOSCId':olOSCId,'olOSCCustom1':olOSCCustom1,'olOSCCustom2':olOSCCustom2,'olOSCCustom3':olOSCCustom3,'olOSCFEIMMon':olOSCFEIMMon,'olOSCExpFESysName':olOSCExpFESysName,'olOSCExpFEIPAddr':olOSCExpFEIPAddr,'olOSCExpFEGrp':olOSCExpFEGrp,'olOSCExpFEDegr':olOSCExpFEDegr,'olOSCFESysName':olOSCFESysName,'olOSCFEIPAddr':olOSCFEIPAddr,'olOSCFEGrp':olOSCFEGrp,'olOSCFEDegr':olOSCFEDegr,'olOSCFEGrpType':olOSCFEGrpType,'olOSCRowStatus':olOSCRowStatus,'odccTable':odccTable,'odccEntry':odccEntry,_AD:odccCpTypeIdx,_AE:odccShelfIdx,_AF:odccSlotIdx,_AG:odccLineIdx,'odccAdminStatus':odccAdminStatus,'odccRowStatus':odccRowStatus,'wdmTable':wdmTable,'wdmEntry':wdmEntry,_i:wdmCpTypeIdx,_j:wdmShelfIdx,_k:wdmSlotIdx,_l:wdmLineIdx,'wdmAdminStatus':wdmAdminStatus,_BE:wdmOperStatus,_BF:wdmOperStatQlfr,'wdmAutoEnableTimer':wdmAutoEnableTimer,'wdmActAutoEnableTimer':wdmActAutoEnableTimer,'wdmId':wdmId,'wdmCustom1':wdmCustom1,'wdmCustom2':wdmCustom2,'wdmCustom3':wdmCustom3,'wdmFiberType':wdmFiberType,'wdmSpanLength':wdmSpanLength,'wdmSpanLossRxHighTh':wdmSpanLossRxHighTh,'wdmSpanLossSpecMax':wdmSpanLossSpecMax,'wdmNumChannels':wdmNumChannels,'wdmRowStatus':wdmRowStatus,'wchXCTable':wchXCTable,'wchXCEntry':wchXCEntry,_AH:wchXCSrcCpTypeIdx,_AI:wchXCSrcShelfIdx,_AJ:wchXCSrcSlotIdx,_AK:wchXCSrcPortTypeIdx,_AL:wchXCSrcPortIdx,_AM:wchXCSrcChannelIdx,_AN:wchXCDstCpTypeIdx,_AO:wchXCDstShelfIdx,_AP:wchXCDstSlotIdx,_AQ:wchXCDstPortTypeIdx,_AR:wchXCDstPortIdx,_AS:wchXCDstChannelIdx,'wchXCServiceName':wchXCServiceName,'wchXCRowStatus':wchXCRowStatus,'wchTable':wchTable,'wchEntry':wchEntry,_a:wchCpTypeIdx,_b:wchShelfIdx,_c:wchSlotIdx,_d:wchPortTypeIdx,_e:wchPortIdx,_f:wchIdx,'wchAdminStatus':wchAdminStatus,_BG:wchOperStatus,_BH:wchOperStatQlfr,'wchAutoEnableTimer':wchAutoEnableTimer,'wchActAutoEnableTimer':wchActAutoEnableTimer,'wchId':wchId,'wchCustom1':wchCustom1,'wchCustom2':wchCustom2,'wchCustom3':wchCustom3,'wchBitrate':wchBitrate,'wchGrid':wchGrid,'wchWavelength':wchWavelength,'wchFrequency':wchFrequency,'wchRowStatus':wchRowStatus,'olGroupMerge':olGroupMerge,'olGroupMergeCmd':olGroupMergeCmd,'olGroupMergePrimary':olGroupMergePrimary,'olGroupMergeSecondary':olGroupMergeSecondary,'olPerformance':olPerformance,'olOSCCrntPMTable':olOSCCrntPMTable,'olOSCCrntPMEntry':olOSCCrntPMEntry,_AT:olOSCCrntPMCpTypeIdx,_AU:olOSCCrntPMShelfIdx,_AV:olOSCCrntPMSlotIdx,_AW:olOSCCrntPMLineIdx,_AX:olOSCCrntPMIntervalTypeIdx,'olOSCCrntPMOPRValue':olOSCCrntPMOPRValue,'olOSCCrntPMOPRTimeStamp':olOSCCrntPMOPRTimeStamp,'olOSCCrntPMOPRValidity':olOSCCrntPMOPRValidity,'olOSCCrntPMOPTValue':olOSCCrntPMOPTValue,'olOSCCrntPMOPTTimeStamp':olOSCCrntPMOPTTimeStamp,'olOSCCrntPMOPTValidity':olOSCCrntPMOPTValidity,'olOSCCrntPMOBRValue':olOSCCrntPMOBRValue,'olOSCCrntPMOBRTimeStamp':olOSCCrntPMOBRTimeStamp,'olOSCCrntPMOBRValidity':olOSCCrntPMOBRValidity,'olOSCCrntPMCVSValue':olOSCCrntPMCVSValue,'olOSCCrntPMCVSTimeStamp':olOSCCrntPMCVSTimeStamp,'olOSCCrntPMCVSValidity':olOSCCrntPMCVSValidity,'olOSCCrntPMCVSInitialize':olOSCCrntPMCVSInitialize,'olOSCCrntPMESSValue':olOSCCrntPMESSValue,'olOSCCrntPMESSTimeStamp':olOSCCrntPMESSTimeStamp,'olOSCCrntPMESSValidity':olOSCCrntPMESSValidity,'olOSCCrntPMESSInitialize':olOSCCrntPMESSInitialize,'olOSCCrntPMSESSValue':olOSCCrntPMSESSValue,'olOSCCrntPMSESSTimeStamp':olOSCCrntPMSESSTimeStamp,'olOSCCrntPMSESSValidity':olOSCCrntPMSESSValidity,'olOSCCrntPMSESSInitialize':olOSCCrntPMSESSInitialize,'olOSCCrntPMSEFSSValue':olOSCCrntPMSEFSSValue,'olOSCCrntPMSEFSSTimeStamp':olOSCCrntPMSEFSSTimeStamp,'olOSCCrntPMSEFSSValidity':olOSCCrntPMSEFSSValidity,'olOSCCrntPMSEFSSInitialize':olOSCCrntPMSEFSSInitialize,'olOSCCrntPMUASSValue':olOSCCrntPMUASSValue,'olOSCCrntPMUASSTimeStamp':olOSCCrntPMUASSTimeStamp,'olOSCCrntPMUASSValidity':olOSCCrntPMUASSValidity,'olOSCCrntPMUASSInitialize':olOSCCrntPMUASSInitialize,'olOSCHistPMTable':olOSCHistPMTable,'olOSCHistPMEntry':olOSCHistPMEntry,_AY:olOSCHistPMCpTypeIdx,_AZ:olOSCHistPMShelfIdx,_Aa:olOSCHistPMSlotIdx,_Ab:olOSCHistPMLineIdx,_Ac:olOSCHistPMIntervalTypeIdx,_Ad:olOSCHistPMIntervalIdx,'olOSCHistPMOPRValue':olOSCHistPMOPRValue,'olOSCHistPMOPRTimeStamp':olOSCHistPMOPRTimeStamp,'olOSCHistPMOPRValidity':olOSCHistPMOPRValidity,'olOSCHistPMOPTValue':olOSCHistPMOPTValue,'olOSCHistPMOPTTimeStamp':olOSCHistPMOPTTimeStamp,'olOSCHistPMOPTValidity':olOSCHistPMOPTValidity,'olOSCHistPMOBRValue':olOSCHistPMOBRValue,'olOSCHistPMOBRTimeStamp':olOSCHistPMOBRTimeStamp,'olOSCHistPMOBRValidity':olOSCHistPMOBRValidity,'olOSCHistPMCVSValue':olOSCHistPMCVSValue,'olOSCHistPMCVSTimeStamp':olOSCHistPMCVSTimeStamp,'olOSCHistPMCVSValidity':olOSCHistPMCVSValidity,'olOSCHistPMCVSInitialize':olOSCHistPMCVSInitialize,'olOSCHistPMESSValue':olOSCHistPMESSValue,'olOSCHistPMESSTimeStamp':olOSCHistPMESSTimeStamp,'olOSCHistPMESSValidity':olOSCHistPMESSValidity,'olOSCHistPMESSInitialize':olOSCHistPMESSInitialize,'olOSCHistPMSESSValue':olOSCHistPMSESSValue,'olOSCHistPMSESSTimeStamp':olOSCHistPMSESSTimeStamp,'olOSCHistPMSESSValidity':olOSCHistPMSESSValidity,'olOSCHistPMSESSInitialize':olOSCHistPMSESSInitialize,'olOSCHistPMSEFSSValue':olOSCHistPMSEFSSValue,'olOSCHistPMSEFSSTimeStamp':olOSCHistPMSEFSSTimeStamp,'olOSCHistPMSEFSSValidity':olOSCHistPMSEFSSValidity,'olOSCHistPMSEFSSInitialize':olOSCHistPMSEFSSInitialize,'olOSCHistPMUASSValue':olOSCHistPMUASSValue,'olOSCHistPMUASSTimeStamp':olOSCHistPMUASSTimeStamp,'olOSCHistPMUASSValidity':olOSCHistPMUASSValidity,'olOSCHistPMUASSInitialize':olOSCHistPMUASSInitialize,'olOSCPMThresholdTable':olOSCPMThresholdTable,'olOSCPMThresholdEntry':olOSCPMThresholdEntry,_Ae:olOSCPMThresholdCpTypeIdx,_Af:olOSCPMThresholdShelfIdx,_Ag:olOSCPMThresholdSlotIdx,_Ah:olOSCPMThresholdLineIdx,_Ai:olOSCPMThresholdIntervalTypeIdx,'olOSCPMThresholdCVSValue':olOSCPMThresholdCVSValue,'olOSCPMThresholdESSValue':olOSCPMThresholdESSValue,'olOSCPMThresholdSESSValue':olOSCPMThresholdSESSValue,'olOSCPMThresholdSEFSSValue':olOSCPMThresholdSEFSSValue,'olOSCPMThresholdUASSValue':olOSCPMThresholdUASSValue,'olPortCrntPMTable':olPortCrntPMTable,'olPortCrntPMEntry':olPortCrntPMEntry,_Aj:olPortCrntPMCpTypeIdx,_Ak:olPortCrntPMShelfIdx,_Al:olPortCrntPMSlotIdx,_Am:olPortCrntPMTypeIdx,_An:olPortCrntPMIdx,_Ao:olPortCrntPMIntervalTypeIdx,'olPortCrntPMOPRValue':olPortCrntPMOPRValue,'olPortCrntPMOPRTimeStamp':olPortCrntPMOPRTimeStamp,'olPortCrntPMOPRValidity':olPortCrntPMOPRValidity,'olPortCrntPMOPRMinValue':olPortCrntPMOPRMinValue,'olPortCrntPMOPRMinTimeStamp':olPortCrntPMOPRMinTimeStamp,'olPortCrntPMOPRMinValidity':olPortCrntPMOPRMinValidity,'olPortCrntPMOPRMaxValue':olPortCrntPMOPRMaxValue,'olPortCrntPMOPRMaxTimeStamp':olPortCrntPMOPRMaxTimeStamp,'olPortCrntPMOPRMaxValidity':olPortCrntPMOPRMaxValidity,'olPortCrntPMOPRAvgValue':olPortCrntPMOPRAvgValue,'olPortCrntPMOPRAvgTimeStamp':olPortCrntPMOPRAvgTimeStamp,'olPortCrntPMOPRAvgValidity':olPortCrntPMOPRAvgValidity,'olPortCrntPMOPRStdDevValue':olPortCrntPMOPRStdDevValue,'olPortCrntPMOPRStdDevTimeStamp':olPortCrntPMOPRStdDevTimeStamp,'olPortCrntPMOPRStdDevValidity':olPortCrntPMOPRStdDevValidity,'olPortCrntPMOPTValue':olPortCrntPMOPTValue,'olPortCrntPMOPTTimeStamp':olPortCrntPMOPTTimeStamp,'olPortCrntPMOPTValidity':olPortCrntPMOPTValidity,'olPortCrntPMOPTMinValue':olPortCrntPMOPTMinValue,'olPortCrntPMOPTMinTimeStamp':olPortCrntPMOPTMinTimeStamp,'olPortCrntPMOPTMinValidity':olPortCrntPMOPTMinValidity,'olPortCrntPMOPTMaxValue':olPortCrntPMOPTMaxValue,'olPortCrntPMOPTMaxTimeStamp':olPortCrntPMOPTMaxTimeStamp,'olPortCrntPMOPTMaxValidity':olPortCrntPMOPTMaxValidity,'olPortCrntPMOPTAvgValue':olPortCrntPMOPTAvgValue,'olPortCrntPMOPTAvgTimeStamp':olPortCrntPMOPTAvgTimeStamp,'olPortCrntPMOPTAvgValidity':olPortCrntPMOPTAvgValidity,'olPortCrntPMOPTStdDevValue':olPortCrntPMOPTStdDevValue,'olPortCrntPMOPTStdDevTimeStamp':olPortCrntPMOPTStdDevTimeStamp,'olPortCrntPMOPTStdDevValidity':olPortCrntPMOPTStdDevValidity,'olPortCrntPMLossRxValue':olPortCrntPMLossRxValue,'olPortCrntPMLossRxTimeStamp':olPortCrntPMLossRxTimeStamp,'olPortCrntPMLossRxValidity':olPortCrntPMLossRxValidity,'olPortCrntPMLossTxValue':olPortCrntPMLossTxValue,'olPortCrntPMLossTxTimeStamp':olPortCrntPMLossTxTimeStamp,'olPortCrntPMLossTxValidity':olPortCrntPMLossTxValidity,'olPortCrntPMInitializeAll':olPortCrntPMInitializeAll,'olPortHistPMTable':olPortHistPMTable,'olPortHistPMEntry':olPortHistPMEntry,_Ap:olPortHistPMCpTypeIdx,_Aq:olPortHistPMShelfIdx,_Ar:olPortHistPMSlotIdx,_As:olPortHistPMTypeIdx,_At:olPortHistPMIdx,_Au:olPortHistPMIntervalTypeIdx,_Av:olPortHistPMIntervalIdx,'olPortHistPMOPRValue':olPortHistPMOPRValue,'olPortHistPMOPRTimeStamp':olPortHistPMOPRTimeStamp,'olPortHistPMOPRValidity':olPortHistPMOPRValidity,'olPortHistPMOPRMinValue':olPortHistPMOPRMinValue,'olPortHistPMOPRMinTimeStamp':olPortHistPMOPRMinTimeStamp,'olPortHistPMOPRMinValidity':olPortHistPMOPRMinValidity,'olPortHistPMOPRMaxValue':olPortHistPMOPRMaxValue,'olPortHistPMOPRMaxTimeStamp':olPortHistPMOPRMaxTimeStamp,'olPortHistPMOPRMaxValidity':olPortHistPMOPRMaxValidity,'olPortHistPMOPRAvgValue':olPortHistPMOPRAvgValue,'olPortHistPMOPRAvgTimeStamp':olPortHistPMOPRAvgTimeStamp,'olPortHistPMOPRAvgValidity':olPortHistPMOPRAvgValidity,'olPortHistPMOPRStdDevValue':olPortHistPMOPRStdDevValue,'olPortHistPMOPRStdDevTimeStamp':olPortHistPMOPRStdDevTimeStamp,'olPortHistPMOPRStdDevValidity':olPortHistPMOPRStdDevValidity,'olPortHistPMOPTValue':olPortHistPMOPTValue,'olPortHistPMOPTTimeStamp':olPortHistPMOPTTimeStamp,'olPortHistPMOPTValidity':olPortHistPMOPTValidity,'olPortHistPMOPTMinValue':olPortHistPMOPTMinValue,'olPortHistPMOPTMinTimeStamp':olPortHistPMOPTMinTimeStamp,'olPortHistPMOPTMinValidity':olPortHistPMOPTMinValidity,'olPortHistPMOPTMaxValue':olPortHistPMOPTMaxValue,'olPortHistPMOPTMaxTimeStamp':olPortHistPMOPTMaxTimeStamp,'olPortHistPMOPTMaxValidity':olPortHistPMOPTMaxValidity,'olPortHistPMOPTAvgValue':olPortHistPMOPTAvgValue,'olPortHistPMOPTAvgTimeStamp':olPortHistPMOPTAvgTimeStamp,'olPortHistPMOPTAvgValidity':olPortHistPMOPTAvgValidity,'olPortHistPMOPTStdDevValue':olPortHistPMOPTStdDevValue,'olPortHistPMOPTStdDevTimeStamp':olPortHistPMOPTStdDevTimeStamp,'olPortHistPMOPTStdDevValidity':olPortHistPMOPTStdDevValidity,'olPortHistPMLossRxValue':olPortHistPMLossRxValue,'olPortHistPMLossRxTimeStamp':olPortHistPMLossRxTimeStamp,'olPortHistPMLossRxValidity':olPortHistPMLossRxValidity,'olPortHistPMLossTxValue':olPortHistPMLossTxValue,'olPortHistPMLossTxTimeStamp':olPortHistPMLossTxTimeStamp,'olPortHistPMLossTxValidity':olPortHistPMLossTxValidity,'olPortHistPMInitializeAll':olPortHistPMInitializeAll,'wchCrntPMTable':wchCrntPMTable,'wchCrntPMEntry':wchCrntPMEntry,_Aw:wchCrntPMCpTypeIdx,_Ax:wchCrntPMShelfIdx,_Ay:wchCrntPMSlotIdx,_Az:wchCrntPMPortTypeIdx,_A_:wchCrntPMPortIdx,_B0:wchCrntPMIdx,_B1:wchCrntPMIntervalTypeIdx,'wchCrntPMOPRValue':wchCrntPMOPRValue,'wchCrntPMOPRTimeStamp':wchCrntPMOPRTimeStamp,'wchCrntPMOPRValidity':wchCrntPMOPRValidity,'wchCrntPMOPRMinValue':wchCrntPMOPRMinValue,'wchCrntPMOPRMinTimeStamp':wchCrntPMOPRMinTimeStamp,'wchCrntPMOPRMinValidity':wchCrntPMOPRMinValidity,'wchCrntPMOPRMinInitialize':wchCrntPMOPRMinInitialize,'wchCrntPMOPRMaxValue':wchCrntPMOPRMaxValue,'wchCrntPMOPRMaxTimeStamp':wchCrntPMOPRMaxTimeStamp,'wchCrntPMOPRMaxValidity':wchCrntPMOPRMaxValidity,'wchCrntPMOPRMaxInitialize':wchCrntPMOPRMaxInitialize,'wchCrntPMOPTValue':wchCrntPMOPTValue,'wchCrntPMOPTTimeStamp':wchCrntPMOPTTimeStamp,'wchCrntPMOPTValidity':wchCrntPMOPTValidity,'wchCrntPMOPTMinValue':wchCrntPMOPTMinValue,'wchCrntPMOPTMinTimeStamp':wchCrntPMOPTMinTimeStamp,'wchCrntPMOPTMinValidity':wchCrntPMOPTMinValidity,'wchCrntPMOPTMinInitialize':wchCrntPMOPTMinInitialize,'wchCrntPMOPTMaxValue':wchCrntPMOPTMaxValue,'wchCrntPMOPTMaxTimeStamp':wchCrntPMOPTMaxTimeStamp,'wchCrntPMOPTMaxValidity':wchCrntPMOPTMaxValidity,'wchCrntPMOPTMaxInitialize':wchCrntPMOPTMaxInitialize,'wchHistPMTable':wchHistPMTable,'wchHistPMEntry':wchHistPMEntry,_B2:wchHistPMCpTypeIdx,_B3:wchHistPMShelfIdx,_B4:wchHistPMSlotIdx,_B5:wchHistPMPortTypeIdx,_B6:wchHistPMPortIdx,_B7:wchHistPMIdx,_B8:wchHistPMIntervalTypeIdx,_B9:wchHistPMIntervalIdx,'wchHistPMOPRValue':wchHistPMOPRValue,'wchHistPMOPRTimeStamp':wchHistPMOPRTimeStamp,'wchHistPMOPRValidity':wchHistPMOPRValidity,'wchHistPMOPRMinValue':wchHistPMOPRMinValue,'wchHistPMOPRMinTimeStamp':wchHistPMOPRMinTimeStamp,'wchHistPMOPRMinValidity':wchHistPMOPRMinValidity,'wchHistPMOPRMinInitialize':wchHistPMOPRMinInitialize,'wchHistPMOPRMaxValue':wchHistPMOPRMaxValue,'wchHistPMOPRMaxTimeStamp':wchHistPMOPRMaxTimeStamp,'wchHistPMOPRMaxValidity':wchHistPMOPRMaxValidity,'wchHistPMOPRMaxInitialize':wchHistPMOPRMaxInitialize,'wchHistPMOPTValue':wchHistPMOPTValue,'wchHistPMOPTTimeStamp':wchHistPMOPTTimeStamp,'wchHistPMOPTValidity':wchHistPMOPTValidity,'wchHistPMOPTMinValue':wchHistPMOPTMinValue,'wchHistPMOPTMinTimeStamp':wchHistPMOPTMinTimeStamp,'wchHistPMOPTMinValidity':wchHistPMOPTMinValidity,'wchHistPMOPTMinInitialize':wchHistPMOPTMinInitialize,'wchHistPMOPTMaxValue':wchHistPMOPTMaxValue,'wchHistPMOPTMaxTimeStamp':wchHistPMOPTMaxTimeStamp,'wchHistPMOPTMaxValidity':wchHistPMOPTMaxValidity,'wchHistPMOPTMaxInitialize':wchHistPMOPTMaxInitialize,'olOSCEvtNotifications':olOSCEvtNotifications,'olOSCStatusChangeEvt':olOSCStatusChangeEvt,'olOSCTcaEvt':olOSCTcaEvt,'olPortEvtNotifications':olPortEvtNotifications,'olPortStatusChangeEvt':olPortStatusChangeEvt,'wdmEvtNotifications':wdmEvtNotifications,'wdmStatusChangeEvt':wdmStatusChangeEvt,'wchEvtNotifications':wchEvtNotifications,'wchStatusChangeEvt':wchStatusChangeEvt,'olOSCCondNotifications':olOSCCondNotifications,'olOSCLossOfLightRxCond':olOSCLossOfLightRxCond,'olOSCLossOfLightRxClear':olOSCLossOfLightRxClear,'olOSCLossOfFrameCond':olOSCLossOfFrameCond,'olOSCLossOfFrameClear':olOSCLossOfFrameClear,'olOSCLossOfLightTxCond':olOSCLossOfLightTxCond,'olOSCLossOfLightTxClear':olOSCLossOfLightTxClear,'olOSCFarEndIdMismatchCond':olOSCFarEndIdMismatchCond,'olOSCFarEndIdMismatchClear':olOSCFarEndIdMismatchClear,'olOSCFarEndNodeCnfgInconsistentCond':olOSCFarEndNodeCnfgInconsistentCond,'olOSCFarEndNodeCnfgInconsistentClear':olOSCFarEndNodeCnfgInconsistentClear,'olOSCSpanContCommCond':olOSCSpanContCommCond,'olOSCSpanContCommClear':olOSCSpanContCommClear,'olOSCEqlzContCommCond':olOSCEqlzContCommCond,'olOSCEqlzContCommClear':olOSCEqlzContCommClear,'olOSCOpticalBackReflOutOfSpecCond':olOSCOpticalBackReflOutOfSpecCond,'olOSCOpticalBackReflOutOfSpecClear':olOSCOpticalBackReflOutOfSpecClear,'olOSCOpticalBackReflHighThCond':olOSCOpticalBackReflHighThCond,'olOSCOpticalBackReflHighThClear':olOSCOpticalBackReflHighThClear,'olPortCondNotifications':olPortCondNotifications,'olPortPowerOutOfSpecRxCond':olPortPowerOutOfSpecRxCond,'olPortPowerOutOfSpecRxClear':olPortPowerOutOfSpecRxClear,'olPortLossOfLightRxCond':olPortLossOfLightRxCond,'olPortLossOfLightRxClear':olPortLossOfLightRxClear,'olPortLossRxOutOfSpecCond':olPortLossRxOutOfSpecCond,'olPortLossRxOutOfSpecClear':olPortLossRxOutOfSpecClear,'olPortLossRxHighThCond':olPortLossRxHighThCond,'olPortLossRxHighThClear':olPortLossRxHighThClear,'olPortAPSDCond':olPortAPSDCond,'olPortAPSDClear':olPortAPSDClear,'olPortPayloadMissingIndCond':olPortPayloadMissingIndCond,'olPortPayloadMissingIndClear':olPortPayloadMissingIndClear,'olPortBackwardDefectIndCond':olPortBackwardDefectIndCond,'olPortBackwardDefectIndClear':olPortBackwardDefectIndClear,'olPortChannelCountDeficiencyCond':olPortChannelCountDeficiencyCond,'olPortChannelCountDeficiencyClear':olPortChannelCountDeficiencyClear,'olPortConnectionMismatchCond':olPortConnectionMismatchCond,'olPortConnectionMismatchClear':olPortConnectionMismatchClear,'olPortConnectionValidationTimeoutCond':olPortConnectionValidationTimeoutCond,'olPortConnectionValidationTimeoutClear':olPortConnectionValidationTimeoutClear,'wdmCondNotifications':wdmCondNotifications,'wdmInvalidPreAmpOperCnfgCond':wdmInvalidPreAmpOperCnfgCond,'wdmInvalidPreAmpOperCnfgClear':wdmInvalidPreAmpOperCnfgClear,'wdmInvalidMidAmpOperCnfgCond':wdmInvalidMidAmpOperCnfgCond,'wdmInvalidMidAmpOperCnfgClear':wdmInvalidMidAmpOperCnfgClear,'wdmInvalidBoostAmpOperCnfgCond':wdmInvalidBoostAmpOperCnfgCond,'wdmInvalidBoostAmpOperCnfgClear':wdmInvalidBoostAmpOperCnfgClear,'wchCondNotifications':wchCondNotifications,'wchPowerOutOfSpecRxCond':wchPowerOutOfSpecRxCond,'wchPowerOutOfSpecRxClear':wchPowerOutOfSpecRxClear,'wchLossOfLightRxCond':wchLossOfLightRxCond,'wchLossOfLightRxClear':wchLossOfLightRxClear,'wchPowerOutOfSpecTxCond':wchPowerOutOfSpecTxCond,'wchPowerOutOfSpecTxClear':wchPowerOutOfSpecTxClear,'wchLossOfLightTxCond':wchLossOfLightTxCond,'wchLossOfLightTxClear':wchLossOfLightTxClear,'wchUnequippedCond':wchUnequippedCond,'wchUnequippedClear':wchUnequippedClear,'wchAISCond':wchAISCond,'wchAISClear':wchAISClear,'wchPowerOutOfSpecRxHighCond':wchPowerOutOfSpecRxHighCond,'wchPowerOutOfSpecRxHighClear':wchPowerOutOfSpecRxHighClear,'wchPowerOutOfSpecRxLowCond':wchPowerOutOfSpecRxLowCond,'wchPowerOutOfSpecRxLowClear':wchPowerOutOfSpecRxLowClear,'wchPowerRxHighFailCond':wchPowerRxHighFailCond,'wchPowerRxHighFailClear':wchPowerRxHighFailClear})