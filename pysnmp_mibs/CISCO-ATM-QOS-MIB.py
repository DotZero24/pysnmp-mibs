_A6='ciscoAtmQosVcQueuingGroup'
_A5='ciscoAtmQosVpcGroup'
_A4='ciscoAtmQosVccGroup'
_A3='caqQueuingParamsClassMrkProb'
_A2='caqQueuingParamsClassMaxThre'
_A1='caqQueuingParamsClassMinThre'
_A0='caqQueuingParamsClassTailDrp'
_z='caqQueuingParamsClassRandDrp'
_y='caqQueuingParamsMeanQDepth'
_x='caqVpcParamsAvailBw'
_w='caqVpcParamsMbs'
_v='caqVpcParamsScr'
_u='caqVpcParamsVcdF4Ete'
_t='caqVpcParamsVcdF4Seg'
_s='caqVpcParamsCesVcCount'
_r='caqVpcParamsDataVcCount'
_q='caqVpcParamsCesRate'
_p='caqVpcParamsPeakRate'
_o='caqVpcParamsVpState'
_n='caqVccParamsAdtf'
_m='caqVccParamsInvCdf'
_l='caqVccParamsInvTrm'
_k='caqVccParamsNrm'
_j='caqVccParamsFrtt'
_i='caqVccParamsTbe'
_h='caqVccParamsIcr'
_g='caqVccParamsCdvt'
_f='caqVccParamsCdv'
_e='caqVccParamsRfl'
_d='caqVccParamsInvRif'
_c='caqVccParamsInvRdf'
_b='caqVccParamsMcrOut'
_a='caqVccParamsMcrIn'
_Z='caqVccParamsInheritLevel'
_Y='caqVccParamsBcsOut01'
_X='caqVccParamsBcsOut0'
_W='caqVccParamsBcsIn01'
_V='caqVccParamsBcsIn0'
_U='caqVccParamsScrOut01'
_T='caqVccParamsScrOut0'
_S='caqVccParamsScrIn01'
_R='caqVccParamsScrIn0'
_Q='caqVccParamsPcrOut01'
_P='caqVccParamsPcrOut0'
_O='caqVccParamsPcrIn01'
_N='caqVccParamsPcrIn0'
_M='caqVccParamsType'
_L='caqQueuingParamsClassIndex'
_K='atmVplVpi'
_J='atmVclVpi'
_I='atmVclVci'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='ATM-MIB'
_D='read-only'
_C='read-write'
_B='CISCO-ATM-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmServiceCategory,=mibBuilder.importSymbols('ATM-FORUM-TC-MIB','AtmServiceCategory')
atmVclVci,atmVclVpi,atmVplVpi=mibBuilder.importSymbols(_E,_I,_J,_K)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAtmQosMIB=ModuleIdentity((1,3,6,1,4,1,9,9,279))
if mibBuilder.loadTexts:ciscoAtmQosMIB.setRevisions(('2002-06-10 00:00',))
class VcParamConfigLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('configDefault',1),('configVcDirect',2),('configVcClass',3),('configVcClassSubInterface',4),('configVcClassInterface',5)))
class VpState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpStateInactive',1),('vpStateActive',2)))
_CiscoAtmQosMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAtmQosMIBNotifs=_CiscoAtmQosMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,279,0))
_CiscoAtmQosMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmQosMIBObjects=_CiscoAtmQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,279,1))
_CaqVccParams_ObjectIdentity=ObjectIdentity
caqVccParams=_CaqVccParams_ObjectIdentity((1,3,6,1,4,1,9,9,279,1,1))
_CaqVccParamsTable_Object=MibTable
caqVccParamsTable=_CaqVccParamsTable_Object((1,3,6,1,4,1,9,9,279,1,1,1))
if mibBuilder.loadTexts:caqVccParamsTable.setStatus(_A)
_CaqVccParamsEntry_Object=MibTableRow
caqVccParamsEntry=_CaqVccParamsEntry_Object((1,3,6,1,4,1,9,9,279,1,1,1,1))
caqVccParamsEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:caqVccParamsEntry.setStatus(_A)
_CaqVccParamsType_Type=AtmServiceCategory
_CaqVccParamsType_Object=MibTableColumn
caqVccParamsType=_CaqVccParamsType_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,1),_CaqVccParamsType_Type())
caqVccParamsType.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsType.setStatus(_A)
_CaqVccParamsPcrIn0_Type=Unsigned32
_CaqVccParamsPcrIn0_Object=MibTableColumn
caqVccParamsPcrIn0=_CaqVccParamsPcrIn0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,2),_CaqVccParamsPcrIn0_Type())
caqVccParamsPcrIn0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsPcrIn0.setStatus(_A)
_CaqVccParamsPcrIn01_Type=Unsigned32
_CaqVccParamsPcrIn01_Object=MibTableColumn
caqVccParamsPcrIn01=_CaqVccParamsPcrIn01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,3),_CaqVccParamsPcrIn01_Type())
caqVccParamsPcrIn01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsPcrIn01.setStatus(_A)
_CaqVccParamsPcrOut0_Type=Unsigned32
_CaqVccParamsPcrOut0_Object=MibTableColumn
caqVccParamsPcrOut0=_CaqVccParamsPcrOut0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,4),_CaqVccParamsPcrOut0_Type())
caqVccParamsPcrOut0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsPcrOut0.setStatus(_A)
_CaqVccParamsPcrOut01_Type=Unsigned32
_CaqVccParamsPcrOut01_Object=MibTableColumn
caqVccParamsPcrOut01=_CaqVccParamsPcrOut01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,5),_CaqVccParamsPcrOut01_Type())
caqVccParamsPcrOut01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsPcrOut01.setStatus(_A)
_CaqVccParamsScrIn0_Type=Unsigned32
_CaqVccParamsScrIn0_Object=MibTableColumn
caqVccParamsScrIn0=_CaqVccParamsScrIn0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,6),_CaqVccParamsScrIn0_Type())
caqVccParamsScrIn0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsScrIn0.setStatus(_A)
_CaqVccParamsScrIn01_Type=Unsigned32
_CaqVccParamsScrIn01_Object=MibTableColumn
caqVccParamsScrIn01=_CaqVccParamsScrIn01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,7),_CaqVccParamsScrIn01_Type())
caqVccParamsScrIn01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsScrIn01.setStatus(_A)
_CaqVccParamsScrOut0_Type=Unsigned32
_CaqVccParamsScrOut0_Object=MibTableColumn
caqVccParamsScrOut0=_CaqVccParamsScrOut0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,8),_CaqVccParamsScrOut0_Type())
caqVccParamsScrOut0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsScrOut0.setStatus(_A)
_CaqVccParamsScrOut01_Type=Unsigned32
_CaqVccParamsScrOut01_Object=MibTableColumn
caqVccParamsScrOut01=_CaqVccParamsScrOut01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,9),_CaqVccParamsScrOut01_Type())
caqVccParamsScrOut01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsScrOut01.setStatus(_A)
_CaqVccParamsBcsIn0_Type=Unsigned32
_CaqVccParamsBcsIn0_Object=MibTableColumn
caqVccParamsBcsIn0=_CaqVccParamsBcsIn0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,10),_CaqVccParamsBcsIn0_Type())
caqVccParamsBcsIn0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsBcsIn0.setStatus(_A)
_CaqVccParamsBcsIn01_Type=Unsigned32
_CaqVccParamsBcsIn01_Object=MibTableColumn
caqVccParamsBcsIn01=_CaqVccParamsBcsIn01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,11),_CaqVccParamsBcsIn01_Type())
caqVccParamsBcsIn01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsBcsIn01.setStatus(_A)
_CaqVccParamsBcsOut0_Type=Unsigned32
_CaqVccParamsBcsOut0_Object=MibTableColumn
caqVccParamsBcsOut0=_CaqVccParamsBcsOut0_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,12),_CaqVccParamsBcsOut0_Type())
caqVccParamsBcsOut0.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsBcsOut0.setStatus(_A)
_CaqVccParamsBcsOut01_Type=Unsigned32
_CaqVccParamsBcsOut01_Object=MibTableColumn
caqVccParamsBcsOut01=_CaqVccParamsBcsOut01_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,13),_CaqVccParamsBcsOut01_Type())
caqVccParamsBcsOut01.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsBcsOut01.setStatus(_A)
_CaqVccParamsInheritLevel_Type=VcParamConfigLocation
_CaqVccParamsInheritLevel_Object=MibTableColumn
caqVccParamsInheritLevel=_CaqVccParamsInheritLevel_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,14),_CaqVccParamsInheritLevel_Type())
caqVccParamsInheritLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVccParamsInheritLevel.setStatus(_A)
_CaqVccParamsMcrIn_Type=Unsigned32
_CaqVccParamsMcrIn_Object=MibTableColumn
caqVccParamsMcrIn=_CaqVccParamsMcrIn_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,15),_CaqVccParamsMcrIn_Type())
caqVccParamsMcrIn.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsMcrIn.setStatus(_A)
_CaqVccParamsMcrOut_Type=Unsigned32
_CaqVccParamsMcrOut_Object=MibTableColumn
caqVccParamsMcrOut=_CaqVccParamsMcrOut_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,16),_CaqVccParamsMcrOut_Type())
caqVccParamsMcrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsMcrOut.setStatus(_A)
_CaqVccParamsInvRdf_Type=Unsigned32
_CaqVccParamsInvRdf_Object=MibTableColumn
caqVccParamsInvRdf=_CaqVccParamsInvRdf_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,17),_CaqVccParamsInvRdf_Type())
caqVccParamsInvRdf.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsInvRdf.setStatus(_A)
_CaqVccParamsInvRif_Type=Unsigned32
_CaqVccParamsInvRif_Object=MibTableColumn
caqVccParamsInvRif=_CaqVccParamsInvRif_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,18),_CaqVccParamsInvRif_Type())
caqVccParamsInvRif.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsInvRif.setStatus(_A)
_CaqVccParamsRfl_Type=VcParamConfigLocation
_CaqVccParamsRfl_Object=MibTableColumn
caqVccParamsRfl=_CaqVccParamsRfl_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,19),_CaqVccParamsRfl_Type())
caqVccParamsRfl.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVccParamsRfl.setStatus(_A)
_CaqVccParamsCdv_Type=Unsigned32
_CaqVccParamsCdv_Object=MibTableColumn
caqVccParamsCdv=_CaqVccParamsCdv_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,20),_CaqVccParamsCdv_Type())
caqVccParamsCdv.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVccParamsCdv.setStatus(_A)
_CaqVccParamsCdvt_Type=Unsigned32
_CaqVccParamsCdvt_Object=MibTableColumn
caqVccParamsCdvt=_CaqVccParamsCdvt_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,21),_CaqVccParamsCdvt_Type())
caqVccParamsCdvt.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsCdvt.setStatus(_A)
_CaqVccParamsIcr_Type=Unsigned32
_CaqVccParamsIcr_Object=MibTableColumn
caqVccParamsIcr=_CaqVccParamsIcr_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,22),_CaqVccParamsIcr_Type())
caqVccParamsIcr.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsIcr.setStatus(_A)
_CaqVccParamsTbe_Type=Unsigned32
_CaqVccParamsTbe_Object=MibTableColumn
caqVccParamsTbe=_CaqVccParamsTbe_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,23),_CaqVccParamsTbe_Type())
caqVccParamsTbe.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsTbe.setStatus(_A)
_CaqVccParamsFrtt_Type=Unsigned32
_CaqVccParamsFrtt_Object=MibTableColumn
caqVccParamsFrtt=_CaqVccParamsFrtt_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,24),_CaqVccParamsFrtt_Type())
caqVccParamsFrtt.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsFrtt.setStatus(_A)
_CaqVccParamsNrm_Type=Unsigned32
_CaqVccParamsNrm_Object=MibTableColumn
caqVccParamsNrm=_CaqVccParamsNrm_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,25),_CaqVccParamsNrm_Type())
caqVccParamsNrm.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsNrm.setStatus(_A)
_CaqVccParamsInvTrm_Type=Unsigned32
_CaqVccParamsInvTrm_Object=MibTableColumn
caqVccParamsInvTrm=_CaqVccParamsInvTrm_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,26),_CaqVccParamsInvTrm_Type())
caqVccParamsInvTrm.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsInvTrm.setStatus(_A)
_CaqVccParamsInvCdf_Type=Unsigned32
_CaqVccParamsInvCdf_Object=MibTableColumn
caqVccParamsInvCdf=_CaqVccParamsInvCdf_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,27),_CaqVccParamsInvCdf_Type())
caqVccParamsInvCdf.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsInvCdf.setStatus(_A)
_CaqVccParamsAdtf_Type=Unsigned32
_CaqVccParamsAdtf_Object=MibTableColumn
caqVccParamsAdtf=_CaqVccParamsAdtf_Object((1,3,6,1,4,1,9,9,279,1,1,1,1,28),_CaqVccParamsAdtf_Type())
caqVccParamsAdtf.setMaxAccess(_C)
if mibBuilder.loadTexts:caqVccParamsAdtf.setStatus(_A)
_CaqVpcParams_ObjectIdentity=ObjectIdentity
caqVpcParams=_CaqVpcParams_ObjectIdentity((1,3,6,1,4,1,9,9,279,1,2))
_CaqVpcParamsTable_Object=MibTable
caqVpcParamsTable=_CaqVpcParamsTable_Object((1,3,6,1,4,1,9,9,279,1,2,1))
if mibBuilder.loadTexts:caqVpcParamsTable.setStatus(_A)
_CaqVpcParamsEntry_Object=MibTableRow
caqVpcParamsEntry=_CaqVpcParamsEntry_Object((1,3,6,1,4,1,9,9,279,1,2,1,1))
caqVpcParamsEntry.setIndexNames((0,_G,_H),(0,_E,_K))
if mibBuilder.loadTexts:caqVpcParamsEntry.setStatus(_A)
_CaqVpcParamsVpState_Type=VpState
_CaqVpcParamsVpState_Object=MibTableColumn
caqVpcParamsVpState=_CaqVpcParamsVpState_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,1),_CaqVpcParamsVpState_Type())
caqVpcParamsVpState.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsVpState.setStatus(_A)
_CaqVpcParamsPeakRate_Type=Unsigned32
_CaqVpcParamsPeakRate_Object=MibTableColumn
caqVpcParamsPeakRate=_CaqVpcParamsPeakRate_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,2),_CaqVpcParamsPeakRate_Type())
caqVpcParamsPeakRate.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsPeakRate.setStatus(_A)
_CaqVpcParamsCesRate_Type=Unsigned32
_CaqVpcParamsCesRate_Object=MibTableColumn
caqVpcParamsCesRate=_CaqVpcParamsCesRate_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,3),_CaqVpcParamsCesRate_Type())
caqVpcParamsCesRate.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsCesRate.setStatus(_A)
class _CaqVpcParamsDataVcCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CaqVpcParamsDataVcCount_Type.__name__=_F
_CaqVpcParamsDataVcCount_Object=MibTableColumn
caqVpcParamsDataVcCount=_CaqVpcParamsDataVcCount_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,4),_CaqVpcParamsDataVcCount_Type())
caqVpcParamsDataVcCount.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsDataVcCount.setStatus(_A)
class _CaqVpcParamsCesVcCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CaqVpcParamsCesVcCount_Type.__name__=_F
_CaqVpcParamsCesVcCount_Object=MibTableColumn
caqVpcParamsCesVcCount=_CaqVpcParamsCesVcCount_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,5),_CaqVpcParamsCesVcCount_Type())
caqVpcParamsCesVcCount.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsCesVcCount.setStatus(_A)
class _CaqVpcParamsVcdF4Seg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CaqVpcParamsVcdF4Seg_Type.__name__=_F
_CaqVpcParamsVcdF4Seg_Object=MibTableColumn
caqVpcParamsVcdF4Seg=_CaqVpcParamsVcdF4Seg_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,6),_CaqVpcParamsVcdF4Seg_Type())
caqVpcParamsVcdF4Seg.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsVcdF4Seg.setStatus(_A)
class _CaqVpcParamsVcdF4Ete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CaqVpcParamsVcdF4Ete_Type.__name__=_F
_CaqVpcParamsVcdF4Ete_Object=MibTableColumn
caqVpcParamsVcdF4Ete=_CaqVpcParamsVcdF4Ete_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,7),_CaqVpcParamsVcdF4Ete_Type())
caqVpcParamsVcdF4Ete.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsVcdF4Ete.setStatus(_A)
_CaqVpcParamsScr_Type=Unsigned32
_CaqVpcParamsScr_Object=MibTableColumn
caqVpcParamsScr=_CaqVpcParamsScr_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,8),_CaqVpcParamsScr_Type())
caqVpcParamsScr.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsScr.setStatus(_A)
_CaqVpcParamsMbs_Type=Unsigned32
_CaqVpcParamsMbs_Object=MibTableColumn
caqVpcParamsMbs=_CaqVpcParamsMbs_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,9),_CaqVpcParamsMbs_Type())
caqVpcParamsMbs.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsMbs.setStatus(_A)
_CaqVpcParamsAvailBw_Type=Unsigned32
_CaqVpcParamsAvailBw_Object=MibTableColumn
caqVpcParamsAvailBw=_CaqVpcParamsAvailBw_Object((1,3,6,1,4,1,9,9,279,1,2,1,1,10),_CaqVpcParamsAvailBw_Type())
caqVpcParamsAvailBw.setMaxAccess(_D)
if mibBuilder.loadTexts:caqVpcParamsAvailBw.setStatus(_A)
_CaqQueuingParams_ObjectIdentity=ObjectIdentity
caqQueuingParams=_CaqQueuingParams_ObjectIdentity((1,3,6,1,4,1,9,9,279,1,3))
_CaqQueuingParamsTable_Object=MibTable
caqQueuingParamsTable=_CaqQueuingParamsTable_Object((1,3,6,1,4,1,9,9,279,1,3,1))
if mibBuilder.loadTexts:caqQueuingParamsTable.setStatus(_A)
_CaqQueuingParamsEntry_Object=MibTableRow
caqQueuingParamsEntry=_CaqQueuingParamsEntry_Object((1,3,6,1,4,1,9,9,279,1,3,1,1))
caqQueuingParamsEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:caqQueuingParamsEntry.setStatus(_A)
_CaqQueuingParamsMeanQDepth_Type=Unsigned32
_CaqQueuingParamsMeanQDepth_Object=MibTableColumn
caqQueuingParamsMeanQDepth=_CaqQueuingParamsMeanQDepth_Object((1,3,6,1,4,1,9,9,279,1,3,1,1,1),_CaqQueuingParamsMeanQDepth_Type())
caqQueuingParamsMeanQDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsMeanQDepth.setStatus(_A)
_CaqQueuingParamsClassTable_Object=MibTable
caqQueuingParamsClassTable=_CaqQueuingParamsClassTable_Object((1,3,6,1,4,1,9,9,279,1,3,2))
if mibBuilder.loadTexts:caqQueuingParamsClassTable.setStatus(_A)
_CaqQueuingParamsClassEntry_Object=MibTableRow
caqQueuingParamsClassEntry=_CaqQueuingParamsClassEntry_Object((1,3,6,1,4,1,9,9,279,1,3,2,1))
caqQueuingParamsClassEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_I),(0,_B,_L))
if mibBuilder.loadTexts:caqQueuingParamsClassEntry.setStatus(_A)
class _CaqQueuingParamsClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CaqQueuingParamsClassIndex_Type.__name__=_F
_CaqQueuingParamsClassIndex_Object=MibTableColumn
caqQueuingParamsClassIndex=_CaqQueuingParamsClassIndex_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,1),_CaqQueuingParamsClassIndex_Type())
caqQueuingParamsClassIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:caqQueuingParamsClassIndex.setStatus(_A)
_CaqQueuingParamsClassRandDrp_Type=Unsigned32
_CaqQueuingParamsClassRandDrp_Object=MibTableColumn
caqQueuingParamsClassRandDrp=_CaqQueuingParamsClassRandDrp_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,2),_CaqQueuingParamsClassRandDrp_Type())
caqQueuingParamsClassRandDrp.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsClassRandDrp.setStatus(_A)
_CaqQueuingParamsClassTailDrp_Type=Unsigned32
_CaqQueuingParamsClassTailDrp_Object=MibTableColumn
caqQueuingParamsClassTailDrp=_CaqQueuingParamsClassTailDrp_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,3),_CaqQueuingParamsClassTailDrp_Type())
caqQueuingParamsClassTailDrp.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsClassTailDrp.setStatus(_A)
_CaqQueuingParamsClassMinThre_Type=Unsigned32
_CaqQueuingParamsClassMinThre_Object=MibTableColumn
caqQueuingParamsClassMinThre=_CaqQueuingParamsClassMinThre_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,4),_CaqQueuingParamsClassMinThre_Type())
caqQueuingParamsClassMinThre.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsClassMinThre.setStatus(_A)
_CaqQueuingParamsClassMaxThre_Type=Unsigned32
_CaqQueuingParamsClassMaxThre_Object=MibTableColumn
caqQueuingParamsClassMaxThre=_CaqQueuingParamsClassMaxThre_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,5),_CaqQueuingParamsClassMaxThre_Type())
caqQueuingParamsClassMaxThre.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsClassMaxThre.setStatus(_A)
_CaqQueuingParamsClassMrkProb_Type=Unsigned32
_CaqQueuingParamsClassMrkProb_Object=MibTableColumn
caqQueuingParamsClassMrkProb=_CaqQueuingParamsClassMrkProb_Object((1,3,6,1,4,1,9,9,279,1,3,2,1,6),_CaqQueuingParamsClassMrkProb_Type())
caqQueuingParamsClassMrkProb.setMaxAccess(_D)
if mibBuilder.loadTexts:caqQueuingParamsClassMrkProb.setStatus(_A)
_CiscoAtmQosMIBConform_ObjectIdentity=ObjectIdentity
ciscoAtmQosMIBConform=_CiscoAtmQosMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,279,2))
_CiscoAtmQosMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmQosMIBCompliances=_CiscoAtmQosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,279,2,1))
_CiscoAtmQosMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmQosMIBGroups=_CiscoAtmQosMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,279,2,2))
ciscoAtmQosVccGroup=ObjectGroup((1,3,6,1,4,1,9,9,279,2,2,1))
ciscoAtmQosVccGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoAtmQosVccGroup.setStatus(_A)
ciscoAtmQosVccAddon1Group=ObjectGroup((1,3,6,1,4,1,9,9,279,2,2,2))
ciscoAtmQosVccAddon1Group.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoAtmQosVccAddon1Group.setStatus(_A)
ciscoAtmQosVpcGroup=ObjectGroup((1,3,6,1,4,1,9,9,279,2,2,3))
ciscoAtmQosVpcGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ciscoAtmQosVpcGroup.setStatus(_A)
ciscoAtmQosVpcAddon1Group=ObjectGroup((1,3,6,1,4,1,9,9,279,2,2,4))
ciscoAtmQosVpcAddon1Group.setObjects((_B,_x))
if mibBuilder.loadTexts:ciscoAtmQosVpcAddon1Group.setStatus(_A)
ciscoAtmQosVcQueuingGroup=ObjectGroup((1,3,6,1,4,1,9,9,279,2,2,5))
ciscoAtmQosVcQueuingGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoAtmQosVcQueuingGroup.setStatus(_A)
ciscoAtmQosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,279,2,1,1))
ciscoAtmQosMIBCompliance.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoAtmQosMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VcParamConfigLocation':VcParamConfigLocation,'VpState':VpState,'ciscoAtmQosMIB':ciscoAtmQosMIB,'ciscoAtmQosMIBNotifs':ciscoAtmQosMIBNotifs,'ciscoAtmQosMIBObjects':ciscoAtmQosMIBObjects,'caqVccParams':caqVccParams,'caqVccParamsTable':caqVccParamsTable,'caqVccParamsEntry':caqVccParamsEntry,_M:caqVccParamsType,_N:caqVccParamsPcrIn0,_O:caqVccParamsPcrIn01,_P:caqVccParamsPcrOut0,_Q:caqVccParamsPcrOut01,_R:caqVccParamsScrIn0,_S:caqVccParamsScrIn01,_T:caqVccParamsScrOut0,_U:caqVccParamsScrOut01,_V:caqVccParamsBcsIn0,_W:caqVccParamsBcsIn01,_X:caqVccParamsBcsOut0,_Y:caqVccParamsBcsOut01,_Z:caqVccParamsInheritLevel,_a:caqVccParamsMcrIn,_b:caqVccParamsMcrOut,_c:caqVccParamsInvRdf,_d:caqVccParamsInvRif,_e:caqVccParamsRfl,_f:caqVccParamsCdv,_g:caqVccParamsCdvt,_h:caqVccParamsIcr,_i:caqVccParamsTbe,_j:caqVccParamsFrtt,_k:caqVccParamsNrm,_l:caqVccParamsInvTrm,_m:caqVccParamsInvCdf,_n:caqVccParamsAdtf,'caqVpcParams':caqVpcParams,'caqVpcParamsTable':caqVpcParamsTable,'caqVpcParamsEntry':caqVpcParamsEntry,_o:caqVpcParamsVpState,_p:caqVpcParamsPeakRate,_q:caqVpcParamsCesRate,_r:caqVpcParamsDataVcCount,_s:caqVpcParamsCesVcCount,_t:caqVpcParamsVcdF4Seg,_u:caqVpcParamsVcdF4Ete,_v:caqVpcParamsScr,_w:caqVpcParamsMbs,_x:caqVpcParamsAvailBw,'caqQueuingParams':caqQueuingParams,'caqQueuingParamsTable':caqQueuingParamsTable,'caqQueuingParamsEntry':caqQueuingParamsEntry,_y:caqQueuingParamsMeanQDepth,'caqQueuingParamsClassTable':caqQueuingParamsClassTable,'caqQueuingParamsClassEntry':caqQueuingParamsClassEntry,_L:caqQueuingParamsClassIndex,_z:caqQueuingParamsClassRandDrp,_A0:caqQueuingParamsClassTailDrp,_A1:caqQueuingParamsClassMinThre,_A2:caqQueuingParamsClassMaxThre,_A3:caqQueuingParamsClassMrkProb,'ciscoAtmQosMIBConform':ciscoAtmQosMIBConform,'ciscoAtmQosMIBCompliances':ciscoAtmQosMIBCompliances,'ciscoAtmQosMIBCompliance':ciscoAtmQosMIBCompliance,'ciscoAtmQosMIBGroups':ciscoAtmQosMIBGroups,_A4:ciscoAtmQosVccGroup,'ciscoAtmQosVccAddon1Group':ciscoAtmQosVccAddon1Group,_A5:ciscoAtmQosVpcGroup,'ciscoAtmQosVpcAddon1Group':ciscoAtmQosVpcAddon1Group,_A6:ciscoAtmQosVcQueuingGroup})