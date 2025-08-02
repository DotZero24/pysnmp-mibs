_W='lspGroup'
_V='lspAssociatedMplsTunnel'
_U='lspAssociatedPeerLSP'
_T='lspNextHop'
_S='lspNum'
_R='lspSupportingEqptAid'
_Q='lspLoopBackbehaviour'
_P='lspLoopBack'
_O='lspAvailableBW'
_N='lspMaxReservableBw'
_M='lspConfiguredTrafficClass'
_L='lspConfiguredTTL'
_K='lspQOSModel'
_J='lspOutgoingLabel'
_I='lspIncomingLabel'
_H='lspType'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-create'
_C='read-write'
_B='INFINERA-TP-PXMLSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnEnableDisable,InfnLSPLoopBackBehaviour,InfnLSPType,InfnMplsQosModel=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEnableDisable','InfnLSPLoopBackBehaviour','InfnLSPType','InfnMplsQosModel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lspMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,71))
_LspTable_Object=MibTable
lspTable=_LspTable_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1))
if mibBuilder.loadTexts:lspTable.setStatus(_A)
_LspEntry_Object=MibTableRow
lspEntry=_LspEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1))
lspEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lspEntry.setStatus(_A)
_LspType_Type=InfnLSPType
_LspType_Object=MibTableColumn
lspType=_LspType_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,1),_LspType_Type())
lspType.setMaxAccess(_C)
if mibBuilder.loadTexts:lspType.setStatus(_A)
_LspIncomingLabel_Type=Integer32
_LspIncomingLabel_Object=MibTableColumn
lspIncomingLabel=_LspIncomingLabel_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,2),_LspIncomingLabel_Type())
lspIncomingLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:lspIncomingLabel.setStatus(_A)
_LspOutgoingLabel_Type=Integer32
_LspOutgoingLabel_Object=MibTableColumn
lspOutgoingLabel=_LspOutgoingLabel_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,3),_LspOutgoingLabel_Type())
lspOutgoingLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:lspOutgoingLabel.setStatus(_A)
_LspQOSModel_Type=InfnMplsQosModel
_LspQOSModel_Object=MibTableColumn
lspQOSModel=_LspQOSModel_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,4),_LspQOSModel_Type())
lspQOSModel.setMaxAccess(_D)
if mibBuilder.loadTexts:lspQOSModel.setStatus(_A)
_LspConfiguredTTL_Type=Integer32
_LspConfiguredTTL_Object=MibTableColumn
lspConfiguredTTL=_LspConfiguredTTL_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,5),_LspConfiguredTTL_Type())
lspConfiguredTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:lspConfiguredTTL.setStatus(_A)
_LspConfiguredTrafficClass_Type=Integer32
_LspConfiguredTrafficClass_Object=MibTableColumn
lspConfiguredTrafficClass=_LspConfiguredTrafficClass_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,6),_LspConfiguredTrafficClass_Type())
lspConfiguredTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lspConfiguredTrafficClass.setStatus(_A)
_LspMaxReservableBw_Type=Integer32
_LspMaxReservableBw_Object=MibTableColumn
lspMaxReservableBw=_LspMaxReservableBw_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,7),_LspMaxReservableBw_Type())
lspMaxReservableBw.setMaxAccess(_E)
if mibBuilder.loadTexts:lspMaxReservableBw.setStatus(_A)
_LspAvailableBW_Type=Integer32
_LspAvailableBW_Object=MibTableColumn
lspAvailableBW=_LspAvailableBW_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,8),_LspAvailableBW_Type())
lspAvailableBW.setMaxAccess(_E)
if mibBuilder.loadTexts:lspAvailableBW.setStatus(_A)
_LspLoopBack_Type=InfnEnableDisable
_LspLoopBack_Object=MibTableColumn
lspLoopBack=_LspLoopBack_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,9),_LspLoopBack_Type())
lspLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:lspLoopBack.setStatus(_A)
_LspLoopBackbehaviour_Type=InfnLSPLoopBackBehaviour
_LspLoopBackbehaviour_Object=MibTableColumn
lspLoopBackbehaviour=_LspLoopBackbehaviour_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,10),_LspLoopBackbehaviour_Type())
lspLoopBackbehaviour.setMaxAccess(_E)
if mibBuilder.loadTexts:lspLoopBackbehaviour.setStatus(_A)
_LspId_Type=DisplayString
_LspId_Object=MibTableColumn
lspId=_LspId_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,11),_LspId_Type())
lspId.setMaxAccess(_C)
if mibBuilder.loadTexts:lspId.setStatus(_A)
_LspSupportingEqptAid_Type=DisplayString
_LspSupportingEqptAid_Object=MibTableColumn
lspSupportingEqptAid=_LspSupportingEqptAid_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,12),_LspSupportingEqptAid_Type())
lspSupportingEqptAid.setMaxAccess(_D)
if mibBuilder.loadTexts:lspSupportingEqptAid.setStatus(_A)
_LspNum_Type=Integer32
_LspNum_Object=MibTableColumn
lspNum=_LspNum_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,13),_LspNum_Type())
lspNum.setMaxAccess(_E)
if mibBuilder.loadTexts:lspNum.setStatus(_A)
_LspNextHop_Type=DisplayString
_LspNextHop_Object=MibTableColumn
lspNextHop=_LspNextHop_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,14),_LspNextHop_Type())
lspNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:lspNextHop.setStatus(_A)
_LspAssociatedPeerLSP_Type=DisplayString
_LspAssociatedPeerLSP_Object=MibTableColumn
lspAssociatedPeerLSP=_LspAssociatedPeerLSP_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,15),_LspAssociatedPeerLSP_Type())
lspAssociatedPeerLSP.setMaxAccess(_C)
if mibBuilder.loadTexts:lspAssociatedPeerLSP.setStatus(_A)
_LspAssociatedMplsTunnel_Type=DisplayString
_LspAssociatedMplsTunnel_Object=MibTableColumn
lspAssociatedMplsTunnel=_LspAssociatedMplsTunnel_Object((1,3,6,1,4,1,21296,2,2,2,2,71,1,1,16),_LspAssociatedMplsTunnel_Type())
lspAssociatedMplsTunnel.setMaxAccess(_C)
if mibBuilder.loadTexts:lspAssociatedMplsTunnel.setStatus(_A)
_LspConformance_ObjectIdentity=ObjectIdentity
lspConformance=_LspConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,71,3))
_LspCompliances_ObjectIdentity=ObjectIdentity
lspCompliances=_LspCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,71,3,1))
_LspGroups_ObjectIdentity=ObjectIdentity
lspGroups=_LspGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,71,3,2))
lspGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,71,3,2,1))
lspGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,'lspId'),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:lspGroup.setStatus(_A)
lspCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,71,3,1,1))
lspCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:lspCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lspMIB':lspMIB,'lspTable':lspTable,'lspEntry':lspEntry,_H:lspType,_I:lspIncomingLabel,_J:lspOutgoingLabel,_K:lspQOSModel,_L:lspConfiguredTTL,_M:lspConfiguredTrafficClass,_N:lspMaxReservableBw,_O:lspAvailableBW,_P:lspLoopBack,_Q:lspLoopBackbehaviour,'lspId':lspId,_R:lspSupportingEqptAid,_S:lspNum,_T:lspNextHop,_U:lspAssociatedPeerLSP,_V:lspAssociatedMplsTunnel,'lspConformance':lspConformance,'lspCompliances':lspCompliances,'lspCompliance':lspCompliance,'lspGroups':lspGroups,_W:lspGroup})