_V='ciscoVismCardCacFailuresGrp'
_U='ciscoVismChanCacGroup'
_T='vismPortCacSvcUpspeedFailures'
_S='vismVcCacPvcUpspeedFailures'
_R='vismVcCacPvcFailures'
_Q='vismPortCacSvcAddFailures'
_P='vismPortCacPvcAddFailures'
_O='networkCacConfigState'
_N='vismChanVADDutyCycle'
_M='vismChanVADTolerance'
_L='vismChanCarrierLossPolicy'
_K='vismChanCacRejectionPolicy'
_J='vismChanCacRejectedCons'
_I='vismChanCacPassedCons'
_H='vismChanCacMaster'
_G='unspecified'
_F='vismChanNum'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-VISM-CAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vismChanCnfGrp,voice=mibBuilder.importSymbols('BASIS-MIB','vismChanCnfGrp','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVismCacMIB=ModuleIdentity((1,3,6,1,4,1,351,150,96))
if mibBuilder.loadTexts:ciscoVismCacMIB.setRevisions(('2004-02-20 00:00','2003-06-18 00:00'))
_VismChanCacTable_Object=MibTable
vismChanCacTable=_VismChanCacTable_Object((1,3,6,1,4,1,351,110,5,5,3,1,3))
if mibBuilder.loadTexts:vismChanCacTable.setStatus(_A)
_VismChanCacEntry_Object=MibTableRow
vismChanCacEntry=_VismChanCacEntry_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1))
vismChanCacEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vismChanCacEntry.setStatus(_A)
class _VismChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismChanNum_Type.__name__=_D
_VismChanNum_Object=MibTableColumn
vismChanNum=_VismChanNum_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,1),_VismChanNum_Type())
vismChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanNum.setStatus(_A)
class _VismChanCacMaster_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_VismChanCacMaster_Type.__name__=_D
_VismChanCacMaster_Object=MibTableColumn
vismChanCacMaster=_VismChanCacMaster_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,2),_VismChanCacMaster_Type())
vismChanCacMaster.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanCacMaster.setStatus(_A)
_VismChanCacPassedCons_Type=Counter32
_VismChanCacPassedCons_Object=MibTableColumn
vismChanCacPassedCons=_VismChanCacPassedCons_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,3),_VismChanCacPassedCons_Type())
vismChanCacPassedCons.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanCacPassedCons.setStatus(_A)
_VismChanCacRejectedCons_Type=Counter32
_VismChanCacRejectedCons_Object=MibTableColumn
vismChanCacRejectedCons=_VismChanCacRejectedCons_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,4),_VismChanCacRejectedCons_Type())
vismChanCacRejectedCons.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanCacRejectedCons.setStatus(_A)
class _VismChanCacRejectionPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delete',1),('maintain',2),(_G,3)))
_VismChanCacRejectionPolicy_Type.__name__=_D
_VismChanCacRejectionPolicy_Object=MibTableColumn
vismChanCacRejectionPolicy=_VismChanCacRejectionPolicy_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,5),_VismChanCacRejectionPolicy_Type())
vismChanCacRejectionPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanCacRejectionPolicy.setStatus(_A)
class _VismChanCarrierLossPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('previousCodec',1),('upspeedCodec',2),(_G,3)))
_VismChanCarrierLossPolicy_Type.__name__=_D
_VismChanCarrierLossPolicy_Object=MibTableColumn
vismChanCarrierLossPolicy=_VismChanCarrierLossPolicy_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,6),_VismChanCarrierLossPolicy_Type())
vismChanCarrierLossPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanCarrierLossPolicy.setStatus(_A)
class _VismChanVADTolerance_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VismChanVADTolerance_Type.__name__=_D
_VismChanVADTolerance_Object=MibTableColumn
vismChanVADTolerance=_VismChanVADTolerance_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,7),_VismChanVADTolerance_Type())
vismChanVADTolerance.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanVADTolerance.setStatus(_A)
if mibBuilder.loadTexts:vismChanVADTolerance.setUnits('0.0001 percentage')
class _VismChanVADDutyCycle_Type(Integer32):defaultValue=61;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismChanVADDutyCycle_Type.__name__=_D
_VismChanVADDutyCycle_Object=MibTableColumn
vismChanVADDutyCycle=_VismChanVADDutyCycle_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,8),_VismChanVADDutyCycle_Type())
vismChanVADDutyCycle.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanVADDutyCycle.setStatus(_A)
if mibBuilder.loadTexts:vismChanVADDutyCycle.setUnits('0.01 percentage')
class _NetworkCacConfigState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('notOk',2)))
_NetworkCacConfigState_Type.__name__=_D
_NetworkCacConfigState_Object=MibTableColumn
networkCacConfigState=_NetworkCacConfigState_Object((1,3,6,1,4,1,351,110,5,5,3,1,3,1,9),_NetworkCacConfigState_Type())
networkCacConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:networkCacConfigState.setStatus(_A)
_VismCardCacFailuresGrp_ObjectIdentity=ObjectIdentity
vismCardCacFailuresGrp=_VismCardCacFailuresGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,20))
_VismPortCacPvcAddFailures_Type=Counter32
_VismPortCacPvcAddFailures_Object=MibScalar
vismPortCacPvcAddFailures=_VismPortCacPvcAddFailures_Object((1,3,6,1,4,1,351,110,5,5,20,1),_VismPortCacPvcAddFailures_Type())
vismPortCacPvcAddFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPortCacPvcAddFailures.setStatus(_A)
_VismPortCacSvcAddFailures_Type=Counter32
_VismPortCacSvcAddFailures_Object=MibScalar
vismPortCacSvcAddFailures=_VismPortCacSvcAddFailures_Object((1,3,6,1,4,1,351,110,5,5,20,2),_VismPortCacSvcAddFailures_Type())
vismPortCacSvcAddFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPortCacSvcAddFailures.setStatus(_A)
_VismVcCacPvcFailures_Type=Counter32
_VismVcCacPvcFailures_Object=MibScalar
vismVcCacPvcFailures=_VismVcCacPvcFailures_Object((1,3,6,1,4,1,351,110,5,5,20,3),_VismVcCacPvcFailures_Type())
vismVcCacPvcFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVcCacPvcFailures.setStatus(_A)
_VismVcCacPvcUpspeedFailures_Type=Counter32
_VismVcCacPvcUpspeedFailures_Object=MibScalar
vismVcCacPvcUpspeedFailures=_VismVcCacPvcUpspeedFailures_Object((1,3,6,1,4,1,351,110,5,5,20,4),_VismVcCacPvcUpspeedFailures_Type())
vismVcCacPvcUpspeedFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVcCacPvcUpspeedFailures.setStatus(_A)
_VismPortCacSvcUpspeedFailures_Type=Counter32
_VismPortCacSvcUpspeedFailures_Object=MibScalar
vismPortCacSvcUpspeedFailures=_VismPortCacSvcUpspeedFailures_Object((1,3,6,1,4,1,351,110,5,5,20,5),_VismPortCacSvcUpspeedFailures_Type())
vismPortCacSvcUpspeedFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPortCacSvcUpspeedFailures.setStatus(_A)
_CiscoVismCacMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismCacMIBConformance=_CiscoVismCacMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,96,2))
_CiscoVismCacMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismCacMIBGroups=_CiscoVismCacMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,96,2,1))
_CiscoVismCacMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismCacMIBCompliances=_CiscoVismCacMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,96,2,2))
ciscoVismChanCacGroup=ObjectGroup((1,3,6,1,4,1,351,150,96,2,1,1))
ciscoVismChanCacGroup.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoVismChanCacGroup.setStatus(_A)
ciscoVismCardCacFailuresGrp=ObjectGroup((1,3,6,1,4,1,351,150,96,2,1,2))
ciscoVismCardCacFailuresGrp.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoVismCardCacFailuresGrp.setStatus(_A)
ciscoVismCacCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,96,2,2,1))
ciscoVismCacCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ciscoVismCacCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismChanCacTable':vismChanCacTable,'vismChanCacEntry':vismChanCacEntry,_F:vismChanNum,_H:vismChanCacMaster,_I:vismChanCacPassedCons,_J:vismChanCacRejectedCons,_K:vismChanCacRejectionPolicy,_L:vismChanCarrierLossPolicy,_M:vismChanVADTolerance,_N:vismChanVADDutyCycle,_O:networkCacConfigState,'vismCardCacFailuresGrp':vismCardCacFailuresGrp,_P:vismPortCacPvcAddFailures,_Q:vismPortCacSvcAddFailures,_R:vismVcCacPvcFailures,_S:vismVcCacPvcUpspeedFailures,_T:vismPortCacSvcUpspeedFailures,'ciscoVismCacMIB':ciscoVismCacMIB,'ciscoVismCacMIBConformance':ciscoVismCacMIBConformance,'ciscoVismCacMIBGroups':ciscoVismCacMIBGroups,_U:ciscoVismChanCacGroup,_V:ciscoVismCardCacFailuresGrp,'ciscoVismCacMIBCompliances':ciscoVismCacMIBCompliances,'ciscoVismCacCompliance':ciscoVismCacCompliance})