_t='ciscoVismSvcAal2CidGrp'
_s='ciscoVismSvcTrfScalingGrp'
_r='ciscoVismSvcAtmQosGroup'
_q='ciscoVismSvcCounterGroup'
_p='vismSvcAal2CidNumber'
_o='vismSvcTrfScalingFactor'
_n='vismSvcAtmQosClr'
_m='vismSvcAtmQosCtd'
_l='vismSvcAtmQosCdv'
_k='vismSvcResyncExpiries'
_j='vismSvcRestartExpiries'
_i='vismSvcConnAckExpiries'
_h='vismSvcConnExpiries'
_g='vismSvcReleasExpiries'
_f='vismSvcCallProcExpiries'
_e='vismSvcRxBulkResyncs'
_d='vismSvcTxBulkResyncs'
_c='vismSvcRxResyncEndAcks'
_b='vismSvcRxResyncEnds'
_a='vismSvcTxResyncEndAcks'
_Z='vismSvcTxResyncEnds'
_Y='vismSvcRxResyncStrtAcks'
_X='vismSvcRxResyncStrts'
_W='vismSvcTxResyncStrtAcks'
_V='vismSvcTxResyncStrts'
_U='vismSvcRxRestartAcks'
_T='vismSvcRxRestarts'
_S='vismSvcTxRestartAcks'
_R='vismSvcTxRestarts'
_Q='vismSvcRxReleaseCompls'
_P='vismSvcRxReleases'
_O='vismSvcTxReleaseCompls'
_N='vismSvcTxReleases'
_M='vismSvcRxConnAcks'
_L='vismSvcRxConns'
_K='vismSvcTxConnAcks'
_J='vismSvcTxConns'
_I='vismSvcRxCallProcs'
_H='vismSvcTxCallProcs'
_G='vismSvcRxSetups'
_F='vismSvcTxSetups'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-VISM-SVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVismSvcMIB=ModuleIdentity((1,3,6,1,4,1,351,150,90))
if mibBuilder.loadTexts:ciscoVismSvcMIB.setRevisions(('2003-10-09 00:00',))
_VismSvcGrp_ObjectIdentity=ObjectIdentity
vismSvcGrp=_VismSvcGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,10))
_VismSvcTxSetups_Type=Counter32
_VismSvcTxSetups_Object=MibScalar
vismSvcTxSetups=_VismSvcTxSetups_Object((1,3,6,1,4,1,351,110,5,5,10,1),_VismSvcTxSetups_Type())
vismSvcTxSetups.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxSetups.setStatus(_A)
_VismSvcRxSetups_Type=Counter32
_VismSvcRxSetups_Object=MibScalar
vismSvcRxSetups=_VismSvcRxSetups_Object((1,3,6,1,4,1,351,110,5,5,10,2),_VismSvcRxSetups_Type())
vismSvcRxSetups.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxSetups.setStatus(_A)
_VismSvcTxCallProcs_Type=Counter32
_VismSvcTxCallProcs_Object=MibScalar
vismSvcTxCallProcs=_VismSvcTxCallProcs_Object((1,3,6,1,4,1,351,110,5,5,10,3),_VismSvcTxCallProcs_Type())
vismSvcTxCallProcs.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxCallProcs.setStatus(_A)
_VismSvcRxCallProcs_Type=Counter32
_VismSvcRxCallProcs_Object=MibScalar
vismSvcRxCallProcs=_VismSvcRxCallProcs_Object((1,3,6,1,4,1,351,110,5,5,10,4),_VismSvcRxCallProcs_Type())
vismSvcRxCallProcs.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxCallProcs.setStatus(_A)
_VismSvcTxConns_Type=Counter32
_VismSvcTxConns_Object=MibScalar
vismSvcTxConns=_VismSvcTxConns_Object((1,3,6,1,4,1,351,110,5,5,10,5),_VismSvcTxConns_Type())
vismSvcTxConns.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxConns.setStatus(_A)
_VismSvcTxConnAcks_Type=Counter32
_VismSvcTxConnAcks_Object=MibScalar
vismSvcTxConnAcks=_VismSvcTxConnAcks_Object((1,3,6,1,4,1,351,110,5,5,10,6),_VismSvcTxConnAcks_Type())
vismSvcTxConnAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxConnAcks.setStatus(_A)
_VismSvcRxConns_Type=Counter32
_VismSvcRxConns_Object=MibScalar
vismSvcRxConns=_VismSvcRxConns_Object((1,3,6,1,4,1,351,110,5,5,10,7),_VismSvcRxConns_Type())
vismSvcRxConns.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxConns.setStatus(_A)
_VismSvcRxConnAcks_Type=Counter32
_VismSvcRxConnAcks_Object=MibScalar
vismSvcRxConnAcks=_VismSvcRxConnAcks_Object((1,3,6,1,4,1,351,110,5,5,10,8),_VismSvcRxConnAcks_Type())
vismSvcRxConnAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxConnAcks.setStatus(_A)
_VismSvcTxReleases_Type=Counter32
_VismSvcTxReleases_Object=MibScalar
vismSvcTxReleases=_VismSvcTxReleases_Object((1,3,6,1,4,1,351,110,5,5,10,9),_VismSvcTxReleases_Type())
vismSvcTxReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxReleases.setStatus(_A)
_VismSvcTxReleaseCompls_Type=Counter32
_VismSvcTxReleaseCompls_Object=MibScalar
vismSvcTxReleaseCompls=_VismSvcTxReleaseCompls_Object((1,3,6,1,4,1,351,110,5,5,10,10),_VismSvcTxReleaseCompls_Type())
vismSvcTxReleaseCompls.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxReleaseCompls.setStatus(_A)
_VismSvcRxReleases_Type=Counter32
_VismSvcRxReleases_Object=MibScalar
vismSvcRxReleases=_VismSvcRxReleases_Object((1,3,6,1,4,1,351,110,5,5,10,11),_VismSvcRxReleases_Type())
vismSvcRxReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxReleases.setStatus(_A)
_VismSvcRxReleaseCompls_Type=Counter32
_VismSvcRxReleaseCompls_Object=MibScalar
vismSvcRxReleaseCompls=_VismSvcRxReleaseCompls_Object((1,3,6,1,4,1,351,110,5,5,10,12),_VismSvcRxReleaseCompls_Type())
vismSvcRxReleaseCompls.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxReleaseCompls.setStatus(_A)
_VismSvcTxRestarts_Type=Counter32
_VismSvcTxRestarts_Object=MibScalar
vismSvcTxRestarts=_VismSvcTxRestarts_Object((1,3,6,1,4,1,351,110,5,5,10,13),_VismSvcTxRestarts_Type())
vismSvcTxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxRestarts.setStatus(_A)
_VismSvcTxRestartAcks_Type=Counter32
_VismSvcTxRestartAcks_Object=MibScalar
vismSvcTxRestartAcks=_VismSvcTxRestartAcks_Object((1,3,6,1,4,1,351,110,5,5,10,14),_VismSvcTxRestartAcks_Type())
vismSvcTxRestartAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxRestartAcks.setStatus(_A)
_VismSvcRxRestarts_Type=Counter32
_VismSvcRxRestarts_Object=MibScalar
vismSvcRxRestarts=_VismSvcRxRestarts_Object((1,3,6,1,4,1,351,110,5,5,10,15),_VismSvcRxRestarts_Type())
vismSvcRxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxRestarts.setStatus(_A)
_VismSvcRxRestartAcks_Type=Counter32
_VismSvcRxRestartAcks_Object=MibScalar
vismSvcRxRestartAcks=_VismSvcRxRestartAcks_Object((1,3,6,1,4,1,351,110,5,5,10,16),_VismSvcRxRestartAcks_Type())
vismSvcRxRestartAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxRestartAcks.setStatus(_A)
_VismSvcTxResyncStrts_Type=Counter32
_VismSvcTxResyncStrts_Object=MibScalar
vismSvcTxResyncStrts=_VismSvcTxResyncStrts_Object((1,3,6,1,4,1,351,110,5,5,10,17),_VismSvcTxResyncStrts_Type())
vismSvcTxResyncStrts.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxResyncStrts.setStatus(_A)
_VismSvcTxResyncStrtAcks_Type=Counter32
_VismSvcTxResyncStrtAcks_Object=MibScalar
vismSvcTxResyncStrtAcks=_VismSvcTxResyncStrtAcks_Object((1,3,6,1,4,1,351,110,5,5,10,18),_VismSvcTxResyncStrtAcks_Type())
vismSvcTxResyncStrtAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxResyncStrtAcks.setStatus(_A)
_VismSvcRxResyncStrts_Type=Counter32
_VismSvcRxResyncStrts_Object=MibScalar
vismSvcRxResyncStrts=_VismSvcRxResyncStrts_Object((1,3,6,1,4,1,351,110,5,5,10,19),_VismSvcRxResyncStrts_Type())
vismSvcRxResyncStrts.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxResyncStrts.setStatus(_A)
_VismSvcRxResyncStrtAcks_Type=Counter32
_VismSvcRxResyncStrtAcks_Object=MibScalar
vismSvcRxResyncStrtAcks=_VismSvcRxResyncStrtAcks_Object((1,3,6,1,4,1,351,110,5,5,10,20),_VismSvcRxResyncStrtAcks_Type())
vismSvcRxResyncStrtAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxResyncStrtAcks.setStatus(_A)
_VismSvcTxResyncEnds_Type=Counter32
_VismSvcTxResyncEnds_Object=MibScalar
vismSvcTxResyncEnds=_VismSvcTxResyncEnds_Object((1,3,6,1,4,1,351,110,5,5,10,21),_VismSvcTxResyncEnds_Type())
vismSvcTxResyncEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxResyncEnds.setStatus(_A)
_VismSvcTxResyncEndAcks_Type=Counter32
_VismSvcTxResyncEndAcks_Object=MibScalar
vismSvcTxResyncEndAcks=_VismSvcTxResyncEndAcks_Object((1,3,6,1,4,1,351,110,5,5,10,22),_VismSvcTxResyncEndAcks_Type())
vismSvcTxResyncEndAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxResyncEndAcks.setStatus(_A)
_VismSvcRxResyncEnds_Type=Counter32
_VismSvcRxResyncEnds_Object=MibScalar
vismSvcRxResyncEnds=_VismSvcRxResyncEnds_Object((1,3,6,1,4,1,351,110,5,5,10,23),_VismSvcRxResyncEnds_Type())
vismSvcRxResyncEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxResyncEnds.setStatus(_A)
_VismSvcRxResyncEndAcks_Type=Counter32
_VismSvcRxResyncEndAcks_Object=MibScalar
vismSvcRxResyncEndAcks=_VismSvcRxResyncEndAcks_Object((1,3,6,1,4,1,351,110,5,5,10,24),_VismSvcRxResyncEndAcks_Type())
vismSvcRxResyncEndAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxResyncEndAcks.setStatus(_A)
_VismSvcTxBulkResyncs_Type=Counter32
_VismSvcTxBulkResyncs_Object=MibScalar
vismSvcTxBulkResyncs=_VismSvcTxBulkResyncs_Object((1,3,6,1,4,1,351,110,5,5,10,25),_VismSvcTxBulkResyncs_Type())
vismSvcTxBulkResyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcTxBulkResyncs.setStatus(_A)
_VismSvcRxBulkResyncs_Type=Counter32
_VismSvcRxBulkResyncs_Object=MibScalar
vismSvcRxBulkResyncs=_VismSvcRxBulkResyncs_Object((1,3,6,1,4,1,351,110,5,5,10,26),_VismSvcRxBulkResyncs_Type())
vismSvcRxBulkResyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRxBulkResyncs.setStatus(_A)
_VismSvcCallProcExpiries_Type=Counter32
_VismSvcCallProcExpiries_Object=MibScalar
vismSvcCallProcExpiries=_VismSvcCallProcExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,27),_VismSvcCallProcExpiries_Type())
vismSvcCallProcExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcCallProcExpiries.setStatus(_A)
_VismSvcReleasExpiries_Type=Counter32
_VismSvcReleasExpiries_Object=MibScalar
vismSvcReleasExpiries=_VismSvcReleasExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,28),_VismSvcReleasExpiries_Type())
vismSvcReleasExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcReleasExpiries.setStatus(_A)
_VismSvcConnExpiries_Type=Counter32
_VismSvcConnExpiries_Object=MibScalar
vismSvcConnExpiries=_VismSvcConnExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,29),_VismSvcConnExpiries_Type())
vismSvcConnExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcConnExpiries.setStatus(_A)
_VismSvcConnAckExpiries_Type=Counter32
_VismSvcConnAckExpiries_Object=MibScalar
vismSvcConnAckExpiries=_VismSvcConnAckExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,30),_VismSvcConnAckExpiries_Type())
vismSvcConnAckExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcConnAckExpiries.setStatus(_A)
_VismSvcRestartExpiries_Type=Counter32
_VismSvcRestartExpiries_Object=MibScalar
vismSvcRestartExpiries=_VismSvcRestartExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,31),_VismSvcRestartExpiries_Type())
vismSvcRestartExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcRestartExpiries.setStatus(_A)
_VismSvcResyncExpiries_Type=Counter32
_VismSvcResyncExpiries_Object=MibScalar
vismSvcResyncExpiries=_VismSvcResyncExpiries_Object((1,3,6,1,4,1,351,110,5,5,10,32),_VismSvcResyncExpiries_Type())
vismSvcResyncExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSvcResyncExpiries.setStatus(_A)
_VismSvcCnfGroups_ObjectIdentity=ObjectIdentity
vismSvcCnfGroups=_VismSvcCnfGroups_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,19))
_VismSvcAtmQosGrp_ObjectIdentity=ObjectIdentity
vismSvcAtmQosGrp=_VismSvcAtmQosGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,19,1))
class _VismSvcAtmQosCdv_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,20000))
_VismSvcAtmQosCdv_Type.__name__=_D
_VismSvcAtmQosCdv_Object=MibScalar
vismSvcAtmQosCdv=_VismSvcAtmQosCdv_Object((1,3,6,1,4,1,351,110,5,5,19,1,1),_VismSvcAtmQosCdv_Type())
vismSvcAtmQosCdv.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSvcAtmQosCdv.setStatus(_A)
class _VismSvcAtmQosCtd_Type(Integer32):defaultValue=150000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20000,150000))
_VismSvcAtmQosCtd_Type.__name__=_D
_VismSvcAtmQosCtd_Object=MibScalar
vismSvcAtmQosCtd=_VismSvcAtmQosCtd_Object((1,3,6,1,4,1,351,110,5,5,19,1,2),_VismSvcAtmQosCtd_Type())
vismSvcAtmQosCtd.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSvcAtmQosCtd.setStatus(_A)
class _VismSvcAtmQosClr_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_VismSvcAtmQosClr_Type.__name__=_D
_VismSvcAtmQosClr_Object=MibScalar
vismSvcAtmQosClr=_VismSvcAtmQosClr_Object((1,3,6,1,4,1,351,110,5,5,19,1,3),_VismSvcAtmQosClr_Type())
vismSvcAtmQosClr.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSvcAtmQosClr.setStatus(_A)
_VismSvcTrfScalingGrp_ObjectIdentity=ObjectIdentity
vismSvcTrfScalingGrp=_VismSvcTrfScalingGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,19,2))
class _VismSvcTrfScalingFactor_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,200))
_VismSvcTrfScalingFactor_Type.__name__=_D
_VismSvcTrfScalingFactor_Object=MibScalar
vismSvcTrfScalingFactor=_VismSvcTrfScalingFactor_Object((1,3,6,1,4,1,351,110,5,5,19,2,1),_VismSvcTrfScalingFactor_Type())
vismSvcTrfScalingFactor.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSvcTrfScalingFactor.setStatus(_A)
_VismSvcAal2CidGrp_ObjectIdentity=ObjectIdentity
vismSvcAal2CidGrp=_VismSvcAal2CidGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,19,3))
class _VismSvcAal2CidNumber_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_VismSvcAal2CidNumber_Type.__name__=_D
_VismSvcAal2CidNumber_Object=MibScalar
vismSvcAal2CidNumber=_VismSvcAal2CidNumber_Object((1,3,6,1,4,1,351,110,5,5,19,3,1),_VismSvcAal2CidNumber_Type())
vismSvcAal2CidNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSvcAal2CidNumber.setStatus(_A)
_CiscoVismSvcMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismSvcMIBConformance=_CiscoVismSvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,90,2))
_CiscoVismSvcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismSvcMIBGroups=_CiscoVismSvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,90,2,1))
_CiscoVismSvcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismSvcMIBCompliances=_CiscoVismSvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,90,2,2))
ciscoVismSvcCounterGroup=ObjectGroup((1,3,6,1,4,1,351,150,90,2,1,1))
ciscoVismSvcCounterGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoVismSvcCounterGroup.setStatus(_A)
ciscoVismSvcAtmQosGroup=ObjectGroup((1,3,6,1,4,1,351,150,90,2,1,2))
ciscoVismSvcAtmQosGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoVismSvcAtmQosGroup.setStatus(_A)
ciscoVismSvcTrfScalingGrp=ObjectGroup((1,3,6,1,4,1,351,150,90,2,1,3))
ciscoVismSvcTrfScalingGrp.setObjects((_B,_o))
if mibBuilder.loadTexts:ciscoVismSvcTrfScalingGrp.setStatus(_A)
ciscoVismSvcAal2CidGrp=ObjectGroup((1,3,6,1,4,1,351,150,90,2,1,4))
ciscoVismSvcAal2CidGrp.setObjects((_B,_p))
if mibBuilder.loadTexts:ciscoVismSvcAal2CidGrp.setStatus(_A)
ciscoVismSvcCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,90,2,2,1))
ciscoVismSvcCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoVismSvcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismSvcGrp':vismSvcGrp,_F:vismSvcTxSetups,_G:vismSvcRxSetups,_H:vismSvcTxCallProcs,_I:vismSvcRxCallProcs,_J:vismSvcTxConns,_K:vismSvcTxConnAcks,_L:vismSvcRxConns,_M:vismSvcRxConnAcks,_N:vismSvcTxReleases,_O:vismSvcTxReleaseCompls,_P:vismSvcRxReleases,_Q:vismSvcRxReleaseCompls,_R:vismSvcTxRestarts,_S:vismSvcTxRestartAcks,_T:vismSvcRxRestarts,_U:vismSvcRxRestartAcks,_V:vismSvcTxResyncStrts,_W:vismSvcTxResyncStrtAcks,_X:vismSvcRxResyncStrts,_Y:vismSvcRxResyncStrtAcks,_Z:vismSvcTxResyncEnds,_a:vismSvcTxResyncEndAcks,_b:vismSvcRxResyncEnds,_c:vismSvcRxResyncEndAcks,_d:vismSvcTxBulkResyncs,_e:vismSvcRxBulkResyncs,_f:vismSvcCallProcExpiries,_g:vismSvcReleasExpiries,_h:vismSvcConnExpiries,_i:vismSvcConnAckExpiries,_j:vismSvcRestartExpiries,_k:vismSvcResyncExpiries,'vismSvcCnfGroups':vismSvcCnfGroups,'vismSvcAtmQosGrp':vismSvcAtmQosGrp,_l:vismSvcAtmQosCdv,_m:vismSvcAtmQosCtd,_n:vismSvcAtmQosClr,'vismSvcTrfScalingGrp':vismSvcTrfScalingGrp,_o:vismSvcTrfScalingFactor,'vismSvcAal2CidGrp':vismSvcAal2CidGrp,_p:vismSvcAal2CidNumber,'ciscoVismSvcMIB':ciscoVismSvcMIB,'ciscoVismSvcMIBConformance':ciscoVismSvcMIBConformance,'ciscoVismSvcMIBGroups':ciscoVismSvcMIBGroups,_q:ciscoVismSvcCounterGroup,_r:ciscoVismSvcAtmQosGroup,_s:ciscoVismSvcTrfScalingGrp,_t:ciscoVismSvcAal2CidGrp,'ciscoVismSvcMIBCompliances':ciscoVismSvcMIBCompliances,'ciscoVismSvcCompliance':ciscoVismSvcCompliance})