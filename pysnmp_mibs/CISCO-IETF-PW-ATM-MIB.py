_g='cpwAtmPerfGroup'
_f='cpwVcAtmGroup'
_e='cpwAtmAvgCellsPacked'
_d='cpwAtmPktsRejected'
_c='cpwAtmPktsSent'
_b='cpwAtmPktsReceived'
_a='cpwAtmHCCellsTagged'
_Z='cpwAtmHCCellsRejected'
_Y='cpwAtmHCCellsReceived'
_X='cpwAtmCellsTagged'
_W='cpwAtmCellsRejected'
_V='cpwAtmCellsSent'
_U='cpwAtmCellsReceived'
_T='cpwAtmMcptTimeout'
_S='cpwAtmEncap'
_R='cpwAtmPeerMncp'
_Q='cpwAtmMncp'
_P='cpwAtmCellPacking'
_O='cpwAtmQosScalingFactor'
_N='cpwAtmOamCellSupported'
_M='cpwAtmClpQosMapping'
_L='cpwAtmRowStatus'
_K='cpwAtmVci'
_J='cpwAtmVpi'
_I='cpwAtmIf'
_H='cpwVcAtmPerfEntry'
_G='cpwVcIndex'
_F='CISCO-IETF-PW-MIB'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-IETF-PW-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
cpwVcIndex,=mibBuilder.importSymbols(_F,_G)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cpwVcAtmMIB=ModuleIdentity((1,3,6,1,4,1,9,10,9000))
if mibBuilder.loadTexts:cpwVcAtmMIB.setRevisions(('2005-04-19 12:00','2003-02-16 12:00'))
_CpwVcAtmNotifications_ObjectIdentity=ObjectIdentity
cpwVcAtmNotifications=_CpwVcAtmNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,9000,0))
_CpwVcAtmObjects_ObjectIdentity=ObjectIdentity
cpwVcAtmObjects=_CpwVcAtmObjects_ObjectIdentity((1,3,6,1,4,1,9,10,9000,1))
_CpwVcAtmTable_Object=MibTable
cpwVcAtmTable=_CpwVcAtmTable_Object((1,3,6,1,4,1,9,10,9000,1,1))
if mibBuilder.loadTexts:cpwVcAtmTable.setStatus(_A)
_CpwVcAtmEntry_Object=MibTableRow
cpwVcAtmEntry=_CpwVcAtmEntry_Object((1,3,6,1,4,1,9,10,9000,1,1,1))
cpwVcAtmEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cpwVcAtmEntry.setStatus(_A)
_CpwAtmIf_Type=InterfaceIndex
_CpwAtmIf_Object=MibTableColumn
cpwAtmIf=_CpwAtmIf_Object((1,3,6,1,4,1,9,10,9000,1,1,1,1),_CpwAtmIf_Type())
cpwAtmIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmIf.setStatus(_A)
_CpwAtmVpi_Type=AtmVpIdentifier
_CpwAtmVpi_Object=MibTableColumn
cpwAtmVpi=_CpwAtmVpi_Object((1,3,6,1,4,1,9,10,9000,1,1,1,2),_CpwAtmVpi_Type())
cpwAtmVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmVpi.setStatus(_A)
_CpwAtmVci_Type=AtmVcIdentifier
_CpwAtmVci_Object=MibTableColumn
cpwAtmVci=_CpwAtmVci_Object((1,3,6,1,4,1,9,10,9000,1,1,1,3),_CpwAtmVci_Type())
cpwAtmVci.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmVci.setStatus(_A)
_CpwAtmClpQosMapping_Type=TruthValue
_CpwAtmClpQosMapping_Object=MibTableColumn
cpwAtmClpQosMapping=_CpwAtmClpQosMapping_Object((1,3,6,1,4,1,9,10,9000,1,1,1,4),_CpwAtmClpQosMapping_Type())
cpwAtmClpQosMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmClpQosMapping.setStatus(_A)
_CpwAtmRowStatus_Type=RowStatus
_CpwAtmRowStatus_Object=MibTableColumn
cpwAtmRowStatus=_CpwAtmRowStatus_Object((1,3,6,1,4,1,9,10,9000,1,1,1,5),_CpwAtmRowStatus_Type())
cpwAtmRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmRowStatus.setStatus(_A)
_CpwAtmOamCellSupported_Type=TruthValue
_CpwAtmOamCellSupported_Object=MibTableColumn
cpwAtmOamCellSupported=_CpwAtmOamCellSupported_Object((1,3,6,1,4,1,9,10,9000,1,1,1,6),_CpwAtmOamCellSupported_Type())
cpwAtmOamCellSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmOamCellSupported.setStatus(_A)
class _CpwAtmQosScalingFactor_Type(Integer32):defaultValue=100
_CpwAtmQosScalingFactor_Type.__name__=_E
_CpwAtmQosScalingFactor_Object=MibTableColumn
cpwAtmQosScalingFactor=_CpwAtmQosScalingFactor_Object((1,3,6,1,4,1,9,10,9000,1,1,1,7),_CpwAtmQosScalingFactor_Type())
cpwAtmQosScalingFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmQosScalingFactor.setStatus(_A)
_CpwAtmCellPacking_Type=TruthValue
_CpwAtmCellPacking_Object=MibTableColumn
cpwAtmCellPacking=_CpwAtmCellPacking_Object((1,3,6,1,4,1,9,10,9000,1,1,1,8),_CpwAtmCellPacking_Type())
cpwAtmCellPacking.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmCellPacking.setStatus(_A)
_CpwAtmMncp_Type=Integer32
_CpwAtmMncp_Object=MibTableColumn
cpwAtmMncp=_CpwAtmMncp_Object((1,3,6,1,4,1,9,10,9000,1,1,1,9),_CpwAtmMncp_Type())
cpwAtmMncp.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmMncp.setStatus(_A)
_CpwAtmPeerMncp_Type=Integer32
_CpwAtmPeerMncp_Object=MibTableColumn
cpwAtmPeerMncp=_CpwAtmPeerMncp_Object((1,3,6,1,4,1,9,10,9000,1,1,1,10),_CpwAtmPeerMncp_Type())
cpwAtmPeerMncp.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmPeerMncp.setStatus(_A)
class _CpwAtmEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mpls',1),('l2tpv3',2),('unknown',3)))
_CpwAtmEncap_Type.__name__=_E
_CpwAtmEncap_Object=MibTableColumn
cpwAtmEncap=_CpwAtmEncap_Object((1,3,6,1,4,1,9,10,9000,1,1,1,11),_CpwAtmEncap_Type())
cpwAtmEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmEncap.setStatus(_A)
_CpwAtmMcptTimeout_Type=Integer32
_CpwAtmMcptTimeout_Object=MibTableColumn
cpwAtmMcptTimeout=_CpwAtmMcptTimeout_Object((1,3,6,1,4,1,9,10,9000,1,1,1,12),_CpwAtmMcptTimeout_Type())
cpwAtmMcptTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwAtmMcptTimeout.setStatus(_A)
_CpwVcAtmPerfTable_Object=MibTable
cpwVcAtmPerfTable=_CpwVcAtmPerfTable_Object((1,3,6,1,4,1,9,10,9000,1,2))
if mibBuilder.loadTexts:cpwVcAtmPerfTable.setStatus(_A)
_CpwVcAtmPerfEntry_Object=MibTableRow
cpwVcAtmPerfEntry=_CpwVcAtmPerfEntry_Object((1,3,6,1,4,1,9,10,9000,1,2,1))
if mibBuilder.loadTexts:cpwVcAtmPerfEntry.setStatus(_A)
_CpwAtmCellsReceived_Type=Counter32
_CpwAtmCellsReceived_Object=MibTableColumn
cpwAtmCellsReceived=_CpwAtmCellsReceived_Object((1,3,6,1,4,1,9,10,9000,1,2,1,1),_CpwAtmCellsReceived_Type())
cpwAtmCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmCellsReceived.setStatus(_A)
_CpwAtmCellsSent_Type=Counter32
_CpwAtmCellsSent_Object=MibTableColumn
cpwAtmCellsSent=_CpwAtmCellsSent_Object((1,3,6,1,4,1,9,10,9000,1,2,1,2),_CpwAtmCellsSent_Type())
cpwAtmCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmCellsSent.setStatus(_A)
_CpwAtmCellsRejected_Type=Counter32
_CpwAtmCellsRejected_Object=MibTableColumn
cpwAtmCellsRejected=_CpwAtmCellsRejected_Object((1,3,6,1,4,1,9,10,9000,1,2,1,3),_CpwAtmCellsRejected_Type())
cpwAtmCellsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmCellsRejected.setStatus(_A)
_CpwAtmCellsTagged_Type=Counter32
_CpwAtmCellsTagged_Object=MibTableColumn
cpwAtmCellsTagged=_CpwAtmCellsTagged_Object((1,3,6,1,4,1,9,10,9000,1,2,1,4),_CpwAtmCellsTagged_Type())
cpwAtmCellsTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmCellsTagged.setStatus(_A)
_CpwAtmHCCellsReceived_Type=Counter64
_CpwAtmHCCellsReceived_Object=MibTableColumn
cpwAtmHCCellsReceived=_CpwAtmHCCellsReceived_Object((1,3,6,1,4,1,9,10,9000,1,2,1,5),_CpwAtmHCCellsReceived_Type())
cpwAtmHCCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmHCCellsReceived.setStatus(_A)
_CpwAtmHCCellsRejected_Type=Counter64
_CpwAtmHCCellsRejected_Object=MibTableColumn
cpwAtmHCCellsRejected=_CpwAtmHCCellsRejected_Object((1,3,6,1,4,1,9,10,9000,1,2,1,6),_CpwAtmHCCellsRejected_Type())
cpwAtmHCCellsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmHCCellsRejected.setStatus(_A)
_CpwAtmHCCellsTagged_Type=Counter64
_CpwAtmHCCellsTagged_Object=MibTableColumn
cpwAtmHCCellsTagged=_CpwAtmHCCellsTagged_Object((1,3,6,1,4,1,9,10,9000,1,2,1,7),_CpwAtmHCCellsTagged_Type())
cpwAtmHCCellsTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmHCCellsTagged.setStatus(_A)
_CpwAtmAvgCellsPacked_Type=Counter32
_CpwAtmAvgCellsPacked_Object=MibTableColumn
cpwAtmAvgCellsPacked=_CpwAtmAvgCellsPacked_Object((1,3,6,1,4,1,9,10,9000,1,2,1,8),_CpwAtmAvgCellsPacked_Type())
cpwAtmAvgCellsPacked.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmAvgCellsPacked.setStatus(_A)
_CpwAtmPktsReceived_Type=Counter32
_CpwAtmPktsReceived_Object=MibTableColumn
cpwAtmPktsReceived=_CpwAtmPktsReceived_Object((1,3,6,1,4,1,9,10,9000,1,2,1,9),_CpwAtmPktsReceived_Type())
cpwAtmPktsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmPktsReceived.setStatus(_A)
_CpwAtmPktsSent_Type=Counter32
_CpwAtmPktsSent_Object=MibTableColumn
cpwAtmPktsSent=_CpwAtmPktsSent_Object((1,3,6,1,4,1,9,10,9000,1,2,1,10),_CpwAtmPktsSent_Type())
cpwAtmPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmPktsSent.setStatus(_A)
_CpwAtmPktsRejected_Type=Counter32
_CpwAtmPktsRejected_Object=MibTableColumn
cpwAtmPktsRejected=_CpwAtmPktsRejected_Object((1,3,6,1,4,1,9,10,9000,1,2,1,11),_CpwAtmPktsRejected_Type())
cpwAtmPktsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwAtmPktsRejected.setStatus(_A)
_CpwVcAtmConformance_ObjectIdentity=ObjectIdentity
cpwVcAtmConformance=_CpwVcAtmConformance_ObjectIdentity((1,3,6,1,4,1,9,10,9000,2))
_CpwVcAtmGroups_ObjectIdentity=ObjectIdentity
cpwVcAtmGroups=_CpwVcAtmGroups_ObjectIdentity((1,3,6,1,4,1,9,10,9000,2,1))
_CpwVcAtmCompliances_ObjectIdentity=ObjectIdentity
cpwVcAtmCompliances=_CpwVcAtmCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,9000,2,2))
cpwVcAtmEntry.registerAugmentions((_B,_H))
cpwVcAtmPerfEntry.setIndexNames(*cpwVcAtmEntry.getIndexNames())
cpwVcAtmGroup=ObjectGroup((1,3,6,1,4,1,9,10,9000,2,1,1))
cpwVcAtmGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cpwVcAtmGroup.setStatus(_A)
cpwAtmPerfGroup=ObjectGroup((1,3,6,1,4,1,9,10,9000,2,1,2))
cpwAtmPerfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cpwAtmPerfGroup.setStatus(_A)
cpwVcAtmModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,9000,2,2,1))
cpwVcAtmModuleCompliance.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cpwVcAtmModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cpwVcAtmMIB':cpwVcAtmMIB,'cpwVcAtmNotifications':cpwVcAtmNotifications,'cpwVcAtmObjects':cpwVcAtmObjects,'cpwVcAtmTable':cpwVcAtmTable,'cpwVcAtmEntry':cpwVcAtmEntry,_I:cpwAtmIf,_J:cpwAtmVpi,_K:cpwAtmVci,_M:cpwAtmClpQosMapping,_L:cpwAtmRowStatus,_N:cpwAtmOamCellSupported,_O:cpwAtmQosScalingFactor,_P:cpwAtmCellPacking,_Q:cpwAtmMncp,_R:cpwAtmPeerMncp,_S:cpwAtmEncap,_T:cpwAtmMcptTimeout,'cpwVcAtmPerfTable':cpwVcAtmPerfTable,_H:cpwVcAtmPerfEntry,_U:cpwAtmCellsReceived,_V:cpwAtmCellsSent,_W:cpwAtmCellsRejected,_X:cpwAtmCellsTagged,_Y:cpwAtmHCCellsReceived,_Z:cpwAtmHCCellsRejected,_a:cpwAtmHCCellsTagged,_e:cpwAtmAvgCellsPacked,_b:cpwAtmPktsReceived,_c:cpwAtmPktsSent,_d:cpwAtmPktsRejected,'cpwVcAtmConformance':cpwVcAtmConformance,'cpwVcAtmGroups':cpwVcAtmGroups,_f:cpwVcAtmGroup,_g:cpwAtmPerfGroup,'cpwVcAtmCompliances':cpwVcAtmCompliances,'cpwVcAtmModuleCompliance':cpwVcAtmModuleCompliance})