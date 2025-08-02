_S='bandPtpGroup'
_R='bandPtpProvisionedOpenWaveRemotePtp'
_Q='bandPtpDemuxFreqSlotAttenProfile'
_P='bandPtpMuxFreqSlotAttenProfile'
_O='bandPtpAssociatedEqptType'
_N='bandPtpRxProvEqptType'
_M='bandPtpTxProvEqptType'
_L='bandPtpRxProvNbrTP'
_K='bandPtpTxProvNbrTP'
_J='bandPtpBringupLoopbackMode'
_I='bandPtpPmHistStatsEnable'
_H='bandPtpProvAseTP'
_G='bandPtpProvisionedNeighborTP'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-BANDPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnCircuitPackType,InfnEnableDisable,InfnEqptType,InfnPmHistStatsControl,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnCircuitPackType','InfnEnableDisable','InfnEqptType','InfnPmHistStatsControl','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bandPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,20))
if mibBuilder.loadTexts:bandPtpMIB.setRevisions(('2008-10-20 00:00',))
_BandPtpTable_Object=MibTable
bandPtpTable=_BandPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1))
if mibBuilder.loadTexts:bandPtpTable.setStatus(_A)
_BandPtpEntry_Object=MibTableRow
bandPtpEntry=_BandPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1))
bandPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bandPtpEntry.setStatus(_A)
_BandPtpProvisionedNeighborTP_Type=DisplayString
_BandPtpProvisionedNeighborTP_Object=MibTableColumn
bandPtpProvisionedNeighborTP=_BandPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,1),_BandPtpProvisionedNeighborTP_Type())
bandPtpProvisionedNeighborTP.setMaxAccess('read-create')
if mibBuilder.loadTexts:bandPtpProvisionedNeighborTP.setStatus(_A)
_BandPtpProvAseTP_Type=DisplayString
_BandPtpProvAseTP_Object=MibTableColumn
bandPtpProvAseTP=_BandPtpProvAseTP_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,2),_BandPtpProvAseTP_Type())
bandPtpProvAseTP.setMaxAccess(_D)
if mibBuilder.loadTexts:bandPtpProvAseTP.setStatus(_A)
_BandPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_BandPtpPmHistStatsEnable_Object=MibTableColumn
bandPtpPmHistStatsEnable=_BandPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,3),_BandPtpPmHistStatsEnable_Type())
bandPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmHistStatsEnable.setStatus(_A)
_BandPtpBringupLoopbackMode_Type=InfnEnableDisable
_BandPtpBringupLoopbackMode_Object=MibTableColumn
bandPtpBringupLoopbackMode=_BandPtpBringupLoopbackMode_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,4),_BandPtpBringupLoopbackMode_Type())
bandPtpBringupLoopbackMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpBringupLoopbackMode.setStatus(_A)
_BandPtpTxProvNbrTP_Type=DisplayString
_BandPtpTxProvNbrTP_Object=MibTableColumn
bandPtpTxProvNbrTP=_BandPtpTxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,5),_BandPtpTxProvNbrTP_Type())
bandPtpTxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpTxProvNbrTP.setStatus(_A)
_BandPtpRxProvNbrTP_Type=DisplayString
_BandPtpRxProvNbrTP_Object=MibTableColumn
bandPtpRxProvNbrTP=_BandPtpRxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,6),_BandPtpRxProvNbrTP_Type())
bandPtpRxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpRxProvNbrTP.setStatus(_A)
_BandPtpTxProvEqptType_Type=InfnEqptType
_BandPtpTxProvEqptType_Object=MibTableColumn
bandPtpTxProvEqptType=_BandPtpTxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,7),_BandPtpTxProvEqptType_Type())
bandPtpTxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:bandPtpTxProvEqptType.setStatus(_A)
_BandPtpRxProvEqptType_Type=InfnEqptType
_BandPtpRxProvEqptType_Object=MibTableColumn
bandPtpRxProvEqptType=_BandPtpRxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,8),_BandPtpRxProvEqptType_Type())
bandPtpRxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:bandPtpRxProvEqptType.setStatus(_A)
_BandPtpAssociatedEqptType_Type=InfnEqptType
_BandPtpAssociatedEqptType_Object=MibTableColumn
bandPtpAssociatedEqptType=_BandPtpAssociatedEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,9),_BandPtpAssociatedEqptType_Type())
bandPtpAssociatedEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:bandPtpAssociatedEqptType.setStatus(_A)
_BandPtpMuxFreqSlotAttenProfile_Type=DisplayString
_BandPtpMuxFreqSlotAttenProfile_Object=MibTableColumn
bandPtpMuxFreqSlotAttenProfile=_BandPtpMuxFreqSlotAttenProfile_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,10),_BandPtpMuxFreqSlotAttenProfile_Type())
bandPtpMuxFreqSlotAttenProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpMuxFreqSlotAttenProfile.setStatus(_A)
_BandPtpDemuxFreqSlotAttenProfile_Type=DisplayString
_BandPtpDemuxFreqSlotAttenProfile_Object=MibTableColumn
bandPtpDemuxFreqSlotAttenProfile=_BandPtpDemuxFreqSlotAttenProfile_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,11),_BandPtpDemuxFreqSlotAttenProfile_Type())
bandPtpDemuxFreqSlotAttenProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpDemuxFreqSlotAttenProfile.setStatus(_A)
_BandPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_BandPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
bandPtpProvisionedOpenWaveRemotePtp=_BandPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,20,1,1,12),_BandPtpProvisionedOpenWaveRemotePtp_Type())
bandPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
_BandPtpConformance_ObjectIdentity=ObjectIdentity
bandPtpConformance=_BandPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,20,3))
_BandPtpCompliances_ObjectIdentity=ObjectIdentity
bandPtpCompliances=_BandPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,20,3,1))
_BandPtpGroups_ObjectIdentity=ObjectIdentity
bandPtpGroups=_BandPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,20,3,2))
bandPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,20,3,2,1))
bandPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:bandPtpGroup.setStatus(_A)
bandPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,20,3,1,1))
bandPtpCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:bandPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bandPtpMIB':bandPtpMIB,'bandPtpTable':bandPtpTable,'bandPtpEntry':bandPtpEntry,_G:bandPtpProvisionedNeighborTP,_H:bandPtpProvAseTP,_I:bandPtpPmHistStatsEnable,_J:bandPtpBringupLoopbackMode,_K:bandPtpTxProvNbrTP,_L:bandPtpRxProvNbrTP,_M:bandPtpTxProvEqptType,_N:bandPtpRxProvEqptType,_O:bandPtpAssociatedEqptType,_P:bandPtpMuxFreqSlotAttenProfile,_Q:bandPtpDemuxFreqSlotAttenProfile,_R:bandPtpProvisionedOpenWaveRemotePtp,'bandPtpConformance':bandPtpConformance,'bandPtpCompliances':bandPtpCompliances,'bandPtpCompliance':bandPtpCompliance,'bandPtpGroups':bandPtpGroups,_S:bandPtpGroup})